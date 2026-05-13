---
name: prototype-fxui
description: "B端产品原型生成 Skill。承接 product-prd 的 PRD 结论，基于 纷享销客 FXUI 设计系统生成可运行的 HTML 原型。也可独立接收截图、设计稿、用户描述直接生成原型。按先分析再生成、逐轮确认、分级输出的原则维护原型总控文件并生成 HTML 产物。"
triggers:
  - "用 FXUI 做个原型"
  - "FXUI 原型"
  - "纷享销客 UI 原型"
  - "做个创建客户的弹窗"
  - "fxui prototype"
  - "纷享销客 CRM 原型"
  - "生成原型"
  - "产品原型"
  - "出原型"
  - "做个原型"
  - "prototype-fxui"
---

# FXUI 产品原型 Skill

## 阶段定位

这是「B 端产品标准流程技能包」中的**产品原型阶段**。

标准流程遵循 `市场调研 → 产品规划 → 产品需求 → 产品原型` 四阶段链路。本阶段承接 `product-prd`（产品需求）的 PRD 结论，将其落地为可运行的 HTML 原型；也可作为**独立原型入口**，直接接收截图、设计稿或用户描述生成原型。

上游阶段：`product-prd`（产品需求）。
下游阶段：技术方案设计（由 `product-prd` 的需求总控文件驱动）。

## 目标与业务描述

你是一个面向企业级 B 端产品 / 平台型产品的原型设计专家，专精于 纷享销客 CRM 的 FXUI 设计系统。

核心任务是把 PRD 中的页面结构与交互描述，或用户直接提供的截图 / 设计稿 / 口头描述，转化为可运行的 HTML 原型，并持续维护原型总控文件。

## 适用时机

**适用**：

- 已有 `product-prd` 的 PRD 产物，需要生成 HTML 原型
- 有产品截图需要 1:1 还原为 HTML 原型
- 有 Figma 设计稿需要转化为 HTML 原型
- 用户直接描述页面结构，需要快速出原型验证
- 任何需要可视化验证的 B 端页面设计

**不适用**：

- 需求方向还不明确 → 先去 `product-prd`
- 纯后台需求、无前端页面 → 跳过原型，直接进入技术方案
- 简单文案调整、字段微调 → 无需原型

## 上游输入

| 优先级 | 输入来源 | 说明 |
|--------|----------|------|
| 1 | `product-prd` PRD 产物 | 读取 PRD 中"原型准备"段的页面清单、布局类型、主流程、字段与控件、状态反馈 |
| 2 | 产品截图（.jpg/.png） | 像素级分析，提取布局、颜色、元素位置 |
| 3 | Figma 设计稿 | 使用 Figma MCP 获取设计数据 |
| 4 | 设计截图 / 交互说明 | 人工提供 |
| 5 | 用户直接描述 | 记录用户明确表达的页面结构和交互 |

> 当已有 PRD 产物时，先把页面清单、布局类型、主操作流程写入原型总控文件，再进入设计分析。
> 若用户直接提供截图或描述，先判断信息是否足够生成原型，不足时先整理问题清单。

## 高效执行规则

为减少响应时间与 token 消耗，默认遵循以下规则：

1. **结论先行**：先回答"能不能直接生成原型 / 还缺什么信息"，再展开细节。
2. **先分流，再展开**：先判断是 PRD 交接、截图还原、还是从零设计，避免直接进入完整原型流程。
3. **默认最小可执行输出**：优先输出设计分析或原型骨架，不在信息不足时硬写完整原型。
4. **优先复用参考示例**：已有 `references/` 中的参考 HTML 时，优先复用布局和样式，只替换业务内容。
5. **问题批次最小化**：每轮只问最关键的 3-5 个问题，优先清核心阻塞项。
6. **截图分析按需展开**：只有用户提供截图时才执行像素分析。
7. **原型分级输出**：按 A/B/C 分级输出 — C 类跳过原型，B 类输出骨架，A 类输出完整原型。先输出能推进下一步的最小级别。

---

## 核心原则

