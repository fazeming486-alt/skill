# 素材库使用指南

`印花集素材库`（本风格的来源素材工程，不在本仓库内）的完整地图 + 每类素材的
正确用法。本 skill 的 `assets/` 里已内置一份**精选子集**（50 张去重母题 +
10 个 OFL 字体），开箱即用；需要更全的素材时回到来源工程库取。

---

## 素材总览

| 目录 | 内容 | 授权 | 用法 |
|---|---|---|---|
| `母题矢量SVG/` | 236 张 vtracer 描摹 SVG（黑填充、透明底） | 自用参考 | **只当形状参考**。要改色/缩放可以，要生产请照 motifs.md 参数化重写 |
| `母题贴片/` | 236 张透明底 PNG + `index.json`（带尺寸与分类）+ 3 张总览表 + 3 张虹带取样条 | 自用参考 | 同上。小图标场景（≤24px）可直接用 |
| `符号库_ISO与GHS/` | ISO 7010 安全标志全集 + GHS 危险公示标签 + ADR/UN 运输标签，514 SVG + 362 PNG(512px) | **MIT**（karlnorling 两个仓库） | **唯一可以放心直接进生产位图的素材**。带 react/vue/sprite/css/elements 多种封装 |
| `06_印刷母题_参考实现/` | `svg-halftone`：把任意图转网点 SVG（default/diamond/hex/poisson 四种网点） | **MIT**（evestera/svg-halftone） | 给图片加"印刷网点"质感的工具；也可只取它的 4 张示例 SVG 当底纹 |
| `08_字体_OFL/` | 10 个 TTF | **OFL 1.1** | 已复制进 skill `assets/fonts/`（含许可证） |
| `配色令牌.json/.css` | 实测配色令牌 | 本项目 | 见 design-tokens.md |

## 母题库分类（index.json 的「类」）

| 类 | 张数 | 内容 |
|---|---|---|
| 方形符号 | 95 | 实心/描边 X、带角标 X、`[+·]` 四角定位标、加号方块、空心方、菱形、◈ 组合菱形、半圆、圆内十字、斜线圆、心形虚线、棋盘小方块 |
| 横向条组 | 93 | 粗黑条三连、细三线组、条码带（左疏右密）、水平刻度尺、▤ 实心条 |
| 纵向条组 | 18 | 竖条码、竖细线簇、`_B42` 竖排标签、竖虹带 |
| 彩色带 | 17 | 粉→青虹带横/竖条、带黑缝的三条带 |
| 细长件 | 13 | 单根长线、带端点引线、虚线弧 + 半圆组合 |

另有两类**文字标**混在里面（未单独分，脚本没做 OCR）：
`HANDLE_WITH_CARE;`、`DESIGN BY WyHXnR;`、`_B42`、`_B15`、`×××Y`。
当"可替换槽位文本"用，格式是 `编号;` / `署名;`。

## 母题库已知缺陷（用之前知道）

1. **重复多** —— 同一形状差几个像素重复排布。先用 skill 的
   `scripts/curate_motifs.py` 按 (类, 尺寸±3px, 大小±15%) 去重再挑。
2. **文字被切** —— `_B42`、`HANDLE_WITH_CARE;` 边界正好压在字上，有截断。
3. **细线断裂** —— 源图 webp 压缩噪声，个别长虚线切成几段。
4. **透明底靠阈值抠** —— 纸白按亮度>235 且 RGB 差<12 判透明，抗锯齿边缘留一圈浅灰。
5. **SVG 是描摹不是重建** —— 直角有零点几像素抖；细线 <2px 偶被吃掉。

## ISO / GHS 符号库（MIT，生产可用）

```
符号库_ISO与GHS/packages/@iso-safety-signs/     # ISO 7010
符号库_ISO与GHS/packages/@ghs-hazard-pictograms/ # GHS
```

每个包都带 `react/`（TS 组件）、`vue/`、`sprite/`（sprite.svg + sprite-ids.json）、
`css/`、`elements/`（Web Components）、`core/`、`assets/`。
**用法**：HTML 里直接 `<use href="…/sprite.svg#ghs06-skull">`；React 项目引包内组件。
它们是红菱形/红边框体系，与印花集的"墨 + 纸"不冲突 —— 红是安全色的职责，
不算装饰彩。禁止事项只有一条：别改它们的形状与红（那是指令性安全色）。

## 网点化（halftone）

给任意图片加印刷网点质感的两种做法：
1. 轻量：直接用 `06_印刷母题_参考实现/images/` 下的 default/diamond/hex/poisson
   四张示例 SVG 当可平铺底纹；
2. 真·网点化：跑该 Rust 项目（或 wasm 版 `svg-halftone-web`）把目标图转成网点 SVG。
   页面上"图片显示"统一走网点化，是这套语言收编照片的标准手法。

## 两处参考实现（抄生成器抄这里）

以下两处是这套风格的原始实现，**不在本仓库内**（属于来源工程）：

1. **CSS 版**（最贴近前端）：ESP32-C5 审计工具固件 Web UI 的
   `components/web_ui/web/index.html` 中 `html[data-theme="printstream"]` 段 ——
   9 个元素逐个落到选择器上，注释里记着每版为什么被否。
   `motifs.md` 的内容就是从这段蒸馏的。
2. **Qt 版**（参数化生成器的原始逻辑）：hashcat_gui 的 `app/widgets.py` ——
   CornerTicks / XStepRuler / BarcodeStrip / ThickBars / BrandBand /
   DiamondCluster / DashedArc / InkProgress / PaperBackground / FooterStamp
   的 QPainter 实现，含密度、渐变、步进的全部参数。

## 重跑/再加工

```bash
# 重新切母题（改阈值/留白/最小面积改脚本常量；需要印花集素材库与 PySide6）
python 印花集素材库/拆母题.py

# 精选去重母题（脚本在本 skill 的 scripts/ 下，参数均有默认值，可直接裸跑）
python scripts/curate_motifs.py \
  "印花集素材库/母题矢量SVG" "motifs" \
  --index "印花集素材库/母题贴片/index.json" --per-cat 10

# 重新描 SVG（两个实测坑）：
#  1) 先把贴片压成"黑形+白底"蒙版再描 —— 直接描带 alpha 的 PNG，
#     vtracer 会把透明当黑，交回来一堆黑方块；
#  2) 这个 Python 绑定没有 background 参数，传了直接 TypeError。
python -c "import vtracer; vtracer.convert_image_to_svg_py('mask.png','out.svg',
        colormode='binary', hierarchical='single', mode='spline',
        filter_speckle=4, corner_threshold=80)"
```
