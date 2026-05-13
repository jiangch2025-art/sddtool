# PRD 模板

> 版本：v1.0 | 创建日期：{{DATE}}
> 需求来源：{{SOURCE: 市场调研|产品规划|TAPD|Wiki|Figma|设计截图/交互说明|用户沟通|混合来源}}
> 优先级：{{PRIORITY: P0|P1|P2}}
> 文档状态：{{DOC_STATUS: 草稿|待确认|已确认}}

---

## 0. 工作区（未定稿前保留，定稿后清理）

> 作用：记录当前做到哪里、为什么中断、下一步该做什么。任何人重新打开此 PRD，都应先阅读本节再继续工作。

### 0.1 中断恢复卡

- **当前阶段**：{{WORK_PHASE: 来源收集|事实抽取|问题确认|PRD骨架|PRD补全|PRD定稿}}
- **当前状态**：{{WORK_STATUS: 进行中|待确认|阻塞中|待续写|已定稿}}
- **最后完成步骤**：{{LAST_COMPLETED_STEP}}
- **当前中断点**：{{INTERRUPTION_POINT}}
- **下一步动作**：{{NEXT_ACTION}}
- **继续前检查**：{{RESUME_CHECKLIST}}
- **最后更新**：{{LAST_UPDATED_AT}}
- **责任人**：{{OWNER}}

### 0.2 本轮输出决策

- **输出级别**：{{OUTPUT_LEVEL: 仅待确认清单|PRD骨架+待确认项|完整PRD}}
- **选择原因**：{{OUTPUT_DECISION_REASON}}
- **当前不可继续的原因**：{{CANNOT_CONTINUE_REASON}}
- **完成条件**：{{DONE_CRITERIA}}

### 0.3 上游阶段摘要

> 若需求来自上游市场调研或产品规划阶段，在此记录引用与关键结论；若跳过，标记为"跳过"。

| 上游阶段 | 是否使用 | 产物引用 | 关键结论 |
|----------|----------|----------|----------|
| 市场调研 `deepresearch` | {{USE_RESEARCH: 是|否|跳过}} | {{RESEARCH_REF}} | {{RESEARCH_SUMMARY}} |
| 产品规划 `product-planning` | {{USE_PLANNING: 是|否|跳过}} | {{PLANNING_REF}} | {{PLANNING_SUMMARY}} |

### 0.4 来源摘要

| 来源类型 | 链接 / 标识 | 已获取信息 | 可信度 |
|----------|-------------|------------|--------|
| {{SOURCE_TYPE_1: 市场调研|产品规划|TAPD|Wiki|Figma|设计截图/交互说明|用户沟通|其他}} | {{SOURCE_REF_1}} | {{SOURCE_FACTS_1}} | {{SOURCE_CONFIDENCE_1: 高|中|低}} |
| {{SOURCE_TYPE_2: 市场调研|产品规划|TAPD|Wiki|Figma|设计截图/交互说明|用户沟通|其他}} | {{SOURCE_REF_2}} | {{SOURCE_FACTS_2}} | {{SOURCE_CONFIDENCE_2: 高|中|低}} |

### 0.5 设计 / 交互分析摘要

- **是否包含设计输入**：{{HAS_DESIGN_INPUT: 是|否}}
- **设计分析状态**：{{DESIGN_STATUS: 未开始|进行中|已完成|阻塞}}
- **设计来源类型**：{{DESIGN_SOURCE_TYPE: Figma MCP|设计截图/交互说明|混合来源|待确认}}
- **MCP 可用性**：{{FIGMA_MCP_STATUS: 可用|不可用|不适用|待确认}}
- **设计文件 / 截图链接**：{{DESIGN_LINK}}
- **Figma fileKey**：{{FIGMA_FILE_KEY}}
- **Figma nodeId**：{{FIGMA_NODE_ID}}
- **页面 / Frame 范围**：{{DESIGN_SCOPE}}
- **主流程摘要**：{{DESIGN_MAIN_FLOW}}
- **关键交互点**：{{DESIGN_KEY_INTERACTIONS}}
- **异常态 / 空态 / 成功态**：{{DESIGN_STATES}}
- **使用工具 / 来源**：{{DESIGN_TOOLING: mcp__figma__get_figma_data|mcp__figma__download_figma_images|人工粘贴|截图分析|其他}}
- **当前阻塞**：{{DESIGN_BLOCKER}}
- **阻塞处理**：若暂时无法获取设计输入，则在此记录阻塞原因，并暂停输出完整 PRD。

