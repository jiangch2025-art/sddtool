---
name: fxui-prototype
description: "Generate HTML prototypes using 纷享销客 FXUI component library and CRM design system. FXUI is a Vue 2 based UI library (https://fe.firstshare.cn/fxui/) used by 纷享销客. Use this skill when the user wants to create CRM prototypes/mockups that follow the 纷享销客 design system."
triggers:
  - "用 FXUI 做个原型"
  - "FXUI 原型"
  - "纷享销客 UI 原型"
  - "做个创建客户的弹窗"
  - "fxui prototype"
  - "纷享销客 CRM 原型"
---
# FXUI Prototype Skill

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

管理后台采用 **两栏布局**（参考 `examples/agentconsole.html`）：

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
参考 `examples/agentconsole.html`:

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
    /* 参考 examples/crm_home.html 和 examples/crm_object.list.html 获取完整样式 */
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
| `examples/crm_home.html` | CRM 工作台/首页（三栏布局、订单列表） |
| `examples/crm_object.list.html` | CRM 对象列表页（搜索、筛选、表格、分页） |
| `examples/agentconsole.html` | 管理后台列表页（两栏布局、菜单分组、Agent 管理表格） |
| `examples/shareclaw-aihome.html` | AI 首页参考图，适用于 AI 门户、AI 工作台、AI 能力聚合页 |
| `examples/shareclaw-aidetail.html` | AI 详情页参考图，适用于 AI 助手详情、能力介绍、单能力工作空间 |

在原型生成时，直接参考这些示例中的 CSS 类名和 HTML 结构即可保持视觉一致性。

### AI 页面优先参考规则

当用户需求涉及以下场景时，应优先调用新增参考图，而不是只沿用通用 CRM 首页 / 列表页示例：

- **AI 首页 / AI 门户 / AI 工作台** → 优先参考 `examples/shareclaw-aihome.html`
- **AI 详情页 / AI 助手详情 / AI 能力详情 / 单能力工作区** → 优先参考 `examples/shareclaw-aidetail.html`

使用方式要求：

1. 先复用对应参考图的整体布局、信息分区和交互层次。
2. 再按当前需求替换文案、卡片内容、按钮、状态和业务数据。
3. 若需求同时包含 AI 首页与详情流转，首页优先参考 `shareclaw-aihome.html`，详情优先参考 `shareclaw-aidetail.html`，保持两页风格一致。
4. 若用户未明确说明，但需求描述出现“AI首页 / AI主页 / AI详情页 / AI助手详情 / 智能体详情”等关键词，也应默认优先参考这两张图。

## 截图分析 → HTML 原型工作流

当用户提供产品截图（.jpg/.png）要求生成原型时，使用以下流程：

### 技术方案

不要直接使用 `execute_code` 执行包含 heredoc 的 Python 脚本（Python multi-line 字符串在 execute_code 沙箱中会语法错误）。取而代之：

1. **写分析脚本到临时文件** — 使用 `write_file` 将 Python/PIL 分析脚本写入 skill 目录
2. **用 `terminal` 执行脚本** — `python3 <script>.py`
3. **根据分析结果直接生成 HTML**

### 标准分析脚本模板

```python
from PIL import Image
img = Image.open('{图片路径}')
# 缩放到一半尺寸方便处理
w, h = img.size
img_small = img.resize((w // 2, h // 2))

# 1. 垂直扫描 — 检测布局分区边界
for y in range(0, h//2, 2):
    px = img_small.getpixel((w//4, y))
    # 检测颜色突变（像素差 > 30）

# 2. 水平扫描 — 检测列边界  
for x in range(0, w//2, 5):
    px = img_small.getpixel((x, header_y))

# 3. 颜色提取 — 主色、按钮色、状态标签色
# 4. 布局推断 — 三栏/两栏比例、元素间距、行高
```

### 工作流步骤

1. **保存图片** — 复制到 skill 目录: `cp {图片路径} {skill_dir}/fxui-{场景}-reference.jpg`
2. **像素分析** — 使用上述脚本提取: 布局分区、颜色值、元素位置、间距比例
3. **生成 HTML 原型** — 基于分析结果，使用本 skill 中的 design tokens 和布局规范
4. **更新 SKILL.md** — 在 `参考图索引` 表中添加新图片条目，在对应布局类型下补充详细描述
5. **保存到 examples/** — HTML 原型存为 `examples/fxui-{场景}-{类型}.html`

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
