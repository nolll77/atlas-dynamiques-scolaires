# ARCHIVE V3 DÉTAILLÉE DES ISSUES (123 ISSUES)

Ce fichier contient la liste exhaustive des issues à générer sur GitHub, avec les descriptions techniques enrichies.

## MILESTONE : Setup & DevOps
### Issue — [DevOps] #001 — Structure du dépôt GitHub & CI/CD
**Labels:** setup, devops, difficulty: easy
- **Contexte Analytique :** Créer la fondation robuste du projet open-source.
- **Périmètre Technique (Ouvert aux contributions) :** Configuration des GitHub Actions (linting, tests), sécurisation de la branche main, et création des templates d'issues et de Pull Requests.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Validation de l'arborescence (src/, exploratory/, data/, figures/).

## MILESTONE : Setup & DevOps
### Issue — [DevOps] #002 — Tests unitaires (infrastructure & pytest)
**Labels:** setup, devops, difficulty: easy
- **Contexte Analytique :** Garantir la reproductibilité et la fiabilité du code analytique.
- **Périmètre Technique (Ouvert aux contributions) :** Mise en place de `pytest`. Écriture des premiers tests unitaires basiques pour les fonctions de nettoyage de données.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Pas de rédaction requise.

## MILESTONE : Setup & DevOps
### Issue — [DevOps] #003 — Experiment tracking (DVC & MLflow)
**Labels:** setup, devops, difficulty: easy
- **Contexte Analytique :** Le projet implique des données lourdes et des modèles de ML (HMM, Louvain). Il faut versionner la donnée.
- **Périmètre Technique (Ouvert aux contributions) :** Configuration de DVC (Data Version Control) pour lier le dataset maître sans le pousser sur GitHub, et setup du dossier `runs/`.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Pas de rédaction requise.

## MILESTONE : Setup & DevOps
### Issue — [Data] #004 — Pipeline Data : Ingestion Base Maître Enrichie
**Labels:** setup, data, difficulty: easy
- **Contexte Analytique :** La recherche nécessite une base multidimensionnelle (IPS, GPS, DVF, Bac).
- **Périmètre Technique (Ouvert aux contributions) :** Script Python dans `src/data/` qui télécharge, nettoie et joint IPS, résultats Bac, IRIS (INSEE), GPS et DVF. Sauvegarde versionnée DVC.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Pas de rédaction requise.

## MILESTONE : Setup & DevOps
### Issue — [Dataviz] #005 — Figure Signature 1 : Carte IPS IDF
**Labels:** setup, dataviz, map, difficulty: medium
- **Contexte Analytique :** Visualiser la structure spatiale de la ségrégation.
- **Périmètre Technique (Ouvert aux contributions) :** Script (GeoPandas) générant une carte choroplèthe haute def (IPS moyen + revenus IRIS superposés).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction de la légende.

## MILESTONE : Setup & DevOps
### Issue — [Dataviz] #006 — Figure Signature 2 : Scatter IPS vs Écart-type
**Labels:** setup, dataviz, difficulty: medium
- **Contexte Analytique :** Montrer que la moyenne masque la mixité interne.
- **Périmètre Technique (Ouvert aux contributions) :** Script générant le scatter plot IPS vs écart-type, coloration public/privé, densité KDE.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse sociologique des quadrants.

## MILESTONE : Setup & DevOps
### Issue — [Dataviz] #007 — Figure Signature 3 : Réseau Louvain
**Labels:** setup, dataviz, network, difficulty: medium
- **Contexte Analytique :** Cartographier la proximité structurelle entre lycées.
- **Périmètre Technique (Ouvert aux contributions) :** Script (NetworkX) construisant le graphe de similarité, coloré par communauté Louvain.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Exploitation visuelle pour le Tome II.

## MILESTONE : Setup & DevOps
### Issue — [Dataviz] #008 — Figure Signature 4 : Trajectoires Temporelles
**Labels:** setup, dataviz, time-series, difficulty: medium
- **Contexte Analytique :** Montrer la dynamique de la ségrégation dans le temps.
- **Périmètre Technique (Ouvert aux contributions) :** Script traçant les séries temporelles avec marquage des changepoints.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Support visuel pour le Tome III.

## MILESTONE : Tome I - Pages Liminaires
### Issue — Préface générale de la trilogie
**Labels:** tome-1, editorial, difficulty: easy
- **Contexte Analytique :** Expliquer pourquoi la trilogie existe (manifeste méthodologique).
- **Périmètre Technique (Ouvert aux contributions) :** Aucun développement.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction du manifeste : l'école face aux structures réelles (8-12 pages).