### 0.6 已确认事实快照

| 类别 | 结论 | 来源 |
|------|------|------|
| 背景 | {{CONFIRMED_BACKGROUND}} | {{BACKGROUND_SOURCE: 用户|市场调研|产品规划|TAPD|Wiki|Figma|混合来源}} |
| 目标 | {{CONFIRMED_GOAL}} | {{GOAL_SOURCE: 用户|市场调研|产品规划|TAPD|Wiki|Figma|混合来源}} |
| 用户 | {{CONFIRMED_USER}} | {{USER_SOURCE: 用户|市场调研|产品规划|TAPD|Wiki|Figma|混合来源}} |
| 场景 | {{CONFIRMED_SCENARIO}} | {{SCENARIO_SOURCE: 用户|市场调研|产品规划|TAPD|Wiki|Figma|混合来源}} |
| 范围 | {{CONFIRMED_SCOPE}} | {{SCOPE_SOURCE: 用户|市场调研|产品规划|TAPD|Wiki|Figma|混合来源}} |
| 验收 | {{CONFIRMED_ACCEPTANCE}} | {{ACCEPTANCE_SOURCE: 用户|市场调研|产品规划|TAPD|Wiki|Figma|混合来源}} |

### 0.7 待确认问题

| 编号 | 优先级 | 问题 | 当前假设 / 缺口 | 状态 |
|------|--------|------|------------------|------|
| Q1 | {{Q1_PRIORITY: P0|P1|P2}} | {{QUESTION_1}} | {{Q1_GAP}} | {{Q1_STATUS: 待确认|已确认|阻塞}} |
| Q2 | {{Q2_PRIORITY: P0|P1|P2}} | {{QUESTION_2}} | {{Q2_GAP}} | {{Q2_STATUS: 待确认|已确认|阻塞}} |
| Q3 | {{Q3_PRIORITY: P0|P1|P2}} | {{QUESTION_3}} | {{Q3_GAP}} | {{Q3_STATUS: 待确认|已确认|阻塞}} |

### 0.8 阻塞与风险

| 类型 | 说明 | 影响 | 处理方式 |
|------|------|------|----------|
| 阻塞 | {{BLOCKER_1}} | {{BLOCKER_IMPACT_1}} | {{BLOCKER_ACTION_1}} |
| 风险 | {{RISK_1}} | {{RISK_IMPACT_1}} | {{RISK_ACTION_1}} |

### 0.9 原型准备（衔接 `prototype-fxui`）

> 当 PRD 需要生成 HTML 原型时，在此记录已准备好的原型输入信息；若尚未进入原型阶段，可暂时留空。

| 项目 | 内容 |
|------|------|
| 页面清单 | {{PAGE_LIST}} |
| 布局类型 | {{LAYOUT_TYPE: 三栏CRM|两栏管理后台|弹窗|详情页|其他}} |
| 主操作流程 | {{MAIN_FLOW}} |
| 关键字段与控件 | {{KEY_FIELDS}} |
| 状态与异常反馈 | {{STATES_AND_FEEDBACK}} |
| 是否需要原型 | {{NEED_PROTOTYPE: 是|否|待定}} |
| 原型交接状态 | {{PROTOTYPE_STATUS: 待交接|已交接|跳过}} |

### 0.10 草稿编写约束

- 仅将已确认信息写为确定结论。
- 未确认内容统一标记为 `待确认`，不得伪造细节。
- 若待确认项较多，优先维护工作区和需求总控文件，不强行补全本 PRD。
- PRD 未定稿前，必须保留"工作区"；PRD 定稿后，清理本节或迁移到附录。

