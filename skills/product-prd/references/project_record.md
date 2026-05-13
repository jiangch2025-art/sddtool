# 项目总控文件

> 本文件是项目的唯一顶层入口，追踪所有阶段产物的状态和流转。

## 项目基础信息

| 字段 | 内容 |
|------|------|
| 项目名称 | {{NAME}} |
| 项目ID | {{ID}} |
| 创建日期 | {{DATE}} |
| 最后更新 | {{UPDATE_DATE}} |
| 当前阶段 | {{CURRENT_STAGE: 市场调研|产品规划|需求分析|原型设计|技术方案|开发|测试|上线}} |

---

## 阶段流转总览

| 阶段 | Skill | 状态 | 产物 | 最后更新 |
|------|-------|------|------|----------|
| 市场调研 | `deepresearch` | {{RESEARCH_STATUS: 跳过|待开始|进行中|已完成}} | {{RESEARCH_OUTPUT}} | {{RESEARCH_DATE}} |
| 产品规划 | `product-planning` | {{PLANNING_STATUS: 跳过|待开始|进行中|已完成}} | {{PLANNING_OUTPUT}} | {{PLANNING_DATE}} |
| 需求分析 | `product-prd` | {{PRD_STATUS: 待开始|进行中|已完成}} | {{PRD_OUTPUT}} | {{PRD_DATE}} |
| 原型设计 | `prototype-fxui` | {{PROTOTYPE_STATUS: 跳过|待开始|进行中|已完成}} | {{PROTOTYPE_OUTPUT}} | {{PROTOTYPE_DATE}} |
| 技术方案 | - | {{TECH_STATUS: 待开始|进行中|已完成}} | {{TECH_OUTPUT}} | {{TECH_DATE}} |
| 开发 | - | {{DEV_STATUS: 待开始|进行中|已完成}} | {{DEV_OUTPUT}} | {{DEV_DATE}} |
| 测试 | - | {{TEST_STATUS: 待开始|进行中|已完成}} | {{TEST_OUTPUT}} | {{TEST_DATE}} |
| 上线 | - | {{RELEASE_STATUS: 待开始|进行中|已完成}} | {{RELEASE_OUTPUT}} | {{RELEASE_DATE}} |

---

## 当前进度

- **当前阶段**：{{CURRENT_STAGE}}
- **当前结论**：{{CURRENT_CONCLUSION}}
- **下一步行动**：{{NEXT_ACTION}}

---

## 重要决策

| 时间 | 决策项 | 决策 | 决策人 |
|------|--------|------|--------|
| {{DECISION_TIME}} | {{DECISION_TOPIC}} | {{DECISION_RESULT}} | {{DECISION_OWNER}} |

---

## 版本变更

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| v1.0 | {{CHANGE_DATE}} | 初始创建 | - |
