---
name: printstream-frontend
description: 印花集（PRINTSTREAM）印刷美术风格的前端设计规范与母题生成器。当用户要求用印花集、Printstream、印刷母题、纸墨印刷、印刷网点、halftone、模版字体（stencil）风格设计或改造网页、UI 组件、仪表盘、设计系统时使用。提供实测设计令牌（纸 #f4f6f9 / 墨 #0d1117 / 虹带三色）、九大母题的参数化 CSS/SVG 生成器（四角定位标、X 阶梯标尺、密度条码、粗黑条三连、虹带、点阵菱形簇、虚线弧、图标三连、黑白反相分区）、组件配方、12 条铁律与 12 个已被否决过的反模式。This skill should be used when designing web pages, UI components, dashboards or design systems in the Printstream / ink-on-paper / printed-motif aesthetic, or when the user mentions 印花集风格 UI.
agent_created: true
---

# 印花集 · PRINTSTREAM 前端设计

把 CS2「印花集」贴纸表的平面美术语言落地成前端代码的一整套规范。
核心认知：**这套语言的识别度全在图案上（网点、条码、X 阶梯、角标、虹带、虚线弧），
不在底色上。只换底色不动图案 = 得到的是"浅色模式"，不是一套设计。**

## 工作流（严格按顺序）

1. **先读铁律再动笔** —— `references/rules-and-antipatterns.md`。
   12 条铁律 + 12 个已验证的反模式（都附"为什么不行"）。跳过这步必然踩坑。
2. **定令牌** —— 读 `references/design-tokens.md`，把 `assets/tokens.css`
   引入项目（或把变量抄进现有主题）。所有组件只吃变量，不写裸 hex
   （虹带定义与设备灯色两类例外除外）。
3. **搭骨架** —— `references/components.md`：面板/按钮/表格/统计卡/进度条/
   告警/空状态/品牌带/页脚印章的完整配方，含各交互态。
4. **落母题** —— `references/motifs.md`：九大母题的参数化生成器，按其中的
   "落点"建议放置，并遵守限量纪律（大×全页只此一枚等）。
5. **要贴图/符号/字体/网点化** —— `references/asset-library.md` +
   `assets/`（50 张去重母题 SVG、10 个 OFL 字体、单文件样板页）。
6. **验收** —— `rules-and-antipatterns.md` 末尾的 11 项自查清单，逐条过。

## 三条最重要的纪律（别的全忘了也要记住）

1. **边框就是墨本身（#0d1117），不是浅灰**；圆角一律归零；唯一的"立体"是
   错版硬边（2~3px offset 实心墨影）。印刷品不发光、不浮起、不渐变填色。
2. **彩色只在虹带**（粉 #f8a8a0 → 品红 #f088f0 → 青 #20e0e0 的三条粗横条）。
   功能三态色是"读数"不是装饰，且必须在纸底上可读（深一档）。
3. **反相分区用独立命名的 --inv-* 变量，绝不让两个变量互指**（CSS 变量没有
   交换语义）；反相只改容器配色，ok/idl/bad 判定一个字不动 —— 读数不许说谎。

## 资产清单

| 路径 | 用途 |
|---|---|
| `assets/tokens.css` | 开箱即用：全部设计令牌 + @font-face，直接 `<link>` |
| `assets/demo-printstream.html` | 九母题全部落地的样板控制台，先看它建立视觉基准 |
| `assets/motifs/` | 50 张去重母题 SVG + `manifest.json`（按类标注） |
| `assets/fonts/` | 10 个 OFL 字体 + 许可证 + 加载说明 |
| `references/design-tokens.md` | 色彩/字体/形状/间距令牌与实测比例 |
| `references/motifs.md` | 九大母题生成器（本 skill 的核心价值） |
| `references/components.md` | 组件配方与交互态 |
| `references/rules-and-antipatterns.md` | 铁律 + 反模式 + 验收清单 |
| `references/asset-library.md` | 工程素材库地图、母题库缺陷、ISO/GHS 与网点化用法 |
| `scripts/curate_motifs.py` | 母题库按 (类, 尺寸±3px, 大小±15%) 去重精选 |

## 执行要点

- **母题用代码生成，不贴位图**。固定分辨率贴片一到别的尺寸就露馅；
  `assets/motifs/` 里的描摹 SVG 只当形状参考，生产按 `motifs.md` 重写参数化版本。
- **每个母题限量**：大×全页一枚；粗黑条只跟分区标题；菱形簇只落留白处。
  撒满 = 倒退成素材堆砌。
- **文字标是槽位文本**：`编号;` / `署名;`（如 `_B42`、`DESIGN BY WyHXnR;`），
  可替换，不是固定图形。
- **移动端**：<620px 收高度收字号，**不删母题**；固定宽输入框加 `max-width:100%`。
- **与深色主题配对**：可仿照参考实现做同一页面两套变量（亮=印花集 / 深=影），
  换主题只换分量，结构不动。
- 交付形态（HTML/CSS、React、Tailwind、Vue）自选 —— 换输出不换语言，
  令牌与母题纪律一致。

## 范围

适合工具型控制台、仪表盘、审计/运维类产品页面，以及需要"工业印刷感"的
营销页。不适合：渐变玻璃拟态产品（语言冲突）、以摄影/插画为主视觉的页面
（印花集收编照片的唯一手段是网点化，见 `asset-library.md`）。