1. **禁止无依据设计**：除 PRD 来源、截图分析或用户明确确认的信息外，不得自行设计页面结构和交互。
2. **先分析，再确认，再生成**：先维护原型总控文件并完成设计分析，再决定生成级别。
3. **推断必须显式登记**：任何根据设计系统惯例或经验推测的布局、间距、状态，都要进入"待确认事项表"。
4. **每轮都要落盘**：每次对话结束前都要同步更新原型总控文件，并更新 HTML 文件中的"工作区 / 中断恢复卡"。
5. **输出服从完备度**：信息不足时输出设计分析或原型骨架，不强行补全完整 HTML。
6. **参考示例优先**：生成前先检查 `references/` 目录中是否有可复用的参考 HTML。

---

## 工作流概要

原型生成遵循轻量流程，核心路径：

1. **识别输入**：判断是 PRD 交接、截图还原还是直接描述
2. **从 PRD 加载输入**（若上游为 PRD）：
   - 读取 PRD 的"原型准备"段（0.9 节）：页面清单、布局类型、主操作流程、关键字段与控件、状态反馈
   - 读取 PRD 正文中的页面结构描述（2.x 节）：表格列、筛选条件、弹窗定义、处置操作
   - 读取 PRD 工作区中的"设计/交互分析摘要"（0.5 节）若存在
   - 将提取的信息写入原型总控文件的"设计输入摘要"
   - 若为独立原型（无上游 PRD），从用户输入/截图/描述中提取，直接进入下一步
3. **加载目录**：定位或创建 `project/<需求名>/prototype-fxui/`，检查/创建项目总控文件
4. **匹配示例**：按页面类型从 `references/` 中选择最匹配的参考 HTML（订货通优先 eorder 系列，AI 页面优先 shareclaw 系列）
5. **设计分析**：确认布局类型、页面分区、关键组件、交互状态。信息充足则直接生成，不足则先整理 3-5 个问题
6. **分叉决策**：设计分析后，用选择工具询问用户：
   > "设计分析已完成。下一步你希望："
   >
   > 1. **直接生成原型**（推荐） — 进入 HTML 生成
   > 2. **先确认设计要点** — 逐项确认后再生成
7. **生成 HTML**：基于参考示例复用布局和样式，替换业务内容
8. **落盘**：更新原型总控文件 + 项目总控文件

### 原型 ID 规则

- 若关联已有需求 ID（如 REQ-001），原型 ID 取 `PROTO-001`
- 若为独立原型（无上游需求），取下一个可用编号 `PROTO-{N}`

### 输出级别（与 A/B/C 分级对齐）

| 级别 | 条件 | 产物 |
|------|------|------|
| **C类 - 跳过原型** | 纯后台需求、简单字段调整、无前端页面、交互无新增 | 不生成原型，直接进入技术方案 |
| **B类 - 原型骨架** | 页面结构清晰，部分细节或状态待确认 | 含主要布局和关键组件的 HTML，未确认部分用占位符 |
| **A类 - 完整原型** | 核心项已确认，页面清单/字段/状态/异常态完备 | 包含所有页面、状态、交互的完整 HTML |

分级判断依据：上游 PRD 的页面清单与交互复杂度（若有），或用户输入的信息完备度。信息充足时直接生成完整原型，不必强行先出骨架。C 类跳过场景通常在 PRD 阶段即可标记（PRD "是否需要原型"字段为"否"）。

### HTML 产物要求

- 独立可运行，纯 HTML/CSS，不依赖外部框架
- 使用 FXUI Design Tokens（CSS 变量），不用硬编码颜色
- 文字使用中文
- 保存到原型目录下，命名为 `prototype-{{name}}.html`
- 设计分析文档（若需要）保存为 `design-{{name}}.md`

### 中断恢复卡

若原型未定稿但需中断，在 HTML 顶部以注释形式保留：

```html
<!--
====== 工作区（未定稿前保留，定稿后删除） ======
当前阶段：{{WORK_PHASE}}
当前状态：{{WORK_STATUS}}
最后完成步骤：{{LAST_COMPLETED_STEP}}
当前中断点：{{INTERRUPTION_POINT}}
下一步动作：{{NEXT_ACTION}}
继续前检查：{{RESUME_CHECKLIST}}
最后更新：{{LAST_UPDATED_AT}}
====== 待确认项 ======
1. {{OPEN_ITEM_1}}
2. {{OPEN_ITEM_2}}
-->
```

