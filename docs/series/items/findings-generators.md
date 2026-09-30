# Generator catalog: first overlap findings

Built from public source at the pinned refs (see [sources.md](sources.md)). Numbers are source defaults, not in-game readings. Reproduce with `python3 scripts/series-item-catalog.py report --category generator`.

Cataloged: Powah, Mekanism Generators, Create Crafts & Additions, Extreme Reactors. Not yet: Flux Networks, Draconic Evolution, Azurum Miner, AE2 (no generators of note expected).

## Overlap groups

| Function | Items | Note |
|---|---|---|
| Solid/fluid fuel starter | Powah Furnator, Magmator; Mek Heat Generator; CA Liquid Blaze Burner (fuel only) | Powah Furnator burns coal/wood; Mek Heat Generator burns fuel plus lava. |
| Solar | Powah Solar Panel (7 tiers); Mek Solar (50) and Advanced Solar (300) | Two full solar ladders. |
| Kinetic to FE | CA Alternator (480 FE/t at 256 RPM) | Only one; makes Create a power source with no ore. |
| Bio | Mek Bio-Generator (bioethanol); CA bioethanol/biomass | Two mods both add a bioethanol fluid. Check for recipe or fluid conflicts. |
| Nuclear multiblock | Powah Reactor; Extreme Reactors; Mek Fission | Three. |
| Steam turbine | Extreme Reactors Turbine; Mek Industrial Turbine | Two. |
| Multiblock energy storage | CA Modular Accumulator (2M FE, 3x3x5); Extreme Reactors Energy Core; Powah Energy Cell (block) | Candidates for the Ender IO-style bank. |
| Wrench | Extreme Reactors Extreme Wrench; Powah Wrench; plus Create, Mekanism, Morph-o-Tool | At least four wrenches. Morph-o-Tool test candidate. |

## Flags

- **Extreme Reactors depends on ore** (yellorite, anglesite, benitoite). Verdant and Elysian disable ore worldgen, so confirm how fuel is obtained there (sieve? none?) before it counts as a working generator.
- **Extreme Reactors ships its own Patchouli book**; low priority next to the Field Manual.
- **Mekanism config energy units** are internal (Joules); compare with FE only after checking in game.

## Tuning candidates (config first)

- Powah: `general.energy_per_fuel_tick`, per-tier `generation_rates` to slot the Furnator below Mek Heat Generator.
- Mek: `generators.toml` solarGeneration/advancedSolarGeneration to fit under the Powah solar tiers, or gate with KubeJS.
- Extreme Reactors: `powerProductionMultiplier`, size caps.
- Create Additions: `fe_at_max_rpm` and connector limits.

## Next

Catalog the remaining transfer and storage mods (Flux Networks, Draconic Evolution), then decide which generator groups stay tiered versus get one item hidden.

## Multiblock scaling (from source)

| Multiblock | Model | What scales it |
|---|---|---|
| Powah Reactor | tiered | Fixed layout of a core plus parts around it; no size variable. A bigger output means a higher tier, not a bigger build. |
| Mekanism Fission | count-scaled | Burn rate and fuel capacity are per fuel assembly; heat and coolant depend on assembly surface area. |
| Mekanism Turbine | count-scaled | Output limited by min(blades, coils x 4); steam flow by dispersers and volume; steam out by vents. |
| Extreme Reactors Reactor / Turbine | count-scaled | Fuel rods and control rods (reactor), blades and coils (turbine); global multipliers in config. Formula details unverified. |
| Create Additions Accumulator | size-scaled | Capacity and transfer grow per block, up to 3 x 3 x 5 by default. |

Powah is the only reactor where "bigger" is a tier; the others reward building larger, which is closer to the Ender IO-style multiblock feel.
