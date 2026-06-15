# Le principe de la "To-Do List" (Test-Driven Architecture)

Dans ce projet, le développement suit un ordre très rigoureux, garantissant les meilleurs standards d'ingénierie :

1. La théorie a d'abord été définie : 31 formules sociologiques dans le Manifeste du Socle 1 (ainsi que 32 pour le Socle 2).
2. Des "moules" (les tests) ont ensuite été créés pour définir informatiquement la bonne réponse attendue pour chaque formule.
3. Mais le code algorithmique final n'a pas encore été écrit ! À l'heure actuelle, seuls l'Indice de Theil et l'Indice d'Entre-Soi ont été codés au sein de l'Atlas (c'est pour cela qu'ils sont marqués "✅ Implémenté").

## Pourquoi ne pas juste faire "Planter" les tests ?

Si l'ensemble de ces tests s'exécutaient normalement aujourd'hui, l'intégration continue (le "robot" de GitHub) chercherait le code de l'algorithme, ne le trouverait pas, et ferait planter tout le projet avec une immense croix rouge ❌ permanente.

Une croix rouge bloque les développements et donne l'impression que le projet est "cassé".

## Le statut "Skipped" (⚠️ Jaune) est un appel aux contributeurs

En marquant ces tests en "Skipped" (Ignoré), le système indique à GitHub : "Il y a un test ici, mais ne le lance pas pour l'instant". Le projet reste ainsi propre et au vert ✅.

C'est en réalité la feuille de route (To-Do List) des futurs contributeurs ! Voici exactement comment va se passer la contribution sur ce projet :

1. En tant que contributeur, vous arrivez sur le projet et lisez la Matrice de Couverture.
2. Vous vous dites : "Tiens, la Distance de Mahalanobis est en Skipped. Je vais la coder !"
3. Vous allez dans le test correspondant, et vous enlevez l'étiquette `Skipped` (`@pytest.mark.skip`).
4. Le test plante logiquement (rouge ❌).
5. Vous écrivez l'algorithme mathématique manquant dans `src/atlas/features/mathematiques/` (ou `dynamique/`).
6. Le test passe au vert (✅).
7. Vous ouvrez une Pull Request, et la Matrice de couverture gagne un nouveau "✅ Implémenté" !

C'est la garantie absolue que le code intégré respecte la théorie : le test est déjà là, agissant comme un "garde-fou", qui n'attend que l'algorithme vienne s'y glisser.
