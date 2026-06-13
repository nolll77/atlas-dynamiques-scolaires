# Glossaire Analytique : Atlas des Dynamiques Scolaires

Ce document est conçu pour aider les contributeurs (développeurs, data scientists, sociologues) à comprendre immédiatement les concepts, acronymes et modèles mathématiques utilisés dans le projet.

---

## 1. Bases de Données & Territoire

- **IPS (Indice de Position Sociale)** : Un score calculé par le Ministère de l'Éducation Nationale mesurant le capital culturel et social moyen des familles d'un établissement. Plus il est élevé, plus le public est favorisé.
- **Écart-type de l'IPS ($\sigma$)** : Mesure la dispersion autour de la moyenne de l'IPS. Un établissement avec un $\sigma$ élevé a une forte mixité interne (des élèves très favorisés et très défavorisés cohabitent).
- **DVF (Demandes de Valeurs Foncières)** : Base de données open data de l'État listant toutes les transactions immobilières. Utilisée ici pour lier la valeur du marché immobilier local à l'IPS du lycée.
- **IRIS (Îlots Regroupés pour l'Information Statistique)** : Le plus petit découpage géographique de l'INSEE (environ 2000 habitants). Permet de connaître le revenu médian du quartier exact entourant un lycée.

---

## 2. Métriques de Ségrégation (Tome I)

- **Indice de Gini** : Traditionnellement utilisé pour mesurer les inégalités de richesse (0 = égalité parfaite, 1 = inégalité totale). Ici, appliqué à la distribution spatiale des IPS scolaires.
- **Indice de Theil** : Outil mesurant l'entropie et l'inégalité. Son grand avantage est d'être *décomposable* : il permet de dire exactement "X% de la ségrégation vient des différences entre les villes, et Y% vient des différences entre le public et le privé".
- **Indice de Duncan (Dissimilarité)** : Mesure le pourcentage d'une population (ex: les élèves très favorisés) qui devrait déménager/changer d'école pour que chaque lycée ait exactement la même composition sociale.
- **ANOVA (Analyse de la Variance)** : Test statistique permettant d'évaluer l'impact de plusieurs variables (le statut public/privé, le prix de l'immobilier, la zone) sur l'IPS.
- **HLM (Modèle Multiniveau)** : Modèle statistique permettant d'emboîter les données (un lycée *dans* une commune *dans* un département) pour isoler le "vrai" effet du quartier indépendamment de la politique de l'école.

---

## 3. Réseaux & Clustering (Tome II)

- **CAH (Classification Ascendante Hiérarchique)** : Algorithme de Machine Learning non-supervisé qui regroupe les lycées en "clusters" ou "mondes scolaires" (ex: "La bourgeoisie catholique", "Les élites publiques") en fonction de leurs ressemblances.
- **Dendrogramme** : L'arbre visuel généré par la CAH. Il montre à quel moment et à quelle "distance" sociologique deux groupes de lycées se séparent.
- **Ultramétrie** : Une propriété mathématique vérifiant si la société scolaire est une arborescence parfaite et stricte (une hiérarchie pure) ou si elle comporte des zones floues.
- **Algorithme de Louvain (Modularité)** : Algorithme détectant des "communautés" dans un réseau. Contrairement à la CAH (qui regroupe par distance), Louvain regroupe les lycées par densité de leurs similarités abstraites.
- **Betweenness Centrality (Centralité d'intermédiarité)** : Dans le graphe scolaire, c'est le score d'un lycée qui agit comme un "pont" incontournable entre deux mondes sociaux très différents.
- **Distance de Mahalanobis** : Une mesure de distance qui tient compte de la corrélation entre les variables. Utilisée pour détecter les "outliers", c'est-à-dire les lycées très atypiques par rapport à la norme.
- **Modèle SAR (Spatial Autoregressive)** : Modèle économétrique vérifiant si la ségrégation d'un lycée "déborde" et contamine les lycées géographiquement voisins.

---

## 4. Modèles Temporels et Exploratoires (Tome III)

> ⚠️ **Note :** Les modèles suivants sont "exploratoires". Ce sont des cadres mathématiques de haut niveau utilisés comme outils de réflexion (placés dans le dossier `exploratory/`), et non des preuves de causalité.

- **HMM (Hidden Markov Model / Modèle de Markov Caché)** : Algorithme probabiliste utilisé pour deviner l'état "caché" d'un système. Ici, utilisé pour voir si un lycée bascule silencieusement d'un régime social (ex: "mixte") à un autre (ex: "gentrifié") au fil des années.
- **PELT (Détection de Changepoints)** : Algorithme cherchant le moment exact dans le temps (l'année précise) où la trajectoire d'un lycée s'est statistiquement "brisée" ou a subi un choc de recrutement.
- **Transitions de Phase / Early Warning Signals** : Empruntés à la physique, ces calculs tentent de repérer les "signaux faibles" (ex: une soudaine augmentation de la variance) qui prédisent qu'un système scolaire est sur le point de s'effondrer ou de basculer radicalement.
- **DAG (Directed Acyclic Graph)** : Un réseau de flèches causales. Utilisé pour formaliser nos hypothèses : "Est-ce le quartier qui gentrifie l'école, ou la réputation de l'école qui fait monter le prix du quartier ?".
- **Variété Riemannienne (Géométrie Dynamique)** : Cadre d'abstraction extrême consistant à imaginer que l'espace scolaire n'est pas plat, mais "courbé" par la gravité des inégalités, créant des distances sociales impossibles à franchir malgré une proximité géographique.
- **GNN (Graph Neural Networks)** : Réseaux de neurones conçus pour faire des prédictions directement sur les nœuds d'un graphe. Utilisés ici pour tenter des simulations de scénarios ou de réformes.