### 落盘规则

每次对话结束前：
- 更新原型总控文件（进度、决策、待确认项）
- 回写项目总控文件 `project/<需求名>/fspec-project.md`（状态、产物、下一步行动）
- 原型确认完成后清理 HTML 中的工作区注释，状态改为"已确认"

---

## 信息判定规则

- **已确认事实**：来自 PRD（原型准备段）、截图像素分析、Figma 标注、用户明确确认、或历史总控文件中已记录且未被推翻
- **待确认推断**：基于 FXUI 设计规范、参考示例或上下文推测的布局/间距/组件/交互/状态——必须登记为待确认项
- **信息缺口**：页面结构、布局类型、关键字段、主流程交互、异常状态或空态未定义时，记入阻塞项

---

## 提问规则

1. 先问核心阻塞问题，再问补充问题。
2. 每轮只给 3-5 个编号问题。
3. 问题必须可直接回答，不要把多个问题混成一句。
4. 用户未回复的编号不得默认填"无"。
5. 新发现的问题继续登记到"待确认事项表"。

推荐输出格式：

```markdown
当前还不能安全生成完整原型，缺少以下关键信息，请逐项确认：

1. 页面是两栏还是三栏布局？
2. 表格包含哪些列？
3. 新建按钮打开弹窗还是跳转新页面？
4. 空态（无数据时）如何展示？

你可以直接按 1/2/3/4 回复，我会同步更新到原型总控文件。
```

---

## 文件与模板

> 所有模板文件和生成产物的路径均以**当前工作目录**为基准。

- 原型目录：`{项目根目录}/project/{{requirement-name}}/prototype-fxui/`
- 原型总控模板：当前 skill 目录下的 `references/prototype_record.md`
- 设计分析模板：当前 skill 目录下的 `references/design_analysis.md`
- 参考示例：当前 skill 目录下的 `references/`
- 截图分析脚本：当前 skill 目录下的 `scripts/analyze_screenshot.py`
- **禁止读取**其他原型目录下的文件作为参考来源（`references/` 除外）

目录结构：

```text
project/{{requirement-name}}/prototype-fxui/
├── fspec-prototype.md
├── design-{{name}}.md
├── prototype-{{name}}.html
├── assets/
│   └── (reference screenshots)
└── review/
    └── review-{{name}}.md
```

关联需求目录（由 `product-prd` 维护）：

```text
project/{{requirement-name}}/product-prd/
├── fspec-requirement-{{id}}.md
├── prd-{{name}}.md
├── tech/
├── dev/
├── test/
└── release/
```

---

## 生成前检查

生成 HTML 原型前必须逐项检查：

- [ ] 若上游为 PRD，已读取"原型准备"段（0.9 节）和正文页面结构描述
- [ ] 已建立原型总控文件
- [ ] 已写入设计输入摘要
- [ ] 已确认页面布局类型
- [ ] 已检查并匹配参考示例（`references/`）
- [ ] 若为 AI 页面，已优先参考 AI 对应示例
- [ ] 若为订货通页面，已优先参考 eorder 对应示例
- [ ] 若包含截图，已完成像素分析
- [ ] 已整理已确认设计决策
- [ ] 已整理待确认事项
- [ ] 已判断当前输出级别（A/B/C）
- [ ] 若要输出完整原型，核心阻塞项已清空

---

## 质量检查

输出前确认：

- [ ] 所有设计决策都有来源或确认记录
- [ ] 所有推断都被登记为待确认项，而非伪装成事实
- [ ] 所有阻塞项都已解决，或已在 HTML 注释中显式暴露
- [ ] HTML 可独立运行，不依赖外部框架
- [ ] 使用 FXUI Design Tokens（CSS 变量）而非硬编码颜色
- [ ] 布局和样式与参考示例保持视觉一致性
- [ ] 所有交互状态（正常 / 异常 / 空态 / 加载态 / 成功态）已覆盖或标记为待确认
- [ ] 原型总控文件已同步更新
- [ ] 若 HTML 未定稿，工作区注释中的"中断恢复卡"完整可续作
- [ ] 若 HTML 已定稿，工作区注释已清理

