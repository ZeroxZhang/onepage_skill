 中文字体方案

本文件定义了不同设计风格对应的字体栈方案。
所有方案均通过 Google Fonts @import 加载网络字体，并配置完整的系统字体 fallback。

---

## 硬性规则

- 字体家族不超过 **2 种**（一种用于标题，一种用于正文）
- 若标题和正文使用同一家族，视为 1 种
- 单行字符数控制在 **25-40 字**（中文），通过调整容器宽度实现
- 字号建立清晰阶梯，推荐比例：**1.25（Major Third）或 1.333（Perfect Fourth）**

---

## 字号阶梯示例

以 A1 纵向长图为例，使用 1.25 比例：

| 层级 | 字号 | 用途 |
|------|------|------|
| L1 主标题 | 38px | 核心论点/产品名 |
| L2 副标题 | 30px | 价值主张/方案名 |
| L3 小标题 | 24px | 模块标题 |
| L4 正文 | 15px | 段落文字 |
| L5 辅助说明 | 12px | 来源/日期/脚注 |

---

## 通用加载方式

在 HTML 的 `<head>` 中使用：

```html
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&display=swap');
</style>
```

如需特殊展示字体，可额外加载：
```html
@import url('https://fonts.googleapis.com/css2?family=ZCOOL+QingKe+HuangYou&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&display=swap');
@import url('https://fonts.googleapis.com/css2?family=ZCOOL+KuaiLe&display=swap');
```

---

## 尺寸-字号对照表（核心参考）

不同画布尺寸需要不同的字号比例，以下是三种尺寸的标准字号范围：

| 尺寸 | 画布宽度 | 主标题 | 副标题 | 小标题 | 正文 | 辅助说明 |
|------|---------|--------|--------|--------|------|---------|
| **A1 纵向长图** | 800px | 32-48px | 20-24px | 18-22px | 15-16px | 12-13px |
| **A2 横向宽图** | 1920px | 48-72px | 28-36px | 22-28px | 18-22px | 14-16px |
| **A3 正方形** | 1080px | 36-52px | 22-28px | 18-24px | 16-18px | 12-14px |

**字号计算原则：**
- 正文字号约为画布宽度的 **1.8%-2.2%**
- 主标题约为正文字号的 **2.5-3.5 倍**
- 副标题约为正文字号的 **1.5-1.8 倍**
- 辅助说明约为正文字号的 **0.8-0.9 倍**

**高密度模式 (C3) 调整：**
- 正文字号可取范围下限，留出更多空间给内容
- 标题字号保持不变，维持视觉层级

**低密度模式 (C1) 调整：**
- 正文字号可取范围上限，增强阅读舒适度
- 标题字号可适当放大，突出视觉焦点

---

## 风格-字体映射

### B1 科技极客 / B2 现代商务

适合使用**现代无衬线体**，传达精确、专业的感觉。

```css
:root {
  --font-heading: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', sans-serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;
}
```

- 主标题：字重 900 或 700，字号 32-48px
- 副标题：字重 700，字号 20-24px
- 正文：字重 400，字号 15-16px
- 辅助说明：字重 300，字号 12-13px

**B1 科技极客额外选项**：大标题可使用等宽字体创造编程/终端感。

### B3 清新自然

适合使用**圆润的无衬线体**或**轻量衬线体**混搭。

```css
:root {
  --font-heading: 'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', sans-serif;
}
```

- 标题字重偏轻：600 或 500
- 正文字重：400
- 整体行高更加宽松：2.0

### B4 新拟态质感

适合使用**圆润体**或**轻质量黑体**。

```css
:root {
  --font-heading: 'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', sans-serif;
}
```

- 标题字重：700
- 正文字重：400-500
- 可在关键数字处使用更大的字重形成视觉焦点

### B5 现代孟菲斯风

需要**极强视觉冲击力**的字体，主标题可以夸张，正文保持清晰。

```css
:root {
  /* 大标题可使用特殊的展示字体，或极粗的黑体 */
  --font-heading: 'ZCOOL KuaiLe', 'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', sans-serif;
}
```

- 主标题：字重 900+ (Black/Heavy)，字号可非常夸张。
- 副标题/重点数据：字重 800-900，可增加描边效果 (`-webkit-text-stroke`)。
- 正文：字重 400-500，保证阅读性。

### B6 现代软 UI 风

强调**轻盈、通透与现代感**。

```css
:root {
  --font-heading: 'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', sans-serif;
}
```

- 标题字重：600-800，干净利落。
- 正文字重：300-400，颜色使用深灰/中灰以降低对比度，体现“软”感。
- 整体字间距可稍微放宽（`letter-spacing: 0.03em`）。

---

## 中文排版核心参数

无论何种风格，以下参数必须遵守：

```css
body {
  font-size: 15px;           /* 正文基础字号 */
  line-height: 1.8;          /* 中文需要更大行高 */
  letter-spacing: 0.02em;    /* 微调字间距 */
  text-align: justify;       /* 两端对齐 */
  word-break: break-all;     /* 中文断字 */
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3 {
  line-height: 1.4;          /* 标题行高可收紧 */
  letter-spacing: 0.04em;    /* 标题字间距稍大 */
  margin-bottom: 0.6em;
}

p {
  margin-bottom: 1em;        /* 段间距 > 行间距 */
}
```

---

## 字体加载失败的 fallback 策略

为保证在字体未能加载的情况下依然呈现良好效果：

1. 始终将系统中文字体放在 fallback 链中
2. macOS: `PingFang SC`, `Hiragino Sans GB`
3. Windows: `Microsoft YaHei`
4. Linux: `WenQuanYi Micro Hei`
5. 最终 fallback: `sans-serif`

完整 fallback 示例：
```css
font-family: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
             'Microsoft YaHei', 'WenQuanYi Micro Hei', sans-serif;
```
```