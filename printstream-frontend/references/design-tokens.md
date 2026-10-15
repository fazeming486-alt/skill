# 设计令牌 · 印花集（PRINTSTREAM）

所有数值来自对参考图的像素统计（Otsu 阈值 + 16 级量化），不是肉眼估的。
铁律：**纸与墨是主色，彩色只出现在虹带**。

---

## 一、色彩令牌

```css
:root{
  /* 纸与墨 —— 整套语言只有这两种主色 */
  --ps-paper:      #f4f6f9;   /* 纸白：面板/页面底 */
  --ps-paper2:     #eaeef3;   /* 纸的第二个明度：次级面板、条纹底 */
  --ps-ink:        #0d1117;   /* 墨黑：文字、边框、实心块 */
  --ps-ink-soft:   #5b6774;   /* 墨的淡化：次要文字（不是灰，是淡墨） */
  --ps-line:       #0d1117;   /* ★ 线就是墨本身，不是浅灰 */
  --ps-line-soft:  #c3ccd8;   /* 只有表格行线这种"低存在感分隔"才用 */

  /* 虹带三色 —— 全页唯一的彩色元素 */
  --ps-iridescent-from: #f8a8a0;  /* 暖粉 */
  --ps-iridescent-mid:  #f088f0;  /* 品红 */
  --ps-iridescent-to:   #20e0e0;  /* 电光青 */

  /* 功能三态：必须在纸底上可读，一律比"亮色"深一档 */
  --ps-ok:   #0e9f6e;
  --ps-warn: #a86f08;
  --ps-bad:  #d23a40;
}
```

### 配色比例（实测，做版面时当分布指南用）

| 参考图 | 纸白 | 墨黑 | 启示 |
|---|---|---|---|
| 1.webp | 67.77% | 24.96% | 白底为主，底部一整块**反相黑面板** |
| 2.webp | 45.87% | 46.12% | 几乎对半 —— "反相分区"的样板 |
| 3.webp | 51.16% | 26.09% + 9.41% 纯黑 | 灰阶多来自抗锯齿，别当成第三种颜色 |

推论：一个页面的墨色覆盖率大致在 25%~50% 之间。低于 20% 会寡淡，高于 60% 不再是"白纸印刷"而是"黑底霓虹"（那是另一套语言）。

### 电光蓝的双角色（需要蓝色 accent 时）

蓝色（或任何 accent 色）在这套语言里**分两个角色，不许混用**：
- `--ps-accent-text`：可读的深色（如电光蓝 `#0a6fb0`）—— 用于文字、边框、链接；
- `--ps-accent-dec`：装饰性的亮色（如 `#0b9bf0`）—— 用于光晕、底纹、渐变。

混用的典型事故：拿装饰亮色写正文，白底上对比度不够，读数看不清。

---

## 二、字体令牌

| 角色 | 字体栈 | 说明 |
|---|---|---|
| 展示体（大标题/品牌名） | `'Saira Stencil One', sans-serif` | 模具体，**最贴工业印刷味**的首选 |
| 窄体标题 | `'Saira Condensed','Teko','Oswald',sans-serif` | 分区标题、密集行 |
| 等宽（读数/数字） | `'JetBrains Mono','Space Mono',ui-monospace,monospace` | 数字默认等宽 + `font-variant-numeric:tabular-nums` |
| 中文正文 | `'Noto Sans SC','Microsoft YaHei',sans-serif` | 中文正文 |
| 切角科技体（备选） | `'Chakra Petch',sans-serif` | 需要"切角"感的标题 |

排印纪律：
- 标题大写 + `letter-spacing:.1em~.16em` + `font-weight:800`（印刷品靠字重与字距，不靠彩色）；
- 小标签 `text-transform:uppercase;letter-spacing:.12em`；
- 数字一律等宽（表格列才对得齐）；
- **标题不许渐变填色** —— 印刷品没有渐变文字，标题的识别靠"墨黑字 + 墨色下划线/标尺"。

字体文件在 `../assets/fonts/`（OFL，可随包再分发，见该目录 README）。

---

## 三、形状令牌

```css
:root{
  --ps-radius: 0;                    /* 圆角归零：印刷品没有圆角 */
  --ps-border: 2px solid var(--ps-ink);   /* 标准墨框 */
  --ps-shadow-hard: 3px 3px 0 var(--ps-ink);  /* 唯一的"立体"：错版硬边 */
  --ps-shadow-hard-sm: 2px 2px 0 var(--ps-ink);
  --ps-shadow-none: none;            /* 印刷品没有柔光投影 */
}
```

- **圆角一律 0**。胶囊、圆按钮、圆点在这套语言里不存在（状态灯也改方块）。
- **阴影只有一种**：offset 实心墨影（2~3px）。用它表达"按下/错版"，不用它表达"浮起"。
- 悬停态不是"浮起来 + 发光"，而是**墨框加粗一档 / 硬投影位移**（见 components.md）。
- 反相区（墨底）里硬投影改用 accent 色（如 `6px 6px 0 var(--ps-accent-text)`），黑底上的黑影看不见。

---

## 四、间距与网格

- 基础网格 4px；面板内边距 12~16px；面板间距 12~16px。
- 墨框 2px 是"结构线"，与 padding 一起算（box-sizing:border-box）。
- 装饰母题的尺寸写死不随字号变（它们是印刷标记，不是文字）：角标 13px、图标三连 11px、大× 约字高 3 倍。

---

## 五、背景纸面（三件套，从参考图提取）

```css
/* 墨点阵(22px 交错) + 细网格(44px) + 顶部两团淡光。压在内容下面，
   亮度低于不干扰读数的程度。点阵是这个主题的灵魂符号。 */
body::before{
  content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(rgba(13,17,23,.055) 1px, transparent 1.6px),
    radial-gradient(60% 42% at 12% -6%,  rgba(accent-dec,.10), transparent 62%),
    radial-gradient(52% 38% at 88% -2%,  rgba(13,17,23,.05),   transparent 60%),
    linear-gradient(rgba(13,17,23,.028) 1px, transparent 1px),
    linear-gradient(90deg, rgba(13,17,23,.028) 1px, transparent 1px),
    var(--ps-paper);
  background-size:22px 22px, auto, auto, 44px 44px, 44px 44px, auto;
}
```

点阵透明度 ≤.06、网格线 ≤.03：**它是背景，不是内容** —— 淡到不影响读数为止。
