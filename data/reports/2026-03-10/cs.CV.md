# cs.CV 日报 (2026-03-10)

## 今日概览

- 论文数: 141
- 独立作者数: 839
- 含代码论文: 33 (23.4%)
- 平均作者数/篇: 6.14

## 热点关键词

- generation: 119
- summary: 105
- failed: 105
- diffusion: 13
- image: 12
- multimodal: 11
- reasoning: 10
- visual: 10

## 重点论文

### 1. [Towards Driver Behavior Understanding: Weakly-Supervised Risk Perception in Driving Scenes](https://arxiv.org/abs/2603.05926)

- TLDR: 本研究提出RAID（驾驶场景风险评估）大规模数据集和弱监督风险目标识别框架，用于驾驶者风险感知和情境风险评估。该框架通过建模驾驶者意图操作与响应之间的关系来识别潜在风险源，并分析了行人注意力在风险评估中的作用。实验表明，该方法在RAID和HDDS数据集上分别取得了20.6%和23.1%的性能提升。
- Authors: Nakul Agarwal, Yi-Ting Chen, Behzad Dariush

### 2. [EffectMaker: Unifying Reasoning and Generation for Customized Visual Effect Creation](https://arxiv.org/abs/2603.06014)

- TLDR: 本文提出了EffectMaker，一个统一的推理-生成框架，用于基于参考的VFX定制，通过多模态大语言模型和扩散transformer的语义-视觉双路径指导机制实现效果一致的合成，无需针对每个效果进行微调，并构建了包含13万视频和3千个VFX类别的最大合成数据集EffectData。
- Authors: Shiyuan Yang, Ruihuang Li, Jiale Tao, Shuai Shao, Qinglin Lu, Jing Liao | Code: https://effectmaker.github.io

### 3. [DeepSight: Bridging Depth Maps and Language with a Depth-Driven Multimodal Model](https://arxiv.org/abs/2603.06090)

- TLDR: 本文提出了DeepSight，这是首个专用的深度多模态大语言模型（MLLM），旨在提升三维场景理解能力。通过构建深度图像-文本对和指令数据集，修改CLIP的ViT编码器以融合局部对象信息，DeepSight显著增强了对深度信息的感知和下游任务性能。
- Authors: Hao Yang, Hongbo Zhang, Yanyan Zhao, Bing Qin

### 4. [CORE-Seg: Reasoning-Driven Segmentation for Complex Lesions via Reinforcement Learning](https://arxiv.org/abs/2603.05911)

- TLDR: 本论文提出了CORE-Seg框架和ComLesion-14K基准数据集，首次将推理能力整合到医学图像分割任务中，通过语义引导的提示适配器和渐进式训练策略（SFT到GRPO），在复杂病变分割上实现了37.06%的平均Dice分数，比第二优基线提升14.89%。
- Authors: Yuxin Xie, Yuming Chen, Yishan Yang, Yi Zhou, Tao Zhou, Zhen Zhao, Jiacheng Liu, Huazhu Fu | Code: https://xyxl024.github.io/CORE-Seg.github.io

### 5. [Devil is in Narrow Policy: Unleashing Exploration in Driving VLA Models](https://arxiv.org/abs/2603.06049)

- TLDR: Curious-VLA是一个通过两阶段设计解决VLA模型中"窄策略"限制的框架，有效释放了模型的探索潜力，在Navsim基准测试上达到最先进性能（PDMS 90.3, EPDMS 85.4，Best-of-N PDMS 94.8）。
- Authors: Canyu Chen, Yuguang Yang, Zhewen Tan, Yizhi Wang, Ruiyi Zhan, Haiyan Liu, Xuanyao Mao, Jason Bao, Xinyue Tang, Linlin Yang, Bingchuan Sun, Yan Wang, Baochang Zhang | Code: https://github.com/Mashiroln/curious_vla

## 趋势总结

- 今日研究呈现出将推理能力与生成任务深度融合的趋势，涵盖视觉特效定制与医学图像分割等应用场景。
- 自动驾驶领域关注风险感知与模型探索能力，新工作提出了弱监督风险评估框架及释放VLA模型潜力的Curious-VLA。
- 多模态大语言模型正向深度感知和三维场景理解延伸，DeepSight模型通过融合深度图信息增强了视觉-语言交互能力。
