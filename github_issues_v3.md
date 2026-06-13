MILESTONE : Setup & Architecture (Data et Figures Signatures)

### Issue #001 — Pipeline Data : Ingestion et consolidation de la Base Maître Enrichie
**Labels:** data, setup
- **Contexte Analytique :** La recherche nécessite une base longitudinale et multi-dimensionnelle dépassant le simple IPS. Il faut y intégrer la géographie, l'immobilier, les transports et les résultats académiques.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python dans `src/data/` qui télécharge, nettoie et joint sur le code UAI : les IPS historiques, résultats du Bac, géographie IRIS (INSEE), coordonnées GPS, sectorisation, et prix de l'immobilier (DVF). Sauvegarde versionnée avec DVC.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Présentation du dataset enrichi dans les annexes de l'ouvrage et justification sociologique des variables retenues.

### Issue #002 — Dataviz : Carte Signature (IPS et ségrégation territoriale IDF)
**Labels:** dataviz, setup, map
- **Contexte Analytique :** Visualiser la structure spatiale de la ségrégation éducative et sa co-production avec la ségrégation résidentielle.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python dans `scripts/` (via GeoPandas/Matplotlib) générant une carte choroplèthe de l'Île-de-France (IPS moyen + revenus IRIS superposés). Export PNG/PDF haute définition (300 dpi).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction de la légende détaillée et intégration narrative dans l'Avant-propos.

### Issue #003 — Dataviz : Figure Signature (Scatter IPS vs Écart-type)
**Labels:** dataviz, setup
- **Contexte Analytique :** Démontrer visuellement que l'IPS moyen masque de grandes disparités de mixité interne, en séparant le public et le privé.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python générant le scatter plot IPS vs $\sigma$, avec couleurs public/privé, annotations des cas extrêmes, et courbe de densité KDE.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse sociologique des quadrants formés par la figure.

### Issue #004 — Dataviz : Figure Signature (Réseau de similarité Louvain)
**Labels:** dataviz, setup, network
- **Contexte Analytique :** Cartographier la proximité structurelle entre établissements (qui ressemble à qui ?), indépendamment de leur géographie pure.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python (NetworkX) construisant le graphe de similarité, coloré par communauté Louvain, avec la taille des nœuds proportionnelle à la centralité Eigenvector.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Exploitation visuelle dans le Tome II pour illustrer les "Mondes scolaires".

### Issue #005 — Dataviz : Figure Signature (Trajectoires Temporelles)
**Labels:** dataviz, setup, time-series
- **Contexte Analytique :** Montrer l'évolution dynamique de la ségrégation dans le temps.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python traçant les séries temporelles des lycées, avec marquage des "changepoints" identifiés (PELT) et coloration par cluster.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Support visuel majeur pour l'introduction du Tome III.

MILESTONE : Tome I - Introduction Générale
### Issue — Chapitre introductif : Le paradoxe de l'école républicaine
**Labels:** tome-1, editorial
- **Contexte Analytique :** Poser le paradoxe de l'égalité de droit face à l'inégalité de fait en utilisant les données de l'IPS et l'écart-type comme révélateur de mixité.
- **Périmètre Technique (Ouvert aux contributions) :** Pas de développement requis ici (voir les issues du Pipeline Data).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction de l'introduction, présentation du corpus enrichi et de la chaîne de collecte des données. Définition stricte de l'IPS et de l'approche structurale.

MILESTONE : Tome I - Partie I
### Issue — Chapitre 1 : L'IPS, un indice, pas une vérité
**Labels:** tome-1, data-analysis, editorial
- **Contexte Analytique :** Déconstruire statistiquement l'IPS pour montrer ce qu'il capture (capital culturel/revenus IRIS) et ce qu'il efface.
- **Périmètre Technique (Ouvert aux contributions) :** Script explorant la corrélation entre IPS, taux de boursiers, PCS et revenus IRIS. Proposition de code en annexe pour un indice composite IPS+σ+revenus.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication de la méthode du Ministère et rédaction narrative de l'encadré 'L'IPS peut-il être instrumentalisé institutionnellement ?' avec rigueur analytique absolue.

