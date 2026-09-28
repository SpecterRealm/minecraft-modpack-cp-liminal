#!/usr/bin/env python3
"""Patch Prism instance.cfg + minecraft/options.txt for dev. Called by Makefile configure-dev."""
from __future__ import annotations

import os
import re
import sys


def patch_key_value_file(path: str, updates: dict[str, str]) -> None:
    """Patch `key:value` lines (Minecraft options.txt). Missing keys are appended."""
    if not os.path.isfile(path):
        print(f"⚠️  skip options patch — missing {path}", file=sys.stderr)
        return
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    seen: set[str] = set()
    out: list[str] = []
    for line in lines:
        matched = False
        for key, value in updates.items():
            if re.match(rf"^{re.escape(key)}:", line):
                out.append(f"{key}:{value}\n")
                seen.add(key)
                matched = True
                break
        if not matched:
            out.append(line)
    for key, value in updates.items():
        if key not in seen:
            out.append(f"{key}:{value}\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)


def patch_fancymenu_options_file(path: str, *, editor: bool) -> None:
    """Patch instance config/fancymenu/options.txt (editor overlay vs player ship)."""
    if not os.path.isfile(path):
        print(f"⚠️  skip fancymenu UI patch — missing {path}", file=sys.stderr)
        return
    overlay = "'true'" if editor else "'false'"
    modpack = "'false'" if editor else "'true'"
    updates = {
        "B:show_customization_overlay": overlay,
        "B:modpack_mode": modpack,
    }
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for key, value in updates.items():
        pattern = rf"^{re.escape(key)} = .*;$"
        replacement = f"{key} = {value};"
        if re.search(pattern, text, flags=re.M):
            text = re.sub(pattern, replacement, text, flags=re.M)
        else:
            text = text.rstrip() + f"\n{replacement}\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _int_env(name: str) -> str:
    """Read a positive integer env var; reject Makefile variable-bleed bugs."""
    raw = os.environ[name].strip()
    if not raw.isdigit():
        print(
            f"✗ {name} must be a positive integer, got {raw!r}\n"
            f"  (If using dev-canvas, update Makefile — GNU Make 3.x can merge target vars.)",
            file=sys.stderr,
        )
        sys.exit(1)
    return raw


# Prism instance.cfg escaping (same as Verdant setup-prism-instances.py).
# Do not append a literal \n — Prism stores the command as a single line;
# OverrideCommands=true is required or PreLaunch never runs.
PACKWIZ_PRELAUNCH = (
    '\\"$INST_JAVA\\" -jar \\"$INST_MC_DIR/packwiz-installer-bootstrap.jar\\" '
    "--bootstrap-no-update http://localhost:8080/pack.toml"
)


def main() -> int:
    cfg_path = os.environ["DEV_CFG"]
    updates = {
        "OverrideMemory": "true",
        "MaxMemAlloc": os.environ["DEV_MAX_MEM"],
        "MinMemAlloc": os.environ["DEV_MIN_MEM"],
        "OverrideJavaArgs": "true",
        "JvmArgs": os.environ["DEV_JVM_ARGS"],
        # Prism ignores PreLaunchCommand unless Custom Commands override is on.
        "OverrideCommands": "true",
        # Wire packwiz pull so setup-dev is one-shot (no buried Prism Settings step).
        "PreLaunchCommand": PACKWIZ_PRELAUNCH,
    }
    # Keep Prism open when MC exits so you can switch Dev ↔ Vanilla (set DEV_QUIT_PRISM=1 to restore).
    if os.environ.get("DEV_QUIT_PRISM", "0") != "1":
        updates["QuitAfterGameStop"] = "false"

    opts_updates: dict[str, str] = {}
    window_note = ""

    # Window size — Prism instance.cfg + Minecraft options.txt (both required on macOS).
    # Prism alone often loses to GLFW's last size when overrideWidth/Height are 0.
    # Set DEV_OVERRIDE_WINDOW=0 to skip (e.g. macOS Retina mouse offset debugging).
    if os.environ.get("DEV_OVERRIDE_WINDOW", "1") != "0":
        width = _int_env("DEV_WIN_WIDTH")
        height = _int_env("DEV_WIN_HEIGHT")
        updates["OverrideWindow"] = "true"
        updates["OverrideMiscellaneous"] = "true"
        updates["MinecraftWinWidth"] = width
        updates["MinecraftWinHeight"] = height
        updates["LaunchMaximized"] = "false"
        opts_updates["overrideWidth"] = width
        opts_updates["overrideHeight"] = height
        opts_updates["fullscreen"] = "false"
        gui_scale = os.environ.get("DEV_GUI_SCALE", "2").strip()
        if gui_scale:
            if not gui_scale.isdigit():
                print(f"✗ DEV_GUI_SCALE must be an integer, got {gui_scale!r}", file=sys.stderr)
                sys.exit(1)
            opts_updates["guiScale"] = gui_scale
        window_note = f", window={width}×{height} windowed"

    with open(cfg_path, encoding="utf-8") as f:
        cfg = f.read()

    for key, value in updates.items():
        if re.search(rf"^{key}=", cfg, re.M):
            cfg = re.sub(rf"^{key}=.*", f"{key}={value}", cfg, flags=re.M)
        else:
            cfg += f"\n{key}={value}"

    with open(cfg_path, "w", encoding="utf-8") as f:
        f.write(cfg)

    opts_path = os.path.join(os.path.dirname(cfg_path), "minecraft", "options.txt")
    if opts_updates:
        patch_key_value_file(opts_path, opts_updates)

    fm_ui = os.environ.get("DEV_FM_UI", "").strip().lower()
    fm_note = ""
    if fm_ui in ("editor", "canvas", "1", "true", "on"):
        fm_opts = os.path.join(
            os.path.dirname(cfg_path), "minecraft", "config", "fancymenu", "options.txt"
        )
        patch_fancymenu_options_file(fm_opts, editor=True)
        fm_note = ", FancyMenu editor UI on"
    elif fm_ui in ("player", "ship", "0", "false", "off"):
        fm_opts = os.path.join(
            os.path.dirname(cfg_path), "minecraft", "config", "fancymenu", "options.txt"
        )
        patch_fancymenu_options_file(fm_opts, editor=False)
        fm_note = ", FancyMenu player UI (overlay off)"

    instance = os.path.basename(os.path.dirname(cfg_path))
    opts_note = ""
    if opts_updates:
        opts_note = f", options.txt patched ({', '.join(opts_updates.keys())})"
    print(
        f"✓ {instance}: memory={updates['MaxMemAlloc']} MiB max / {updates['MinMemAlloc']} MiB min"
        f"{window_note}{opts_note}{fm_note}, Aikar GC flags applied,"
        f" PreLaunch → packwiz http://localhost:8080/pack.toml"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
