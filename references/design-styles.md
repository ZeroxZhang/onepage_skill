# 设计风格详细规范

本文件定义了 OnePage Generator 支持的四种设计风格的完整视觉规范。
生成 HTML 时必须严格遵循所选风格的全部参数。

---

## B1: 科技极客 (Cyber/Tech)

### 配色体系
- 主背景：`#0a0a1a` 至 `#0f0f2e` 的纵向线性渐变
- 辅助背景（卡片）：`rgba(255,255,255,0.03)` 配 1px `rgba(100,200,255,0.1)` 边框
- 主强调色：`#00d4ff`（青色）或 `#7b5cff`（紫色）
- 渐变强调：`linear-gradient(135deg, #00d4ff, #7b5cff)`
- 正文色：`rgba(255,255,255,0.85)`
- 次要文字：`rgba(255,255,255,0.5)`

### 点缀元素
- **背景网格线**：使用 `background-image` 的 `repeating-linear-gradient` 绘制 40px 间距的浅灰网格，透明度约 0.03-0.05
- **发光效果**：标题或关键数据旁可添加 `box-shadow: 0 0 30px rgba(0,212,255,0.15)`
- **渐变光斑**：在页面角落放置大尺寸径向渐变 blob（`radial-gradient`），透明度极低（0.05-0.1）
- **细线装饰**：模块之间使用 1px 的渐变分隔线
- **角标/标签**：使用荧光色小标签 `tag` 样式，圆角 + 半透明背景

### 卡片样式
```css
.card {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(100,200,255,0.08);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 24px rgba(0,0,0,0.3);
}
```

### 标题样式
- 主标题可使用渐变文字：`background: linear-gradient(...); -webkit-background-clip: text;`
- 字重：700-900
- 可在标题左侧添加 3-4px 宽的渐变竖条作为视觉锚点

---

## B2: 现代商务 (Modern Business)

### 配色体系
- 主背景：`#ffffff` 或 `#f8f9fa`
- 辅助背景（卡片）：`#ffffff` 配 `box-shadow: 0 1px 3px rgba(0,0,0,0.06)`
- 主强调色：`#2563eb`（蓝）或 `#0f172a`（深墨）
- 渐变强调：`linear-gradient(135deg, #2563eb, #7c3aed)` 仅用于小面积点缀
- 正文色：`#334155`
- 次要文字：`#94a3b8`

### 点缀元素
- **微投影层级**：使用多层 `box-shadow` 创建细腻的层级感，避免重阴影
- **低饱和度渐变**：页面顶部可添加极浅的渐变色带（高度约 4-6px）
- **几何装饰**：角落可使用低透明度的圆形或矩形几何元素
- **分隔线**：1px `#e2e8f0`，或使用极浅的渐变线

### 卡片样式
```css
.card {
  background: #ffffff;
  border: 1px solid #f1f5f9;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.03);
}
```

### 标题样式
- 主标题：`#0f172a`，字重 700，不使用渐变
- 可使用强调色下划线装饰（2-3px，宽度短于文字）
- 整体克制、专业

---

## B3: 清新自然 (Fresh/Nature)

### 配色体系
- 主背景：`#fefffe` 至 `#f0fdf4` 的微渐变，或 `#faf5ff` 至 `#f0f9ff`
- 辅助背景（卡片）：`rgba(255,255,255,0.7)` 配毛玻璃效果
- 主强调色：`#10b981`（绿）或 `#06b6d4`（青）或 `#8b5cf6`（紫）
- 渐变强调：`linear-gradient(135deg, #a7f3d0, #67e8f9, #c4b5fd)` 弥散风格
- 正文色：`#374151`
- 次要文字：`#9ca3af`

### 点缀元素
- **弥散光影 (Aura)**：使用多个大半径径向渐变 blob，颜色柔和（粉/绿/蓝），透明度 0.1-0.2，放在背景层
- **毛玻璃卡片**：`backdrop-filter: blur(20px); background: rgba(255,255,255,0.6);`
- **柔和圆角**：所有元素圆角 12-16px
- **自然色彩过渡**：避免尖锐的颜色跳变

### 卡片样式
```css
.card {
  background: rgba(255,255,255,0.6);
  border: 1px solid rgba(255,255,255,0.8);
  border-radius: 16px;
  backdrop-filter: blur(20px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.06);
}
```

### 标题样式
- 主标题：深色文字，字重 600-700
- 可使用带弥散效果的彩色圆形作为标题背景点缀
- 整体轻盈、舒适

---

## B4: 新拟态质感 (Neumorphism/Clay)

### 配色体系
- 主背景：`#e0e5ec` 或 `#dfe6ed`
- 辅助背景（卡片）：与主背景同色，通过光影区分
- 主强调色：`#6366f1`（靛蓝）或 `#ec4899`（粉红）
- 正文色：`#475569`
- 次要文字：`#94a3b8`

### 点缀元素
- **凸起效果**：`box-shadow: 6px 6px 12px #b8bec7, -6px -6px 12px #ffffff;`
- **凹陷效果（输入区/引用区）**：`box-shadow: inset 4px 4px 8px #b8bec7, inset -4px -4px 8px #ffffff;`
- **柔和圆角**：12-20px
- **不使用边框**，完全依靠光影创建层级

### 卡片样式
```css
.card-raised {
  background: #e0e5ec;
  border-radius: 16px;
  box-shadow: 6px 6px 12px #b8bec7, -6px -6px 12px #ffffff;
}
.card-inset {
  background: #e0e5ec;
  border-radius: 12px;
  box-shadow: inset 4px 4px 8px #b8bec7, inset -4px -4px 8px #ffffff;
}
```

### 标题样式
- 主标题：深色文字，字重 700
- 标题本身可使用浅凸起效果
- 整体柔和、有触感