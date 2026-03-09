#!/usr/bin/env python3
"""Generate daily category reports from AI-enhanced arXiv JSONL data.

Output layout:
- data/reports/YYYY-MM-DD/<category>.md
- data/reports/YYYY-MM-DD/index.json

Rules:
- Generate reports for every primary category present in today's file.
- Skip the synthetic "all" category.
- Use deterministic statistics + optional LLM trend summary with fallback.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "with",
    "we",
    "our",
    "via",
    "using",
    "based",
    "learning",
    "model",
    "models",
    "network",
    "networks",
    "paper",
    "method",
    "methods",
    "approach",
    "approaches",
    "result",
    "results",
}


@dataclass
class PaperRecord:
    id: str
    title: str
    abs_url: str
    summary: str
    tldr: str
    authors: list[str]
    categories: list[str]
    code_url: str
    code_stars: int


def parse_args() -> argparse.Namespace:
    env_top_n = os.environ.get("REPORT_TOP_N", "5")
    try:
        default_top_n = int(env_top_n) if str(env_top_n).strip() else 5
    except ValueError:
        default_top_n = 5

    parser = argparse.ArgumentParser(description="Generate daily reports per category")
    parser.add_argument("--data", required=True, help="Path to AI-enhanced JSONL file")
    parser.add_argument("--date", default=None, help="Report date (YYYY-MM-DD). Auto-detect if omitted")
    parser.add_argument("--output_dir", default=None, help="Base output dir (default: <data_dir>/reports/<date>)")
    parser.add_argument("--top_n", type=int, default=default_top_n)
    parser.add_argument("--language", default=os.environ.get("LANGUAGE", "Chinese"))
    parser.add_argument("--model_name", default=os.environ.get("REPORT_MODEL_NAME") or os.environ.get("MODEL_NAME", "deepseek-chat"))
    parser.add_argument("--enable_llm_summary", action="store_true", help="Enable LLM-written trend summary")
    return parser.parse_args()


def infer_date(data_file: Path, cli_date: str | None) -> str:
    if cli_date:
        return cli_date
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", data_file.name)
    if m:
        return m.group(1)
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def safe_text(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return ""
    return str(value).strip()


def parse_jsonl(data_file: Path) -> list[PaperRecord]:
    papers: list[PaperRecord] = []
    with data_file.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw:
                continue
            try:
                item = json.loads(raw)
            except json.JSONDecodeError as e:
                print(f"Skip line {line_no}: invalid JSON ({e})", file=sys.stderr)
                continue

            categories = item.get("categories") or []
            if isinstance(categories, str):
                categories = [categories]
            categories = [safe_text(c) for c in categories if safe_text(c)]
            if not categories:
                continue

            ai = item.get("AI") if isinstance(item.get("AI"), dict) else {}
            papers.append(
                PaperRecord(
                    id=safe_text(item.get("id")),
                    title=safe_text(item.get("title")),
                    abs_url=safe_text(item.get("abs")) or f"https://arxiv.org/abs/{safe_text(item.get('id'))}",
                    summary=safe_text(item.get("summary")),
                    tldr=safe_text(ai.get("tldr")) or safe_text(item.get("summary")),
                    authors=item.get("authors") if isinstance(item.get("authors"), list) else [],
                    categories=categories,
                    code_url=safe_text(item.get("code_url")),
                    code_stars=int(item.get("code_stars") or 0),
                )
            )
    return papers


def primary_category(p: PaperRecord) -> str:
    if not p.categories:
        return ""
    return p.categories[0].strip()


def extract_keywords(texts: list[str], top_k: int = 8) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for text in texts:
        for tok in re.findall(r"[A-Za-z][A-Za-z0-9\-]{2,}", text.lower()):
            if tok in STOPWORDS:
                continue
            if tok.isdigit():
                continue
            counter[tok] += 1
    return counter.most_common(top_k)


def score_paper(p: PaperRecord) -> float:
    # Priority = information density + code signal + title signal
    info_density = min(len(p.tldr), 240) / 240
    code_signal = min(p.code_stars, 500) / 500
    title_signal = min(len(p.title.split()), 20) / 20
    return 0.5 * info_density + 0.3 * code_signal + 0.2 * title_signal


def format_overview(category: str, papers: list[PaperRecord]) -> dict[str, Any]:
    paper_count = len(papers)
    unique_authors = len({a.strip() for p in papers for a in p.authors if a and a.strip()})
    with_code = sum(1 for p in papers if p.code_url)
    code_ratio = (with_code / paper_count * 100) if paper_count else 0.0
    avg_authors = (sum(len(p.authors) for p in papers) / paper_count) if paper_count else 0.0
    return {
        "category": category,
        "paper_count": paper_count,
        "unique_authors": unique_authors,
        "with_code": with_code,
        "code_ratio": round(code_ratio, 2),
        "avg_authors": round(avg_authors, 2),
    }


def build_fallback_trends(overview: dict[str, Any], top_keywords: list[tuple[str, int]], top_papers: list[PaperRecord]) -> list[str]:
    lines = [
        f"今日共收录 {overview['paper_count']} 篇，含代码链接占比 {overview['code_ratio']}%。",
        f"作者活跃度：{overview['unique_authors']} 位作者参与，平均每篇 {overview['avg_authors']} 位作者。",
    ]
    if top_keywords:
        lines.append("高频主题集中在：" + "、".join(k for k, _ in top_keywords[:5]) + "。")
    if top_papers:
        lines.append(f"重点论文《{top_papers[0].title}》在内容密度/代码信号上综合得分最高。")
    return lines[:5]


def try_llm_trends(category: str, overview: dict[str, Any], top_keywords: list[tuple[str, int]], top_papers: list[PaperRecord], language: str, model_name: str) -> list[str] | None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_openai import ChatOpenAI
    except Exception:
        return None

    paper_brief = [
        {
            "title": p.title,
            "tldr": p.tldr[:220],
            "code_stars": p.code_stars,
        }
        for p in top_papers[:5]
    ]
    prompt = ChatPromptTemplate.from_template(
        """
