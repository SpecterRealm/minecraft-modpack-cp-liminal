// Colony Protocol: Liminal — recipe viewer entry removal (EMI/JEI/REI).
RecipeViewerEvents.removeEntries('item', (event) => {
  event.remove([
    'ae2:creative_energy_cell',
    'ae2:creative_storage_cell',
    'create:creative_blaze_cake',
    'create:creative_crate',
    'create:creative_fluid_tank',
    'create:creative_motor',
    'mekanism:creative_bin',
    'mekanism:creative_chemical_tank',
    'mekanism:creative_energy_cube',
    'mekanism:creative_fluid_tank',
  ]);
});

console.log('[cpliminal] EMI creative entries removed via RecipeViewerEvents.');
