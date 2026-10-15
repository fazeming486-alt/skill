# skill

智能体（WorkBuddy / Claude 等）可用的设计技能集合仓库。当前收录：

## printstream-frontend

**印花集（PRINTSTREAM）印刷美术风格的前端设计规范与母题生成器。**

把 CS2「印花集」贴纸表的平面美术语言落地成前端代码：纸白底、墨黑框、
印刷网点、条码、X 阶梯、虹带。核心认知 —— 这套语言的识别度全在**图案**上，
不在底色上；只换底色不动图案，得到的是"浅色模式"而不是一套设计。

### 内容

| 路径 | 说明 |
|---|---|
| `SKILL.md` | 技能主入口：触发条件、工作流、三条核心纪律 |
| `references/design-tokens.md` | 实测设计令牌（纸 `#f4f6f9` / 墨 `#0d1117` / 虹带三色）与字体栈 |
| `references/motifs.md` | **九大母题参数化生成器**（核心资产）：四角定位标 / X 阶梯标尺 / 密度条码 / 粗黑条三连 / 虹带 / 点阵菱形簇 / 虚线弧 / 图标三连 / 黑白反相分区 |
| `references/components.md` | 组件配方：面板 / 按钮 / 表格 / 统计卡 / 进度条 / 告警 / 空状态 / 品牌带 / 页脚印章 |
| `references/rules-and-antipatterns.md` | 12 条铁律 + 12 个已被否决的反模式 + 11 项验收清单 |
| `references/asset-library.md` | 来源素材库地图、母题库缺陷、ISO/GHS 符号与网点化用法 |
| `assets/tokens.css` | 开箱即用的 CSS 变量表 + `@font-face` |
| `assets/demo-printstream.html` | 九母题全部落地的样板控制台（浏览器直接打开） |
| `assets/motifs/` | 50 张去重母题 SVG + `manifest.json`（按类标注） |
| `assets/fonts/` | 10 个 OFL 字体 + 许可证 + 加载说明 |
| `scripts/curate_motifs.py` | 母题库去重精选脚本（纯标准库） |

### 使用

1. 把 `printstream-frontend/` 整个目录复制到技能目录
   （WorkBuddy：`~/.workbuddy/skills/`；Claude：`~/.claude/skills/`）。
2. 触发词示例：「用印花集风格做个页面」「Printstream 风格 UI」
   「印刷母题 / 纸墨 / 网点 / halftone 风格改造」。
3. 页面里引入 `assets/tokens.css`，按 `references/` 的规范施工。
4. 先看 `assets/demo-printstream.html` 建立视觉基准。

### 第三方素材授权

见 [NOTICE.md](NOTICE.md)。字体为 SIL OFL 1.1（随包附许可证全文）；
引用的两个 MIT 项目（svg-halftone、ISO/GHS 符号库）未打包，仅文档指引。