MILESTONE : Tome I - Partie I
### Issue — Chapitre 2 : L'écart-type, révélateur de mixité cachée
**Labels:** tome-1, data-analysis, editorial
- **Contexte Analytique :** L'écart-type comme mesure de diversité interne, révélant que deux établissements de même IPS peuvent abriter des mixités très différentes.
- **Périmètre Technique (Ouvert aux contributions) :** Analyse statistique de corrélation entre l'écart-type scolaire et l'hétérogénéité des marchés immobiliers locaux (DVF).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative des cas emblématiques (fortes vs faibles hétérogénéités) en veillant à la règle d'écriture anti-intentionnalité.

MILESTONE : Tome I - Partie I
### Issue — Chapitre 3 : Panorama du corpus enrichi
**Labels:** tome-1, data-analysis, editorial
- **Contexte Analytique :** Vue d'ensemble descriptive du dataset : distributions de l'IPS, de l'écart-type, répartition géographique et statutaire.
- **Périmètre Technique (Ouvert aux contributions) :** Génération de tables descriptives (summary statistics) consolidant le dataset final (corrélations IPS/σ/statut/IRIS/Bac).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation des distributions et de la Figure Signature (Scatter IPS/σ). Rédaction de l'encadré sur le biais de sélection : 'les absents du classement'.

MILESTONE : Tome I - Partie II
### Issue — Chapitre 4 : La carte de l'élite scolaire francilienne
**Labels:** tome-1, map, editorial
- **Contexte Analytique :** Analyser la surreprésentation géographique de l'élite et la corrélation spatiale entre marché scolaire et marché immobilier.
- **Périmètre Technique (Ouvert aux contributions) :** Analyse statistique croisant la moyenne communale des IPS avec les prix médians au m² (DVF).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation de la Figure Signature de la carte IDF et de la logique historique du 'croissant de l'ouest'.

MILESTONE : Tome I - Partie II
### Issue — Chapitre 5 : Les trois couronnes : trois systèmes scolaires ?
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Comparer structurellement Paris, la petite couronne et la grande couronne pour décomposer la variance de la ségrégation.
- **Périmètre Technique (Ouvert aux contributions) :** Code pour un modèle ANOVA spatiale avec trois facteurs (zone, public/privé, revenus IRIS). Calcul de l'indice de dissimilarité de Duncan par commune.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction interprétant la décomposition de la variance (parts explicatives relatives sans déterminisme absolu).

MILESTONE : Tome I - Partie II
### Issue — Chapitre 6 : La ségrégation invisible
**Labels:** tome-1, data-analysis, editorial
- **Contexte Analytique :** Identifier le paradoxe des communes à moyenne sociale modérée cachant une ségrégation interne extrême entre établissements.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation d'un indice formel de 'fausse mixité' ($F_c = M_{global} - M_{interne}$). Exploration des corrélations avec l'accessibilité transport (IDF Mobilités).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des communes paradoxales sans formuler de jugements moraux sur les contournements de carte scolaire.

