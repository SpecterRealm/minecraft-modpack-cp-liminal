// Colony Protocol: Liminal — ensure FTB Quests book on join.
// FTB Quests 2101.x does not auto-give ftbquests:book (same gap as Elysian #16).
// Re-gift if missing so new worlds always start with it.
// (nudge2: trigger Prettier packwiz refresh after valid index stub)

PlayerEvents.loggedIn((event) => {
  const player = event.player;

  if (player.inventory.count('ftbquests:book') < 1) {
    player.give('ftbquests:book');
  }

  player.tell(Text.of(''));
  player.tell(Text.gold('[ COLONY PROTOCOL: LIMINAL ]'));
  player.tell(Text.of('Planetfall training ground online. Reunite what the modules taught.'));
  player.tell(Text.of(''));
  player.tell(Text.aqua('Getting started:'));
  player.tell(
    Text.of('  Press §eB§r (or open the §eQuest Book§r in your inventory) for the quest journal.')
  );
  player.tell(Text.of('  Start with §eWelcome§r — Field Manual unlocks at the chapter gate.'));
  player.tell(Text.of(''));
});