## MILESTONE : Tome I - Pages Liminaires
### Issue — Avant-propos Tome I & Note éthique
**Labels:** tome-1, editorial, difficulty: easy
- **Contexte Analytique :** Introduire le Tome I et cadrer l'éthique.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun développement.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédiger l'avertissement : les noms cités le sont à partir de données publiques, sans évaluation d'intentions individuelles.

## MILESTONE : Tome I - Pages Liminaires
### Issue — Introduction Générale : Le paradoxe de l'école républicaine
**Labels:** tome-1, editorial, difficulty: easy
- **Contexte Analytique :** Poser le paradoxe central.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun développement.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Présentation narrative du corpus enrichi et justification de l'approche structurale.

## MILESTONE : Tome I - Partie I
### Issue — Chapitre 1 — L'IPS, un indice, pas une vérité
**Labels:** tome-1, data-analysis, difficulty: medium
- **Contexte Analytique :** Déconstruire statistiquement l'IPS.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul des corrélations entre IPS, PCS et revenus IRIS. Code pour un indice composite en annexe.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction du chapitre et de l'encadré 'L'IPS peut-il être instrumentalisé ?' sans accusation.

## MILESTONE : Tome I - Partie I
### Issue — Chapitre 2 — L'écart-type, révélateur de mixité cachée
**Labels:** tome-1, data-analysis, difficulty: medium
- **Contexte Analytique :** Montrer que la moyenne est insuffisante.
- **Périmètre Technique (Ouvert aux contributions) :** Corrélation entre écart-type et DVF (marchés immobiliers homogènes).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des cas emblématiques en décrivant des 'clusters d'homogénéité'.

## MILESTONE : Tome I - Partie I
### Issue — Chapitre 3 — Panorama du corpus enrichi
**Labels:** tome-1, stats, difficulty: easy
- **Contexte Analytique :** Vue d'ensemble descriptive.
- **Périmètre Technique (Ouvert aux contributions) :** Génération des summary statistics consolidant IPS/IRIS/Bac.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation des distributions. Encadré sur 'les absents du classement'.

## MILESTONE : Tome I - Partie II
### Issue — Chapitre 4 — La carte de l'élite scolaire francilienne
**Labels:** tome-1, map, difficulty: medium
- **Contexte Analytique :** Analyser le croissant de l'ouest.
- **Périmètre Technique (Ouvert aux contributions) :** Corrélation IPS moyen communal vs prix médian au m² (DVF).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication de la co-production ségrégation scolaire/résidentielle.

## MILESTONE : Tome I - Partie II
### Issue — Chapitre 5 — Les trois couronnes : trois systèmes scolaires ?
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Décomposer la variance spatiale.
- **Périmètre Technique (Ouvert aux contributions) :** ANOVA spatiale à 3 facteurs (zone, public/privé, IRIS). Calcul de Duncan par commune.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation relative : 'La géographie explique X%, le statut Y%'.

## MILESTONE : Tome I - Partie II
### Issue — Chapitre 6 — La ségrégation invisible
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Le paradoxe des communes mixtes mais d'écoles séparées.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de l'indice de fausse mixité Fc. Exploration des données IDF Mobilités (transports).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des mécanismes de contournement (carte scolaire).

## MILESTONE : Tome I - Partie II
### Issue — Chapitre 7 — Secteur public vs privé : géographie différenciée
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Mesurer la polarisation institutionnelle.
- **Périmètre Technique (Ouvert aux contributions) :** Corrélation densité du privé / prix DVF. Calcul du delta IPS par zone.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Histoire du réseau catholique. Encadré sur les lycées hors-contrat.

## MILESTONE : Tome I - Partie III
### Issue — Chapitre 8 — L'aristocratie scolaire fermée
**Labels:** tome-1, cluster, difficulty: medium
- **Contexte Analytique :** Décrire l'élite absolue.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du score d'entre-soi composite (IPS/σ).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse sans imputation d'intention.

## MILESTONE : Tome I - Partie III
### Issue — Chapitre 9 — La grande bourgeoisie catholique élargie
**Labels:** tome-1, cluster, difficulty: medium
- **Contexte Analytique :** Décrire le second cluster.
- **Périmètre Technique (Ouvert aux contributions) :** Extraction des profils statistiques du cluster.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative descriptive.

## MILESTONE : Tome I - Partie III
### Issue — Chapitre 10 — Les élites académiques publiques
**Labels:** tome-1, cluster, difficulty: medium
- **Contexte Analytique :** Décrire le cluster public d'excellence.
- **Périmètre Technique (Ouvert aux contributions) :** Extraction des profils statistiques.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative descriptive.

