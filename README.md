# Claude Code Skills — B端产品标准流程技能包

面向 纷享销客 CRM 的 B 端产品全流程技能套件，覆盖 **市场调研 → 产品规划 → 产品需求 → 产品原型** 四个阶段，每个阶段可独立使用，也可串联协作。

## 技能列表

| 阶段 | 技能 | 说明 |
|------|------|------|
| 1. 市场调研 | `deepresearch` | 结构化盘问 → 并行研究 → 交叉验证，输出可被产品规划直接消费的调研结论 |
| 2. 产品规划 | `product-planning` | 方向收敛、多方案比较、BMAD 对抗式盘问，输出产品定位、能力边界与版本路线 |
| 3. 产品需求 | `product-prd` | 从 TAPD / Wiki / Figma / 用户沟通等来源，通过盘问→打磨→唯一写作输出 PRD |
| 4. 产品原型 | `prototype-fxui` | 基于 纷享销客 FXUI 设计系统生成可运行的 HTML 原型，支持截图分析还原 |

## 目录结构

```
.
├── skills/
│   ├── deepresearch/       # 市场调研技能
│   ├── product-planning/   # 产品规划技能
│   ├── product-prd/        # 产品需求技能
│   └── prototype-fxui/     # FXUI 原型生成技能
│       ├── examples/       # 示例 HTML 原型
│       ├── references/     # 参考页面模板
│       └── scripts/        # 截图分析脚本
└── README.md
```

## 使用方式

在 Claude Code 中通过斜杠命令调用：

```
/deepresearch           # 市场调研
/product-planning       # 产品规划
/product-prd            # 产品需求
/prototype-fxui         # 生成原型
```

简单需求可跳过调研与规划，直接进入 `product-prd`；纯后台需求可跳过原型阶段。

## 版本管理

采用语义化版本（SemVer），通过 Git 发布：

- **MAJOR** — 不兼容变更（技能名、参数协议变化）
- **MINOR** — 新增技能或向后兼容增强
- **PATCH** — 修复与文档更新

## License

MIT
