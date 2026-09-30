// CP Liminal — Recipe Dump (server-side)
// Makes NO changes. Logs recipe counts by type on world load.
// Dev aid for offline audits — comment out or remove before a player-facing release.
// Companion to scripts/build_recipe_wiki.py (make recipe-wiki).

ServerEvents.recipes(function (event) {
  // recipe.type is a Java ResourceLocation — '' + obj can throw in Rhino if the
  // object doesn't expose a default JS primitive value. Use explicit .toString()
  // inside a try-catch per recipe to survive any individual parse failure.
  var typeCounts = {};
  var errorCount = 0;

  event.forEachRecipe({}, function (recipe) {
    try {
      var t = recipe.type;
      var rtype;
      if (t === null || t === undefined) {
        rtype = '_null';
      } else if (typeof t === 'string') {
        rtype = t;
      } else {
        rtype = t.toString();
      }
      if (typeCounts.hasOwnProperty(rtype)) {
        typeCounts[rtype] = typeCounts[rtype] + 1;
      } else {
        typeCounts[rtype] = 1;
      }
    } catch (e) {
      errorCount = errorCount + 1;
    }
  });

  console.log('[CPL] === Recipe counts by type ===');
  var keys = Object.keys(typeCounts);
  // Sort by count descending using a simple insertion pass
  keys.sort(function (a, b) {
    return typeCounts[b] - typeCounts[a];
  });
  for (var i = 0; i < keys.length; i++) {
    console.log('[CPL]   ' + keys[i] + ': ' + typeCounts[keys[i]]);
  }
  console.log('[CPL] === End recipe counts ===');
  console.log('[CPL] Total recipe types: ' + keys.length);
  if (errorCount > 0) {
    console.log('[CPL] Recipes skipped due to type-read errors: ' + errorCount);
  }
});