## MILESTONE : Tome I - Partie III
### Issue — Chapitre 11 — Les privés intermédiaires ouverts
**Labels:** tome-1, cluster, difficulty: medium
- **Contexte Analytique :** Décrire les hybrides urbains.
- **Périmètre Technique (Ouvert aux contributions) :** Extraction des profils statistiques.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative descriptive.

## MILESTONE : Tome I - Partie III
### Issue — Chapitre 12 — Les élites internationales et scientifiques
**Labels:** tome-1, cluster, difficulty: medium
- **Contexte Analytique :** Décrire les filières hors-modèle.
- **Périmètre Technique (Ouvert aux contributions) :** Extraction des profils statistiques.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative descriptive.

## MILESTONE : Tome I - Partie III
### Issue — Chapitre 13 — Les lycées publics favorisés résidentiels
**Labels:** tome-1, cluster, difficulty: medium
- **Contexte Analytique :** Décrire les lycées de quartiers aisés.
- **Périmètre Technique (Ouvert aux contributions) :** Extraction des profils statistiques.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative descriptive.

## MILESTONE : Tome I - Partie IV
### Issue — Chapitre 14 — Construire un score d'entre-soi social
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Créer un indicateur de fermeture.
- **Périmètre Technique (Ouvert aux contributions) :** Code calculant IPS/σ normalisé (z-scores).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note éthique sur ce score analytique.

## MILESTONE : Tome I - Partie IV
### Issue — Chapitre 15 — L'indice de Gini des lycées franciliens
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Mesurer l'inégalité pure.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du Gini spatial et institutionnel.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Comparatif international court.

## MILESTONE : Tome I - Partie IV
### Issue — Chapitre 16 — L'indice de Theil : ségrégation décomposable
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Décomposer l'inégalité totale.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du Theil global, within/between zones et revenus IRIS.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication de la décomposition.

## MILESTONE : Tome I - Partie IV
### Issue — Chapitre 17 — L'indice de dissimilarité spatial
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Mesurer la séparation physique.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de Duncan (D) et corrélation avec l'accessibilité transport.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse de la dissimilarité.

## MILESTONE : Tome I - Partie IV
### Issue — Chapitre 18 — L'indice global de fragmentation scolaire
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Synthèse composite.
- **Périmètre Technique (Ouvert aux contributions) :** Agrégation Theil+ANOVA+Duncan.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Conclusion de la partie analytique.

## MILESTONE : Tome I - Partie V
### Issue — Chapitre 19 — ANOVA simple : public/privé explique-t-il tout ?
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Prouver la part de variance du secteur.
- **Périmètre Technique (Ouvert aux contributions) :** ANOVA unidimensionnelle sur l'IPS.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Formulation prudente des associations.

## MILESTONE : Tome I - Partie V
### Issue — Chapitre 20 — ANOVA multi-facteurs
**Labels:** tome-1, stats, difficulty: medium
- **Contexte Analytique :** Ajouter géographie, type, IRIS, DVF.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle complet ANOVA multidimensionnelle.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Décomposition et interprétation des facteurs.

## MILESTONE : Tome I - Partie V
### Issue — Chapitre 21 — Le modèle multiniveau (HLM)
**Labels:** tome-1, stats, difficulty: hard
- **Contexte Analytique :** Isoler l'effet quartier.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle hiérarchique Lycée -> Commune -> Zone avec covariables niveau 2.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication du R2 marginal vs conditionnel.

## MILESTONE : Tome I - Partie V
### Issue — Chapitre 22 — Vers un modèle causal : DAG statique
**Labels:** tome-1, exploratory, difficulty: hard
- **Contexte Analytique :** Formaliser les hypothèses causales.
- **Périmètre Technique (Ouvert aux contributions) :** Construction du Directed Acyclic Graph (DAG) intégrant géographie, marché et IPS.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Cadrage épistémologique : outil de formalisation, non de causalité stricte.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Conclusion du Tome I
**Labels:** tome-1, editorial, difficulty: easy
- **Contexte Analytique :** Synthèse statique.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun développement.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Transition vers le réseau (Tome II).

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A1 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A1).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A2 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A2).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A3 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A3).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A4 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A4).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A5 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A5).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A6 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A6).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A7 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A7).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A8 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A8).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome I - Conclusion & Annexes
### Issue — Annexe A9 : Documentation et Code Tome I
**Labels:** tome-1, documentation, difficulty: easy
- **Contexte Analytique :** Assurer la reproductibilité.
- **Périmètre Technique (Ouvert aux contributions) :** Mise au propre du code, tableaux et sources (A9).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.


