#!/usr/bin/env python3
"""HTML/texture generation + main for Liminal recipe wiki."""
from __future__ import annotations

from recipe_wiki_core import (
    MODS_DIR,
    OUT_HTML,
    OUT_JSON,
    Path,
    base64,
    build_slim,
    datetime,
    extract_jar_recipes,
    SKIPPED,
    UNPARSED,
    extract_loot,
    extract_tags,
    installed_mod_ids,
    json,
    parse_kubejs,
    timezone,
    zipfile,
)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# 4. Texture extraction
# ---------------------------------------------------------------------------

def extract_textures() -> dict[str, str]:
    """
    Extract item (and block-fallback) textures from all mod JARs.
    Returns item_id → data URI (base64 PNG).
    Item textures win over block textures.
    """
    item_tex: dict[str, str] = {}
    leaf_tex: dict[str, str] = {}   # fallback: leaf filename only (no subdir)
    block_tex: dict[str, str] = {}

    for jar_path in sorted(MODS_DIR.glob("*.jar")):
        try:
            with zipfile.ZipFile(jar_path) as zf:
                for name in zf.namelist():
                    if not name.endswith(".png"):
                        continue
                    parts = name.split("/")
                    # Expected: assets/<modid>/textures/<item|block>/[subpath].png
                    if len(parts) < 5 or parts[0] != "assets":
                        continue
                    modid    = parts[1]
                    tex_kind = parts[3]           # "item" or "block"
                    rel      = "/".join(parts[4:])
                    item_id  = f"{modid}:{rel[:-4]}"  # strip .png

                    if tex_kind == "item":
                        uri = ("data:image/png;base64,"
                               + base64.b64encode(zf.read(name)).decode())
                        if item_id not in item_tex:
                            item_tex[item_id] = uri
                        # Also register leaf (filename only) as a lower-priority fallback
                        # so e.g. advanced_ae:upgrades/evasion_card.png → advanced_ae:evasion_card
                        leaf_id = f"{modid}:{parts[-1][:-4]}"
                        if leaf_id != item_id and leaf_id not in leaf_tex:
                            leaf_tex[leaf_id] = uri
                    elif tex_kind == "block" and item_id not in block_tex:
                        block_tex[item_id] = (
                            "data:image/png;base64,"
                            + base64.b64encode(zf.read(name)).decode()
                        )
        except Exception:
            pass

    # Priority: item_tex (full path) > leaf_tex (filename only) > block_tex
    merged = {**block_tex, **leaf_tex, **item_tex}
    print(f"Textures: {len(item_tex)} item, {len(leaf_tex)} leaf-fallback, "
          f"{len(block_tex)} block → {len(merged)} total")
    return merged


# ---------------------------------------------------------------------------
# 5. HTML generation
# ---------------------------------------------------------------------------

HTML_TEMPLATE_PATH = Path(__file__).with_name("recipe_wiki_template.html")

def _load_html_template() -> str:
    return HTML_TEMPLATE_PATH.read_text(encoding="utf-8")




def generate_html(slim_index: dict, textures: dict) -> str:
    data_js = json.dumps(slim_index, separators=(",", ":"))
    tex_js  = json.dumps(textures,   separators=(",", ":"))
    return (_load_html_template()
            .replace("RECIPE_DATA_PLACEHOLDER", data_js)
            .replace("TEXTURES_PLACEHOLDER",    tex_js))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    jar_recipes         = extract_jar_recipes()
    removals, additions = parse_kubejs()
    mods                = installed_mod_ids()
    tags                = extract_tags(mods)
    loot                = extract_loot({"mods": mods, "tags": tags})
    slim                = build_slim(jar_recipes, removals, additions, {"mods": mods, "tags": tags})
    textures            = extract_textures()

    # Write JSON index
    OUT_JSON.write_text(
        json.dumps({
            "generated": datetime.now(timezone.utc).isoformat(),
            "item_count": len(slim),
            "tags": tags,
            "loot": loot,
            "unparsed": UNPARSED,
            "skipped_types": dict(sorted(SKIPPED.items(), key=lambda kv: -kv[1])),
            "recipes": slim,
        }, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {OUT_JSON} ({OUT_JSON.stat().st_size // 1024} KB)")

    # Write HTML
    html = generate_html(slim, textures)
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_HTML} ({OUT_HTML.stat().st_size // 1024} KB)")
    print(f"\nOpen: file://{OUT_HTML.resolve()}")


if __name__ == "__main__":
    main()