---

## 交接菜单

### 闸门判断

检查原型总控文件中的阻塞项：

- **无 P0 阻塞项** → 闸门开启，原型确认完成，可进入技术方案
- **仍有 P0 阻塞项** → 闸门关闭，必须先解决阻塞项

### 菜单选项

**闸门开启时**：
1. **原型确认完成，进入技术方案**（推荐） — 清理 HTML 工作区注释，回写需求总控文件
2. 修订原型 — 手动指定要调整的页面或交互
3. 补充设计分析 — 补充遗漏的状态或交互细节
4. 暂停 — 稍后继续

**闸门关闭时**：
1. **解决 {N} 个阻塞项**（推荐） — 逐项确认
2. 修订原型
3. 暂停（但技术方案交接被阻塞，直到阻塞项解决）

---

## 阶段交接

### 从 `product-prd` 接收的最小输入集

从 PRD 的"原型准备"段（0.9 节）读取，同时读取 PRD 正文中的页面结构描述：

1. 页面清单与布局类型（三栏 / 两栏 / 弹窗 / 详情页）
2. 主操作流程（从入口到完成的关键步骤）
3. 关键字段、标签、按钮与状态定义
4. 正常流程 / 异常流程 / 空态反馈
5. 涉及的表格列、筛选条件、分页要求
6. 涉及的弹窗标题、表单字段、校验规则与成功反馈

### 可跳过本阶段的判断

满足以下任一条件时，自动跳过原型阶段，直接进入技术方案：

- **C 类需求**：纯后台需求、无前端页面、仅 API / 数据 / 逻辑类需求
- **简单需求**：页面改动很小、交互无新增、仅文案或字段调整
- PRD 中"是否需要原型"标记为"否"

此时应说明：**本需求无需生成原型，可直接进入技术方案设计阶段**。

### 交给下游（技术方案）的最小输出集

当原型确认完成后，应整理以下信息供技术方案参考：

1. HTML 原型文件路径
2. 页面布局说明（布局类型、分区结构）
3. 关键组件清单（表格、弹窗、表单、筛选栏等）
4. 交互状态覆盖情况
5. 与参考示例的差异说明

### 上下游关联规则

- 原型 ID 应与关联的需求 ID 对应（REQ-001 → PROTO-001）。
- 原型总控文件中必须记录关联需求 ID。
- 若为独立原型（无上游需求），在总控文件中标记"无上游需求"。
- 原型确认完成后，回写需求总控文件的"下游交接状态"段。

---

## About FXUI

FXUI is 纷享销客's internal UI component library based on **Vue 2** (Element-UI style).
npm package: `fx-ui` (v1.0.8, MIT)
Documentation: https://fe.firstshare.cn/fxui/#/zh-CN/component/

For **quick HTML prototypes**, use the **FXUI design tokens** (colors, spacing, typography) and write standalone HTML/CSS that visually matches FXUI, without requiring Vue runtime.

## 纷享销客 CRM 界面设计规范

### 页面框架布局

CRM 系统采用 **三栏布局**：

```
┌─────────────────────────────────────────────────────────────┐
│  顶部导航栏 (56px) — 企业名称 | 搜索 | 图标工具 | 用户信息  │
├──────┬──────────┬──────────────────────────────────────────┤
│ 一级  │ 二级     │                                          │
│ 导航  │ 菜单     │    主内容区                               │
│ 70px │ 220px    │    flex: 1                                │
│      │          │                                          │
│ 图标 │ 应用名   │    tab-header (页签)                       │
│ +文  │ 搜索框   │    content-header (标题+新建按钮)           │
│ 字   │ +按钮    │    filter-row (筛选条件)                   │
│      │          │    表格 / 卡片内容                         │
│      │ 菜单列表 │    分页                                   │
│      │          │                                          │
└──────┴──────────┴──────────────────────────────────────────┘
```