你是资深科研编辑。请为分类 {category} 生成 3~5 条“当日趋势总结”，语言为 {language}。
要求：
1) 每条一句话，具体、可读，禁止空话。
2) 仅基于输入信息，不要编造。
3) 返回 JSON 数组字符串，例如 ["...", "..."]。

输入统计：{overview}
输入关键词：{keywords}
输入重点论文：{paper_brief}
""".strip()
    )

    llm = ChatOpenAI(model=model_name, temperature=0.2)
    resp = (prompt | llm).invoke(
        {
            "category": category,
            "language": language,
            "overview": json.dumps(overview, ensure_ascii=False),
            "keywords": json.dumps(top_keywords, ensure_ascii=False),
            "paper_brief": json.dumps(paper_brief, ensure_ascii=False),
        }
    )

    content = getattr(resp, "content", "")
    if not isinstance(content, str):
        return None
    m = re.search(r"\[[\s\S]*\]", content)
    if not m:
        return None
    data = json.loads(m.group(0))
    if not isinstance(data, list):
        return None
    clean = [safe_text(x) for x in data if safe_text(x)]
    return clean[:5] if clean else None


def render_markdown(category: str, date: str, overview: dict[str, Any], top_keywords: list[tuple[str, int]], top_papers: list[PaperRecord], trends: list[str]) -> str:
    lines: list[str] = []
    lines.append(f"# {category} 日报 ({date})")
    lines.append("")
    lines.append("## 今日概览")
    lines.append("")
    lines.append(f"- 论文数: {overview['paper_count']}")
    lines.append(f"- 独立作者数: {overview['unique_authors']}")
    lines.append(f"- 含代码论文: {overview['with_code']} ({overview['code_ratio']}%)")
    lines.append(f"- 平均作者数/篇: {overview['avg_authors']}")
    lines.append("")

    lines.append("## 热点关键词")
    lines.append("")
    if top_keywords:
        for kw, cnt in top_keywords[:8]:
            lines.append(f"- {kw}: {cnt}")
    else:
        lines.append("- 无可用关键词")
    lines.append("")

    lines.append("## 重点论文")
    lines.append("")
    if top_papers:
        for idx, p in enumerate(top_papers, start=1):
            code_suffix = f" | Code: {p.code_url}" if p.code_url else ""
            lines.append(f"### {idx}. [{p.title}]({p.abs_url})")
            lines.append("")
            lines.append(f"- TLDR: {p.tldr}")
            lines.append(f"- Authors: {', '.join(p.authors) if p.authors else 'N/A'}{code_suffix}")
            lines.append("")
    else:
        lines.append("- 今日无重点论文")
        lines.append("")

    lines.append("## 趋势总结")
    lines.append("")
    if trends:
        for t in trends:
            lines.append(f"- {t}")
    else:
        lines.append("- 今日数据不足，暂不输出趋势。")
    lines.append("")

    return "\n".join(lines)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def main() -> int:
    args = parse_args()
    data_file = Path(args.data)
    if not data_file.exists():
        print(f"Data file not found: {data_file}", file=sys.stderr)
        return 1

    date = infer_date(data_file, args.date)
    if args.output_dir:
        out_dir = Path(args.output_dir)
    else:
        out_dir = data_file.parent / "reports" / date
    ensure_dir(out_dir)

    papers = parse_jsonl(data_file)
    if not papers:
        print("No papers parsed, skip report generation.", file=sys.stderr)
        return 0

    grouped: dict[str, list[PaperRecord]] = defaultdict(list)
    for p in papers:
        cat = primary_category(p)
        if not cat:
            continue
        if cat.lower() == "all":
            continue
        grouped[cat].append(p)

    if not grouped:
        print("No category groups found after filtering.", file=sys.stderr)
        return 0

    index_payload: dict[str, Any] = {
        "date": date,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_file": str(data_file),
        "total_categories": len(grouped),
        "categories": [],
    }

    for category in sorted(grouped.keys()):
        cat_papers = grouped[category]
        cat_papers = sorted(cat_papers, key=score_paper, reverse=True)
        overview = format_overview(category, cat_papers)
        top_keywords = extract_keywords([f"{p.title} {p.tldr}" for p in cat_papers], top_k=8)
        top_papers = cat_papers[: max(1, args.top_n)]

        trends: list[str] | None = None
        if args.enable_llm_summary:
            try:
                trends = try_llm_trends(
                    category=category,
                    overview=overview,
                    top_keywords=top_keywords,
                    top_papers=top_papers,
                    language=args.language,
                    model_name=args.model_name,
                )
            except Exception as e:
                print(f"LLM trends failed for {category}: {e}", file=sys.stderr)

        if not trends:
            trends = build_fallback_trends(overview, top_keywords, top_papers)

        markdown = render_markdown(category, date, overview, top_keywords, top_papers, trends)
        md_name = f"{category}.md"
        md_path = out_dir / md_name
        md_path.write_text(markdown, encoding="utf-8")

        index_payload["categories"].append(
            {
                "category": category,
                "paper_count": overview["paper_count"],
                "report_file": f"data/reports/{date}/{md_name}",
                "top_keywords": [k for k, _ in top_keywords[:5]],
            }
        )

    index_path = out_dir / "index.json"
    index_path.write_text(json.dumps(index_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Generated reports: {len(index_payload['categories'])} categories", file=sys.stderr)
    print(f"Output: {out_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
