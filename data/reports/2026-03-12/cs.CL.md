# cs.CL 日报 (2026-03-12)

## 今日概览

- 论文数: 68
- 独立作者数: 331
- 含代码论文: 4 (5.88%)
- 平均作者数/篇: 4.96

## 热点关键词

- generation: 48
- summary: 45
- failed: 45
- language: 23
- large: 13
- llm: 8
- evaluation: 7
- llms: 7

## 重点论文

### 1. [LuxBorrow: From Pompier to Pompjee, Tracing Borrowing in Luxembourgish](https://arxiv.org/abs/2603.10789)

- TLDR: 本文介绍了LuxBorrow，一个对卢森堡语新闻文章（1999-2025年，259,305篇RTL文章，4370万词汇）进行的27年借词分析研究。研究通过句子级语言识别和词汇级借词解析器，揭示了卢森堡语中多语言实践的普遍性。结果显示：卢森堡语仍为基质语言，77.1%文章包含至少一种捐赠语言，代码混合指数（CMI）随时间增长但以局部插入为主。法语是主要借词来源，借词以形态和正字法适应为主（99.7%）。研究提倡采用以借词为中心的评估指标，而非仅依赖文档级混合指数。
- Authors: Nina Hosseini-Kivanani, Fred Philippy

### 2. [Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA LM for Batak and Minang Language](https://arxiv.org/abs/2603.10006)

- TLDR: 本文提出了基于GPT-2架构的1.2B参数三语语言模型TOBA-LM（印尼语、巴塔克语、米南加保语），通过集成Engram Memory机制，在12,973步内将损失值从6.4降至1.7996，训练效率达80%，相比传统Transformer架构所需的70,000多步有显著提升。
- Authors: Hokky Situngkir, Kevin Siringoringo, Andhika Bernard Lumbantobing

### 3. [A Principle-Driven Adaptive Policy for Group Cognitive Stimulation Dialogue for Elderly with Cognitive Impairment](https://arxiv.org/abs/2603.10034)

- TLDR: 本文提出了一个基于原则驱动的自适应群体认知刺激对话系统（GCSD），利用LLM技术解决认知障碍治疗中的群体对话挑战，通过四个核心模块（多说话人上下文控制、动态认知状态建模、认知刺激注意力损失、多维度奖励策略）实现个性化认知刺激治疗，并在实验中显著优于基线模型。
- Authors: Jiyue Jiang, Yanyu Chen, Pengan Chen, Kai Liu, Jingqi Zhou, Zheyong Zhu, He Hu, Fei Ma, Qi Tian, Chuan Wu

### 4. [GATech at AbjadGenEval Shared Task: Multilingual Embeddings for Arabic Machine-Generated Text Classification](https://arxiv.org/abs/2603.10007)

- TLDR: 该研究在AbjadGenEval共享任务中，使用微调的E5-large多语言编码器检测阿拉伯语AI生成文本。尽管尝试了多种复杂的池化策略，但简单的平均池化表现最佳，在测试集上达到0.75的F1分数。此外，观察到人类撰写的文本显著长于机器生成的文本。
- Authors: Ahmed Khaled Khamis

### 5. [PivotAttack: Rethinking the Search Trajectory in Hard-Label Text Attacks via Pivot Words](https://arxiv.org/abs/2603.10842)

- TLDR: 本文提出PivotAttack，一种采用"inside-out"策略的硬标签文本攻击框架，通过多臂老虎机算法识别Pivot Sets并策略性扰动，在保持高攻击成功率的同时显著降低查询成本。
- Authors: Yuzhi Liang, Shiliang Xiao, Jingsong Wei, Qiliang Lin, Xia Li

## 趋势总结

- 研究重点向多语言及低资源语言倾斜，涵盖卢森堡语历时借词分析及印尼语系的高效三语模型构建。
- 大语言模型在垂直领域的应用取得进展，特别是针对认知障碍老年人的群体认知刺激对话系统展现出个性化治疗潜力。
- 模型安全与评估成为热点，研究涵盖了阿拉伯语机器生成文本的检测以及通过Pivot Words降低查询成本的硬标签文本攻击。
- 关键词统计显示“generation”与“failed”频次极高，反映出学界在关注文本生成技术的同时，也高度重视其鲁棒性与失败案例分析。
