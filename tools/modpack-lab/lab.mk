# modpack-lab make targets. Include from a pack Makefile:  include tools/modpack-lab/lab.mk
LAB_DIR  ?= tools/modpack-lab
LAB_OUT  ?= .lab
LAB_ARGS ?=

lab-doctor:    ## check Docker and the pack are ready for a server snapshot
	@$(LAB_DIR)/lab.sh doctor --out $(LAB_OUT) $(LAB_ARGS)

lab-snapshot:  ## boot the pack on a headless server in Docker and save .lab/snapshot.json (needs EULA=1)
	@$(LAB_DIR)/lab.sh snapshot --out $(LAB_OUT) $(if $(EULA),--accept-eula,) $(LAB_ARGS)

lab-dump: lab-snapshot  ## snapshot, then write docs/recipe_data.json from the server's recipes
	@python3 scripts/snapshot-to-dump.py --snapshot $(LAB_OUT)/snapshot.json

.PHONY: lab-doctor lab-snapshot lab-dump