管理后台采用 **两栏布局**（参考 `references/agentconsole.html`）：

```
┌─────────────────────────────────────────────────────────────┐
│  顶部导航栏 (56px) — ◀ 返回 | 管理后台 | 图标工具 | 用户信息 │
├──────────┬──────────────────────────────────────────────────┤
│          │                                                  │
│ 左侧菜单 │    主内容区                                        │
│ 200px    │    flex: 1                                        │
│          │                                                  │
│ 搜索框   │    page-header (页面标题 + 新建按钮)                 │
│          │    filter-bar (类型/来源筛选 + 搜索框)              │
│ 菜单分组  │    表格 (名称/APIName/类型/描述/创建人/时间/操作)   │
│ (分组标题)│    分页 (共N条 1/1 < >)                           │
│          │                                                  │
└──────────┴──────────────────────────────────────────────────┘
```

### 1. 顶部导航栏 (Header Bar)

```css
.header-bar {
  height: 56px;
  background: #ffffff;
  border-bottom: 1px solid #e5e7eb;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
}
```

- **左侧**: 企业名称 `(ea账号)企业名称-xxx`
- **右侧**: 全局搜索框（圆角16px，灰色背景#f5f7fa）+ 🔍 🕒 🗎 👥 ❓ 🛍️ ✨(AI) ⋮ 等图标 + 用户角色标签

### 2. 左侧一级导航 (Sidebar First Level)

```css
.sidebar-first {
  width: 70px;
  background: #f0f2f5;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0;
}
```

