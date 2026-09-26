PACK_NAME    := $(shell grep '^name' pack.toml | sed 's/.*= "\(.*\)"/\1/' | tr -d ':' | tr ' ' '-')
PACK_VERSION := $(shell grep '^version' pack.toml | sed 's/.*= "\(.*\)"/\1/')
DIST_DIR     := dist

CF_OUT  := $(DIST_DIR)/$(PACK_NAME)-$(PACK_VERSION)-curseforge.zip
MR_OUT  := $(DIST_DIR)/$(PACK_NAME)-$(PACK_VERSION).mrpack

PRISM          := /Applications/Prism\ Launcher.app/Contents/MacOS/prismlauncher
PRISM_DATA     := $(HOME)/Library/Application Support/PrismLauncher
PRISM_INSTANCE ?= CP-Liminal-Dev
DEV_CFG        := $(PRISM_DATA)/instances/$(PRISM_INSTANCE)/instance.cfg
SERVE_PID      := .serve.pid

DEV_MAX_MEM    ?= 4096
DEV_MIN_MEM    ?= 512
DEV_WIN_WIDTH  ?= 1920
DEV_WIN_HEIGHT ?= 1080
DEV_OVERRIDE_WINDOW ?= 1
DEV_GUI_SCALE  ?= 2
DEV_JVM_ARGS   := -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 \
                  -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch \
                  -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M \
                  -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 \
                  -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 \
                  -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1
DEV_MC_DIR     := $(PRISM_DATA)/instances/$(PRISM_INSTANCE)/minecraft
BOOTSTRAP_JAR  := $(DEV_MC_DIR)/packwiz-installer-bootstrap.jar
INSTALLER_JAR  := $(DEV_MC_DIR)/packwiz-installer.jar
BOOTSTRAP_URL  := https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar
INSTALLER_URL  := https://github.com/packwiz/packwiz-installer/releases/latest/download/packwiz-installer.jar

.PHONY: help serve refresh check-index install-hooks update export-cf export-mr validate-export all \
	dev dev-launch stop logs configure-dev setup-dev prune-dev-mods version set-version \
	sync-issue-templates version-check config-pull config-diff config-promote config-ship-full

help:
	@echo "Colony Protocol: Liminal — packwiz targets"
	@echo ""
	@echo "  make check-index        fail if index.toml is stale (CI)"
	@echo "  make install-hooks      enable pre-commit packwiz refresh"
	@echo "  make setup-dev          download packwiz installer jars + configure Prism"
	@echo "  make dev                serve + launch $(PRISM_INSTANCE)"
	@echo "  make prune-dev-mods     remove instance mod JARs not in mods/*.pw.toml"
	@echo "  make stop               stop background packwiz serve"
	@echo "  make logs               tail Prism latest.log"
	@echo "  make serve              http://localhost:8080"
	@echo "  make refresh            rebuild index.toml"
	@echo "  make config-pull        rsync instance config → config/"
	@echo "  make config-diff        diff repo config/ vs instance"
	@echo "  make config-promote PROMOTE=\"file.toml …\"  copy selected paths"
	@echo "  make config-ship-full   seed fml.toml before export"
	@echo "  make version            print pack.toml version"
	@echo "  make set-version VERSION=x.y.z"
	@echo "  make export-cf          → $(CF_OUT)"
	@echo "  make validate-export    verify CF zip (after export-cf)"
	@echo "  make export-mr          → $(MR_OUT)"
	@echo "  make all                version-check + export-cf + export-mr"
	@echo ""
	@echo "  PRISM_INSTANCE=$(PRISM_INSTANCE)  DEV_MAX_MEM=$(DEV_MAX_MEM)"

setup-dev: configure-dev
	@[ -d "$(DEV_MC_DIR)" ] || { echo "✗ Instance '$(PRISM_INSTANCE)' minecraft folder not found"; exit 1; }
	@echo "→ downloading packwiz-installer-bootstrap.jar..."
	@curl -fsSL -o "$(BOOTSTRAP_JAR)" "$(BOOTSTRAP_URL)"
	@echo "→ downloading packwiz-installer.jar..."
	@curl -fsSL -o "$(INSTALLER_JAR)" "$(INSTALLER_URL)"
	@echo "✓ jars installed in $(DEV_MC_DIR)"

