<!-- 他山协会 Logo -->
<p align="center">
  <a href="https://tashan.ac.cn" target="_blank" rel="noopener noreferrer">
    <img src="docs/assets/tashan.svg" alt="他山 Logo" width="280" />
  </a>
</p>

<p align="center">
  <strong>他山 PNAS 论文写作技能组</strong><br>
  <em>Tashan PNAS Writing, Figure Design &amp; Polishing Skills</em>
</p>

<p align="center">
  <a href="#项目简介">项目简介</a> •
  <a href="#三个技能怎么选">技能选择</a> •
  <a href="#安装方法">安装</a> •
  <a href="#每个技能的用法">用法</a> •
  <a href="#使用前后对比">前后对比</a> •
  <a href="#生态位置">生态位置</a> •
  <a href="README.en.md">English</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 3](https://img.shields.io/badge/Skills-3-2E74B5.svg)](skills/)

> 从研究证据到论文论证、科学图组与准确表达。

---

## 项目简介

本项目是他山「人—智能体混合数字世界」中科研方法与成果表达层的一组 Agent Skills。它把论文写作中反复使用的判断整理成可复用工作流：先明确科学问题、证据和结论边界，再安排正文与图组，最后打磨语言。研究者提供材料并负责科学判断，智能体协助组织、检查和表达。

这三个技能由他山在实际科研项目中开发，适合理论与模拟生物学、计算生物学、生物物理、系统生物学等研究；对反应扩散主方程（RDME）、随机细胞极性、力化学反馈和景观/通量分析提供了专门检查表。它们也可用于其他领域，但应按研究对象调整检查项。

- **以证据组织文章**：每个主要论点对应图、方程、数据或已核实文献，并说明适用范围。
- **把图组当作论证**：明确每个面板的任务、变量定义、统计含义和数据来源。
- **润色时保留科学含义**：区分模型结果、生物学解释与待检验预测，保留参数和不确定性。

适合正在整理初稿、重构 Results、设计多面板图、处理中译英或回复审稿意见的研究者。技能本身是文本工作流，不内置模型、文献数据库、绘图引擎或 Word/LaTeX 编译器；实际文件处理使用所在 Agent 的工具。

PNAS 在这里表示写作取向。本项目由他山独立维护，与 PNAS 期刊无隶属或认证关系，不承诺录用或固定质量提升。投稿字数、格式与图片规格应在投稿时核实官方要求。

---

## 三个技能怎么选

| 技能 | 什么时候用 | 主要输入 | 交付内容 |
| --- | --- | --- | --- |
| [`pnas-writing`](skills/pnas-writing/SKILL.md) | 尚未成文，或文章结构与论证需要调整 | 科学问题、模型/方法、图表、结果、证据缺口 | 正文或提纲、论点—证据映射、结构说明、过强论断与缺口 |
| [`pnas-figure`](skills/pnas-figure/SKILL.md) | 规划、审查或修改科学图组 | 图要回答的问题、数据/脚本、变量与参数、统计定义 | 图的主张、面板图谱、布局、图注、复现要求；工具可用时生成图文件 |
| [`pnas-polishing`](skills/pnas-polishing/SKILL.md) | 科学逻辑已明确，需要准确简洁地表达 | 原文、所属章节、术语、需要保留的事实与边界 | 润色稿、修改说明、论断强度提示、缺失证据标记 |

可以单独安装、单独使用。完整论文通常先用 `pnas-writing` 搭建论证，再用 `pnas-figure` 检查图组，最后用 `pnas-polishing` 处理语言；图组检查发现证据不足时，应回到论证与研究本身。

---

## 安装方法

### 1. 获取仓库

需要 Git 和 Python 3.9+；安装脚本只使用 Python 标准库。技能运行本身不需要 Python，绘图或文档输出所需依赖取决于具体任务。

```bash
git clone https://github.com/TashanGKD/tashan-pnas-skills.git
cd tashan-pnas-skills
```

也可以通过 GitHub 的 **Code → Download ZIP** 下载后解压，在解压目录运行以下命令。

### 2. 安装到 Codex

Windows PowerShell：

```powershell
# 预览将复制的目录，不修改任何文件
python .\scripts\install.py --dry-run

# 安装全部三个技能到当前用户的 ~/.agents/skills
python .\scripts\install.py

# 或仅安装写作技能
python .\scripts\install.py --skill pnas-writing
```

macOS / Linux：

```bash
python3 scripts/install.py --dry-run
python3 scripts/install.py
# 单独安装图组技能
python3 scripts/install.py --skill pnas-figure
```

当前 Codex 文档列出的个人目录为 `~/.agents/skills`，项目目录为 `<project>/.agents/skills`。见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。若现有环境已配置其他目录，用 `--dest` 指定；不要在多个扫描目录重复安装同名技能。

```powershell
# 仅供一个项目使用：替换为你的项目目录
python .\scripts\install.py --dest 'D:\my-paper\.agents\skills'

# 兼容现有使用 ~/.codex/skills 的环境
python .\scripts\install.py --dest "$env:USERPROFILE\.codex\skills"
```

也可直接把 `skills/` 下所需的完整技能文件夹复制到运行环境的技能目录。保留其中的 `references/` 与 `agents/`。其他兼容 `SKILL.md` 的 Agent 可复用这些文件；自动发现目录和调用语法以对应产品文档为准，跨产品行为尚未逐一验证。

### 3. 确认可以调用

在 Codex 新对话中输入以下内容；若技能未出现，重启 Codex，并检查是否存在 `~/.agents/skills/pnas-writing/SKILL.md`。

```text
请使用 $pnas-writing，读取我提供的研究材料，
先输出论点—证据—适用边界表，再给出 Results 提纲。
如果缺少证据，请明确标注，不要补造结果或引用。
```

### 更新与卸载

安装器遇到任意同名目标目录时，会在复制前停止，避免覆盖已有定制。更新时先 `git pull --ff-only`，把旧技能目录备份到**技能扫描目录之外**，再运行安装器。也可先安装到独立暂存目录检查差异。卸载时只移除所安装的对应技能文件夹；安装器不修改 Agent 配置、不读取密钥、不联网。

---

## 每个技能的用法

### pnas-writing：把研究材料组织成文章

**准备材料**：研究问题、主要结果、已有图表/方程、模型假设、参数范围、验证结果及目标章节。可从不完整材料开始，但缺口必须保留。

```text
请使用 $pnas-writing，依据我提供的研究笔记、图表和方法说明写中文初稿。
主题：一个随机细胞极性模型中的状态切换。
先整理每张图能支持什么结论、不能支持什么结论，
再给出 Significance、Abstract、Introduction、Results、Discussion 和 Methods 框架。
区分模拟观察、机制解释和实验预测；缺失的对照和参数来源保留占位。
```

**你会得到**：目标章节的草稿或重构版本；论点与证据映射；结构调整说明；过强论断、缺失文献/数据清单；下一步修改建议。也可以只请求标题、摘要、Significance、引言或单个 Results 小节。

**检查结果**：正文是否忠于输入；每个主要论点是否有证据；Methods 是否记录真实使用的方法；尚未完成的验证是否仍标为缺口。

### pnas-figure：设计和检查有证据作用的图

**准备材料**：图要回答的问题、现有面板、数据文件与绘图脚本、变量/单位、参数、随机种子和统计定义。没有数据时可做面板规划，不能生成声称来自实验或模拟的结果图。

```text
请使用 $pnas-figure，检查提供的三张轨迹图能否支持“反馈影响切换动力学”。
先给出图的主张和面板角色，再检查变量、单位、种子数、观测时长和切换定义。
指出哪些结论目前只能算代表性示例，哪些需要系综或对照验证。
请给出布局和图注；如果数据足够，再修改绘图脚本，
导出 SVG/PDF、PNG 预览及参数和数据来源记录。
```

**你会得到**：图的中心问题、面板角色图谱、布局与配色建议、图注草稿、数据与复现清单、审查风险。有可执行环境和真实输入时，进一步输出绘图代码与图文件。

**检查结果**：代表性轨迹和系综是否分开；相图分类与插值是否定义；误差条是否有含义；模型比较是否区分拟合与预测；缩放到目标尺寸后文字是否可读。

### pnas-polishing：在不改变证据的前提下润色

**准备材料**：原段落、所属章节、术语约定、不能改变的数字/条件，以及支持关键句的证据。中文输入默认先给英文稿，再给简短中文说明；可明确要求只用中文。

```text
请使用 $pnas-polishing，润色下面的 Results 段落并提供英文版本。
保留所有数字、参数、图号与限定条件，不增加新机制或引用。
说明主要修改，并单独列出强于证据的句子及所缺的验证。
原文：[粘贴段落]
证据范围：[说明数据、模型和已完成的验证]
```

**你会得到**：润色稿、修改说明、措辞与证据强度检查、缺失信息标记。若输入的科学逻辑不成立，应先指出结构问题，不能只把句子改得更流畅。

---

## 使用前后对比

以下是**人工编写的教学示例**，展示技能要求的工作方式；不是模型 A/B 测试、真实论文结果或效果保证。完整输入、目标输出与人工验收项见 [示例文件](examples/before-after.md)。

| 技能 | 使用前的输入或做法 | 按技能要求处理后的示例 |
| --- | --- | --- |
| `pnas-writing` | 按“建模 → 跑图 → 得到切换”记录过程，并写成“发现细胞极性的普遍机制” | 按模型定义、已有验证、切换观察、机制待检验、适用边界组织 Results；每条主张链接证据，缺失干预对照明确标出 |
| `pnas-figure` | 把三条漂亮轨迹拼在一起，图注只有“极性随时间变化” | 明确轨迹为代表性样本；补齐变量、单位和参数；提出系综统计与反馈对照面板，并标为待补数据 |
| `pnas-polishing` | “本研究首次彻底揭示了细胞极性切换的普适机制。” | “在所考察的参数条件下，模拟轨迹呈现极性状态之间的切换。这一观察尚不足以确定反馈的因果作用。” |

同一条事实在英文稿中的表达示例：

> In the simulated trajectory, polarity switched between states under the tested parameter conditions. Establishing a causal role for feedback requires a matched perturbation control.

有用的变化是论证结构、可检查性与表述边界。技能不会把单次模拟变成系综证据，也不会把缺失实验变成已验证机制。

---

## 目录结构与文档

```text
tashan-pnas-skills/
├── README.md / README.en.md       # 中英文说明、安装与用法
├── skills/
│   ├── pnas-writing/              # 正文与论证；SKILL.md + references + agents
│   ├── pnas-figure/               # 图组与复现；SKILL.md + references + agents
│   └── pnas-polishing/            # 润色与论断校准；同样结构
├── examples/before-after.md       # 三个技能的教学对比与验收项
├── scripts/install.py            # 无第三方依赖、拒绝覆盖的安装器
├── tests/test_install.py          # 安装、冲突与文件完整性检查
├── docs/PROVENANCE.md             # 自建来源、外部参考、公开范围
├── docs/assets/tashan.svg         # 他山统一 logo
├── licenses/nature-skills-MIT.txt # 外部设计参考的许可声明
├── CONTRIBUTING.md / CHANGELOG.md
└── LICENSE                       # MIT
```

技能包含的历史报告名称用于交代来源，报告原件并未随仓库发布，也不是运行依赖。无需下载原项目或论文全文即可使用技能。原始科研数据、未发表稿件、个人对话、访问凭据均不属于本技能包。

---

## 来源与验证范围

2026 年 5 月，这套技能在他山的研究工作中建立，并依据本地 PNAS/相关论文阅读记录补充。模块组织与工作流设计参考了 `Yuan1z0825/nature-skills`；正文与专门检查表针对 PNAS 写作和理论模拟研究整理。完整说明及许可归属见 [PROVENANCE](docs/PROVENANCE.md)。

本发布版检查技能结构、内部引用、安装行为和打包内容。教学对比尚未进行独立模型对照评测；历史论文观察不是期刊硬性规定，也不能代替当前官方投稿指南。

---

## 生态位置

```text
他山数字世界
├── 通用 Agent 工作流与协作
├── 科研方法与成果表达
│   ├── tashan-research-skills     # 广泛科研任务
│   ├── tashan-pnas-skills         # 本仓库：论文论证、图组与润色
│   └── tashan-ppt-skills          # 演示文稿与 BP
└── 具体科研项目与应用
```

| 相关仓库 | 关系 |
| --- | --- |
| [tashan-research-skills](https://github.com/TashanGKD/tashan-research-skills) | 通用科研技能，可按任务配合使用；不是安装依赖 |
| [tashan-ppt-skills](https://github.com/TashanGKD/tashan-ppt-skills) | 研究成果的演示表达；不是安装依赖 |
| [tashan-world](https://github.com/TashanGKD/tashan-world) | 他山数字世界应用；不是运行依赖 |

---

## 贡献

欢迎提交有输入材料、问题描述和可复核改进的案例。不要提交未获授权的稿件、数据或论文全文。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 更新日志

版本变更见 [CHANGELOG.md](CHANGELOG.md)。

---

## 许可证

[MIT License](LICENSE)。外部设计参考的声明见 [第三方许可](licenses/nature-skills-MIT.txt)。他山名称与 logo 用于项目归属标识；代码许可不授予冒用组织身份或宣称官方背书的权利。
