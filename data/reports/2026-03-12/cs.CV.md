# cs.CV 日报 (2026-03-12)

## 今日概览

- 论文数: 83
- 独立作者数: 455
- 含代码论文: 25 (30.12%)
- 平均作者数/篇: 5.57

## 热点关键词

- generation: 73
- summary: 65
- failed: 65
- image: 15
- video: 8
- unified: 7
- vision: 7
- framework: 6

## 重点论文

### 1. [TractoRC: A Unified Probabilistic Learning Framework for Joint Tractography Registration and Clustering](https://arxiv.org/abs/2603.10418)

- TLDR: TractoRC是一个统一的概率框架，联合执行扩散MRI纤维束图注册和流线聚类任务。该方法通过学习共享的流线点潜在嵌入空间，将两个任务都表述为概率推断，并引入变换等变自监督策略进行优化。实验证明联合优化显著优于独立处理的最先进方法。
- Authors: Yijie Li, Xi Zhu, Junyi Wang, Ye Wu, Lauren J. O'Donnell, Fan Zhang | Code: https://github.com/yishengpoxiao/TractoRC

### 2. [One Token, Two Fates: A Unified Framework via Vision Token Manipulation Against MLLMs Hallucination](https://arxiv.org/abs/2603.10360)

- TLDR: 提出一种统一的无训练框架，通过协同视觉校准(SVC)和因果表示校准(CRC)两个模块，分别利用增强图像的互补视觉语义和修剪视觉令牌产生的信息差，有效恢复多模态大语言模型的视觉-语言平衡，显著减少对象幻觉。
- Authors: Zhan Fa, Yue Duan, Jian Zhang, Lei Qi, Yinghuan Shi

### 3. [Just-in-Time: Training-Free Spatial Acceleration for Diffusion Transformers](https://arxiv.org/abs/2603.10744)

- TLDR: 这篇论文提出了JiT（Just-in-Time）框架，一个用于加速扩散变换器推理的训练无关方法，通过利用生成过程中的空间冗余，基于动态选择的稀疏锚点令牌子集来近似完整的潜在状态演化，在FLUX.1-dev模型上实现了高达7倍的加速且几乎没有性能损失。
- Authors: Wenhao Sun, Ji Li, Zhaoqiang Liu

### 4. [From Imitation to Intuition: Intrinsic Reasoning for Open-Instance Video Classification](https://arxiv.org/abs/2603.10300)

- TLDR: 本文提出了一种名为DeepIntuit的内在推理框架，将开放实例视频分类从传统的特征模仿模式进化到直觉推理模式，通过冷启动监督对齐、GRPO强化学习精炼和直觉校准三个阶段，显著提升了在复杂现实场景中的视频分类性能。
- Authors: Ke Zhang, Xiangchen Zhao, Yunjie Tian, Jiayu Zheng, Vishal M. Patel, Di Fu | Code: https://bwgzk-keke.github.io/DeepIntuit/

### 5. [StyleGallery: Training-free and Semantic-aware Personalized Style Transfer from Arbitrary Image References](https://arxiv.org/abs/2603.10354)

- TLDR: 这篇论文提出了StyleGallery，一个无需训练且语义感知的图像风格迁移框架，通过语义区域分割、聚类区域匹配和风格迁移优化三个核心阶段，实现了对任意参考图像的有效个性化定制，在多个指标上超越现有方法。
- Authors: Boyu He, Yunfan Ye, Chang Liu, Weishang Wu, Fang Liu, Zhiping Cai

## 趋势总结

- 当日研究显著关注“无训练”方法，多篇论文提出了无需额外训练即可实现多模态大模型去幻觉、扩散模型加速及个性化风格迁移的高效框架。
- “统一框架”成为方法论热点，研究涵盖了联合执行纤维束图注册与聚类的概率学习框架，以及协同视觉校准与因果表示校准的多模态大语言模型修正方案。
- 关键词统计显示“generation”与“summary”热度极高，表明生成模型与内容摘要技术仍是当日计算机视觉领域的核心议题。
- 视频理解领域取得进展，新提出的内在推理框架通过从模仿到直觉的进化，显著提升了开放实例视频分类在复杂场景下的性能。