configure-dev:
	@[ -f "$(DEV_CFG)" ] || { echo "✗ Instance '$(PRISM_INSTANCE)' not found — create it in Prism first"; exit 1; }
	@echo "⚠️  Prism must be fully closed before running this"
	DEV_CFG="$(DEV_CFG)" DEV_MAX_MEM="$(DEV_MAX_MEM)" DEV_MIN_MEM="$(DEV_MIN_MEM)" DEV_JVM_ARGS="$(DEV_JVM_ARGS)" \
		DEV_WIN_WIDTH="$(DEV_WIN_WIDTH)" DEV_WIN_HEIGHT="$(DEV_WIN_HEIGHT)" DEV_OVERRIDE_WINDOW="$(DEV_OVERRIDE_WINDOW)" \
		DEV_GUI_SCALE="$(DEV_GUI_SCALE)" \
		python3 scripts/configure-dev.py

prune-dev-mods:
	@PRISM_INSTANCE="$(PRISM_INSTANCE)" DEV_MC_DIR="$(PRISM_DATA)/instances/$(PRISM_INSTANCE)/minecraft" python3 scripts/prune-dev-mods.py

dev-launch: refresh prune-dev-mods
	@pkill -f "packwiz serve" 2>/dev/null; true
	@echo "→ starting packwiz serve on http://localhost:8080..."
	packwiz serve & echo $$! > $(SERVE_PID)
	@sleep 1
	@echo "→ launching $(PRISM_INSTANCE)..."
	@$(PRISM) --launch "$(PRISM_INSTANCE)" --show-window &
	@echo "✓ Prism launched — run 'make logs' in another terminal; 'make stop' when done"

dev: configure-dev dev-launch

logs:
	@[ -f "$(PRISM_DATA)/instances/$(PRISM_INSTANCE)/minecraft/logs/latest.log" ] \
		&& tail -f "$(PRISM_DATA)/instances/$(PRISM_INSTANCE)/minecraft/logs/latest.log" \
		|| echo "⚠️  No log for $(PRISM_INSTANCE)"

stop:
	@[ -f $(SERVE_PID) ] \
		&& kill $$(cat $(SERVE_PID)) 2>/dev/null \
		&& rm -f $(SERVE_PID) \
		&& echo "✓ packwiz serve stopped" \
		|| echo "⚠️  no serve process found"

serve:
	packwiz serve

refresh:
	packwiz refresh

check-index:
	bash scripts/check-pack-index.sh

install-hooks:
	bash scripts/install-git-hooks.sh

config-pull:
	@PRISM_INSTANCE="$(PRISM_INSTANCE)" DEV_MC_DIR="$(DEV_MC_DIR)" bash scripts/sync-configs.sh

config-diff:
	@bash scripts/config-diff.sh

config-promote:
	@bash scripts/config-promote.sh $(PROMOTE)

config-ship-full:
	@bash scripts/config-ship-full.sh

update:
	packwiz update --all

version:
	@echo "$(PACK_VERSION)"

set-version:
	@test -n "$(VERSION)" || { echo "Usage: make set-version VERSION=x.y.z"; exit 1; }
	@bash scripts/set-version.sh "$(VERSION)"

sync-issue-templates:
	@bash scripts/sync-issue-template-version.sh

version-check:
	@echo "→ Colony Protocol: Liminal $(PACK_VERSION) (from pack.toml)"
	@test -n "$(PACK_VERSION)" || { echo "✗ Could not read version from pack.toml"; exit 1; }

$(DIST_DIR):
	mkdir -p $(DIST_DIR)

export-cf: $(DIST_DIR)
	@rm -f "$(CF_OUT)"
	packwiz curseforge export -o $(CF_OUT)
	@echo "✓ CurseForge export: $(CF_OUT)"

validate-export:
	@test -f "$(CF_OUT)" || { echo "✗ Missing $(CF_OUT) — run make export-cf first"; exit 1; }
	python3 scripts/validate_cf_export.py --zip "$(CF_OUT)"

export-mr: $(DIST_DIR)
	@rm -f "$(MR_OUT)"
	packwiz modrinth export -o $(MR_OUT)
	@echo "✓ Modrinth export: $(MR_OUT)"

all: version-check export-cf export-mr
	@echo "✓ Exports for $(PACK_VERSION):"
	@echo "    $(CF_OUT)"
	@echo "    $(MR_OUT)"
