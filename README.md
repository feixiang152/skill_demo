# Article Summarizer Skill

一个用于**总结技术文章并生成结构化摘要**的 Agent Skill。支持从 URL、文件路径或粘贴文本中提取内容，按用户选择的详细程度生成摘要，并可保存为 Markdown 文件。

本仓库遵循开放的 **Agent Skills** 规范，可被 Claude Code、Cursor、GitHub Copilot、Codex 等支持 Agent Skills 的工具加载使用。

## 功能特性

- 支持三种摘要详细程度：**简短 / 中等 / 详细**
- 支持 URL、本地文件、直接粘贴文本三种输入方式
- 输出结构化摘要：一句话总结、核心要点、关键结论 / 行动建议
- 可将摘要保存为 Markdown 文件
- 附带确定性保存脚本，避免模型每次临时编写文件读写逻辑
- 纯本地运行，不上传文章内容，不依赖外部 API Key

## 仓库结构

```text
article-summarizer-skill/
├── README.md
├── LICENSE
└── skills/
    └── article-summarizer/
        ├── SKILL.md
        ├── scripts/
        │   └── save_summary.py
        └── references/
            └── summary-format.md
```

核心 Skill 位于 `skills/article-summarizer/`，工具只需拉取该目录即可使用。

## 安装

### 方式一：使用 GitHub CLI（推荐）

需要 GitHub CLI **v2.90.0+**，并确保你的工具支持 Agent Skills 安装。

```bash
gh skill install <your-username>/article-summarizer-skill article-summarizer
```

将 `<your-username>` 替换为仓库所属的 GitHub 用户名或组织名。

如需锁定版本：

```bash
gh skill install <your-username>/article-summarizer-skill article-summarizer --pin v1.0.0
```

### 方式二：手动安装

克隆仓库：

```bash
git clone https://github.com/<your-username>/article-summarizer-skill.git
cd article-summarizer-skill
```

将 Skill 目录复制到对应工具的 skills 目录。

**Claude Code（用户级，所有项目可用）：**

```bash
mkdir -p ~/.claude/skills
cp -r skills/article-summarizer ~/.claude/skills/
```

**Claude Code（项目级，仅当前项目可用）：**

```bash
mkdir -p .claude/skills
cp -r skills/article-summarizer .claude/skills/
```

**Cursor：**

```bash
mkdir -p .cursor/skills
cp -r skills/article-summarizer .cursor/skills/
```

Windows 用户可直接将 `skills/article-summarizer` 文件夹复制到对应工具的 skills 目录。

安装完成后，重新加载或重启对应工具，确认 Skill 已被加载。

### 方式三：从 ZIP 安装

1. 在 GitHub 仓库页面点击 **Code → Download ZIP**。
2. 解压后找到 `skills/article-summarizer/`。
3. 将该文件夹复制到上文对应的 skills 目录。

## 使用示例

安装后，在支持的 AI 编程工具中直接提出请求即可触发，例如：

```text
帮我总结这篇文章：https://example.com/some-technical-article
```

```text
总结一下 ./docs/architecture.md，要详细版
```

```text
把下面这段内容生成中等长度的摘要：
<粘贴文章内容>
```

Skill 会按以下流程执行：

1. 确认文章来源（URL、文件路径或粘贴文本）
2. 确认摘要详细程度（简短 / 中等 / 详细，默认中等）
3. 读取文章内容
4. 生成结构化摘要
5. 按需调用 `scripts/save_summary.py` 保存到文件

输出示例（中等长度）：

```markdown
**一句话总结**：文章介绍了如何通过渐进式加载降低 Agent Skill 的上下文开销。

**核心要点**
1. Skill 启动时只加载 description，触发后才读取正文。
2. 正文建议控制在 500 行以内，细节拆到 references。
3. 确定性操作应放入 scripts，由模型按需调用。

**关键结论**
将稳定流程写成 Skill，可以显著提升 Agent 行为的一致性和可维护性。
```

## 保存脚本说明

`scripts/save_summary.py` 负责将摘要内容保存为 Markdown 文件。

```bash
python scripts/save_summary.py <摘要内容文件> [输出路径]
```

- 不传输出路径时，默认保存为 `summary-YYYY-MM-DD.md`
- 脚本只读写本地文件，不发起网络请求
- 需要 Python 3.8+

## 兼容性

本 Skill 遵循开放 Agent Skills 规范，理论上可被支持该规范的工具加载。常见包括：

- Claude Code
- Cursor
- GitHub Copilot
- Codex
- 其他支持 `SKILL.md` 与 Agent Skills 目录结构的工具

不同工具的 skills 目录和加载方式可能不同，请以对应工具文档为准。

## 安全说明

- 本 Skill 不会主动上传文章内容。
- `scripts/save_summary.py` 仅进行本地文件读写。
- 请勿在 `SKILL.md` 或脚本中硬编码 API Key、Token、内部 URL 等敏感信息。
- 从网络获取文章内容时，请遵守目标网站的服务条款和 robots 协议。

## 自定义与扩展

- 修改 `skills/article-summarizer/SKILL.md` 可调整触发条件、执行步骤和约束。
- 修改 `skills/article-summarizer/references/summary-format.md` 可调整摘要模板。
- 新增其他 Skill 时，建议放在 `skills/<skill-name>/` 下，并保持 `SKILL.md` 中的 `name` 与文件夹名一致。

## 贡献

欢迎提交 Issue 或 Pull Request。

提交新 Skill 时，请确保：

1. 目录位于 `skills/<skill-name>/`
2. 包含合法的 `SKILL.md`，且 `name`、`description` 完整
3. 不包含敏感信息
4. 如有脚本，说明运行环境和依赖

## License

本项目采用 [MIT License](./LICENSE)。