## MILESTONE : Tome II - Pages Liminaires
### Issue — Avant-propos Tome II & Note éthique
**Labels:** tome-2, editorial, difficulty: easy
- **Contexte Analytique :** Transition du territoire au réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note éthique : les positions dans le graphe sont analytiques, pas institutionnelles.

## MILESTONE : Tome II - Pages Liminaires
### Issue — Introduction : Du classement au réseau
**Labels:** tome-2, editorial, difficulty: easy
- **Contexte Analytique :** Présenter la similarité sociale comme un lien topologique.
- **Périmètre Technique (Ouvert aux contributions) :** Justification formelle de la métrique de similarité choisie.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Cadrage de l'approche réseau sur données agrégées.

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 1 — La CAH comme outil sociologique
**Labels:** tome-2, cluster, difficulty: medium
- **Contexte Analytique :** Classification sur vecteur enrichi.
- **Périmètre Technique (Ouvert aux contributions) :** Script CAH de Ward, Silhouette, Gap, Mojena.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Comparaison conceptuelle des métriques.

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 2 — Le dendrogramme comme arbre social
**Labels:** tome-2, cluster, difficulty: medium
- **Contexte Analytique :** Lecture des branches de séparation.
- **Périmètre Technique (Ouvert aux contributions) :** Tracé du dendrogramme avec variables enrichies.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Le premier split est-il défini par le capital culturel ou les revenus ?

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 3 — Cinq clusters, cinq mondes scolaires
**Labels:** tome-2, cluster, difficulty: medium
- **Contexte Analytique :** Description des mondes.
- **Périmètre Technique (Ouvert aux contributions) :** Analyse descriptive moyenne des 5 clusters.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Description analytique (sans intention).

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 4 — Validation statistique des clusters
**Labels:** tome-2, stats, difficulty: medium
- **Contexte Analytique :** Prouver la robustesse des clusters.
- **Périmètre Technique (Ouvert aux contributions) :** Stabilité bootstrap (ARI) avec retrait de 10% des données.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des cas ambigus.

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 5 — L'ultramétrie
**Labels:** tome-2, math, difficulty: hard
- **Contexte Analytique :** Le système est-il une hiérarchie stricte ?
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de corrélation cophenétique. Identification des ponts ultramétriques.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note de prudence sur la hiérarchie formelle.

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 6 — Détection de communautés : Louvain
**Labels:** tome-2, network, difficulty: medium
- **Contexte Analytique :** Passer de la distance à la modularité.
- **Périmètre Technique (Ouvert aux contributions) :** Graphe de similarité + Algo de Louvain. Comparaison réseau pur vs réseau enrichi.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Différence conceptuelle avec la CAH.

## MILESTONE : Tome II - Partie I : Topologie et Clustering
### Issue — Chapitre 7 — Louvain multi-couches (Multiplex)
**Labels:** tome-2, network, difficulty: hard
- **Contexte Analytique :** Réseau à N dimensions.
- **Périmètre Technique (Ouvert aux contributions) :** Graphe multiplex (Social, Académique, Géographique). Détection transversale.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des divergences topologie/géographie.

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 8 — Construire un réseau de similarité
**Labels:** tome-2, network, difficulty: medium
- **Contexte Analytique :** Matrice de distance et seuillage.
- **Périmètre Technique (Ouvert aux contributions) :** Comparaison avec réseau aléatoire (modèle nul) pour tester la significativité.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation de la densité.

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 9 — Centralité : qui structure le réseau ?
**Labels:** tome-2, network, difficulty: medium
- **Contexte Analytique :** Hubs et ponts.
- **Périmètre Technique (Ouvert aux contributions) :** Degree, betweenness, eigenvector. Corrélation avec les résultats Bac.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Un lycée central est-il performant ?

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 10 — Les ponts entre mondes scolaires
**Labels:** tome-2, network, difficulty: medium
- **Contexte Analytique :** Lycées à la frontière de mondes sociaux.
- **Périmètre Technique (Ouvert aux contributions) :** Top 10 score de pont composite.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note éthique : pont = structure, pas intention d'ouverture.

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 11 — Flux de mobilité : matrice de Markov
**Labels:** tome-2, stats, difficulty: medium
- **Contexte Analytique :** Mobilité inter-cluster simulée.
- **Périmètre Technique (Ouvert aux contributions) :** Matrice de transition simulée (et calibrée avec données Affelnet si dispos).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note de prudence stricte.

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 12 — Corridors sociaux
**Labels:** tome-2, network, difficulty: medium
- **Contexte Analytique :** Autoroutes de mobilité.
- **Périmètre Technique (Ouvert aux contributions) :** Score de corridor = observé / attendu.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Identification des flux massifs.

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 13 — Ascenseurs sociaux vs filtres
**Labels:** tome-2, network, difficulty: medium
- **Contexte Analytique :** Gradient des corridors.
- **Périmètre Technique (Ouvert aux contributions) :** Gradient positif = ascenseur, négatif = filtre.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Éthique : éviter les jugements normatifs.

