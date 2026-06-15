# Le principe de la "To-Do List" (Test-Driven Architecture)

Dans ce projet, nous avons fait les choses dans un ordre très rigoureux, digne des meilleurs standards d'ingénierie :

1. Vous avez d'abord défini la théorie : 31 formules sociologiques dans le Manifeste (ainsi que 32 pour le Socle 2).
2. J'ai ensuite créé ces "moules" (les tests) qui définissent informatiquement la bonne réponse attendue pour chaque formule.
3. Mais le code algorithmique final n'a pas encore été écrit ! À l'heure actuelle, seuls l'Indice de Theil et l'Indice d'Entre-Soi ont été codés par vos soins (c'est pour cela qu'ils sont marqués "✅ Implémenté").

## Pourquoi ne pas juste faire "Planter" les tests ?

Si je laissais les autres tests s'exécuter normalement, le "robot" de GitHub chercherait le code de l'algorithme, ne le trouverait pas, et ferait planter tout le projet avec une immense croix rouge ❌ permanente.

Une croix rouge bloque les autres développeurs et donne l'impression que le projet est "cassé".

## Le "Skipped" (⚠️ Jaune) est un appel aux bénévoles

En marquant ces tests en "Skipped" (Ignoré), le robot de GitHub dit : "Je vois qu'il y a un test ici, mais on m'a dit de ne pas le lancer pour l'instant". Le projet reste propre et au vert ✅.

C'est en réalité la feuille de route (To-Do List) de vos futurs bénévoles ! Voici exactement comment va se passer la suite de votre projet :

1. Un bénévole arrive sur votre projet et lit la Matrice.
2. Il se dit : "Tiens, la Distance de Mahalanobis est en Skipped. Je vais la coder !"
3. Il va dans le test, enlève l'étiquette Skipped.
4. Le test plante (rouge ❌).
5. Il écrit l'algorithme mathématique dans `src/atlas/features/mathematiques/` (ou `dynamique/`).
6. Le test passe au vert (✅).
7. Il vous propose sa modification, et la Matrice de couverture gagne un nouveau "✅ Implémenté" !

C'est la garantie absolue que personne ne va coder n'importe quoi : le test est déjà là, comme un "garde-fou", qui attend que l'algorithme vienne se glisser dedans.
