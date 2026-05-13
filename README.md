# Claude Code Skills 套件

  本仓库提供一套可复用的 Claude Code
  Skills，面向日常研发与协作场景，帮助团队在需求拆解、实现执行、代码评审和质量检查等环节提升效率与一致性。

  ---

  ## 仓库目标

  - 统一技能组织方式与命名规范
  - 降低团队使用 Claude Code Skills 的门槛
  - 通过 Git 进行版本化管理与发布
  - 支持后续扩展业务技能与团队私有技能

  ---

  ## 目录建议

  ```text
  .
  ├─ skills/                  # 技能定义（建议按领域分组）
  │  ├─ core/                 # 通用技能：plan / execute / review / security-review 等
  │  ├─ productivity/         # 效率类技能
  │  ├─ biz/                  # 业务类技能（可选）
  │  └─ ...
  ├─ examples/                # 示例输入与使用案例（可选）
  ├─ docs/                    # 补充文档（可选）
  └─ README.md

  ▎ 如当前项目目录与上述不一致，可按实际结构调整本节内容。

  ---
  技能范围（示例）

  本套件可包含但不限于以下能力：

  - 需求到实现：/plan、/execute
  - 代码质量：/review、/security-review
  - 配置与效率：/update-config、/fewer-permission-prompts
  - 其他团队定制技能（按实际情况补充）

  ---
  使用方式

  在 Claude Code 中通过斜杠命令调用技能：

  /plan
  /execute
  /review
  /security-review

  如技能支持参数：

  /<skill-name> <args>

  ---
  发布流程（Git）

  1) 检查变更

  git status
  git diff

  2) 提交代码

  git add .
  git commit -m "release: publish skills bundle v1.0.0"

  3) 打标签并推送（推荐）

  git tag v1.0.0
  git push origin main --tags

  ---
  版本管理建议

  采用语义化版本（SemVer）：

  - MAJOR：不兼容变更（如技能名、参数协议变化）
  - MINOR：新增技能或向后兼容增强
  - PATCH：修复与文档更新

  ---
  协作约定（建议）

  - 新增技能需附最小示例（输入/输出预期）
  - 修改已有技能需说明兼容性影响
  - 合并前至少完成一次自测与一次评审
  - 重要变更建议在 PR 中附迁移说明

  ---
  Roadmap（可选）

  - 增加技能结构与字段自动校验
  - 增加变更日志自动生成
  - 增加更多业务场景模板

  ---
  License

  MIT
