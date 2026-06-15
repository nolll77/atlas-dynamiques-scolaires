# Architecture Collaborative : Philosophie et Infrastructure

## Comprendre notre fonctionnement : La Désynchronisation

On pourrait légitimement se demander : *"Si on a déjà décrit tout ce qu'il faut faire dans les Issues GitHub, à quoi servent ces matrices de couverture et ces fichiers de tests remplis de code vide ou ignoré ?"*

La réponse tient en un concept clé de notre architecture : **La désynchronisation**.

Dans un projet collaboratif d'envergure, nous devons séparer strictement l'intention sociologique de l'exécution mathématique. Voici la différence fondamentale entre nos trois piliers :

1. **L'Issue GitHub : Le "Quoi" (L'Organisation sociologique)**
   L'Issue (ex: *#025 — Chapitre 17 : L'indice de dissimilarité spatial*) donne le **contexte sociologique**. Elle indique au contributeur : *"Pour que l'auteur puisse écrire ce chapitre, nous avons besoin de calculer l'Indice de Duncan sur les communes"*. C'est un cahier des charges textuel et narratif.

2. **Le Test `SKIPPED` : Le "Comment" (L'Ingénierie du Code)**
   L'Issue ne dit pas au contributeur *comment* il doit nommer ses variables ou structurer ses données. Sans règles, le code deviendrait un chaos où chaque bénévole imposerait son propre style. C'est là qu'intervient le Test unitaire (ex: `test_indice_dissimilarite_duncan`). Il agit comme le **cahier des charges mathématique**. Il force le contributeur à respecter l'architecture globale : *"Ta fonction doit s'appeler exactement comme ça, prendre ces matrices en entrée, et le résultat doit obligatoirement être positif"*.

3. **La Matrice de Couverture : Le Tableau de Bord (Management)**
   Si un contributeur arrive sur le dépôt dans 6 mois, face à 120 Issues ouvertes, il sera perdu : *"Qu'est-ce qui a déjà été codé par d'autres bénévoles ?"* La Matrice de Couverture (ex: `MATRICE_DE_COUVERTURE_SOCLE_1.md`) est l'unique boussole technique en temps réel. Un statut ⚠️ `Skipped` signifie que l'algorithme manque. Un statut ✅ `Implémenté` indique que la brique est prête et intégrée. Le contributeur peut donc se mettre au travail en toute autonomie.

---

## L'Infrastructure Intangible : Les Gardiens du Temple

Vous constaterez la présence de nombreux fichiers qui ne contiennent pas directement les algorithmes finaux (tests vides, documents méthodologiques). **Il est impératif de conserver ces fichiers et cette arborescence intacts.** Ils constituent la colonne vertébrale du projet :

1. **Les dossiers de tests (ex: `tests/socle_1_mathematiques/`)**
   Ce sont eux qui bloquent et conditionnent notre Intégration Continue (la CI GitHub). Ils agissent comme les **"gardiens du temple"**. Sans eux, n'importe quel contributeur pourrait pousser un code mathématique erroné, qui s'exécuterait silencieusement et corromprait l'ensemble de l'Atlas. Ces tests vides sont des "serrures" que seul le bon code peut ouvrir.

2. **Les Matrices de Couverture (`MATRICE_DE_COUVERTURE...`)**
   Elles constituent notre **vitrine technique**. Lorsqu'un développeur bénévole décide de s'investir un dimanche soir, il n'a pas besoin d'attendre qu'un mainteneur lui assigne une tâche pour savoir ce qu'il reste à faire. Il consulte simplement ce document, repère immédiatement une fonction en statut ⚠️ `Skipped`, et sait qu'il peut se mettre au travail en toute autonomie pour débloquer la situation.

3. **La documentation épistémologique (`REPRODUCTIBILITE_SCIENTIFIQUE.md`, `APPROCHE_MACHINE_LEARNING.md`, `CAUSALITY_LIMITS.md`)**
   C'est l'âme du projet. Cette documentation est ce qui donne tout le prestige au projet et le différencie d'un simple script Python jetable. C'est la preuve qu'il s'agit d'une **infrastructure de recherche de niveau académique** qui pose des règles strictes sur les limites de la causalité, la reproductibilité, et le *White-Box Machine Learning*.
