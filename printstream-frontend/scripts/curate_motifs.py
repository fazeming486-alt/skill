#!/usr/bin/env python3
"""从印花集母题库精选去重母题 SVG，产出可直接进项目的素材子集。

背景：母题库（母题矢量SVG/）是按连通域从参考图切出来的，同一形状常差几个像素
重复出现（横向条组 93 张里大量是同一形状的重复）。直接用会得到一堆近似文件。

去重判据（纯本地、无第三方依赖）：
  同类 + 宽高各差 ≤3px + 文件大小相差 ≤15% ⇒ 判为同一母题的重复切片；
  每簇保留文件最小的一个（vtracer 描摹里文件最小通常路径最干净）。

分类沿用手抠贴片那套 index.json 的「类」字段（SVG 与 PNG 同编号）。

用法：
  python curate_motifs.py [输入SVG目录] [输出目录] [--index 分类JSON] [--per-cat 10]

  输入目录需提供 index.json（母题贴片那套分类表，与 SVG 同编号），
  用 --index 指定。参数均可省略，默认按当前目录下的约定相对路径找：
    输入   印花集素材库/母题矢量SVG
    分类   印花集素材库/母题贴片/index.json
    输出   motifs
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_IN = Path("印花集素材库/母题矢量SVG")
DEFAULT_OUT = Path("motifs")
DEFAULT_INDEX = Path("印花集素材库/母题贴片/index.json")

NAME_RE = re.compile(r"^(?P<src>\d+)_(?P<idx>\d+)_(?P<w>\d+)x(?P<h>\d+)\.svg$")
SIZE_TOL = 0.15  # 文件大小相差 ±15% 以内视为同一形状
DIM_TOL = 3     # 宽/高各差 ≤3px 视为同一形状（源图里的重复就是差几个像素）


def load_categories(index_path: Path) -> dict[str, str]:
    """index.json: [{"file": "1_000_100x72.png", "类": "方形符号", ...}, ...]"""
    if not index_path.exists():
        return {}
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out: dict[str, str] = {}
    for item in data:
        f = item.get("file", "")
        stem = f.rsplit(".", 1)[0] if "." in f else f
        if stem:
            out[stem] = item.get("类", "未分类")
    return out


def curate(in_dir: Path, out_dir: Path, index_path: Path, per_cat: int) -> list[dict]:
    cats = load_categories(index_path)
    files = sorted(in_dir.glob("*.svg"))
    if not files:
        raise SystemExit(f"输入目录没有 SVG：{in_dir}")

    # 1) 解析 + 2) 聚类：同类 + 尺寸相近(±3px) + 大小相近(±15%) ⇒ 同一形状
    entries: list[dict] = []
    for f in files:
        m = NAME_RE.match(f.name)
        if not m:
            continue
        stem = f"{m['src']}_{m['idx']}_{m['w']}x{m['h']}"
        entries.append({
            "file": f, "stem": stem, "w": int(m["w"]), "h": int(m["h"]),
            "size": f.stat().st_size, "cat": cats.get(stem, "未分类"),
        })
    if not entries:
        raise SystemExit("没有符合 <图号>_<序号>_<宽>x<高>.svg 命名规则的文件")

    picked: list[dict] = []
    used: list[dict] = []  # 已选代表，用于模糊比对
    for e in sorted(entries, key=lambda e: (e["cat"], e["w"] * e["h"], e["size"])):
        twin = next((u for u in used
                     if u["cat"] == e["cat"]
                     and abs(u["w"] - e["w"]) <= DIM_TOL
                     and abs(u["h"] - e["h"]) <= DIM_TOL
                     and abs(u["size"] - e["size"]) / max(u["size"], 1) <= SIZE_TOL), None)
        if twin is not None:
            twin["dupes"] += 1
            # 保留更"干净"的：同簇里文件更小的换上来做代表
            if e["size"] < twin["size"] * 0.9:
                twin["file"], twin["stem"] = e["file"], e["stem"]
                twin["w"], twin["h"] = e["w"], e["h"]
                twin["size"] = e["size"]
        else:
            used.append({**e, "dupes": 0})
            picked.append(used[-1])

    # 3) 每类限量，先看簇内重复多的（信息密度高），再看尺寸大的（视觉权重高）
    picked.sort(key=lambda e: (e["cat"], -e["dupes"], -(e["w"] * e["h"])))
    by_cat: dict[str, list[dict]] = {}
    for e in picked:
        by_cat.setdefault(e["cat"], []).append(e)

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    for cat, items in sorted(by_cat.items()):
        for e in items[:per_cat]:
            dst = out_dir / e["file"].name
            shutil.copyfile(e["file"], dst)
            manifest.append({
                "file": e["file"].name, "w": e["w"], "h": e["h"],
                "类": cat, "簇内重复": e["dupes"],
            })
    manifest.sort(key=lambda m: m["file"])
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("in_dir", nargs="?", default=str(DEFAULT_IN))
    ap.add_argument("out_dir", nargs="?", default=str(DEFAULT_OUT))
    ap.add_argument("--index", default=str(DEFAULT_INDEX))
    ap.add_argument("--per-cat", type=int, default=10)
    a = ap.parse_args()
    manifest = curate(Path(a.in_dir), Path(a.out_dir), Path(a.index), a.per_cat)
    total_dupes = sum(m["簇内重复"] for m in manifest)
    print(f"精选 {len(manifest)} 张 → {a.out_dir}")
    for cat in sorted({m['类'] for m in manifest}):
        n = sum(1 for m in manifest if m["类"] == cat)
        print(f"  {cat}: {n}")
    print(f"（这些精选张背后共砍掉 {total_dupes} 张近似重复）")


if __name__ == "__main__":
    sys.exit(main())
