# cs.CL 日报 (2026-03-10)

## 今日概览

- 论文数: 49
- 独立作者数: 227
- 含代码论文: 8 (16.33%)
- 平均作者数/篇: 4.88

## 热点关键词

- generation: 41
- summary: 38
- failed: 38
- language: 16
- large: 14
- reasoning: 8
- llm: 5
- context: 4

## 重点论文

### 1. [Addressing the Ecological Fallacy in Larger LMs with Human Context](https://arxiv.org/abs/2603.05928)

- TLDR: 该论文研究了通过建模作者上下文来解决生态学谬误，是否能提升大规模语言模型（8B Llama）的性能。论文提出了HuLM（基于作者上下文的预训练）和HuFT（人类感知微调）两种方法。实验结果表明，仅通过微调阶段引入作者上下文即可提升模型性能，而基于QLoRA的持续HuLM预训练能够泛化到八个下游任务并实现性能提升，证明了建模作者上下文的有效性和重要性。
- Authors: Nikita Soni, Dhruv Vijay Kunjadiya, Pratham Piyush Shah, Dikshya Mohanty, H. Andrew Schwartz, Niranjan Balasubramanian

### 2. [Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation](https://arxiv.org/abs/2603.05881)

- TLDR: CoCA（Co-optimized Confidence and Answers）是一个基于GRPO强化学习的框架，采用置信度优先范式，通过分段信用分配联合优化置信度校准和答案准确性，在数学、代码和事实问答基准测试中实现了更好的不确定性校准和答案质量。
- Authors: Changcheng Li, Jiancan Wu, Hengheng Zhang, Zhengsu Chen, Guo An, Junxiang Qiu, Xiang Wang, Qi Tian

### 3. [ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning](https://arxiv.org/abs/2603.05863)

- TLDR: 提出ReflexiCoder，一种基于强化学习的代码生成框架，通过将结构化推理轨迹（初始生成、缺陷感知反思、自我修正）内化到模型权重中，实现无需外部反馈的自主自我反思和修正能力。
- Authors: Juyong Jiang, Jiasi Shen, Sunghun Kim, Kang Min Yoo, Jeonghoon Kim, Sungju Kim | Code: https://github.com/juyongjiang/ReflexiCoder

### 4. [Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understanding and Editing](https://arxiv.org/abs/2603.06503)

- TLDR: 本文提出了Beyond Rows to Reasoning (BRTR)，一个用于电子表格理解的多模态智能体框架，通过迭代工具调用循环替代单次检索，支持端到端Excel工作流，在三个前沿基准上达到最先进性能。
- Authors: Anmol Gulati, Sahil Sen, Waqar Sarguroh, Kevin Paul

### 5. [FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling](https://arxiv.org/abs/2603.06199)

- TLDR: FlashPrefill是一个通过瞬时模式发现和动态阈值化实现超快速预填充的框架，在256K序列上实现了27.78倍加速，在4K短序列上仍保持1.71倍加速，显著突破了现有稀疏注意力机制的效率瓶颈。
- Authors: Qihang Fan, Huaibo Huang, Zhiying Wu, Juqiu Wang, Bingning Wang, Ran He

## 趋势总结

- FlashPrefill 框架通过瞬时模式发现和动态阈值化，在 256K 长序列预填充上实现了 27.78 倍加速，显著提升了长上下文推理效率。
- ReflexiCoder 利用强化学习将自我反思与修正内化到模型权重中，实现了无需外部反馈的代码生成自主纠错。
- BRTR 框架采用迭代工具调用替代单次检索，支持端到端 Excel 工作流，在电子表格理解与编辑任务中达到最先进水平。
- CoCA 框架提出置信度优先范式，通过联合优化置信度校准与答案准确性，在多项基准测试中改善了 LLM 的不确定性估计。
- 研究提出 HuFT 方法，证明仅在微调阶段引入作者上下文即可有效解决生态学谬误并提升大模型性能。
