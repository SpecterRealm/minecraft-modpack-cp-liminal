#!/usr/bin/env python3
"""First-pass auto tagger: adds `tags` to every item in docs/series/items/scan/<mod>.json.

Rules match the item id / name (see RULES). They only add tags the wording makes fairly certain; power tags
are added only for clear cases (generators, batteries, cables). Everything else is left for the loop-back pass
(`series-item-tags.py check --missing`). Hand-curated entries in data/<mod>.json are never touched, and they win
over auto tags in reports.

Usage:
    python3 scripts/series-item-autotag.py run      # tag all scan files (overwrites previous auto tags; items tagged review:checked are kept)
    python3 scripts/series-item-autotag.py sample <mod> [N]
Re-running `series-mod-scan.py run` regenerates the scan files, so run this after it.
"""
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCAN = os.path.join(HERE, "..", "docs", "series", "items", "scan")

W = lambda *ws: re.compile(r"(?:^|[_./ -])(?:" + "|".join(ws) + r")(?:$|[_./ -]|s$)")  # whole-word-ish on id/name

RULES = [
    # (pattern, tags)
    (W("sword", "dagger", "spear", "katana", "scythe", "mace", "halberd", "glaive", "rapier", "claymore", "battleaxe", "trident", "crossbow", "bow", "greatsword", "saber", "sabre", "cutlass", "whip", "flail", "blade"), ["kind:weapon", "function:defend"]),
    (W("arrow", "bolt", "bullet", "ammo", "dart"), ["kind:consumable", "function:defend"]),
    (W("helmet", "chestplate", "leggings", "boots", "cuirass", "hood", "robe", "robes", "tunic", "cap", "hat", "shield", "armor", "armour", "gauntlets", "pauldrons", "greaves", "mask"), ["kind:armor", "function:defend"]),
    (W("pickaxe", "shovel", "hoe", "axe", "hammer", "wrench", "sickle", "shears", "fishing_rod", "paxel", "knife", "crook", "trowel", "chisel", "screwdriver", "saw", "mattock", "excavator"), ["kind:tool"]),
    (W("wrench", "configurator", "screwdriver"), ["function:craft"]),
    (W("apple", "bread", "cake", "pie", "soup", "stew", "cooked", "steak", "porridge", "jam", "juice", "sandwich", "burger", "cookie", "candy", "berries", "berry", "fruit", "meat", "pizza", "chop", "sausage", "salad", "noodles", "pasta", "muffin", "donut", "honey", "cheese", "milk", "egg", "rice", "kelp", "carrot", "potato", "beef", "pork", "mutton", "chicken", "fish", "salmon", "cod"), ["kind:food"]),
    (W("chest", "barrel", "crate", "backpack", "drawer", "shulker", "storage", "cabinet", "bin", "vault", "locker", "safe", "box", "jar", "tank", "silo"), ["function:store"]),
    (W("chest", "barrel", "crate", "backpack", "drawer", "cabinet", "locker", "safe", "box"), ["kind:storage"]),
    (W("battery", "capacitor", "energy_cell", "accumulator", "energy_core", "energycore", "energy_bank", "power_bank", "cell"), ["function:store", "power-role:stores", "power-type:fe"]),
    (W("generator", "furnator", "magmator", "solar_panel", "solar", "dynamo", "alternator", "turbine", "reactor", "thermo_generator", "combustion", "geothermal", "windmill"), ["function:generate", "power-role:makes"]),
    (W("water_wheel", "windmill", "windmill_bearing", "steam_engine", "hand_crank", "creative_motor", "motor", "flywheel"), ["power-type:stress"]),
    (W("cable", "conduit", "connector", "relay", "flux_plug", "flux_point", "flux_controller", "energy_hopper", "energy_transfer"), ["function:transfer", "power-role:transfers", "power-type:fe"]),
    (W("pipe", "tube", "duct", "conveyor", "funnel", "chute", "belt", "sorter", "hopper"), ["function:transfer"]),
    (W("furnace", "smelter", "crusher", "grinder", "pulverizer", "press", "mixer", "centrifuge", "enricher", "compressor", "infuser", "washer", "purifier", "crystallizer", "sieve", "oven", "kiln", "assembler", "fabricator", "processor", "recycler", "extractor", "separator", "smeltery", "foundry", "blender", "cutter", "sawmill", "evaporator", "electrolyzer", "condenser", "distiller", "brewery", "fermenter"), ["kind:machine", "function:process"]),
    (W("factory", "crucible", "nucleosynthesizer", "synthesizer", "charger", "incubator", "spawner"), ["kind:machine", "function:process"]),
    (W("reactor", "turbine", "fission", "fusion", "evaporation", "boiler"), ["kind:multiblock"]),
    (W("bag", "energy_cube", "tank", "bin", "drawer"), ["kind:storage"]),
    (W("bucket", "bucket"), ["kind:tool"]),
    (W("staff", "wand", "focus"), ["kind:tool", "function:enchant"]),
    (W("seed", "seeds", "sapling", "crop", "planter", "soil", "fertilizer", "farmland", "hydroponic", "bee", "hive", "comb", "cultivator", "pot", "harvester", "tree", "flower"), ["function:farm"]),
    (W("miner", "drill", "quarry", "excavator", "digger", "bore", "pickaxe"), ["function:mine"]),
    (W("interface", "pattern", "crafter", "autocraft", "planner", "deployer", "mechanical_arm", "terminal", "assembler", "molecular"), ["function:automate"]),
    (W("crafting_table", "workbench", "anvil", "forge", "smithing", "station", "table"), ["function:craft"]),
    (W("enchant", "enchanting", "rune", "glyph", "spell", "spellbook", "sigil"), ["function:enchant"]),
    (W("lamp", "lantern", "torch", "light", "glowstone"), ["function:light"]),
    (W("teleport", "portal", "elevator", "waypoint", "warp", "elytra", "glider", "jetpack", "rail", "boat", "minecart", "saddle", "horse"), ["function:travel"]),
    (W("rail", "boat", "minecart", "cart", "wagon"), ["kind:transport"]),
    (W("mana", "spell", "glyph"), ["power-type:mana"]),
    (W("source", "sourcelink", "source_jar", "sourcestone", "sourceberry"), ["power-type:source"]),
    (W("emc", "transmutation", "philosopher", "condenser"), ["power-type:emc"]),
    (W("magnet", "jetpack", "goggles", "radar", "scanner", "remote", "tablet", "card", "upgrade", "module", "binding", "compass", "map", "charm", "ring", "amulet", "necklace", "belt"), ["kind:gadget"]),
    (W("potion", "elixir", "scroll", "tonic", "pill", "bandage", "medkit", "canteen", "spawn_egg", "flask", "vial", "tincture"), ["kind:consumable"]),
    (W("dust", "ingot", "nugget", "plate", "gear", "rod", "gem", "crystal", "shard", "powder", "sheet", "essence", "catalyst", "flake", "grit", "pellet", "bar", "raw", "scrap", "fragment", "chunk", "slag", "ash", "coal", "lump"), ["kind:material"]),
    (re.compile(r"(?:^|[_:])(?:raw_[a-z_]+|[a-z_]+_ore|ore_[a-z_]+)$"), ["needs:ore"]),
    (W("nether", "netherite", "blaze", "wither", "soul", "ghast", "crimson", "warped", "basalt", "blackstone"), ["needs:nether"]),
    (W("end_stone", "end_rod", "chorus", "dragon", "purpur", "end_crystal", "shulker"), ["needs:end"]),
    (W("slab", "stairs", "wall", "fence", "door", "trapdoor", "planks", "log", "leaves", "carpet", "pane", "glass", "banner", "painting", "sign", "bed", "statue", "brick", "bricks", "tile", "pillar", "panel", "wool", "concrete", "terracotta", "stone", "cobblestone", "flower", "moss", "mushroom", "vine", "sand", "gravel", "dirt", "grass", "pot"), ["kind:decoration"]),
]
MOD_DEFAULTS = [  # (slug prefix regex, tags) added to every item in matching mods
    (re.compile(r"^(ars-|irons-spells|occultism|theurgy|hexerei)"), ["needs:spell-tech"]),
]


