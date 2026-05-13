# 需求总控文件

> 本文件是需求从创建到上线的唯一入口，串联所有阶段文档，也是需求确认与待确认事项的唯一维护入口。

## 需求基础信息

| 字段 | 内容 |
|------|------|
| 需求名称 | {{NAME}} |
| 需求ID | {{ID}} |
| 需求来源 | {{SOURCE_TYPE: TAPD|Wiki|Figma|设计截图/交互说明|用户沟通|市场调研|产品规划|混合来源}} |
| 来源链接 | {{LINK}} |
| 优先级 | {{PRIORITY: P0|P1|P2}} |
| 状态 | {{STATUS: 分析中|技术设计中|开发中|测试中|已上线}} |
| 创建日期 | {{DATE}} |
| 最后更新 | {{UPDATE_DATE}} |

---

## 上游阶段来源

> 说明：来源阶段如果为"市场调研"或"产品规划"，则在这里记录引用和关键结论摘要，避免本需求重复分析。

| 上游阶段 | 是否使用 | 产物引用 | 关键结论摘要 |
|----------|----------|----------|-------------|
| 市场调研 `deepresearch` | {{USE_RESEARCH: 是|否|跳过}} | {{RESEARCH_REF}} | {{RESEARCH_SUMMARY}} |
| 产品规划 `product-planning` | {{USE_PLANNING: 是|否|跳过}} | {{PLANNING_REF}} | {{PLANNING_SUMMARY}} |

---

## 阶段文档引用

| 阶段 | 文档 | 状态 | 更新时间 |
|------|------|------|----------|
| 需求分析 | [prd-{{name}}.md](prd/prd-{{name}}.md) | {{PRD_STATUS: 进行中|已确认}} | {{PRD_UPDATED_AT}} |
| 技术方案 | [tech-{{name}}.md](tech/tech-{{name}}.md) | {{TECH_STATUS: 待开始|进行中|已评审}} | {{TECH_UPDATED_AT}} |
| 开发 | [dev-{{name}}.md](dev/dev-{{name}}.md) | {{DEV_STATUS: 待开始|进行中|已完成}} | {{DEV_UPDATED_AT}} |
| 测试 | [test-{{name}}.md](test/test-{{name}}.md) | {{TEST_STATUS: 待开始|进行中|已验收}} | {{TEST_UPDATED_AT}} |
| 上线 | [release-{{name}}.md](release/release-{{name}}.md) | {{RELEASE_STATUS: 待开始|进行中|已完成}} | {{RELEASE_UPDATED_AT}} |

---

## 下游交接状态

> 说明：PRD 定稿后，若进入原型设计阶段，检查是否需要调用 `prototype-fxui`。

| 下游阶段 | 当前是否需要 | 已准备信息 | 交接状态 |
|----------|-------------|-----------|----------|
| 产品原型 `prototype-fxui` | {{NEED_PROTOTYPE: 是|否|待定}} | {{PROTOTYPE_INPUT_READY}} | {{PROTOTYPE_STATUS: 待交接|已交接|跳过}} |

---

## 当前进度

- **当前阶段**：{{CURRENT_PHASE: 需求分析|需求确认|PRD草稿|PRD定稿|技术设计|开发|测试|上线}}
- **当前结论**：{{CURRENT_CONCLUSION: 信息收集中|待确认中|可输出草稿|可输出正式PRD|已转技术阶段}}
- **下一步行动**：{{NEXT_ACTION}}

### 阶段流转说明

1. **PRD 阶段**（分析中 → 已确认）
   - PRD 文档完成并确认后，更新状态为"已确认"。
   - 若需要原型表达，调用 `prototype-fxui`。
   - 下一步：进入技术方案设计阶段。
2. **技术方案阶段**（待开始 → 已评审）
3. **后续阶段**（开发 → 测试 → 上线）

---

## 原始输入与来源摘要

### 原始需求
{{RAW_REQUIREMENT}}

### 来源摘要

| 来源类型 | 链接 / 标识 | 摘要 | 是否已核对 |
|----------|-------------|------|------------|
| {{SOURCE_TYPE: TAPD|Wiki|Figma|设计截图/交互说明|用户沟通|市场调研|产品规划|其他}} | {{SOURCE_REF}} | {{SOURCE_SUMMARY}} | {{IS_VERIFIED: 是|否}} |

---

## 已确认信息表

| 编号 | 类别 | 内容 | 确认来源 | 确认时间 |
|------|------|------|----------|----------|
| C1 | {{CATEGORY: 背景|目标|用户|场景|范围|验收|约束|风险|上线}} | {{CONTENT}} | {{CONFIRM_SOURCE: 用户|TAPD|Wiki|Figma|设计截图/交互说明|市场调研|产品规划|历史记录}} | {{CONFIRM_TIME}} |

---

## 待确认事项表

| 编号 | 优先级 | 类别 | 待确认问题 | 当前假设 / 缺口 | 风险 | 状态 |
|------|--------|------|------------|------------------|------|------|
| T1 | {{PRIORITY: P0|P1|P2}} | {{CATEGORY: 背景|目标|用户|场景|范围|验收|约束|风险|上线}} | {{QUESTION}} | {{CURRENT_GAP_OR_ASSUMPTION}} | {{RISK_LEVEL: 高|中|低}} | {{ITEM_STATUS: 待确认|已确认|已废弃}} |

> 规则：任何推断、模糊描述、未明确边界，都必须先进入此表，再等待用户确认。

---

## 阻塞项

> 只有当 P0 阻塞项清空，或用户明确接受"带待确认项的草稿"时，才能继续输出完整 PRD。

| 编号 | 阻塞说明 | 影响 | 解决方式 | 状态 |
|------|----------|------|----------|------|
| B1 | {{BLOCKER_DESC}} | {{BLOCKER_IMPACT}} | {{RESOLUTION_PLAN}} | {{BLOCKER_STATUS: 未解决|处理中|已解决}} |

---

## 下一轮待提问清单

1. {{QUESTION_1}}
2. {{QUESTION_2}}
3. {{QUESTION_3}}

---

## 核心目标

- 目标1：{{GOAL_1}}
- 目标2：{{GOAL_2}}

---

## 关键里程碑

| 里程碑 | 计划日期 | 实际日期 | 状态 |
|--------|----------|----------|------|
| PRD 评审 | {{PRD_REVIEW_PLAN}} | {{PRD_REVIEW_ACTUAL}} | {{PRD_REVIEW_STATUS}} |
| 技术方案评审 | {{TECH_REVIEW_PLAN}} | {{TECH_REVIEW_ACTUAL}} | {{TECH_REVIEW_STATUS}} |
| 开发完成 | {{DEV_DONE_PLAN}} | {{DEV_DONE_ACTUAL}} | {{DEV_DONE_STATUS}} |
| 测试验收 | {{TEST_ACCEPT_PLAN}} | {{TEST_ACCEPT_ACTUAL}} | {{TEST_ACCEPT_STATUS}} |
| 上线发布 | {{RELEASE_PLAN}} | {{RELEASE_ACTUAL}} | {{RELEASE_MILESTONE_STATUS}} |

---

## 重要决策

| 时间 | 决策项 | 决策 | 决策人 |
|------|--------|------|--------|
| {{DECISION_TIME}} | {{DECISION_TOPIC}} | {{DECISION_RESULT}} | {{DECISION_OWNER}} |

---

## 版本变更

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| v1.0 | {{CHANGE_DATE}} | {{CHANGE_LOG}} | {{CHANGE_OWNER}} |