## MILESTONE : Tome II - Partie II : Réseau de flux et Mobilité
### Issue — Chapitre 14 — Réseau multiplex et analyse multi-couches
**Labels:** tome-2, network, difficulty: hard
- **Contexte Analytique :** Centralité inter-couches.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul IFC (Indice de Fragmentation Inter-Couches).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Corrélation entre les couches.

## MILESTONE : Tome II - Partie III : Structures Cachées
### Issue — Chapitre 15 — Distance de Mahalanobis (Atypicité)
**Labels:** tome-2, math, difficulty: hard
- **Contexte Analytique :** Trouver les outliers structurels.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul des distances de Mahalanobis. Croisement avec Valeur Ajoutée (Bac).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Les outliers sont-ils des paradoxes académiques ?

## MILESTONE : Tome II - Partie III : Structures Cachées
### Issue — Chapitre 16 — Les zones de bascule
**Labels:** tome-2, math, difficulty: medium
- **Contexte Analytique :** Inversion de gradient.
- **Périmètre Technique (Ouvert aux contributions) :** Détection des points où plus d'IPS = moins de performance.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation causale spéculative (note).

## MILESTONE : Tome II - Partie III : Structures Cachées
### Issue — Chapitre 17 — Résidus structurels
**Labels:** tome-2, stats, difficulty: medium
- **Contexte Analytique :** Où le modèle se trompe-t-il le plus ?
- **Périmètre Technique (Ouvert aux contributions) :** Score de blind spot spatial. Corrélation résidus / accessibilité transport.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Effets de réseau non capturés.

## MILESTONE : Tome II - Partie III : Structures Cachées
### Issue — Chapitre 18 — Classes latentes : mondes cachés
**Labels:** tome-2, math, difficulty: hard
- **Contexte Analytique :** Multi-appartenance.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle GMM.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Entropie locale.

## MILESTONE : Tome II - Partie III : Structures Cachées
### Issue — Chapitre 19 — Frontières sociales floues (KDE)
**Labels:** tome-2, stats, difficulty: hard
- **Contexte Analytique :** Où les mondes se mélangent.
- **Périmètre Technique (Ouvert aux contributions) :** Gradient KDE et entropie de transition.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Indice de flou.

## MILESTONE : Tome II - Partie III : Structures Cachées
### Issue — Chapitre 20 — Tension hiérarchie/réseau
**Labels:** tome-2, math, difficulty: medium
- **Contexte Analytique :** Cohérence globale.
- **Périmètre Technique (Ouvert aux contributions) :** Score de désalignement arbre/réseau.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Où la mobilité échappe à la hiérarchie.

## MILESTONE : Tome II - Partie IV : Fragmentation avancée
### Issue — Chapitre 21 — Pression ségrégative locale (PSL)
**Labels:** tome-2, stats, difficulty: medium
- **Contexte Analytique :** Tension ressentie locale.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul PSL avec IRIS+DVF.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Carte IDF et transport.

## MILESTONE : Tome II - Partie IV : Fragmentation avancée
### Issue — Chapitre 22 — Indice de fragmentation inter-couches
**Labels:** tome-2, stats, difficulty: hard
- **Contexte Analytique :** Décomposition multi-couches.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul IFC public/privé, IPS, GPS.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Asymétrie.

## MILESTONE : Tome II - Partie IV : Fragmentation avancée
### Issue — Chapitre 23 — Perméabilité structurelle
**Labels:** tome-2, stats, difficulty: medium
- **Contexte Analytique :** Optimum de perméabilité.
- **Périmètre Technique (Ouvert aux contributions) :** Flux x distance hiérarchique.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Passerelles vs verrous.

## MILESTONE : Tome II - Partie IV : Fragmentation avancée
### Issue — Chapitre 24 — Clusters absorbants
**Labels:** tome-2, stats, difficulty: medium
- **Contexte Analytique :** Puits scolaires.
- **Périmètre Technique (Ouvert aux contributions) :** Condition spectrale d'attracteur.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Accumulation des ressources.