def tag_item(mod, key, it):
    name = key.split(":", 1)[1].lower()
    if "." in name or len(it["name"]) > 60:  # tooltip / hover text that slipped through the scan filter
        return []
    hay = name + " " + it["name"].lower().replace(" ", "_")
    tags = []
    if it["kind"] == "entity":
        tags.append("kind:mob")
    elif it["kind"] == "fluid":
        tags.append("kind:fluid")
    for pat, ts in RULES:
        if pat.search(hay):
            tags += ts
    for pat, ts in MOD_DEFAULTS:
        if pat.search(mod):
            tags += ts
    out = []
    for t in tags:  # stable de-dup
        if t not in out:
            out.append(t)
    if it["kind"] == "block" and not any(t.startswith("kind:") for t in out):
        out.append("kind:block")
    # a block that is only decoration-ish alongside a stronger kind: drop decoration
    kinds = [t for t in out if t.startswith("kind:")]
    if len(kinds) > 1 and "kind:decoration" in out:
        out.remove("kind:decoration")
    return out


def run():
    n = t = 0
    for p in sorted(glob.glob(os.path.join(SCAN, "*.json"))):
        mod = os.path.basename(p)[:-5]
        d = json.load(open(p))
        if "same_repo_as" in d or not d.get("items"):
            continue
        for key, it in d["items"].items():
            if "review:checked" in it.get("tags", []):  # hand-checked: leave alone
                continue
            it["tags"] = tag_item(mod, key, it) + ["review:auto"]
            n += 1
            t += len(it["tags"]) > 1
        d["tags_source"] = "auto (scripts/series-item-autotag.py)"
        d["tagged_on"] = datetime.date.today().isoformat()
        d["tagged_version"] = d.get("ref")
        json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
    print(f"{t}/{n} items tagged")


def sample(mod, n):
    d = json.load(open(os.path.join(SCAN, mod + ".json")))
    for k, it in list(d["items"].items())[:n]:
        print(f"{k:55} {', '.join(it.get('tags', [])) or '-'}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "run":
        run()
    elif len(sys.argv) >= 3 and sys.argv[1] == "sample":
        sample(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 25)
    else:
        print(__doc__)
