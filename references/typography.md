 中文字体方案

本文件定义了不同设计风格对应的字体栈方案。
所有方案均通过 Google Fonts @import 加载网络字体，并配置完整的系统字体 fallback。

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