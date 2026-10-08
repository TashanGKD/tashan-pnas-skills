# 来源与公开范围 / Provenance and scope

## 开发来源

`pnas-writing`、`pnas-figure`、`pnas-polishing` 在 2026 年 5 月 18 日的本地开发记录中被初始化、编写并安装。后续参考文件于 5 月补充了 PNAS/相关论文阅读中归纳的写作、图组、SI、参数和审稿风险检查。本公开包以现有安装版本为基础，保留核心工作流。

发布整理只调整可移植性和说明：修正 UI 元数据层级；把原项目特定论点改为有条件的示例；解释历史报告与论文简称的来源性质；增加安装、用法和对比文档。原始研究工作区和个人安装副本未由本次打包修改。

## 外部设计参考

本地来源记录将 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) 列为设计参考，涉及模块化技能、图组约定、写作/润色工作流和按需加载参考资料的组织方式。PNAS 技能在本地围绕期刊写作取向及理论模拟研究需求编写；不将整个技能组声称为无外部参考的原创。

保留该参考项目的 [MIT 许可声明](../licenses/nature-skills-MIT.txt)，其中版权署名为 Yuan Yizhe。未捆绑该项目的完整源码，也未将其列为安装依赖。

## 证据层次

| 类型 | 在此技能包中的含义 |
| --- | --- |
| 官方规则 | 当前投稿要求须从期刊官方来源核实；本包不把易变限制写死 |
| 论文观察 | 从历史阅读记录归纳的结构和表达方式，不能等同于强制规范 |
| 工作流改编 | 从外部技能设计中吸收的组织思路，注明设计参考 |
| 项目经验 | 来自 RDME、随机极性和力化学研究的领域检查项 |
| 教学示例 | 本次发布编写的输入和目标输出，不是实验结果或模型测评 |

部分 `references/` 中保留历史 `pnas-style-research-project/reports/...` 文件名，以及作者—年份简称，帮助追溯规则形成过程。原始报告、文献库和 PDF 未公开随附。**这些名称不是可用的仓库路径，也不是运行时必须读取的资源。** 外部使用者应以随包说明执行工作流；若要在论文中引用某篇文献，必须另行核实完整书目、原文和具体支持关系。

原阅读记录的证据深度不完全相同：部分页面曾逐页检查，部分归纳依赖解析文本、图注或缩略图。此发布没有重新验证所有原论文，不能将历史简称当作完整、已复核的引用列表。

## 品牌与验证范围

README 按他山统一规范编写：原版 `tashan.svg`、居中宽度 280、官网链接、双语导航、生态位置，以及贡献—更新日志—许可证尾部。Logo 为组织识别资产；MIT 软件许可不授权冒用身份或虚假背书。

发布检查包括技能结构、内部文件引用、安装器与文件复制、无覆盖行为，以及待提交文件范围。**未完成独立模型 A/B 效果评测**；示例说明预期工作方式，不报告提升百分比或录用概率。

## English summary

The three skills were initialized, authored, and installed locally on 18 May 2026,
then expanded from PNAS and related-paper reading notes. This distribution packages
the existing installed versions with portability edits, corrected UI metadata,
installation instructions, and teaching examples; it does not modify the original
research workspace or personal skill copies.

The local source ledger identifies `Yuan1z0825/nature-skills` as an architectural
and workflow reference. Its MIT notice is retained under `licenses/`. The upstream
source tree is not bundled and is not a runtime dependency.

Historical report names and author–year shorthand in references document development
provenance, not accessible repository files or verified publication citations. The
private reports and paper corpus are not distributed. Verify original articles and
bibliographic details independently before citing them. Historical inspection depth
varied; this release does not revalidate all literature observations.

The public package contains workflow instructions, references, documentation, a logo,
and installation code—not research datasets, unpublished manuscripts, conversations,
or credentials. Validation covers packaging and installation, not a controlled model
quality benchmark. PNAS affiliation or endorsement is not claimed.
