# NOTICE · 第三方素材与授权

## 字体（`printstream-frontend/assets/fonts/`，随包分发）

- Saira Stencil One / Saira Condensed / Teko / Oswald / Bebas Neue /
  Archivo / Chakra Petch / JetBrains Mono / Space Mono / Noto Sans SC
- 来源：Google Fonts
- 许可：SIL Open Font License 1.1（全文见 `assets/fonts/OFL.txt`）
- 遵守项：再分发需随附许可证；不得单独售卖字体；不得将 Reserved Font Name
  用于衍生字体。

## 参考实现（未打包，仅文档引用）

- [svg-halftone](https://github.com/evestera/svg-halftone)（evestera）— MIT —
  图片转网点 SVG 的工具，本规范中"网点化"手法的来源。
- [iso-safety-signs](https://github.com/karlnorling/iso-safety-signs) 与
  [ghs-hazard-pictograms](https://github.com/karlnorling/ghs-hazard-pictograms)
  （karlnorling）— MIT — ISO 7010 / GHS 安全符号库，`references/asset-library.md`
  中有用法指引。

## 母题（`printstream-frontend/assets/motifs/`）

- 由用户提供的印花集参考图经连通域切片 + vtracer 描摹得到，属**自用参考**。
- 已知缺陷：重复切片（已用 `scripts/curate_motifs.py` 去重）、文字标截断、
  细线断裂、阈值抠图灰边、描摹亚像素抖。
- 生产用途请按 `references/motifs.md` 的参数化生成器重写，不要直接放大位图。

## 自有内容许可

- `SKILL.md` 与 `references/` 下的文档与代码片段：仓库主人可自行添加
  `LICENSE` 文件声明；未声明前保留所有权利。