## MILESTONE : Tome II - Partie V : Spatial et Causal
### Issue — Chapitre 25 — Modèle autorégressif spatial (SAR)
**Labels:** tome-2, stats, difficulty: hard
- **Contexte Analytique :** La ségrégation par contagion.
- **Périmètre Technique (Ouvert aux contributions) :** PySAL: estimation de rho avec DVF/IRIS. Effets spatiaux marginaux.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note : association spatiale, non causalité.

## MILESTONE : Tome II - Partie V : Spatial et Causal
### Issue — Chapitre 26 — Modèle SEM spatial
**Labels:** tome-2, stats, difficulty: hard
- **Contexte Analytique :** L'impact des variables latentes.
- **Périmètre Technique (Ouvert aux contributions) :** SEM incluant IPS, IRIS, DVF, transport.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Comparaison R2 marginal/conditionnel.

## MILESTONE : Tome II - Partie V : Spatial et Causal
### Issue — Chapitre 27 — Modèle causal non-linéaire (GAM)
**Labels:** tome-2, stats, difficulty: hard
- **Contexte Analytique :** Effets de seuils (splines).
- **Périmètre Technique (Ouvert aux contributions) :** GAM spatial. *Random Forest relégué dans exploratory/*.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Absence de design expérimental.

## MILESTONE : Tome II - Partie V : Spatial et Causal
### Issue — Chapitre 28 — Décomposition effets indirects
**Labels:** tome-2, stats, difficulty: hard
- **Contexte Analytique :** Quartier vs Réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Variance multiniveau avec spatial lag.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Le réseau neutralise-t-il le quartier ?

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Conclusion du Tome II
**Labels:** tome-2, editorial, difficulty: easy
- **Contexte Analytique :** Bilan du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Les 5 lycées structurants. Comparaison Londres/NY.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A1 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A1).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A2 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A2).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A3 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A3).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A4 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A4).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A5 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A5).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A6 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A6).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome II - Conclusion & Annexes
### Issue — Annexe A7 : Documentation et Code Tome II
**Labels:** tome-2, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Matrices et scripts python (A7).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.


## MILESTONE : Tome III - Pages Liminaires
### Issue — Avant-propos Tome III & Note éthique
**Labels:** tome-3, editorial, difficulty: easy
- **Contexte Analytique :** Transition vers le temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note éthique : le modèle dynamique est un outil formel exploratoire.

## MILESTONE : Tome III - Pages Liminaires
### Issue — Introduction : Le système scolaire comme processus
**Labels:** tome-3, editorial, difficulty: easy
- **Contexte Analytique :** Le système est un flux.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Limites des séries temporelles (biais, années manquantes).

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 1 — Le temps des lycées
**Labels:** tome-3, time-series, difficulty: medium
- **Contexte Analytique :** Lissage longitudinal.
- **Périmètre Technique (Ouvert aux contributions) :** Script calculant le score de trajectoire $\Delta S$.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Qui monte, qui stagne ?

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 2 — CAH Dynamique
**Labels:** tome-3, cluster, difficulty: hard
- **Contexte Analytique :** Le réseau bouge-t-il ?
- **Périmètre Technique (Ouvert aux contributions) :** Partitions annuelles et matrice de transition inter-temporelle.
- **Périmètre Éditorial (Réservé à l'Auteur) :** L'ultramétrie temporelle modifie-t-elle la hiérarchie ?

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 3 — Évolution des 5 clusters
**Labels:** tome-3, cluster, difficulty: medium
- **Contexte Analytique :** Profils d'évolution.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle des transitions.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation de la dynamique.

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 4 — Modèle de Markov Caché (HMM)
**Labels:** tome-3, exploratory, difficulty: hard
- **Contexte Analytique :** États latents et probabilité de bascule.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation HMM sur séries IPS, $\sigma$, DVF.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Le modèle révèle des états cachés non observables.

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 5 — Les trajectoires invisibles
**Labels:** tome-3, exploratory, difficulty: hard
- **Contexte Analytique :** Le HMM couplé au réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Viterbi algorithme temporel. *GNN (Graph Neural Network) en exploratory/*.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Cadrage épistémologique du HMM.

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 6 — Dynamique de Theil
**Labels:** tome-3, time-series, difficulty: medium
- **Contexte Analytique :** L'inégalité temporelle.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de $T(t)$ et $\Delta T$. Corrélation temporelle avec DVF.
- **Périmètre Éditorial (Réservé à l'Auteur) :** La ségrégation augmente-t-elle ?

## MILESTONE : Tome III - Partie I : Trajectoires temporelles
### Issue — Chapitre 7 — Corridors Temporels (Sankey abstrait)
**Labels:** tome-3, dataviz, difficulty: medium
- **Contexte Analytique :** Modélisation des mobilités abstraites.
- **Périmètre Technique (Ouvert aux contributions) :** Diagramme de Sankey des transitions entre clusters.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Les mobilités abstraites ne sont pas des parcours d'élèves physiques.

## MILESTONE : Tome III - Partie II : Changepoints et Causalité temporelle
### Issue — Chapitre 8 — Détection de Changepoints (PELT)
**Labels:** tome-3, stats, difficulty: hard
- **Contexte Analytique :** Années de rupture.
- **Périmètre Technique (Ouvert aux contributions) :** Algo PELT/Segmentation binaire.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérifier l'absence d'artefacts ministériels (changement méthode IPS).

## MILESTONE : Tome III - Partie II : Changepoints et Causalité temporelle
### Issue — Chapitre 9 — Phase Transitions
**Labels:** tome-3, physics, difficulty: hard
- **Contexte Analytique :** Seuils critiques d'inégalité.
- **Périmètre Technique (Ouvert aux contributions) :** Équations aux différences et seuil critique ($\rho\lambda \ge 1$).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Métaphore formelle issue de la physique, non une loi démontrée.

## MILESTONE : Tome III - Partie II : Changepoints et Causalité temporelle
### Issue — Chapitre 10 — Early Warning Signals
**Labels:** tome-3, physics, difficulty: hard
- **Contexte Analytique :** Variance et autocorrélation.
- **Périmètre Technique (Ouvert aux contributions) :** Indicateurs pré-transition (variance locale augmentée).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation heuristique.

## MILESTONE : Tome III - Partie II : Changepoints et Causalité temporelle
### Issue — Chapitre 11 — DAG Inter-temporel
**Labels:** tome-3, exploratory, difficulty: hard
- **Contexte Analytique :** Causalité séquentielle.
- **Périmètre Technique (Ouvert aux contributions) :** DAG étendu (temps $t-1 \rightarrow t$).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Cascade causale : le quartier cause-t-il l'école ou inversement ?

## MILESTONE : Tome III - Partie II : Changepoints et Causalité temporelle
### Issue — Chapitre 12 — Inférence Causale Temporelle
**Labels:** tome-3, exploratory, difficulty: hard
- **Contexte Analytique :** Granger ou Diff-in-Diff abstrait.
- **Périmètre Technique (Ouvert aux contributions) :** Tests de causalité de Granger sur DVF vs IPS.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Pas d'inférence expérimentale stricte.

## MILESTONE : Tome III - Partie III : Modèles Unifiés
### Issue — Chapitre 13 — Géométrie Dynamique
**Labels:** tome-3, math, difficulty: hard
- **Contexte Analytique :** L'espace scolaire courbé.
- **Périmètre Technique (Ouvert aux contributions) :** Formalisme de variété riemannienne (courbure de l'espace social).
- **Périmètre Éditorial (Réservé à l'Auteur) :** L'espace social vivant, courbé par les inégalités (métaphore).

## MILESTONE : Tome III - Partie III : Modèles Unifiés
### Issue — Chapitre 14 — Architecture du modèle final (HMM+GNN+DAG)
**Labels:** tome-3, exploratory, difficulty: hard
- **Contexte Analytique :** Modèle complet.
- **Périmètre Technique (Ouvert aux contributions) :** Architecture logicielle `exploratory/`.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Valorisation du jumeau numérique expérimental.

## MILESTONE : Tome III - Partie III : Modèles Unifiés
### Issue — Chapitre 15 — Limites du modèle unifié
**Labels:** tome-3, exploratory, difficulty: medium
- **Contexte Analytique :** Éthique du ML.
- **Périmètre Technique (Ouvert aux contributions) :** Documentation des limites.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Avertissement sur les biais algorithmiques.

## MILESTONE : Tome III - Partie IV : Anomalies
### Issue — Chapitre 16 — Score de Paradoxalité
**Labels:** tome-3, stats, difficulty: medium
- **Contexte Analytique :** Sur ou Sous-performance.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul incluant Valeur Ajoutée (VA).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Performance statistique relative, non de la qualité du professeur.

## MILESTONE : Tome III - Partie IV : Anomalies
### Issue — Chapitre 17 — Les sur-performances académiques
**Labels:** tome-3, stats, difficulty: medium
- **Contexte Analytique :** Lycées modèles.
- **Périmètre Technique (Ouvert aux contributions) :** Top 20 du score.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des outliers positifs.

## MILESTONE : Tome III - Partie IV : Anomalies
### Issue — Chapitre 18 — Les sous-performances
**Labels:** tome-3, stats, difficulty: medium
- **Contexte Analytique :** Lycées en difficulté relative.
- **Périmètre Technique (Ouvert aux contributions) :** Bottom 20 du score.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Facteurs géographiques explicatifs (DVF).

## MILESTONE : Tome III - Partie IV : Anomalies
### Issue — Chapitre 19 — Les signaux faibles
**Labels:** tome-3, stats, difficulty: medium
- **Contexte Analytique :** Détection avancée des retournements.
- **Périmètre Technique (Ouvert aux contributions) :** Analyse des résidus temporels.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Les quartiers en cours de gentrification.

## MILESTONE : Tome III - Partie IV : Anomalies
### Issue — Chapitre 20 — L'impact des ouvertures/fermetures
**Labels:** tome-3, stats, difficulty: medium
- **Contexte Analytique :** Effet réseau des nouveaux établissements.
- **Périmètre Technique (Ouvert aux contributions) :** Choc exogène sur la centralité.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Éthique sur l'évaluation des réformes locales.

## MILESTONE : Tome III - Partie V : Simulations
### Issue — Chapitre 21 — Simulation : Redistribution aléatoire
**Labels:** tome-3, simulation, difficulty: hard
- **Contexte Analytique :** Choc abstrait.
- **Périmètre Technique (Ouvert aux contributions) :** Redistribution des IPS dans le graphe.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Ignorer les contournements familiaux (avertissement).

## MILESTONE : Tome III - Partie V : Simulations
### Issue — Chapitre 22 — Simulation : Altération de la centralité
**Labels:** tome-3, simulation, difficulty: hard
- **Contexte Analytique :** Suppression de hubs.
- **Périmètre Technique (Ouvert aux contributions) :** Retrait topologique des 5% de lycées les plus centraux.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Effet cascade.

## MILESTONE : Tome III - Partie V : Simulations
### Issue — Chapitre 23 — Simulation : Contrainte de mixité
**Labels:** tome-3, simulation, difficulty: hard
- **Contexte Analytique :** Forçage de la variance.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle modifiant $\sigma$ globalement.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rêve mathématique vs Réalité institutionnelle.

## MILESTONE : Tome III - Partie V : Simulations
### Issue — Chapitre 24 — Le modèle prédictif
**Labels:** tome-3, exploratory, difficulty: hard
- **Contexte Analytique :** Prévision à T+5.
- **Périmètre Technique (Ouvert aux contributions) :** Lancement du GNN sur les prochaines années.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Modèle purement académique (avertissement).

## MILESTONE : Tome III - Partie V : Simulations
### Issue — Chapitre 25 — Atlas Dynamique Interactif
**Labels:** tome-3, dataviz, difficulty: medium
- **Contexte Analytique :** Outil de visualisation web.
- **Périmètre Technique (Ouvert aux contributions) :** Dashboard ou app Streamlit.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interface finale.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Chapitre 26 — Limites méthodologiques (Très Important)
**Labels:** tome-3, editorial, difficulty: medium
- **Contexte Analytique :** Honnêteté scientifique.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Le risque de naturaliser les inégalités.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Chapitre 27 — Comparatif international
**Labels:** tome-3, editorial, difficulty: medium
- **Contexte Analytique :** Mise en perspective.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Londres, New York, Berlin.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Chapitre 28 — Ouvertures disciplinaires
**Labels:** tome-3, editorial, difficulty: medium
- **Contexte Analytique :** Sociologie + ML.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** L'avenir des méthodes numériques en sociologie.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Chapitre 29 — Agenda de recherche futur
**Labels:** tome-3, editorial, difficulty: medium
- **Contexte Analytique :** Prochaines étapes.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Quelles données manquent (hors contrat, etc.).

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Conclusion Générale de la Trilogie
**Labels:** tome-3, editorial, difficulty: easy
- **Contexte Analytique :** Bilan total.
- **Périmètre Technique (Ouvert aux contributions) :** Aucun.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Ce que l'Île-de-France dit de la France scolaire.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A1 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A1).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A2 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A2).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A3 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A3).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A4 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A4).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A5 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A5).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A6 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A6).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A7 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A7).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A8 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A8).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A9 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A9).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.

## MILESTONE : Tome III - Partie VI : Conclusion & Agenda
### Issue — Annexe A10 : Documentation et Code Tome III
**Labels:** tome-3, documentation, difficulty: easy
- **Contexte Analytique :** Reproductibilité du temporel.
- **Périmètre Technique (Ouvert aux contributions) :** Modèles dynamiques et données (A10).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Vérification scientifique.