MILESTONE : Tome I - Partie II
### Issue — Chapitre 7 : Secteur public vs privé : une géographie différenciée
**Labels:** tome-1, data-analysis, editorial
- **Contexte Analytique :** Mesurer la polarisation géographique entre établissements publics et privés sous contrat.
- **Périmètre Technique (Ouvert aux contributions) :** Analyse de la densité du privé par rapport aux données immobilières DVF (hypothèse d'implantation dans les zones coûteuses). Calcul du $\Delta$ IPS public/privé par zone.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction historique et géographique. Encadré sur les limites analytiques de l'absence de données sur les lycées hors-contrat.

MILESTONE : Tome I - Partie III
### Issue — Chapitre 8 : L'aristocratie scolaire fermée
**Labels:** tome-1, cluster, editorial
- **Contexte Analytique :** Décrire statistiquement le premier cluster (IPS extrêmes, écart-type faible, profil socio-géographique très spécifique).
- **Périmètre Technique (Ouvert aux contributions) :** Calcul d'un 'score d'entre-soi composite' (IPS/$\sigma$) et croisement de ce cluster avec les données Bac et CSP INSEE.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédiger l'analyse de ce cluster en respectant strictement la règle : décrire les effets de réseau sans imputer d'intention d'exclusion aux directions.

MILESTONE : Tome I - Partie III
### Issue — Chapitres 9 à 13 : Les autres mondes scolaires
**Labels:** tome-1, cluster, editorial
- **Contexte Analytique :** Caractériser les 4 autres macro-groupes : bourgeoisie élargie, élites académiques publiques, privés mixtes, internationaux/scientifiques.
- **Périmètre Technique (Ouvert aux contributions) :** Profilage descriptif complet par cluster (IPS, variance, revenus du quartier, résultats Bac). Identification des sous-performances relatives ('paradoxes analytiques').
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction des chapitres 9 à 13 (un pour chaque cluster). Maintien constant du lexique analytique ('les données suggèrent une surreprésentation...').

MILESTONE : Tome I - Partie IV
### Issue — Chapitre 14 : Construire un score d'entre-soi social
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Formaliser mathématiquement un indicateur synthétique de fermeture sociale.
- **Périmètre Technique (Ouvert aux contributions) :** Code Python calculant le score IPS/$\sigma$ normalisé par z-scores pour l'ensemble du dataset.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse des extrêmes du score. Rédiger la note éthique précisant que le classement révèle une structure statistique et non une hiérarchie de vertu.

MILESTONE : Tome I - Partie IV
### Issue — Chapitre 15 : L'indice de Gini des lycées franciliens
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Appliquer un outil classique d'inégalité économique (Gini) à la distribution scolaire spatiale.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation de l'indice de Gini sur la distribution des IPS, avec décompositions spatiales et institutionnelles.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Intégration d'une courte mise en perspective nationale et internationale (Londres, Berlin) basée sur la littérature existante.

MILESTONE : Tome I - Partie IV
### Issue — Chapitre 16 : L'indice de Theil : une ségrégation décomposable
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Décomposer l'inégalité éducative totale en parts (entre villes, entre public/privé, entre quartiers).
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du Theil global et décompositions 'within'/'between'. Intégration novatrice de la couche de revenus IRIS dans la décomposition.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication pédagogique de l'indice et interprétation de la part expliquée par le lieu de résidence vs le statut institutionnel.

MILESTONE : Tome I - Partie IV
### Issue — Chapitre 17 : L'indice de dissimilarité spatial
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Mesurer l'intensité de la séparation physique entre différentes populations scolaires.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de l'indice de Duncan $D$ par ville, couplé à une analyse exploratoire de sa corrélation avec l'accessibilité transport.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative de la dissimilarité et de l'impact des infrastructures de transport sur le contournement scolaire.

MILESTONE : Tome I - Partie IV
### Issue — Chapitre 18 : L'indice global de fragmentation scolaire
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Résumer toutes les métriques précédentes en un score composite de l'état du système.
- **Périmètre Technique (Ouvert aux contributions) :** Synthèse mathématique (Theil + ANOVA + Polarisation + Hétérogénéité) produisant un score unique pour l'Île-de-France.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation de l'indice composite. Conclusion de la partie IV.

MILESTONE : Tome I - Partie V
### Issue — Chapitre 19 & 20 : ANOVA simple et multi-facteurs
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Prouver statistiquement l'importance relative de la géographie par rapport au statut public/privé.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python modélisant les ANOVA simples et complexes intégrant l'IPS, la zone, le statut, les revenus IRIS, les prix DVF et les transports.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction des chapitres 19 et 20. Interprétation prudente des décompositions ('les données suggèrent des associations fortes').

MILESTONE : Tome I - Partie V
### Issue — Chapitre 21 : Le modèle multiniveau (HLM)
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Isoler mathématiquement l''effet quartier' de l''effet établissement'.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle statistique multiniveau hiérarchique (Lycée $\rightarrow$ Commune $\rightarrow$ Zone) utilisant les revenus IRIS en variable de niveau 2. Calcul du $R^2$ marginal et conditionnel.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication de ce que la géographie structurelle explique au-delà des efforts ou des politiques propres à chaque lycée.

MILESTONE : Tome I - Partie V
### Issue — Chapitre 22 : Vers un modèle causal : DAG statique
**Labels:** tome-1, stats, editorial
- **Contexte Analytique :** Formaliser les hypothèses d'influence entre marché résidentiel, marché scolaire, et mixité finale.
- **Périmètre Technique (Ouvert aux contributions) :** Construction du graphe acyclique dirigé (DAG) incluant IRIS, DVF et IPS. Modélisation structurelle (effets directs/indirects).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction de l'avertissement épistémologique crucial ('Le DAG est un outil de formalisation des hypothèses, non une démonstration causale'). Discussion du rôle amplificateur du privé.

MILESTONE : Tome I - Conclusion
### Issue — Conclusion du Tome I
**Labels:** tome-1, editorial
- **Contexte Analytique :** Synthétiser la structure statique (la carte) avant de passer à la structure dynamique (le réseau, Tome II).
- **Périmètre Technique (Ouvert aux contributions) :** Pas de développement requis.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction du chapitre conclusif. Mise en perspective avec d'autres métropoles. Inventaire explicite des 'données manquantes' nécessaires pour aller plus loin.


MILESTONE : Tome II - Introduction
### Issue — Chapitre introductif : Du territoire au réseau
**Labels:** tome-2, editorial
- **Contexte Analytique :** Effectuer le saut analytique de l'approche spatiale à l'approche topologique (graphes). Poser la fonction de similarité retenue.
- **Périmètre Technique (Ouvert aux contributions) :** Pas de dev. Justification mathématique formelle de la métrique choisie (ex: exponentielle de Mahalanobis).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction de l'avant-propos 'pourquoi changer de regard'. Intégration de la note de prudence : 'les liens représentent des similarités, non des flux réels sauf mention explicite'.

MILESTONE : Tome II - Partie I
### Issue — Chapitres 1 & 2 : CAH et Dendrogramme enrichis
**Labels:** tome-2, cluster, editorial
- **Contexte Analytique :** Classification Ascendante Hiérarchique de l'écosystème scolaire francilien en utilisant le vecteur enrichi (IPS, écart-type, IRIS, Bac).
- **Périmètre Technique (Ouvert aux contributions) :** Script Python implémentant la CAH de Ward. Calculs de l'index Silhouette, Gap statistic et critère de Mojena. Tracé du dendrogramme.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Lecture sociologique du dendrogramme : le premier split est-il défini par l'homogénéité ou par la performance/localisation ?

MILESTONE : Tome II - Partie I
### Issue — Chapitres 3 & 4 : Les cinq clusters de la V3
**Labels:** tome-2, cluster, stats
- **Contexte Analytique :** Définition structurelle des mondes scolaires détectés par la CAH et validation par bootstrap.
- **Périmètre Technique (Ouvert aux contributions) :** Analyse descriptive moyenne des 5 clusters sur toutes les variables. Sous-échantillonnage (bootstrap) retirant 10% des données pour tester la robustesse (ARI).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Description formelle des clusters sans interprétation normative ('ces établissements présentent en moyenne un profil...').

MILESTONE : Tome II - Partie I
### Issue — Chapitre 5 : L'ultramétrie
**Labels:** tome-2, math, editorial
- **Contexte Analytique :** Vérifier si le système scolaire a une véritable logique arborescente et hiérarchique absolue.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de la corrélation cophenétique. Identification des 'ponts ultramétriques' qui violent l'arborescence.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Interprétation prudente de l'indice de hiérarchisation. La hiérarchie est-elle brisée par certaines hybridations locales ?

MILESTONE : Tome II - Partie I
### Issue — Chapitre 6 : Détection de communautés : Louvain
**Labels:** tome-2, network, code
- **Contexte Analytique :** Passer de la distance euclidienne à l'analyse de modularité sur le réseau.
- **Périmètre Technique (Ouvert aux contributions) :** Application de l'algorithme de Louvain sur deux graphes (IPS seul vs vecteur enrichi). Mesure de l'ARI entre CAH et Louvain.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Explication de la différence conceptuelle entre la CAH (hiérarchique) et Louvain (communautaire/réticulaire).

MILESTONE : Tome II - Partie I
### Issue — Chapitre 7 : Louvain multi-couches (Multiplex)
**Labels:** tome-2, network, code
- **Contexte Analytique :** Intégrer simultanément les dimensions sociale, académique, géographique et statutaire.
- **Périmètre Technique (Ouvert aux contributions) :** Construction d'un réseau multiplex à 4 couches (dont GPS). Identification des communautés transversales et de l'IFC.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédiger l'analyse des divergences : quand la topologie s'oppose à la géographie pure, signe d'effets institutionnels.

MILESTONE : Tome II - Partie II
### Issue — Chapitre 8 & 9 : Construction du graphe et Centralité
**Labels:** tome-2, network, editorial
- **Contexte Analytique :** Trouver quels lycées sont les 'hubs' et les 'cœurs' du système francilien.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle nul de graphe aléatoire pour tester la significativité de la modularité. Calcul de la centralité pondérée et de l'Eigenvector.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Analyse narrative de la corrélation entre les lycées centraux dans le réseau et les performances au Bac (un lycée central est-il performant ?).

MILESTONE : Tome II - Partie II
### Issue — Chapitre 10 : Les ponts entre mondes scolaires
**Labels:** tome-2, network, editorial
- **Contexte Analytique :** Identifier les établissements situés à l'intersection des différents mondes socio-scolaires.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du betweenness centrality et du score de pont composite. Extraction du top 10.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note éthique ('les lycées ponts sont des structures analytiques'). Discussion des lycées de l'élite publique en bordure du privé bourgeois.

MILESTONE : Tome II - Partie II
### Issue — Chapitres 11 à 14 : Modélisation des flux et Corridors sociaux
**Labels:** tome-2, stats, code
- **Contexte Analytique :** Simuler mathématiquement les circulations entre clusters et utiliser les données réelles partielles.
- **Périmètre Technique (Ouvert aux contributions) :** Génération de la matrice de Markov. Calibration de la matrice si données d'affectation (Affelnet partiel) disponibles. Détection asymétrique (ascenseurs vs filtres).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Formulation prudente de la mobilité simulée vs réelle. Rédaction des chapitres sur les corridors sociaux.

MILESTONE : Tome II - Partie III
### Issue — Chapitres 15 à 17 : Anomalies, Bascules et Résidus structurels
**Labels:** tome-2, math, code
- **Contexte Analytique :** Trouver les lycées atypiques et les 'trous aveugles' du modèle dominant.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul des outliers par Mahalanobis. Identification des zones d'inversion de gradient. Calcul de l'autocorrélation de Moran sur les résidus SAR.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Les outliers ont-ils des valeurs ajoutées Bac atypiques ? Corrélation narrative entre les erreurs du modèle et l'accessibilité transport.

MILESTONE : Tome II - Partie III
### Issue — Chapitres 18 à 20 : Classes latentes et frontières floues
**Labels:** tome-2, math, editorial
- **Contexte Analytique :** Explorer l'incertitude et la multi-appartenance de certains établissements.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle Gaussian Mixture (GMM) et calcul de l'entropie locale H(x) pour cartographier le 'flou' des frontières.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Écriture des chapitres dédiés à la tension entre la rigidité hiérarchique (arborescence) et l'élasticité réticulaire (réseau).

MILESTONE : Tome II - Partie IV
### Issue — Chapitres 21 à 24 : Pression Ségrégative Locale (PSL)
**Labels:** tome-2, stats, code
- **Contexte Analytique :** Mettre au point un indicateur hybride de la tension sociale locale ressentie par un établissement.
- **Périmètre Technique (Ouvert aux contributions) :** Développement et calcul du score PSL en intégrant DVF et IRIS. Cartographie et corrélation avec l'accessibilité aux transports.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction de l'analyse : les zones mal desservies ont-elles une PSL artificiellement plus élevée ?

MILESTONE : Tome II - Partie V
### Issue — Chapitres 25 & 26 : Modèles Spatiaux Avancés (SAR & SEM)
**Labels:** tome-2, stats, code
- **Contexte Analytique :** Tester si la ségrégation se 'propage' géographiquement par effet de contagion.
- **Périmètre Technique (Ouvert aux contributions) :** Code Python (PySAL) estimant un modèle SAR et un modèle structurel SEM. Calcul de la décomposition des effets directs vs indirects.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note épistémologique systématique : 'le modèle capture des associations spatiales, potentiellement des variables omises (immobilier), non une contagion causale'.

MILESTONE : Tome II - Partie V
### Issue — Chapitres 27 & 28 : Modèles Causaux Non-linéaires (GAM)
**Labels:** tome-2, exploratory, code
- **Contexte Analytique :** Chercher des effets de seuil (tipping points) dans l'influence spatiale.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation d'un GAM (Generalized Additive Model) avec splines. *Attention : Déplacer le Random Forest Spatial dans `exploratory/`*.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Avertissement majeur d'absence de design expérimental. Rédaction de la décomposition des effets indirects (quartier vs transport).

MILESTONE : Tome II - Conclusion
### Issue — Conclusion du Tome II
**Labels:** tome-2, editorial
- **Contexte Analytique :** Fermer le pan 'réticulaire' avant d'ouvrir la dimension dynamique du Tome III.
- **Périmètre Technique (Ouvert aux contributions) :** Pas de dev requis.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Bilan des 5 lycées les plus structurants du réseau. Courte comparaison métropolitaine (réseaux scolaires de Londres/NY) sur base de littérature existante.


MILESTONE : Tome III - Pages liminaires & Introduction
### Issue — Chapitre introductif : Le système scolaire comme processus
**Labels:** tome-3, editorial, time-series
- **Contexte Analytique :** Définir l'approche temporelle. Le système scolaire n'est pas un état figé, c'est un flux.
- **Périmètre Technique (Ouvert aux contributions) :** Pas de code ici. La présentation du dataset longitudinal est assurée par le Pipeline Data (Issue #001).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note épistémologique stricte : 'Les modèles présentés sont des outils d'exploration formelle, non des instruments de prédiction ou d'estimation causale.' Explication claire de la qualité et des limites des séries temporelles (biais, années manquantes).

MILESTONE : Tome III - Partie I
### Issue — Chapitres 1 à 3 : Trajectoires de lycées et CAH Dynamique
**Labels:** tome-3, cluster, time-series
- **Contexte Analytique :** Suivre l'évolution des établissements dans le temps : qui monte, qui stagne, qui décline ?
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du score de trajectoire $\Delta S$. Modélisation de partitions annuelles et matrice de transition inter-temporelle (stabilité via ARI). Corrélation avec les prix DVF locaux.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Les lycées ascendants suivent-ils la gentrification locale ? L'ultramétrie temporelle montre-t-elle une recomposition de la hiérarchie globale ?

MILESTONE : Tome III - Partie I
### Issue — Chapitres 4 & 5 : Le modèle HMM (Régimes cachés)
**Labels:** tome-3, exploratory, time-series
- **Contexte Analytique :** Modéliser la probabilité de basculer d'un état socio-scolaire (régime) à un autre.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation d'un Modèle de Markov Caché (HMM) sur la série historique des IPS, $\sigma$, DVF. *Placer le modèle couplé réseau/HMM dans `exploratory/`*.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note : 'Appliqué à des données agrégées, ce modèle ne constitue pas une démonstration probabiliste.' Rédiger l'analyse de la diffusion markovienne.

MILESTONE : Tome III - Partie I
### Issue — Chapitres 6 & 7 : Dynamique de Theil et Corridors Temporels
**Labels:** tome-3, time-series, code
- **Contexte Analytique :** Voir si la ségrégation globale augmente au fil du temps et modéliser un 'Sankey' abstrait des mobilités.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul de $T(t)$ et $\Delta T$. Corrélation avec les dynamiques DVF immobilières.
- **Périmètre Éditorial (Réservé à l'Auteur) :** La fragmentation scolaire suit-elle la fragmentation résidentielle ? Traitement analytique abstrait.

MILESTONE : Tome III - Partie II
### Issue — Chapitre 8 : Détection de Changepoints
**Labels:** tome-3, stats, code
- **Contexte Analytique :** Trouver les années de rupture statistique (bascule) pour un établissement donné.
- **Périmètre Technique (Ouvert aux contributions) :** Code appliquant l'algo PELT/Segmentation binaire. Comparaison temporelle des ruptures avec les données DVF immobilières.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note impérative de l'Auteur : 'Vérifier l'absence d'artefacts liés aux changements de méthodologie de calcul de l'IPS par le Ministère'.

MILESTONE : Tome III - Partie II
### Issue — Chapitre 9 & 10 : Analyse Causale et Phase Transitions
**Labels:** tome-3, exploratory, physics
- **Contexte Analytique :** S'inspirer de la physique statistique pour voir si le système éducatif est au bord d'un seuil critique de ségrégation.
- **Périmètre Technique (Ouvert aux contributions) :** Modèle causal dynamique (équations aux différences). Calcul des indicateurs de phase critique ($\rho\lambda_{max} \ge 1$).
- **Périmètre Éditorial (Réservé à l'Auteur) :** Mise en garde : 'Ce cadre est une métaphore formelle heuristique, non une loi démontrée.' Interprétation purement conceptuelle des 'Early Warning Signals' (Chap 11).

MILESTONE : Tome III - Partie II
### Issue — Chapitres 11 & 12 : DAG inter-temporel
**Labels:** tome-3, exploratory, graph
- **Contexte Analytique :** Tenter d'inférer la directionnalité : le quartier cause-t-il l'école ou inversement, dans le temps ?
- **Périmètre Technique (Ouvert aux contributions) :** Extension du DAG statique en mode inter-temporel. Code placé dans `exploratory/`.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Écriture du chapitre sur les cascades causales comme support théorique sans inférence expérimentale stricte.

MILESTONE : Tome III - Partie III
### Issue — Chapitres 13 à 15 : Géométrie Dynamique et Modèle Unifié
**Labels:** tome-3, exploratory, math
- **Contexte Analytique :** Modélisation de très haut niveau abstrait considérant l'espace scolaire comme un espace courbe.
- **Périmètre Technique (Ouvert aux contributions) :** Formalisme de variété riemannienne et architecture du Modèle final unifié (HMM+GNN+DAG) à pousser dans `exploratory/` avec hyperparamètres $\lambda_i$.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Note : 'Ces formalismes mathématiques avancés sont des langages de modélisation, non des descriptions mesurables.' Valorisation du jumeau numérique expérimental.

MILESTONE : Tome III - Partie IV
### Issue — Chapitres 16 à 20 : Anomalies et Signaux faibles
**Labels:** tome-3, stats, editorial
- **Contexte Analytique :** Étudier les lycées à succès inattendu (sur-performance) et les déceptions de l'élite.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul du score de paradoxalité incluant la Valeur Ajoutée ministérielle (Bac). Croisement massif avec DVF.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Éthique : 'Performances relatives à un modèle statistique, non évaluations de la qualité de l'enseignement.' Les paradoxes sont-ils liés à des marchés immobiliers atypiques ?

MILESTONE : Tome III - Partie V
### Issue — Chapitres 21 à 25 : Simulations de Réforme
**Labels:** tome-3, exploratory, simulation
- **Contexte Analytique :** Que se passe-t-il si l'on modifie la carte scolaire ou si l'on neutralise certains établissements élitistes ?
- **Périmètre Technique (Ouvert aux contributions) :** Simulations sur le réseau : redistribution des IPS, réallocation des flux dans le graphe.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Cadrage impératif : 'Ces scénarios analytiques ignorent les comportements familiaux adaptatifs qui contournent les réformes réelles.' Chapitre final sur l'Atlas dynamique multi-couches interactif.

MILESTONE : Tome III - Partie VI
### Issue — Chapitres 26 à 29 : Limites, Éthique et Agenda
**Labels:** tome-3, editorial
- **Contexte Analytique :** Chapitres de clôture, honnêteté scientifique totale et mise en garde sociopolitique.
- **Périmètre Technique (Ouvert aux contributions) :** Pas de développement technique.
- **Périmètre Éditorial (Réservé à l'Auteur) :** Rédaction du chapitre le plus important : 'Limites méthodologiques'. Éthique de la quantification : le risque de naturaliser les inégalités. Ouvertures disciplinaires et comparatif international.

MILESTONE : Tome III - Conclusion Générale
### Issue — Conclusion : Ce que l'Île-de-France dit de la France scolaire
**Labels:** tome-3, editorial
- **Contexte Analytique :** Synthèse ultime des trois volumes.
- **Périmètre Technique (Ouvert aux contributions) :** Pas de développement technique.
- **Périmètre Éditorial (Réservé à l'Auteur) :** La trilogie comme outil d'analyse, pas comme verdict. L'espace social vivant, courbé par les inégalités. Rédaction narrative finale.


