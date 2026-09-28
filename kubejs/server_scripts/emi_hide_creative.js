// Colony Protocol: Liminal — hide unobtainable / creative-only items from EMI/JEI/REI.
ServerEvents.tags('item', (event) => {
  event.add('c:hidden_from_recipe_viewers', '#cpliminal:hidden_from_emi');
});

console.log(
  '[cpliminal] EMI hide tag registered (c:hidden_from_recipe_viewers ← cpliminal:hidden_from_emi).'
);
