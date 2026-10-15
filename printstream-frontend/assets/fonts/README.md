# 字体清单（全部 SIL OFL 1.1，来源 Google Fonts）

再分发规则：随包携带本目录下的 `OFL.txt`；不得单独售卖字体文件；
不得把 Reserved Font Name 用在衍生字体上。文档/页面用了这些字体不受
"必须保持 OFL"约束。

| 文件 | 字体 | 角色 | 用在哪 |
|---|---|---|---|
| `sairastencilone_0.ttf` | Saira Stencil One | 模具体 | **最贴这套工业印刷味**。大标题、品牌名、母题上的文字标 |
| `sairacondensed.ttf` | Saira Condensed | 窄体无衬线 | 分区标题、密集读数行 |
| `teko.ttf` | Teko | 窄体 | 同上，备选 |
| `oswald.ttf` | Oswald | 窄体 | 同上，备选 |
| `bebasneue.ttf` | Bebas Neue | 全大写窄体 | 标签、大写小字 |
| `archivo.ttf` | Archivo | grotesque | 正文备选 |
| `chakrapetch.ttf` | Chakra Petch | 切角科技体 | 需要"切角"感的标题 |
| `jetbrainsmono.ttf` | JetBrains Mono | 等宽 | **读数/数字默认**。tabular-nums 场景 |
| `spacemono.ttf` | Space Mono | 等宽 | 读数备选 |
| `notosanssc.ttf` | Noto Sans SC | 中文正文 | 中文正文默认；10.5MB，按需加载 |

CSS 里的加载顺序（先 Latin 后中文，先展示后补字）：

```css
@font-face{
  font-family:'PS Stencil';src:url('fonts/sairastencilone_0.ttf') format('truetype');
  font-display:swap;
}
/* 字体栈（完整版见 references/design-tokens.md）：
   标题  'PS Stencil','Saira Stencil One',sans-serif
   窄体  'Saira Condensed','Teko','Oswald',sans-serif
   等宽  'JetBrains Mono','Space Mono',ui-monospace,monospace
   中文  'Noto Sans SC','Microsoft YaHei',sans-serif   */
```

授权备注：以上字体均为 Google Fonts 上 OFL 1.1 开源字体；各字体的
Copyright Holder 以字体文件内元数据为准（本包随附许可证全文即满足
OFL 第 2 条的携带要求）。
