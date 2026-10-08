# 使用前后对比 / Before and after

**性质：人工编写的教学样例。** 下列材料是虚构的最小输入，展示各技能预期的判断与交付。没有运行模型对照实验，也不代表真实研究结果。英文部分对齐相同的输入与边界。

## 共同输入 / Shared input

> 一个研究者提供了随机极性模型的三张轨迹图，声称观察到状态切换。模型含正反馈，但未提供去除反馈的匹配对照。未提供种子数、参数数值、观测时长、切换判据或实验验证。

> A researcher supplies three trajectory plots from a stochastic polarity model and reports switching. The model contains positive feedback, but no matched feedback-removal control is supplied. Seed count, parameter values, observation duration, transition criterion, and experimental validation are missing.

这些信息不足以证明反馈因果作用、稳态切换率或普适生物学机制。下面展示如何处理已知观察和缺口。

## 1. pnas-writing

**使用前**

> 我们建立了模型，运行模拟，画出了三张图，因此首次发现了细胞极性切换的普遍机制。

**调用**

```text
使用 $pnas-writing，根据共同输入整理 Results 提纲与论点—证据表。
不要添加原材料没有的模拟结果；对尚未验证的机制写出最小检验。
```

**目标输出示例**

| 拟写内容 | 当前证据 | 边界与下一步 |
| --- | --- | --- |
| 定义随机模型及正反馈项 | 仅知道模型类型和含反馈 | 补充状态变量、守恒律、事件倾向与参数 |
| 展示轨迹中的状态切换 | 三张提供的轨迹图 | 定义状态、切换判据、时间单位与样本来源 |
| 讨论反馈的可能作用 | 反馈存在，但没有匹配对照 | 在其他条件相同下比较反馈开启/关闭，采用多个独立种子 |
| 限定生物学解释 | 未提供实验 | 将生物学机制写为假设与验证方向 |

Results 可先写模型定义与轨迹观察；反馈对照、系综统计和适用范围验证列为待完成内容，而不是写成已得到的结果。

**English target**: organize Results around model definition and the supplied trajectory observations. Mark feedback perturbation, ensemble statistics, and scope tests as incomplete. A feedback term in a model is not itself causal evidence.

**验收**：没有新增结果、样本数或文献；每个论点对应证据；未完成部分不会因提纲更完整而变成已完成。

## 2. pnas-figure

**使用前**：三条轨迹平铺，标题“反馈控制切换”，图注“极性随时间变化”，坐标和样本含义不明。

**调用**

```text
使用 $pnas-figure，规划上述图组。分开已有面板与拟新增面板，
列出需要补充的数据、定义与统计信息；给出不夸大结论的图注。
```

**目标输出示例**

| 面板 | 科学作用 | 状态 |
| --- | --- | --- |
| A 模型示意 | 定义变量与反馈连接 | 需要模型细节后绘制 |
| B 代表性轨迹 | 展示已观察到的切换样例 | 已有图，需补单位、参数与种子标识 |
| C 系综统计 | 检查切换是否具有统计稳定性 | 待提供独立重复、判据、观测时长与不确定性 |
| D 反馈对照 | 检验反馈对切换的影响 | 待完成匹配干预，不能提前画出结果 |

**图注草稿**

> 图 X. 随机极性模型中的代表性状态切换轨迹。B 展示所提供的模拟轨迹。极性变量定义、时间单位、参数组和种子标识待补。A、C、D 为规划面板，尚未构成结果证据。

**English target caption**

> Figure X. Representative switching trajectories in a stochastic polarity model. Panel B shows the supplied trajectories. The polarity definition, time units, parameter set, and seed identifiers remain to be supplied. Panels A, C, and D are planned and are not yet evidence for a result.

**验收**：把规划与已有数据分开；不伪造 C/D；不把三张图自动解释成三个独立样本；缺信息时不臆定误差条。

## 3. pnas-polishing

**使用前**

> 本研究首次彻底揭示了反馈驱动细胞极性切换的普适机制，具有重大意义。

**调用**

```text
使用 $pnas-polishing，结合共同输入润色这句话。
提供英文稿和中文解释，明确模型观察与反馈因果判断的差别。
```

**目标英文稿**

> The supplied simulations illustrate switching between polarity states in a model with positive feedback. Determining whether feedback drives these transitions requires a matched perturbation control and ensemble analysis.

**中文说明**：保留“模型含反馈”和“观察到切换”；去掉缺乏文献检索支持的“首次”和超出证据的“普适机制”；将反馈的因果作用列为待检验问题。未添加参数、样本数、显著性或生物实验结论。

**验收**：保留原有可支持事实；不把 with feedback 改成 caused by feedback；不凭润色新增机制或引用。

## 如何做真正的使用前后评测 / A real comparison protocol

若需要测量技能效果，请让相同模型、工具权限与输入分别在启用/未启用技能的独立上下文中完成任务，保留完整输出与模型配置，使用多项案例并盲评以下指标：事实保留、证据可追溯、结论校准、图注完整性、可复现性与阅读清晰度。报告失败案例与评审差异，不仅展示最佳输出。

For a measured comparison, hold the model, tools, and inputs fixed, use independent
contexts with and without the skill, preserve outputs and configuration, and assess
multiple cases with blinded review. Score factual fidelity, evidence traceability,
claim calibration, caption completeness, reproducibility, and clarity. Report failures
and reviewer disagreement. No such measured result is claimed in this release.
