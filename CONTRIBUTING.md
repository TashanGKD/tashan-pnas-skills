# 贡献 / Contributing

欢迎改进技能指令、图组检查表、翻译、安装说明与可复核案例。

1. 说明具体任务、输入、实际问题及修改后预期行为。
2. 保持三个技能的职责边界；不要把一次案例变成所有研究都必须遵循的规则。
3. 将事实、假设、解释、建议和待验证信息分开。引用论文时提供可核查书目信息，不上传无权分发的全文。
4. 使用合成或已获授权的数据。不要提交访问凭据、个人路径、私有对话或未获授权稿件。
5. 同步更新中英文 README；实际行为评测需记录输入、模型、设置、日期与评审标准。教学示例须保留标签。

提交前运行：

```bash
python -m unittest discover -s tests -v
python scripts/install.py --dest ./installation-preview --dry-run
```

如本地提供 `skill-creator`，再对改动的技能运行其 `quick_validate.py`。检查 `SKILL.md` 的每个本地引用可解析，`agents/openai.yaml` 使用 `interface` 字段，且每个技能可以单独复制使用。

English: Describe the task, input, observed problem, and expected behavior. Keep changes scoped, preserve evidence and uncertainty, and update both READMEs. Share only synthetic or authorized materials. Run the checks above and validate changed skills with the host's skill validator when available. Teaching examples must not be presented as measured benchmarks.
