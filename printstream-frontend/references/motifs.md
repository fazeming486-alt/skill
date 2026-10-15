# 九大母题 · 参数化生成器

这套美术语言的识别度全在**图案**上：网点、条码、X 阶梯、角标、虹带、虚线弧。
它们全部是规则可描述的 —— 尺寸、密度、间距、条数都能调，所以**用代码生成，
不要贴位图**（固定分辨率母题一到别的尺寸就露馅）。

以下每个母题都给出：来源 → 生成代码 → 可调参数 → 建议落点。
所有代码只依赖 design-tokens.md 的变量，不引第三方库。

---

## ① 四角定位标 [+·]

**来源**：参考图里每个框的四角都是「直角角括号」，左上内侧一个加号、右下一个点
（不对称布局，别做成四角全同）。

```html
<div class="ps-panel">…</div>
```
```css
.ps-panel{position:relative}
.ps-panel::before,.ps-panel::after{
  content:'';position:absolute;width:13px;height:13px;pointer-events:none;
}
.ps-panel::before{left:4px;top:4px;
  border-left:2px solid var(--ps-ink);border-top:2px solid var(--ps-ink)}
.ps-panel::after{right:4px;bottom:4px;
  border-right:2px solid var(--ps-ink);border-bottom:2px solid var(--ps-ink)}
/* 加号与点：用元素自身内容或一个 <i> 画，左上 12/9px 处 */
```

可调：`arm`（角臂长，默认 13px）、`gap`（距框 4px）、线宽 2px。
**落点**：每个面板/表格/告警条的四角。它是使用频率最高的母题，但只服务"容器"。

## ② X 形阶梯标尺 ★ 招牌符号

**来源**：参考图里一条粗黑对角十字；所谓"阶梯"是**一排 X 从实心到虚线渐隐**，
不是两个不同图形。

**正确做法：一条 SVG 路径出三种形态**（实心/描边/虚线只改 stroke 与 fill，
形状永远一致 —— 拼图层永远会错位）：

```html
<svg width="0" height="0" style="position:absolute">
  <symbol id="ps-x" viewBox="0 0 24 24">
    <path d="M4 4 L9.4 4 L12 8.4 L14.6 4 L20 4 L14.8 12 L20 20 L14.6 20
             L12 15.6 L9.4 20 L4 20 L9.2 12 Z"/>
  </symbol>
</svg>
<!-- 实心大×：fill 墨；描边×：fill:none stroke:墨；虚线×：stroke-dasharray -->
<svg class="ps-x-big" width="66" height="66" viewBox="0 0 24 24"
     fill="currentColor"><use href="#ps-x"/></svg>
```

路径要点：24×24 视框、笔画等宽 5.4、末端平切、交点在正中。
实测笔画宽 ≈ 字高的 20%（旧版 46% 粗笨一倍已废弃）。

阶梯排（5 枚，实心→描边→虚线渐隐，CSS 版）：

```css
.ps-x-ladder{display:inline-flex;gap:2px;align-items:center}
.ps-x-ladder svg{width:18px;height:18px;color:var(--ps-ink)}
.ps-x-ladder svg:nth-child(1){opacity:1}
.ps-x-ladder svg:nth-child(2){opacity:.82}
.ps-x-ladder svg:nth-child(3){opacity:.6;fill:none;stroke:currentColor;stroke-width:1.4}
.ps-x-ladder svg:nth-child(4){opacity:.4;fill:none;stroke:currentColor;stroke-width:1.4;
  stroke-dasharray:3 3}
.ps-x-ladder svg:nth-child(5){opacity:.22;fill:none;stroke:currentColor;stroke-width:1.4;
  stroke-dasharray:3 3}
```

**落点**：分区标题左侧标尺 / 面板标题行。**全页大×只此一枚**（首屏主视觉锚点），
不到处撒 —— 这是用户拍过板的纪律。

## ③ 密度渐变条码（左疏右密）

**来源**：参考图里那条"扫描条"：由密到疏的竖线印刷带。