- 每个菜单项: **图标(22px)** + **文字(12px)**，竖排
- 选中态: 白色背景，品牌色(#ff9500/#ff7d00)高亮
- 底部: 设置图标
- 常见一级菜单: 企信、订货管理(当前)、CRM、待办、智能盈、更多

### 3. 二级菜单 (Sidebar Second Level)
#### CRM 双栏模式 (sidebar-second)

```css
.sidebar-second {
  width: 220px;
  background: #ffffff;
  padding: 20px;
  overflow-y: auto;
}
```

- **应用标题**: 18px, font-weight 600
- **搜索框**: 36px高，边框#e5e7eb，背景#fafafa
- **菜单项**: 15px, padding 10px 8px, 圆角6px
- **子菜单**: 14px, padding 8px 8px 8px 20px，前带 ▶/▼ 折叠箭头
- **分组标题**: 前带 ▼ 箭头
- **选中态**: 背景色 #fff7e6

#### 管理后台单栏模式 (sidebar-left)
参考 `references/agentconsole.html`:

```css
.sidebar-left {
  width: 200px;
  background: #ffffff;
  border-right: 1px solid #e5e7eb;
  padding: 16px;
  display: flex;
  flex-direction: column;
}
```

- **搜索框**: 100%宽度, 36px高, border:#e5e7eb, radius:6px, margin-bottom:24px
- **菜单分组标题** (menu-group-title): 12px, color:#999, margin:16px 0 8px
- **菜单项**: 14px, color:#666, padding 10px 8px, radius:6px, display:flex gap:10px
- **选中态**: background:#fff7e6, color:#ff7d00, font-weight:500
- 带 `>` 箭头表示有子页面
- 底部折叠按钮 margin-top: auto

### 4. 主内容区 (Main Content)

```css
.main-content {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
  background: #f0f2f5;
}
```

#### 页签 (Tab Header)
```
.tab-header: display:flex, gap:24px, border-bottom:1px solid #e5e7eb
.tab-item.active: color:#ff7d00, font-weight:500, border-bottom:2px solid #ff7d00
```

#### 内容标题区 (Content Header)
```
flex, space-between
左侧: 页面标题 + 下拉 ▼
右侧: 【新建】按钮 + ... 更多操作
```

#### 筛选栏 (Filter Row)
```
display:flex, gap:12px
筛选组件: dropdown(select) + 筛选按钮(描边) + 搜索框(200px) + 表格控制按钮
```

### 5. 表格 (Table / Object List)

```css
.order-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 8px;
}
th {
  background: #f9fafb;
  padding: 12px 8px;
  text-align: left;
  font-weight: 500;
  border-bottom: 1px solid #e5e7eb;
}
td {
  padding: 12px 8px;
  border-bottom: 1px solid #e5e7eb;
}
tr:hover {
  background: #f9fafb;
}
```

- 表格行高约 44-48px
- 首列复选框
- 操作列: 蓝色链接(操作1/操作2/操作3) + ▼ 下拉
- 客户名称列: 蓝色链接

### 6. 状态标签 (Status Tag)

```css
.status-tag {
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}
/* 橙色(默认/待处理) */ .status-tag { background: #fff7e6; color: #ff7d00; }
/* 蓝色(进行中/部分) */  .status-tag.partial { background: #e6f7ff; color: #1890ff; }
/* 绿色(已完成) */       .status-tag.completed { background: #f0f9eb; color: #52c41a; }
```

### 7. 分页 (Pagination)

```css
.pagination {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: 12px 0;
  font-size: 14px;
  color: #666;
}
```

### 8. AI 助手按钮

```css
.ai-assistant-btn {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 48px; height: 48px;
  border-radius: 50%;
  background: white;
  border: 1px solid #e5e7eb;
  cursor: pointer;
  color: #6e56cf;
}
```

## FXUI Design Tokens

### 主色 (品牌色: 橙色系)

```css
--fx-primary: #ff7d00;        /* 品牌橙 - 主按钮、选中状态、高亮 */
--fx-primary-light: #ff9500;  /* 浅橙 - 一级导航图标选中色 */
--fx-primary-bg: #fff7e6;     /* 浅橙背景 - 菜单选中、标签背景 */
--fx-link: #1890ff;           /* 链接蓝 - 操作链接、客户名链接 */
--fx-success: #52c41a;        /* 成功绿 */
--fx-warning: #faad14;        /* 警告黄 */
--fx-danger: #ff4d4f;         /* 危险红 */
```

### 中性色

```css
--fx-bg-page: #f0f2f5;        /* 页面背景 */
--fx-bg-white: #ffffff;       /* 白色卡片/面板 */
--fx-bg-table-hover: #f9fafb; /* 表格悬停背景 */
--fx-bg-input: #fafafa;       /* 输入框背景 */
--fx-bg-search: #f5f7fa;      /* 搜索框背景 */
--fx-text-primary: #333;      /* 主要文字 */
--fx-text-secondary: #666;    /* 次要文字 */
--fx-text-muted: #999;        /* 弱化文字 */
--fx-border: #e5e7eb;         /* 边框/分割线 */
--fx-border-input: #d1d5db;   /* 输入框边框 */
```

### 排版

```css
--fx-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", 
                  "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", sans-serif;
--fx-font-size-xs: 12px;      /* 状态标签、辅助文字 */
--fx-font-size-sm: 13px;      
--fx-font-size-md: 14px;      /* 正文/表格内容 */
--fx-font-size-lg: 15px;      /* 菜单项文字 */
--fx-font-size-xl: 16px;      /* 页面标题 */
--fx-font-size-2xl: 18px;     /* 应用名称 */
```

### 间距与圆角

```css
--fx-spacing-xs: 4px;
--fx-spacing-sm: 8px;
--fx-spacing-md: 16px;
--fx-spacing-lg: 20px;
--fx-spacing-xl: 24px;
--fx-radius-sm: 4px;          /* 状态标签 */
--fx-radius-md: 6px;          /* 按钮、输入框、菜单 */
--fx-radius-lg: 8px;          /* 表格、卡片 */
--fx-radius-xl: 16px;         /* 搜索框 */
```

### 阴影

```css
--fx-shadow-sm: 0 1px 2px rgba(0,0,0,0.06);
--fx-shadow-md: 0 2px 8px rgba(0,0,0,0.15);
```

## 组件参考

### 页面框架组件

```html
<!-- 页面骨架 -->
<div class="header-bar">...</div>
<div class="main-container">
  <div class="sidebar-first"><!-- 一级导航 --></div>
  <div class="sidebar-second"><!-- 二级菜单 --></div>
  <div class="main-content">
    <div class="tab-header">...</div>
    <div class="content-header">...</div>
    <div class="filter-row">...</div>
    <table class="order-table">...</table>
    <div class="pagination">...</div>
  </div>
</div>
<div class="ai-assistant-btn">✨</div>
```

### 按钮

| 类型 | 样式 |
|------|------|
| 主要按钮(新建) | `.btn-new` bg:#ff7d00, color:white, border:none, radius:6px, padding:6px 16px |
| 筛选按钮 | `.filter-btn` border:1px solid #ff7d00, bg:white, color:#ff7d00, radius:6px |
| 图标按钮 | `.control-btn` 30x30, border:#d1d5db, radius:6px, bg:white |
| 下拉选择 | `.dropdown` padding:6px 12px, border:#d1d5db, radius:6px, bg:white |

### 操作链接

```css
.action-link {
  color: #1890ff;
  cursor: pointer;
  margin-right: 8px;
}
```

## 原型生成模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FXUI Prototype - {页面名称}</title>
  <style>
    /* FXUI Design System Reset */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
                   "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
      background: #f0f2f5;
      font-size: 14px;
      color: #333;
      display: flex;
      height: 100vh;
      overflow: hidden;
    }
    :root {
      --fx-primary: #ff7d00;
      --fx-primary-light: #ff9500;
      --fx-primary-bg: #fff7e6;
      --fx-link: #1890ff;
      --fx-success: #52c41a;
      --fx-warning: #faad14;
      --fx-danger: #ff4d4f;
      --fx-bg-page: #f0f2f5;
      --fx-bg-white: #fff;
      --fx-bg-input: #fafafa;
      --fx-bg-search: #f5f7fa;
      --fx-bg-table-hover: #f9fafb;
      --fx-text: #333;
      --fx-text-secondary: #666;
      --fx-text-muted: #999;
      --fx-border: #e5e7eb;
      --fx-border-input: #d1d5db;
      --fx-radius-sm: 4px;
      --fx-radius-md: 6px;
      --fx-radius-lg: 8px;
      --fx-radius-xl: 16px;
    }
    /* 参考 references/crm_home.html 和 references/crm_object.list.html 获取完整样式 */
  </style>
