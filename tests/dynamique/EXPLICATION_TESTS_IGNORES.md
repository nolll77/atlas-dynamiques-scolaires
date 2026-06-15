# Pourquoi les tests sont-ils "Ignorés" (Jaunes) ?

*Note pédagogique sur le fonctionnement de la validation automatique du projet.*

Sur GitHub, il y a un "robot" (la fameuse intégration continue) qui lance la commande `make tests` à chaque fois qu'un bénévole propose une modification de code.
- Si les tests passent, le robot met une coche verte ✅.
- Si un test échoue, il met une croix rouge ❌, et le code est bloqué.

Le problème qui s'est posé lors de la conception architecturale de l'Atlas est le suivant : l'Auteur a défini 32 tests très stricts pour vérifier les 32 formules mathématiques complexes du Socle 2... mais au démarrage du projet, personne n'a encore programmé le code de ces formules !

Si nous avions laissé les tests normaux : 
Les 32 tests se seraient exécutés, auraient cherché les formules, ne les auraient pas trouvées, et auraient "planté". Le projet afficherait une immense croix rouge ❌ permanente. Cela risque de faire paniquer les contributeurs ("Au secours, tout est cassé !") et empêcherait le robot de valider d'autres travaux.

Nous avons donc choisi l'option **Skipped / Ignoré** : 
Nous avons mis une petite étiquette `@pytest.mark.skip(reason="À implémenter")` sur chacun des 32 tests. Le robot voit les tests, ne les exécute pas pour l'instant, et affiche un petit rond jaune 🟡 (Ignoré).

**Concrètement, qu'est-ce que cela change ?**
1. Le projet garde sa belle coche verte ✅ globale.
2. Les bénévoles voient une liste "To-Do" claire de 32 tests jaunes avec le message : "À implémenter".
3. Dès qu'un développeur code la Formule 12, il enlève l'étiquette jaune sur le test 12. Le test s'exécute enfin "pour de vrai".

Cette stratégie pose les fondations et trace la route pour les développeurs (les tests sont écrits et visibles), tout en gardant notre dépôt GitHub propre et vert !