```css
.ps-barcode{
  height:9px;width:100%;
  background:
    repeating-linear-gradient(90deg,var(--ps-ink) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,var(--ps-ink) 0 1px,transparent 1px 3px);
  background-size:100% 60%,100% 100%;
  background-position:0 100%,0 0;
  background-repeat:no-repeat;
  opacity:.18;               /* 底纹级；要更明显就 .3~.5 */
}
```

原理：两层不同周期的 1px 线叠加，各自只画一段高度，接缝处形成密度变化。
可调：周期（3/4px）、线宽（1px）、透明度。
**落点**：面板顶边、统计格底纹、表格 thead 上方。

## ④ 粗黑条三连

**来源**：参考图里那组 `▤▤▤`：三条不等长粗横条，硬分隔。

```css
.ps-thickbars{
  width:58px;height:8px;flex:0 0 auto;
  background:
    linear-gradient(var(--ps-ink),var(--ps-ink)) 0 0/26px 8px no-repeat,
    linear-gradient(var(--ps-ink),var(--ps-ink)) 31px 0/13px 8px no-repeat,
    linear-gradient(var(--ps-ink),var(--ps-ink)) 48px 2px/10px 4px no-repeat;
}
```

可调：三条的长度比例（默认 26/13/10，递减）、条高（8px，第三条 4px 制造节奏）。
**落点**：分区标题右侧、按钮组分隔。**挂在标题元素内部**（标题自己是 flex），
不要 `margin-left:auto` 挂外层 —— 会被 flex-wrap 甩到下一行撞到右侧控件（实测事故）。

## ⑤ 虹带 ★ 全页唯一的彩色元素

**来源**：参考图底部横贯全宽的彩色带。**定稿构造（第四轮，用户拍板）：
三条粗横条，每条左端粉红 → 右端青蓝，条与条之间是宽黑缝，右边接一列更窄的条。**

```css
.ps-iridescent{
  height:3px;                    /* 全宽细版：header/toc 交界那条 */
  background:linear-gradient(90deg,
    #ff4f9a 0%, #ff9a8f 9%,  #e6d9c9 17%, #3de8ff 27%,
    #f45cf0 38%,#b09ae0 47%, #4cc0e4 55%, #3de8ff 63%,
    #e6d9c9 72%,#ff9a8f 82%, #ff4f9a 100%);
}
```

三条粗横版（参考图原构造，约 4~5px 条 + 5px 黑缝）：

```css
.ps-band3{
  height:22px;background:var(--ps-ink);   /* 黑缝就是底色 */
  background-image:
    linear-gradient(90deg,var(--ps-iridescent-from),var(--ps-iridescent-to)),
    linear-gradient(90deg,var(--ps-iridescent-from),var(--ps-iridescent-to)),
    linear-gradient(90deg,var(--ps-iridescent-from),var(--ps-iridescent-to));
  background-size:72% 4px, 72% 4px, 72% 4px;
  background-position:0 2px, 0 9px, 0 16px;
  background-repeat:no-repeat;
}
```

**颜色纪律**：这两个 hex 序列是全页唯一允许出现的"裸 hex"—— 它们是虹带
定义本身，不是组件配色。其他所有彩色必须走令牌。
**落点**：品牌带底线（3px 全宽）。全页彩色只允许：品牌带 + 高危反相区小块。

## ⑥ 点阵菱形簇

**来源**：参考图留白处的装饰：3×3 旋转 45° 的方块簇，中心与四角实心、其余渐隐。

```css
.ps-diamonds{width:46px;height:46px;display:grid;
  grid-template:repeat(3,1fr)/repeat(3,1fr);place-items:center}
.ps-diamonds i{width:70%;height:70%;background:var(--ps-ink);transform:rotate(45deg)}
.ps-diamonds i:nth-child(1),.ps-diamonds i:nth-child(3),
.ps-diamonds i:nth-child(7),.ps-diamonds i:nth-child(9){opacity:.35}
.ps-diamonds i:nth-child(2),.ps-diamonds i:nth-child(4),
.ps-diamonds i:nth-child(6),.ps-diamonds i:nth-child(8){opacity:.8}
.ps-diamonds i:nth-child(5){opacity:1}
```