---

# 一、需求概述

## 1.1 当前信息完备度

| 项目 | 状态 | 说明 |
|------|------|------|
| 背景 | {{BACKGROUND_STATUS: 已确认|待确认}} | {{BACKGROUND_NOTE}} |
| 目标 | {{GOAL_STATUS: 已确认|待确认}} | {{GOAL_NOTE}} |
| 用户 | {{USER_STATUS: 已确认|待确认}} | {{USER_NOTE}} |
| 场景 | {{SCENARIO_STATUS: 已确认|待确认}} | {{SCENARIO_NOTE}} |
| 范围 | {{SCOPE_STATUS: 已确认|待确认}} | {{SCOPE_NOTE}} |
| 验收标准 | {{ACCEPTANCE_STATUS: 已确认|待确认}} | {{ACCEPTANCE_NOTE}} |

## 1.2 需求业务场景

1. 需求场景：{{SCENARIO}}
2. 图示介绍：{{DIAGRAM}}
3. 设计图 / 交互图引用：{{DESIGN_ARTIFACTS}}

## 1.3 需求竞品现状

{{COMPETITOR_ANALYSIS}}

## 1.4 产品价值

1. 整体解决了 {{TARGET_SCENARIO}} 场景的问题
2. {{VALUE_POINT_2}}

## 1.5 待确认事项

1. 待确认：{{OPEN_QUESTION_1}}
2. 待确认：{{OPEN_QUESTION_2}}
3. 待确认：{{OPEN_QUESTION_3}}

---

# 二、产品方案

## 2.1 整体方案

1. 方案描述：{{OVERALL_DESCRIPTION}}
2. 方案整体图示及关键业务流程：{{OVERALL_DIAGRAM}}
3. 设计图与交互图：{{INTERACTION_DIAGRAMS}}
4. 涉及对象间的关系架构说明：{{ARCHITECTURE}}

## 2.2 功能 1：{{FEATURE_1_NAME}}

### 2.2.1 {{SUB_FEATURE_1_1}}

1. 方案说明：{{DESCRIPTION_1_1}}
2. 交互图示：{{INTERACTION_1_1}}
3. 需求逻辑（Use Case）：{{USE_CASE_1_1}}

> **Use Case 描述规范**：根据场景复杂度选择格式
>
> **场景简单**（CRUD 类）→ 使用表格版：
> | 编号 | 场景 | 描述 | 参与者 | 前置条件 | 后置条件 |
> |------|------|------|--------|----------|----------|
> | UC-01 | 新增客户 | 填写表单保存客户信息 | 销售人员 | 登录系统 | 客户创建成功 |
>
> **场景复杂**（有分支 / 异常）→ 使用叙事版：
> ### UC-01 新增客户
> **参与者**：销售人员
> **前置条件**：用户已登录、有客户新增权限
> **基本流程**：
> 1. 用户进入客户管理页面
> 2. 点击"新增"按钮
> 3. 填写客户信息
> 4. 点击"保存"
> 5. 系统创建记录
> **备选流程**：
> - 4a. 校验失败 → 提示错误信息
> **后置条件**：客户记录创建成功

### 2.2.2 {{SUB_FEATURE_1_2}}

1. 方案说明：{{DESCRIPTION_1_2}}
2. 交互图示：{{INTERACTION_1_2}}
3. 需求逻辑（Use Case）：{{USE_CASE_1_2}}

> 参考上方 UC 描述规范

## 2.3 功能 2：{{FEATURE_2_NAME}}

### 2.3.1 {{SUB_FEATURE_2_1}}

1. 方案说明：{{DESCRIPTION_2_1}}
2. 交互图示：{{INTERACTION_2_1}}
3. 需求逻辑（Use Case）：{{USE_CASE_2_1}}

> 参考上方 UC 描述规范

### 2.3.2 {{SUB_FEATURE_2_2}}