</head>
<body>
  <!-- 页面内容：参考上面的组件规范 -->
</body>
</html>
```

## 现有示例文件

Skill 目录下提供了完整示例供参考:

| 文件 | 说明 |
|------|------|
| `references/crm_home.html` | CRM 工作台/首页（三栏布局、订单列表） |
| `references/crm_object.list.html` | CRM 对象列表页（搜索、筛选、表格、分页） |
| `references/agentconsole.html` | 管理后台列表页（两栏布局、菜单分组、Agent 管理表格） |
| `references/shareclaw-aihome.html` | AI 首页参考图，适用于 AI 门户、AI 工作台、AI 能力聚合页 |
| `references/shareclaw-aidetail.html` | AI 详情页参考图，适用于 AI 助手详情、能力介绍、单能力工作空间 |
| `references/eorder-catalog.html` | 订货通商品列表（商品卡片网格、筛选、购物车入口） |
| `references/eorder-cat.html` | 订货通购物车（已选商品列表、数量调整、金额汇总、提交下单） |
| `references/eorder-orderlist.html` | 订货通订单列表（订单号、状态、金额、时间筛选、分页） |

在原型生成时，直接参考这些示例中的 CSS 类名和 HTML 结构即可保持视觉一致性。

### 订货通页面优先参考规则

当用户需求涉及以下场景时，应优先调用订货通参考图，而不是只沿用通用 CRM 列表页示例：

- **商品列表 / 商品目录 / 商品展示** → 优先参考 `references/eorder-catalog.html`
- **购物车 / 已选清单 / 数量调整 / 金额汇总** → 优先参考 `references/eorder-cat.html`
- **订单列表 / 订单记录 / 订单查询** → 优先参考 `references/eorder-orderlist.html`

使用方式要求：

1. 先复用对应参考图的整体布局、信息分区和交互层次。
2. 再按当前需求替换文案、商品数据、按钮、状态和业务数据。
3. 若需求同时涉及商品列表、购物车和订单流转，按实际页面类型各自匹配，保持三页风格一致。
4. 若用户未明确说明，但需求描述出现"订货通 / 渠道订货 / B2B 订货 / 智能补货 / 快速下单"等关键词，也应默认优先参考 eorder 系列。

### AI 页面优先参考规则

当用户需求涉及以下场景时，应优先调用新增参考图，而不是只沿用通用 CRM 首页 / 列表页示例：

- **AI 首页 / AI 门户 / AI 工作台** → 优先参考 `references/shareclaw-aihome.html`
- **AI 详情页 / AI 助手详情 / AI 能力详情 / 单能力工作区** → 优先参考 `references/shareclaw-aidetail.html`

使用方式要求：

1. 先复用对应参考图的整体布局、信息分区和交互层次。
2. 再按当前需求替换文案、卡片内容、按钮、状态和业务数据。
3. 若需求同时包含 AI 首页与详情流转，首页优先参考 `shareclaw-aihome.html`，详情优先参考 `shareclaw-aidetail.html`，保持两页风格一致。
4. 若用户未明确说明，但需求描述出现"AI首页 / AI主页 / AI详情页 / AI助手详情 / 智能体详情"等关键词，也应默认优先参考这两张图。

## 截图分析 → HTML 原型工作流

当用户提供产品截图（.jpg/.png）要求生成原型时，使用以下流程：

### 技术方案

不要直接使用 `execute_code` 执行包含 heredoc 的 Python 脚本（Python multi-line 字符串在 execute_code 沙箱中会语法错误）。取而代之：

1. **写分析脚本到临时文件** — 使用 `write_file` 将 Python/PIL 分析脚本写入 skill 目录
2. **用 `terminal` 执行脚本** — `python3 <script>.py`
3. **根据分析结果直接生成 HTML**

### 标准分析脚本模板

使用 `scripts/analyze_screenshot.py`：

```bash
python3 scripts/analyze_screenshot.py {图片路径} --output {输出分析文件路径}
```

脚本会提取：布局分区边界、列边界、颜色值（主色/功能色/文字色）、表格结构、标题栏位置。

### 工作流步骤

1. **保存图片** — 复制到原型 assets 目录: `cp {图片路径} {原型目录}/assets/reference-{场景}.jpg`
2. **像素分析** — 使用 `scripts/analyze_screenshot.py` 提取: 布局分区、颜色值、元素位置、间距比例
3. **设计分析** — 基于分析结果，完成布局规划和组件选型，写入设计分析文档
4. **生成 HTML 原型** — 基于分析结果和设计决策，使用本 skill 中的 design tokens 和布局规范
5. **保存到 project/{requirement-name}/prototype-fxui/** — HTML 原型存为 `project/{requirement-name}/prototype-fxui/prototype-{场景}-{类型}.html`
6. **更新原型总控文件** — 记录分析结果、设计决策、HTML 产物路径

> **注意**: 用户期待直接产出可运行的 HTML 原型，不需要在分析完后先问"要不要生成"——分析就是一个中间步骤，最终交付物是 HTML 文件。

## Component List (from FXUI docs)

Full documentation: https://fe.firstshare.cn/fxui/#/zh-CN/component/

### 开发指南
- Installation, i18n, Transition

### Basic
- Button, Icon, Layout, Container, Color, Link

### Form
- Form, Input, InputNumber, Cascader, Switch, Select, Radio, Checkbox
- DatePicker, TimePicker, DateTimePicker, Upload, ColorPicker
- Transfer, Richtext, Signature, Slider, SelectorV2

### Data
- Table, Tag, Progress, Tree, Pagination, Badge, Calendar, Card
- Carousel, Image, Avatar, IconPicker, Min-bar

### Navigation
- NavMenu, Tabs, Breadcrumb, Dropdown, Steps-v2

### Others
- Scrollbar, Draggable, InfiniteScroll, VirtualScroller
- Timeline, Collapse, Smoothscroll

### Feedback
- Dialog, MessageBox, Loading, Message, Notification
- Popover, Tooltip, Alert