**落点**：只落在留白处（页面底部、空面板角）。不承载任何信息。

## ⑦ 虚线圆弧 + 半圆（空状态）

**来源**：参考图左下角那组。空状态用它，替代灰色骨架屏。

```css
.ps-empty-arc{
  display:inline-block;width:30px;height:15px;vertical-align:middle;
  border:2px dashed var(--ps-ink-soft);
  border-radius:30px 30px 0 0;      /* 真正的上半圆，不是"去掉下边"的直角缺口 */
  border-bottom:none;
}
```

**语义红线**：没数据 ≠ 失败。圆弧是中性淡墨虚线，**绝不染红**。
**落点**：等待数据处、空列表、骨架屏的替代。

## ⑧ 图标三连（中空圆 / 斜杠圆 / 小方块）

**来源**：参考图里并排的那组印刷图标。纯装饰，不承载读数。

```css
.ps-trio{display:inline-flex;gap:5px;align-items:center;pointer-events:none}
.ps-trio i{display:block;width:11px;height:11px;border:2px solid var(--ps-ink)}
.ps-trio i:nth-child(1){border-radius:50%}
.ps-trio i:nth-child(2){border-radius:50%;
  background:linear-gradient(45deg,transparent 44%,var(--ps-ink) 44% 56%,transparent 56%)}
.ps-trio i:nth-child(3){border-radius:0}
```

加 `aria-hidden="true"`。**落点**：面板标题右侧的视觉锚，一处就够。

## ⑨ 黑白反相分区

**来源**：参考图下半整块反白 —— 这套语言里最狠的一招。**克制使用：
只给真正需要警示/强调的区域**（高危操作、关键告警）。

```css
.ps-invert{
  /* ★ 用独立命名的变量，绝不让两个变量互指（原因见 rules-and-antipatterns.md §6） */
  --inv-bg:#0d1117; --inv-fg:#f4f6f9; --inv-line:#f4f6f9;
  --inv-soft:#3b444f; --inv-dim:#9aa5b1;
  background:var(--inv-bg);color:var(--inv-fg);
  border:2px solid var(--inv-line);
  box-shadow:6px 6px 0 var(--ps-accent-text);   /* 黑底上的墨影看不见，换 accent */
}
/* 反相区里的"纸底"子元素（输入框/按钮/格）统一翻成 --inv-fg 底 --inv-bg 字 */
.ps-invert button,.ps-invert input,.ps-invert select{
  background:var(--inv-fg);color:var(--inv-bg);border-color:var(--inv-bg);
}
```

**纪律**：反相只改容器配色，**不动任何 ok/warn/bad 三态判定**（不许说谎）。
输入框全家一个都不能漏 —— 反相区把文字色翻成浅色而底色不翻 = 浅底浅字，
打字看不见（实测现场事故）。

---

## 附：纸面背景与页脚印章

纸面三件套见 design-tokens.md §五。页脚印章：

```css
.ps-stamp{
  display:flex;align-items:center;gap:9px;
  font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;
  letter-spacing:.16em;color:var(--ps-ink);
  border-top:1px solid rgba(13,17,23,.35);padding-top:8px;
}
.ps-stamp::before{            /* 左侧三道斜杠 */
  content:'';width:14px;height:12px;flex:0 0 auto;
  background:
    linear-gradient(45deg,transparent 42%,var(--ps-ink) 42% 58%,transparent 58%) 0 0/5px 12px no-repeat,
    linear-gradient(45deg,transparent 42%,var(--ps-ink) 42% 58%,transparent 58%) 4px 0/5px 12px no-repeat,
    linear-gradient(45deg,transparent 42%,var(--ps-ink) 42% 58%,transparent 58%) 8px 0/5px 12px no-repeat;
}
```

槽位文本格式：`编号;`（如 `_B42;`）或 `署名;`（如 `DESIGN BY WyHXnR;`）——
内容是**可替换的槽位**，不是固定图形。