1. 方案说明：{{DESCRIPTION_2_2}}
2. 交互图示：{{INTERACTION_2_2}}
3. 需求逻辑（Use Case）：{{USE_CASE_2_2}}

> 参考上方 UC 描述规范

---

# 三、其他说明

## 3.1 平台能力支持

### 3.1.1 沙盒 / 更改集能力

> 附：原则上，凡是新增的配置项，均需要支持沙盒 / 更改集。

- 沙盒 / 更改集支持：{{SANDBOX_SUPPORT: 是|否|待确认}}
- 说明：{{SANDBOX_NOTE}}

### 3.1.2 多语、国际化能力支持

> 附：原则上，新增的对象、操作界面，均需要支持多语 / 国际化。

| 能力项 | 是否需要 | 说明 |
|--------|----------|------|
| 接入翻译工作台 | {{TRANSLATION_WORKBENCH: 是|否|待确认}} | 词条类别：{{TRANSLATION_WORKBENCH_NOTE}} |
| CRM 提醒 | {{CRM_NOTICE: 是|否|待确认}} | 内容：{{CRM_NOTICE_NOTE}} |
| 企信消息提醒 | {{IM_NOTICE: 是|否|待确认}} | 内容：{{IM_NOTICE_NOTE}} |
| 修改记录 | {{CHANGE_LOG_SUPPORT: 是|否|待确认}} | {{CHANGE_LOG_NOTE}} |
| 审计日志 | {{AUDIT_LOG_SUPPORT: 是|否|待确认}} | {{AUDIT_LOG_NOTE}} |
| 支持快捷翻译能力 | {{QUICK_TRANSLATION_SUPPORT: 是|否|待确认}} | {{QUICK_TRANSLATION_NOTE}} |
| 支持数据多语能力 | {{DATA_I18N_SUPPORT: 是|否|待确认}} | {{DATA_I18N_NOTE}} |
| 预置配置多语 | {{PRESET_CONFIG_I18N: 是|否|待确认}} | 由产品经理在模板企业中配置：{{PRESET_CONFIG_I18N_NOTE}} |
| 预置示例数据多语 | {{PRESET_SAMPLE_I18N: 是|否|待确认}} | 由产品经理在模板企业中配置：{{PRESET_SAMPLE_I18N_NOTE}} |
| 多币种 | {{MULTI_CURRENCY: 是|否|待确认}} | {{MULTI_CURRENCY_NOTE}} |
| 多时区 | {{MULTI_TIMEZONE: 是|否|待确认}} | {{MULTI_TIMEZONE_NOTE}} |
| 国际地图 | {{GLOBAL_MAP: 是|否|待确认}} | {{GLOBAL_MAP_NOTE}} |

### 3.1.3 操作日志说明

> 附：原则上，新增的对象、配置等，均需要日志记录。

- 操作日志支持：{{OPERATION_LOG_SUPPORT: 是|否|待确认}}
- 日志内容说明：{{LOG_CONTENT}}

### 3.1.4 新对象 / 新字段做流程、BI 分析申请

| 申请项 | 是否需要 | 说明 |
|--------|----------|------|
| BI 分析支持 | {{BI_SUPPORT: 是|否|待确认}} | {{BI_SUPPORT_NOTE}} |
| 流程支持 | {{FLOW_SUPPORT: 是|否|待确认}} | {{FLOW_SUPPORT_NOTE}} |

### 3.1.5 新增预置图表 / 驾驶舱

- 预置图表 / 驾驶舱：{{DASHBOARD_SUPPORT: 是|否|待确认}}
- 说明：{{DASHBOARD_NOTE}}

## 3.2 需求风险点检测

> 说明：任何需求，务必思考本次发布可能会产生的风险点。若信息不足，应明确标记为待确认。

