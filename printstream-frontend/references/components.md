# 组件配方

每个配方都是"纸 + 墨 + 母题"的组合。所有交互态的共性：
**悬停 = 墨框加粗 / 硬投影位移（错版感），不是浮起 + 发光。**

---

## 面板 Panel

```css
.ps-panel{
  position:relative;                /* 给①角标定位用 */
  background:var(--ps-paper);
  border:2px solid var(--ps-line);
  border-radius:0;
  box-shadow:none;
  padding:12px 14px;
}
.ps-panel:hover{
  border-color:var(--ps-ink);
  box-shadow:var(--ps-shadow-hard);   /* 3px 3px 0 墨 */
}
```

标题行：`<h3>` 小字大写 + letter-spacing，配 ②X 阶梯 或 ④粗黑条三连（二选一，别都上）。

## 按钮 Button

```css
.ps-btn{
  font:inherit;font-weight:700;letter-spacing:.06em;
  background:var(--ps-paper);color:var(--ps-ink);
  border:2px solid var(--ps-line);border-radius:0;
  box-shadow:2px 2px 0 var(--ps-ink);
  padding:5px 12px;cursor:pointer;
  transition:transform .12s steps(2,end),box-shadow .12s;
}
.ps-btn:hover{transform:translate(-1px,-1px);box-shadow:3px 3px 0 var(--ps-ink)}
.ps-btn:active{transform:translate(2px,2px);box-shadow:0 0 0 transparent}
.ps-btn.on{                          /* 选中态 = 黑白反相，没有第三种表达 */
  background:var(--ps-ink);color:var(--ps-paper);border-color:var(--ps-ink);
  box-shadow:2px 2px 0 var(--ps-accent-text);
}
.ps-btn.danger{background:var(--ps-bad);color:#fff;border-color:var(--ps-ink)}
```

- 动画用 `steps()` 或干脆无动画 —— 印刷品的"运动"是错版位移，不是缓动浮起。
- 焦点态：`outline:2px solid var(--ps-accent-text);outline-offset:3px`（键盘可达性硬指标）。

## 表格 Table

```css
.ps-table{width:100%;border-collapse:collapse;
  background:var(--ps-paper);border:2px solid var(--ps-line)}
.ps-table thead th{
  background:var(--ps-paper2);border-bottom:2px solid var(--ps-line);
  letter-spacing:.1em;text-transform:uppercase;font-weight:700;
  font-size:11px;padding:6px 10px;text-align:left;
}
.ps-table td{padding:6px 10px;border-bottom:1px solid var(--ps-line-soft)}
.ps-table tbody tr{border-bottom:1px dashed var(--ps-line-soft)}  /* 行线是点线 */
.ps-table tbody tr:hover{background:rgba(var(--ps-accent-dec-rgb),.09)}
```

- 表头下方可挂 ③密度条码（贴在 thead 上边框，不占布局高度）。
- "当前关注行"用左侧 4px 实心墨条标记（`box-shadow:inset 4px 0 0 var(--ps-ink)`），
  比换行背景色更印刷。

## 统计卡 StatCard

大读数 + 单位 + 底部梯尺：

```css
.ps-stat{
  border:2px solid var(--ps-line);background:var(--ps-paper);
  padding:9px 11px 15px;position:relative;
}
.ps-stat .k{font-size:10px;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ps-ink-soft)}
.ps-stat .v{font-family:'JetBrains Mono',monospace;font-size:26px;font-weight:800;
  font-variant-numeric:tabular-nums;letter-spacing:-.02em;line-height:1.1}
.ps-stat::after{                     /* 底部印刷梯尺：6px 等距墨线 */
  content:'';position:absolute;left:12px;right:12px;bottom:6px;height:5px;
  background:repeating-linear-gradient(90deg,var(--ps-ink) 0 1px,transparent 1px 4px);
}
```

**读数必须看得清是底线**：数值用等宽 800 字重，副说明截断放 tooltip
（截断是诚实的，但全文一键可查）。

## 进度条 InkProgress

实心墨块推进 + 每 10% 一刻度 + 两侧都读得清：

```css
.ps-prog{position:relative;height:26px;border:2px solid var(--ps-ink);
  background:var(--ps-paper2);overflow:hidden}
.ps-prog .fill{position:absolute;inset:1px auto 1px 1px;background:var(--ps-ink)}
.ps-prog .ticks{position:absolute;inset:0;
  background:repeating-linear-gradient(90deg,transparent 0 calc(10% - 1px),
    var(--ps-paper) calc(10% - 1px) 10%)}
.ps-prog .txt{position:absolute;inset:0;display:flex;justify-content:space-between;
  align-items:center;padding:0 8px;font-size:11px;font-weight:700;
  font-variant-numeric:tabular-nums;mix-blend-mode:difference;color:#fff}
```

- 刻度线用纸色压在填充上（印刷标尺感）。
- 百分比文字跨填充边界时两边都得读得清（`mix-blend-mode:difference` 是最省事的做法，
  或按填充宽度裁两次各用对比色）。

## 告警条 Alert

```css
.ps-alert{border:2px solid var(--ps-line);background:var(--ps-paper)}
.ps-alert .al{border-left:8px solid var(--ps-warn);
  background:rgba(168,111,8,.13);padding:8px 12px;font-weight:600}
.ps-alert .al.storm{border-left-color:var(--ps-bad);background:rgba(210,58,64,.13)}
```

等级用左侧粗色条 + 底色浓度区分，不用图标不用圆点。

## 目标/状态条 Target strip

```css
.ps-target{border:2px solid var(--ps-line);border-left:8px solid var(--ps-ink-soft);
  background:var(--ps-paper);padding:8px 12px}
.ps-target.set{border-left-color:var(--ps-ink);background:rgba(accent-dec,.10)}
```

## 状态灯（方块，不是圆点）

```css
.ps-lamp{display:inline-block;width:11px;height:11px;border:2px solid var(--ps-ink)}
.ps-lamp.ok{background:var(--ps-ok)}
.ps-lamp.bad{background:var(--ps-bad)}
.ps-lamp.idl{background:transparent;border:2px dashed var(--ps-ink-soft)}
```

**ok/bad/idl 三态色是信任基础，反相也不能抹成同一个色。**

## 空状态 Empty state

`⑦虚线圆弧` + 中性淡墨文案（见 motifs.md）。不用骨架屏、不用灰色占位图。

## 品牌带 BrandBand

页头下方那条横带：左 ⑧图标三连/大× + 中 标题（stencil 体）+ 右 读数小格
（直角墨框 min-width:64px）+ 底线 ⑤虹带 3px。移动端塌缩成 min-height:62px。

## 页脚印章 FooterStamp

`HANDLE_WITH_CARE;` + 斜杠组 + 顶线（见 motifs.md 附）。槽位文本：
`编号;` / `署名;` 可替换。

---

## 移动端注意

- 固定宽输入框一律 `max-width:100%`（否则窄屏顶破容器整页横滚 —— 最难看的失败方式）。
- 母题装饰（大×/条组/品牌带）在 <620px 收高度、收字号，**不删** —— 删了就不是这套语言。
- 表格窄屏可横向滚动，容器加 `overflow-x:auto`，滚动条改直角墨棍。
