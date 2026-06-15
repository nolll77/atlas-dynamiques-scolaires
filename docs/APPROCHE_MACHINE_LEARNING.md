# Approche Machine Learning et Modélisation Algorithmique

L'Atlas des Dynamiques Scolaires s'appuie massivement sur des algorithmes d'apprentissage automatique (Machine Learning). Toutefois, il est essentiel de définir **le type** de Machine Learning utilisé ici, qui diffère fondamentalement de l'Intelligence Artificielle générative (LLM) ou des réseaux de neurones profonds (Deep Learning) omniprésents dans la sphère tech.

Ce document détaille l'arsenal algorithmique du projet et sa finalité scientifique.

---

## 1. Philosophie : "White-Box ML" vs "Black-Box AI"

L'Atlas n'est pas un outil de prédiction ("Prédire la note au bac d'un élève selon son adresse"). C'est une infrastructure d'**inférence structurale**. L'objectif n'est pas de faire un modèle opaque avec $R^2 = 0.99$ mais incompréhensible, mais d'utiliser l'apprentissage pour **extraire de la structure sociologique**, cartographier des trajectoires et prouver mathématiquement des dynamiques (ségrégation, contagion spatiale, ruptures).

Nous pratiquons donc un **Machine Learning scientifique, explicable et interprétable (White-Box)**, reposant principalement sur l'apprentissage non-supervisé, la théorie des graphes et l'économétrie spatiale.

---

## 2. Machine Learning Non-Supervisé (Extraction de Structure)

La question fondamentale du Tome I de l'Atlas est : *Comment définir objectivement les "Mondes Scolaires" sans imposer de seuils subjectifs ?* Pour cela, nous déléguons la classification aux algorithmes.

### A. Clustering Statistique (`scikit-learn`)
L'algorithme analyse l'espace multidimensionnel des lycées (IPS, écart-type IPS, Valeur Foncière, Résultats).
- **Classification Ascendante Hiérarchique (CAH / Ward)** : Construit un arbre de similarité sociologique entre les établissements.
- **Validation Algorithmique** : Le nombre optimal de "Mondes" (clusters) n'est pas choisi au hasard. Il est calculé par la machine via la maximisation du **Silhouette Score** (qui évalue la compacité intra-classe et la séparation inter-classe) et la **Gap Statistic** (qui compare la dispersion avec une distribution uniforme aléatoire).

### B. Détection de Communautés Topologiques (`python-louvain`, `networkx`)
Au-delà des coordonnées GPS, l'Atlas modélise le système scolaire comme un *Réseau Multiplexe*.
- **Algorithme de Louvain** : Une méthode de Machine Learning sur graphe cherchant à maximiser la *modularité*. L'algorithme apprend quelles coalitions de lycées sont plus densément connectées entre elles qu'avec le reste du système (détection de "bulles" de ségrégation ou de bassins de mobilité fermés).

---

## 3. Machine Learning Séquentiel (Dynamiques Temporelles)

Le Tome III (Le Temps et la Réforme) nécessite de comprendre comment les établissements mutent d'une année sur l'autre. Le modèle ne considère plus les variables de manière statique, mais comme des séries temporelles (Time Series).

### A. Les Modèles de Markov Cachés (HMM) via `hmmlearn`
L'hypothèse sociologique forte est qu'un établissement peut changer de "régime" social bien avant que cela ne se reflète massivement dans les moyennes d'IPS.
- L'algorithme HMM (*Hidden Markov Model*) est entraîné pour détecter ces **états latents**. Il modélise les probabilités de transition invisibles, permettant d'identifier de manière précoce les lycées entrant dans une spirale de décrochage ou de gentrification.

### B. Détection Algorithmique de Ruptures (Changepoints) via `ruptures`
Comment prouver qu'une politique publique (comme une modification de la sectorisation) a eu un effet structurel ? 
- Plutôt que d'inspecter visuellement les courbes, l'Atlas utilise l'algorithme **PELT (Pruned Exact Linear Time)**. Il segmente automatiquement les séries temporelles pour trouver le point de rupture exact minimisant une fonction de coût pénalisée. Si l'algorithme "casse" la série précisément l'année de la réforme, la rupture structurelle est prouvée.

---

## 4. Économétrie Spatiale et Modèles Statistiques

La géographie n'est pas juste un "fond de carte", c'est une variable active. Les modèles de Machine Learning classiques (Random Forest, OLS) supposent l'indépendance des observations. Dans l'Atlas, un lycée dépend fortement de ses voisins (Première loi de la géographie de Tobler).

### A. Les Modèles d'Autocorrélation (SAR / SEM) via `pysal`
- **Spatial Autoregressive Models (SAR)** : Le modèle apprend le coefficient de contagion $\rho$ (rho). Il prouve dans quelle mesure l'état sociologique d'un lycée est causé par la moyenne spatiale de son voisinage ($W \times Y$).
- **Spatial Error Models (SEM)** : Apprend à isoler les chocs inobservés (ex: l'ouverture d'une ligne de transport) qui affectent simultanément plusieurs lycées d'une même zone.

### B. Modèles Additifs Généralisés (GAM) via `statsmodels`
- En sociologie de l'éducation, les effets sont rarement linéaires. Par exemple, l'augmentation du prix de l'immobilier impacte la sélection scolaire jusqu'à un certain seuil, puis l'effet plafonne. Les modèles **GAM** permettent au Machine Learning de s'ajuster avec des fonctions de lissage (splines) pour capturer ces effets de saturation (plafonds de verre).

---

## Conclusion : Algorithmes sous contraintes causales

L'introduction de ces bibliothèques puissantes (`scikit-learn`, `pysal`, `hmmlearn`) au sein de l'Atlas permet de passer de la simple cartographie descriptive à la **modélisation systémique complexe**. 

Toutefois, la communauté doit veiller à ce que la sortie de ces modèles (clusters, probabilités de Markov, effets spatiaux) ne soit jamais interprétée de manière déterministe. Le respect strict du cadre théorique est impératif : 👉 **[Lire les Limites de la Causalité](CAUSALITY_LIMITS.md)**.