| ID | 风险分组 | 风险类型 | 有无风险 | 功能点 | 影响企业数 | 是否报备 | 响应策略 |
|----|----------|----------|----------|--------|------------|----------|----------|
| 1 | 对现逻辑有影响的风险点 | 交互体验有变化 | {{RISK_1_FLAG: 是|否|待确认}} | {{RISK_1_FEATURE}} | {{RISK_1_TENANT_IMPACT}} | {{RISK_1_REPORT: 是|否|待确认}} | {{RISK_1_ACTION}} |
| 2 | 对现逻辑有影响的风险点 | 功能有减少 | {{RISK_2_FLAG: 是|否|待确认}} | {{RISK_2_FEATURE}} | {{RISK_2_TENANT_IMPACT}} | {{RISK_2_REPORT: 是|否|待确认}} | {{RISK_2_ACTION}} |
| 3 | 对现逻辑有影响的风险点 | 功能逻辑的调整 | {{RISK_3_FLAG: 是|否|待确认}} | {{RISK_3_FEATURE}} | {{RISK_3_TENANT_IMPACT}} | {{RISK_3_REPORT: 是|否|待确认}} | {{RISK_3_ACTION}} |
| 4 | 对现逻辑有影响的风险点 | 其他 | {{RISK_4_FLAG: 是|否|待确认}} | {{RISK_4_FEATURE}} | {{RISK_4_TENANT_IMPACT}} | {{RISK_4_REPORT: 是|否|待确认}} | {{RISK_4_ACTION}} |
| 5 | 新能力风险点 | 逻辑不完善 | {{RISK_5_FLAG: 是|否|待确认}} | {{RISK_5_FEATURE}} | {{RISK_5_TENANT_IMPACT}} | {{RISK_5_REPORT: 是|否|待确认}} | {{RISK_5_ACTION}} |
| 6 | 新能力风险点 | 性能压力 | {{RISK_6_FLAG: 是|否|待确认}} | {{RISK_6_FEATURE}} | {{RISK_6_TENANT_IMPACT}} | {{RISK_6_REPORT: 是|否|待确认}} | {{RISK_6_ACTION}} |
| 7 | 新能力风险点 | 其他 | {{RISK_7_FLAG: 是|否|待确认}} | {{RISK_7_FEATURE}} | {{RISK_7_TENANT_IMPACT}} | {{RISK_7_REPORT: 是|否|待确认}} | {{RISK_7_ACTION}} |

报备对象：{{RISK_OWNER}}

## 3.3 上线策略

### 3.3.1 适用版本

| 项目 | 选择 |
|------|------|
| 新增功能 | {{NEW_FEATURE_RELEASE: 是|否|待确认}} |
| 功能优化 | {{OPTIMIZATION_RELEASE: 是|否|待确认}} |

### 3.3.2 收费标准

- 收费模式：{{PRICING_MODE: 不收费|收费|待确认}}
- 收费策略：{{PRICING_STRATEGY}}

### 3.3.3 上线节奏

- 上线方式：{{RELEASE_MODE: 全网|灰度|待确认}}
- 灰度发布的原因：{{GRAY_REASON}}
- 预计全网时机：{{FULL_RELEASE_TIME}}
- 灰度批次：{{GRAY_BATCHES}}

### 3.3.4 老客户升级策略

> 若需求方案涉及老功能改造，请分析并写明对老客户的升级策略。

- 是否涉及老客户升级：{{UPGRADE_REQUIRED: 是|否|待确认}}
- 升级策略：{{UPGRADE_STRATEGY}}

---

# 四、需求埋点

| 模块 | 埋点名称 | 事件类型 | 参数1 | 参数2 | 参数3 | 参数4 | 参数5 |
|------|----------|----------|-------|-------|-------|-------|-------|
| {{MODULE}} | {{EVENT_NAME}} | {{EVENT_TYPE: 点击|曝光|提交|成功|失败|其他}} | {{PARAM_1}} | {{PARAM_2}} | {{PARAM_3}} | {{PARAM_4}} | {{PARAM_5}} |

---

# 附录

## 附录 A：词汇表

| 术语 | 定义 |
|------|------|
| {{TERM}} | {{DEFINITION}} |

## 附录 B：关联文档

| 文档名称 | 链接 |
|----------|------|
| {{DOC_NAME}} | {{DOC_LINK}} |
