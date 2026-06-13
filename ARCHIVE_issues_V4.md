# 🐙 GitHub Issues — Trilogie *Vers un Atlas des Dynamiques Scolaires*

## 🏗️ MILESTONE 0 — Infrastructure & Setup Transversal

### Issue #001 — Structure du dépôt GitHub
**Labels** : `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Déploiement de l'environnement de recherche reproductible pour l'Atlas.
- **Périmètre Technique (Ouvert aux contributions)** : Création des dossiers (`data/`, `src/`, `exploratory/`, `figures/`, `tests/`, `runs/`, `config/`, `docs/`, `paper_arxiv/`, `manifesto/`). Fichiers `pyproject.toml`, `Makefile` et `config/analysis.yaml`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Architecture transparente et documentée.
- **Artefacts générés** : Dépôt structuré, `README.md` bilingue, `MANIFESTO.md`, `DATA_SOURCES.md`, `LICENSE`.

- **Pistes d'exploration suggérées :**
- [ ] Créer la structure de dossiers complète (`data/`, `src/`, `exploratory/`, `figures/`, `tests/`, `runs/`, `config/`, `docs/`, `paper_arxiv/`, `manifesto/`)
- [ ] Initialiser `README.md` bilingue FR/EN
- [ ] Créer `LICENSE` (MIT)
- [ ] Créer `MANIFESTO.md`
- [ ] Créer `DATA_SOURCES.md`
- [ ] Créer `config/analysis.yaml` avec tous les hyperparamètres centralisés
- [ ] Créer `requirements.txt`
- [ ] Créer `Makefile`



### Issue #002 — Dataset maître et pipeline de collecte
**Labels** : `data`, `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Constitution de la matrice d'état $S_i$. L'IPS seul est insuffisant, il faut capturer l'écosystème local.
- **Périmètre Technique (Ouvert aux contributions)** : Scraping/API et jointure spatiale (Geopandas) de l'IPS historique, résultats bac (IVAL), IRIS INSEE, coordonnées GPS, sectorisation, DVF Etalab, IDF Mobilités.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Traitement factuel des sources publiques, sourçage rigoureux.
- **Artefacts générés** : Pipeline de collecte, table maître (`data/processed/master_dataset.parquet`).

- **Pistes d'exploration suggérées :**
- [ ] Collecter IPS historiques par année (data.gouv.fr)
- [ ] Collecter résultats bac (taux réussite, mentions, valeur ajoutée IVAL)
- [ ] Collecter géographie IRIS INSEE (revenus médians, CSP, chômage, logement social)
- [ ] Collecter coordonnées GPS des établissements (lat/lon)
- [ ] Collecter données sectorisation scolaire
- [ ] Collecter données DVF Etalab (prix m² par zone)
- [ ] Collecter données IDF Mobilités (accessibilité transport)
- [ ] Collecter données démographiques temporelles INSEE
- [ ] Construire la table maître : `| uai | nom | annee | ips | sigma_ips | taux_mention | lat | lon | iris | revenu_median | prix_dvf | ... |`
- [ ] Documenter toutes les sources dans `DATA_SOURCES.md`



### Issue #003 — Documents éthiques, épistémologiques et socles mathématiques
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Cadrage des limites de l'inférence causale, définition du lexique mathématique (modélisation statique et dynamique) et du vocabulaire sociologique.
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction des fichiers Markdown fondateurs.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Affirmation de la doctrine descriptive vs normative (aucun jugement moral).
- **Artefacts générés** : `docs/CAUSALITY_LIMITS.md`, `docs/NETWORK_INTERPRETATION.md`, `docs/SOCLE_MATHEMATIQUE.md`, `docs/SOCLE_DYNAMIQUE.md`, `docs/GLOSSAIRE.md`.

- **Pistes d'exploration suggérées :**
- [ ] Créer `docs/CAUSALITY_LIMITS.md` (template validé dans info_github.md)
- [ ] Créer `docs/NETWORK_INTERPRETATION.md` (template validé dans info_github.md)
- [ ] Intégrer `docs/SOCLE_MATHEMATIQUE.md` (Formules statistiques et indices de ségrégation)
- [ ] Intégrer `docs/SOCLE_DYNAMIQUE.md` (Modèles dynamiques, causaux et temporels)
- [ ] Intégrer `docs/GLOSSAIRE.md` (Lexique unifié déjà existant)
- [ ] Vérifier que chaque tome intègre la note éthique modèle



### Issue #004 — Tests unitaires (infrastructure)
**Labels** : `code`, `validation`, `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Validation mathématique des outils de l'Atlas (Modèles 1 à 15).
- **Périmètre Technique (Ouvert aux contributions)** : Tests sous `pytest`. Vérification : Theil_total = Theil_between + Theil_within, symétrie des graphes, poids inversés pour closeness, transitions de Markov sum=1, distribution nulle de Moran centrée sur 0.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Garantie de la rigueur algorithmique de la recherche.
- **Artefacts générés** : Suite de tests `tests/` opérationnelle.

- **Pistes d'exploration suggérées :**
- [ ] `tests/test_theil_decomposition.py` — Theil_total = Theil_between + Theil_within
- [ ] `tests/test_graph_construction.py` — symétrie, pas de self-loops
- [ ] `tests/test_closeness_weights.py` — poids inversés avant calcul closeness
- [ ] `tests/test_markov_transitions.py` — lignes de transition sommant à 1
- [ ] `tests/test_moran_permutation.py` — distribution nulle centrée sur 0



### Issue #005 — Experiment tracking (`runs/`)
**Labels** : `infrastructure`, `code`, `difficulty: hard`
- **Contexte Analytique** : Traçabilité des explorations algorithmiques (spécialement pour HMM, Louvain, PELT).
- **Périmètre Technique (Ouvert aux contributions)** : Mise en place d'un format JSON pour enregistrer : git_hash, timestamp, config, metrics. Script d'enregistrement automatique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité totale et transparence des essais.
- **Artefacts générés** : Système de logging opérationnel dans le dossier `runs/`.

- **Pistes d'exploration suggérées :**
- [ ] Définir le format JSON des runs (git_hash, timestamp, config, metrics)
- [ ] Script d'enregistrement automatique des runs


---

## 🗺️ TOME I — LA CARTE ET LE TERRITOIRE

### MILESTONE T1-INTRO — Pages liminaires & Introduction


### Issue #006 — Note éthique Tome I + Préface générale
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Cadrage de l'approche descriptive et statique.
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction Markdown.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : On décrit des structures spatiales, on ne juge pas les politiques d'établissement. Focus sur les données cartographiques.
- **Artefacts générés** : Note éthique T1, Préface générale de la trilogie (8-12 pages), Avant-propos Tome I.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger note éthique spécifique au Tome I (focus : données cartographiques et statistiques descriptives)
- [ ] Rédiger préface générale de la trilogie (8–12 pages, version narrative du manifeste)
- [ ] Rédiger avant-propos du Tome I (passage "classement → structure spatiale", guide de lecture)



### Issue #007 — Introduction générale : Le paradoxe de l'école républicaine
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Exposition du paradoxe central (égalité de droit / inégalité de fait spatialisée).
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Présentation factuelle du corpus enrichi, de la méthode Ministère (IPS), justification des ajouts (σ, DVF).
- **Artefacts générés** : Texte de l'Introduction Générale.

- **Pistes d'exploration suggérées :**
- [ ] Formaliser le paradoxe central (égalité de droit / inégalité de fait comme objet d'analyse)
- [ ] Présenter le corpus et toutes les couches du dataset enrichi
- [ ] Expliquer la construction de l'IPS (méthode Ministère)
- [ ] Présenter σ comme révélateur de mixité sous-utilisé
- [ ] Justifier chaque couche de données ajoutée ("nous ajoutons X parce que Y ne capture pas Z")
- [ ] Premières observations descriptives
- [ ] Annonce du plan du tome


---

### MILESTONE T1-P1 — Partie I : Lire le classement


### Issue #008 — Chapitre 1 : L'IPS, un indice, pas une vérité
**Labels** : `chapitre`, `data`, `difficulty: medium`
- **Contexte Analytique** : Déconstruction de la moyenne de l'IPS.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de l'IPS composite (IPS + σ + revenus IRIS). Script de calcul composite.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : IPS vs capital culturel. Distinction entre statistiques et utilisation politique ou médiatique.
- **Artefacts générés** : Texte du Chapitre 1, Code Python (annexe A5).

- **Pistes d'exploration suggérées :**
- [ ] Construction statistique de l'IPS (méthode Ministère)
- [ ] Ce que l'IPS capture et ce qu'il efface
- [ ] IPS et capital culturel : distinction bourdieusienne revisitée
- [ ] Comparaison IPS vs revenus médians IRIS (corrélation forte mais imparfaite → effets institutionnels propres)
- [ ] **Nouveauté** : encadré "peut-on corriger l'IPS ?" — indice composite IPS + σ + revenus IRIS
- [ ] Code Python pour reproduire le calcul composite (annexe A5)
- [ ] Encadré : "L'IPS peut-il être interprété abusivement ?institutionnellement ?" (formulation analytique stricte)
- [ ] Encadré : différence IPS / taux de boursiers / PCS



### Issue #009 — Chapitre 2 : L'écart-type, révélateur de mixité cachée
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : L'écart-type $\sigma$ (Modèle 1) comme mesure vitale de la diversité interne.
- **Périmètre Technique (Ouvert aux contributions)** : Extraction du Top 20 lycées homogènes / hétérogènes. Corrélation exploratoire $\sigma$ × DVF.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Homogénéité" est un fait statistique, pas un jugement moral sur la valeur des élèves ou le projet pédagogique.
- **Artefacts générés** : Texte du Chapitre 2, Tableaux du Top 20.

- **Pistes d'exploration suggérées :**
- [ ] Définition statistique et interprétation sociologique de σ
- [ ] Deux lycées même IPS, structures sociales opposées
- [ ] σ comme mesure de diversité interne
- [ ] Cas emblématiques : Saint-Jean de Passy (σ=15,7) vs Henri-IV (σ=32,4)
- [ ] **Nouveauté** : corrélation σ × données DVF immobilières (test exploratoire)
- [ ] Encadré : l'écart-type et la théorie de la ségrégation résidentielle
- [ ] Tableau : top 20 lycées les plus homogènes / les plus hétérogènes
- [ ] Cas emblématiques décrits comme "appartenant à des clusters de forte homogénéité" (note éthique)



### Issue #010 — Chapitre 3 : Panorama du corpus enrichi
**Labels** : `chapitre`, `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Distribution statistique globale du système scolaire francilien.
- **Périmètre Technique (Ouvert aux contributions)** : Densité KDE, corrélations croisées. Script `figures/fig2_scatter_ips_sigma.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mention des "absents du classement" (biais de sélection). Standard Nature/Science pour la Figure 2.
- **Artefacts générés** : Texte du Chapitre 3, Figure Signature 2.

- **Pistes d'exploration suggérées :**
- [ ] Distribution statistique : IPS, σ, répartition public/privé, géographie
- [ ] Répartition par type (général, technologique, polyvalent, international)
- [ ] Premières corrélations IPS / σ / statut / revenus IRIS / résultats bac
- [ ] **Figure signature 2** : scatter IPS vs σ, couleurs public/privé, densité KDE, annotations, sous-panel DVF
- [ ] Encadré "les absents du classement" (lycées populaires hors corpus, biais de sélection)
- [ ] Script `figures/fig2_scatter_ips_sigma.py`


---

### MILESTONE T1-P2 — Partie II : Géographie de l'inégalité


### Issue #011 — Chapitre 4 : La carte de l'élite scolaire francilienne
**Labels** : `chapitre`, `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Spatialisation de la performance (IPS) et des prix de l'immobilier (DVF).
- **Périmètre Technique (Ouvert aux contributions)** : Corrélation OLS (IPS vs Prix DVF). Script `figures/fig1_map.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Constat du "croissant de l'ouest" et des "déserts scolaires favorisés". Purement descriptif géographique.
- **Artefacts générés** : Texte du Chapitre 4, Figure Signature 1.

- **Pistes d'exploration suggérées :**
- [ ] Villes surreprésentées : Paris, Neuilly, Versailles, Saint-Germain-en-Laye
- [ ] Histoire du "croissant de l'ouest" (géographie et histoire)
- [ ] Carte choroplèthe des IPS moyens par commune
- [ ] **Nouveauté majeure** : corrélation IPS scolaire × prix DVF (€/m²)
- [ ] Scatter plot IPS communal vs prix médian m²
- [ ] Script `figures/fig1_map.py`
- [ ] Encadré : les arrondissements parisiens (du 6e au 20e, gradient saisissant)
- [ ] Les "déserts scolaires favorisés" : communes aisées sans lycée élite (analyse spécifique)



### Issue #012 — Chapitre 5 : Les trois couronnes
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Mesurer l'effet pur de la géographie.
- **Périmètre Technique (Ouvert aux contributions)** : ANOVA spatiale (zone × statut × revenus IRIS). Indice de dissimilarité de Duncan par commune.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les trois couronnes sont-elles trois systèmes distincts ? La géographie explique-t-elle plus que le statut institutionnel ?
- **Artefacts générés** : Texte du Chapitre 5, Résultats ANOVA.

- **Pistes d'exploration suggérées :**
- [ ] Profil analytique de Paris (hétérogénéité maximale)
- [ ] Profil de la petite couronne (compétition et polarisation)
- [ ] Profil de la grande couronne (homogénéité relative)
- [ ] **Nouveauté** : ANOVA spatiale (zone × statut × revenus IRIS)
- [ ] Décomposition de variance : "géographie explique X%, statut Y%, revenus IRIS Z%"
- [ ] Indice de dissimilarité de Duncan par commune
- [ ] Tableau comparatif des trois zones avec toutes les variables



### Issue #013 — Chapitre 6 : La ségrégation invisible
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Le paradoxe de la commune "mixte" contenant des lycées "homogènes".
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de l'indice de "fausse mixité" $F_c = M_{global} - M_{interne}$. Test croisé avec IDF Mobilités.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Fausse mixité" est un écart statistique, pas une accusation de volonté politique locale.
- **Artefacts générés** : Texte du Chapitre 6, Topologie des communes paradoxales.

- **Pistes d'exploration suggérées :**
- [ ] Le paradoxe de la mixité apparente
- [ ] Mécanismes : carte scolaire, dérogations, filières sélectives, réputation
- [ ] **Nouveauté** : indice de "fausse mixité" formalisé `F_c = M_global - M_interne`
- [ ] Test exploratoire : accessibilité transport × niveau de ségrégation (données IDF Mobilités)



### Issue #014 — Chapitre 7 : Secteur public vs privé, géographie différenciée
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Effet de ségrégation institutionnelle spatialisée.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul du $\Delta$ IPS public/privé par zone. Régression : densité privé vs prix DVF.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Analyse neutre de la répartition. Encadré sur le hors contrat comme terra incognita.
- **Artefacts générés** : Texte du Chapitre 7.

- **Pistes d'exploration suggérées :**
- [ ] Répartition spatiale public/privé
- [ ] Histoire du réseau catholique en Île-de-France
- [ ] Polarisation Δ IPS public/privé par zone
- [ ] **Nouveauté** : corrélation densité privé × prix DVF
- [ ] Encadré : lycées hors contrat (terra incognita statistique)


---

### MILESTONE T1-P3 — Partie III : Sociologie des établissements


### Issue #015 — Note éthique renforcée Partie III
**Labels** : `ethique`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Préparation au clustering CAH (Création de typologies de lycées).
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Un cluster statistique est un groupe mathématique, non une volonté délibérée d'exclusion. Les termes ("Aristocratie", etc.) sont des étiquettes typologiques.
- **Artefacts générés** : Note introductive de la Partie III.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger la note d'ouverture de la Partie III (résultats d'une analyse statistique, aucun jugement sur pratiques internes)
- [ ] Intégrer la note dans le texte principal



### Issue #016 — Chapitre 8 : L'aristocratie scolaire fermée (Cluster 1)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du premier cluster (IPS > 158, $\sigma$ < 20).
- **Périmètre Technique (Ouvert aux contributions)** : Extraction du profil moyen. Calcul du Score d'entre-soi composite (IPS/$\sigma$).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Indicateur de concentration sociale" jamais "ce lycée s'organise pour exclure". Effet systémique, pas intention.
- **Artefacts générés** : Texte du Chapitre 8.

- **Pistes d'exploration suggérées :**
- [ ] Définition structurelle : IPS > 158, σ < 20, privé catholique
- [ ] Profil sociologique : bourgeoisie patrimoniale, réseaux familiaux anciens
- [ ] Établissements emblématiques : Saint-Jean de Passy, Saint-Dominique, Massillon, Saint-Louis de Gonzague
- [ ] Score d'entre-soi composite (IPS/σ) : calcul et interprétation formelle
- [ ] Logique de reproduction : de l'école au réseau des grandes écoles
- [ ] Formulation éthique : "indicateur de concentration sociale" jamais "ce lycée s'organise pour exclure"
- [ ] Logique de reproduction comme effet systémique (pas intention individuelle)
- [ ] Encadré : les alumni et les réseaux professionnels
- [ ] Encadré : le rôle des associations de parents d'élèves
- [ ] Enrichissement résultats bac et valeur ajoutée → "paradoxe analytique" si applicable



### Issue #017 — Chapitre 9 : La grande bourgeoisie catholique élargie (Cluster 2)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du deuxième cluster (IPS 153-158, $\sigma$ 20-25).
- **Périmètre Technique (Ouvert aux contributions)** : Profilage sur toutes les variables (IPS, $\sigma$, DVF, IRIS, bac).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Formulation statistique systématique.
- **Artefacts générés** : Texte du Chapitre 9.

- **Pistes d'exploration suggérées :**
- [ ] Profil : IPS 153-158, écart-type 20-25
- [ ] Établissements : Sainte-Marie Neuilly, Notre-Dame du Grandchamp, Blanche de Castille, Madeleine Daniélou
- [ ] Capital scolaire familial : professions libérales, cadres dirigeants
- [ ] Le projet éducatif catholique : entre confessionnalité et excellence académique
- [ ] Différences internes : établissements «vieille bourgeoisie» vs «nouvelle bourgeoisie»
- [ ] Formulation éthique systématique : structures statistiques, pas intentions institutionnelles
- [ ] Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)



### Issue #018 — Chapitre 10 : Les élites académiques publiques (Cluster 3)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du cluster public méritocratique (IPS 145-153, $\sigma$ > 30).
- **Périmètre Technique (Ouvert aux contributions)** : Analyse de l'écart-type très élevé (diversité réelle). Analyse de la valeur ajoutée IVAL.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La méritocratie républicaine en acte et le rôle des classes préparatoires (filtre secondaire).
- **Artefacts générés** : Texte du Chapitre 10.

- **Pistes d'exploration suggérées :**
- [ ] Profil paradoxal : IPS élevé (145-153), mais mixité forte (σ > 30)
- [ ] Établissements : Henri-IV, Louis-le-Grand, Hoche, Lakanal, Fénelon, Blaise-Pascal
- [ ] La méritocratie républicaine en acte
- [ ] Présence de boursiers, recrutement académique national
- [ ] L'effet réseau : concours d'entrée implicites, classes préparatoires
- [ ] Écart-type comme indicateur de diversité réelle : qui sont les élèves ?
- [ ] Encadré : les classes préparatoires comme filtre social secondaire
- [ ] Enrichissement : valeur ajoutée IVAL — paradoxe analytique si applicable
- [ ] Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)



### Issue #019 — Chapitre 11 : Les privés intermédiaires ouverts (Cluster 4)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du cluster hybride (IPS 145-152, $\sigma$ 28-32).
- **Périmètre Technique (Ouvert aux contributions)** : Extraction des données spatiales (positionnement géographique).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Constat d'ouverture relative.
- **Artefacts générés** : Texte du Chapitre 11.

- **Pistes d'exploration suggérées :**
- [ ] Profil : IPS 145-152, écart-type 28-32
- [ ] Établissements : Charles Péguy, Notre-Dame de la Providence, Rambam, Montalembert
- [ ] Des établissements privés qui recrutent dans des milieux plus variés
- [ ] Proximité avec les publics parisiens : un positionnement hybride
- [ ] Hypothèses : localisation, tradition, offre pédagogique
- [ ] Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)



### Issue #020 — Chapitre 12 : Les élites internationales et scientifiques (Cluster 5)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse de l'écologie scolaire singulière (ex: Saclay, Saint-Germain-en-Laye).
- **Périmètre Technique (Ouvert aux contributions)** : Identification des atypismes statistiques.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Position hors logique nationale classique.
- **Artefacts générés** : Texte du Chapitre 12.

- **Pistes d'exploration suggérées :**
- [ ] Établissements : École Jeannine Manuel, Lycée international de Saint-Germain-en-Laye, Lycée franco-allemand, Blaise-Pascal, Vallée de Chevreuse
- [ ] Capital culturel mondialisé vs capital technoscientifique
- [ ] Recrutement : expatriés, ingénieurs, chercheurs, hauts fonctionnaires internationaux
- [ ] Position atypique dans le système : hors logique nationale classique
- [ ] Encadré : le bassin de Paris-Saclay — une écologie scolaire singulière
- [ ] Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)



### Issue #021 — Chapitre 13 : Les lycées publics favorisés résidentiels
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse des lycées de quartier aisés.
- **Périmètre Technique (Ouvert aux contributions)** : Comparaison avec le Cluster 3 et le Cluster 1. Cartographie complète des 5 clusters.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Synthèse neutre des 5 mondes scolaires.
- **Artefacts générés** : Texte du Chapitre 13, Carte spatiale IDF des 5 mondes.

- **Pistes d'exploration suggérées :**
- [ ] Établissements : Lycée Alain, Louis de Broglie, La Bruyère, Louis Pasteur Neuilly
- [ ] Profil : bons bassins résidentiels, public local favorisé
- [ ] Mixité modérée, stabilité sociale
- [ ] Rôle dans la hiérarchie locale : entre «lycée de quartier aisé» et «lycée d'excellence»
- [ ] Comparaison avec Cluster 3 (public académique) et Cluster 1 (privé fermé)
- [ ] Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)
- [ ] Carte spatiale des 5 clusters sur l'IDF + formulation éthique transversale


---

### MILESTONE T1-P4 — Partie IV : Mesures de la ségrégation


### Issue #022 — Chapitre 14 : Construire un score d'entre-soi social
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 12. L'agrégation de l'IPS et de l'inverse de la dispersion.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul par z-scores : $Z_{entre-soi} = Z(IPS) + Z(1/\sigma)$. Carte spatiale IDF.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Limites de l'indice brut précisées.
- **Artefacts générés** : Texte du Chapitre 14, Script de calcul, Top 20 "Ouverts" / "Fermés".

- **Pistes d'exploration suggérées :**
- [ ] Calculer les z-scores spatiaux (entre-soi) et générer la carte d'Île-de-France.
- [ ] Rédiger le texte du Chapitre 14 et exporter le script ainsi que le Top 20.

### Issue #023 — Chapitre 15 : L'indice de Gini des lycées franciliens
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 9. Gini de la distribution des IPS.
- **Périmètre Technique (Ouvert aux contributions)** : Décomposition within/between (secteur, géographie). Tracé de la Courbe de Lorenz.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Application d'un standard mathématique universel.
- **Artefacts générés** : Texte du Chapitre 15, Courbe de Lorenz.

- **Pistes d'exploration suggérées :**
- [ ] Décomposer mathématiquement la variance (secteur, géographie) et tracer la Courbe de Lorenz.
- [ ] Intégrer les graphiques et rédiger l'analyse finale dans le Chapitre 15.

### Issue #024 — Chapitre 16 : L'indice de Theil : ségrégation décomposable
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 10. Indice d'entropie décomposable spatialement et institutionnellement.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul $T_{total} = T_{between} + T_{within}$ à trois niveaux (zones, statut, revenus IRIS).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Objectivation rigoureuse des parts de variance.
- **Artefacts générés** : Texte du Chapitre 16, Tableau de décomposition de variance.

- **Pistes d'exploration suggérées :**
- [ ] Calculer l'indice de Theil aux trois niveaux géographiques et institutionnels.
- [ ] Dresser le tableau complet de décomposition de la variance pour le Chapitre 16.

### Issue #025 — Chapitre 17 : L'indice de dissimilarité spatial (Duncan D)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 11. Dissimilarité entre "classes favorisées" et "classes populaires" par commune.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de $D$ par ville. Corrélation avec la richesse communale et l'accessibilité transport (IDF Mobilités).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mise en évidence des paradoxes locaux.
- **Artefacts générés** : Texte du Chapitre 17, Carte choroplèthe de $D$.

- **Pistes d'exploration suggérées :**
- [ ] Calculer l'indice de dissimilarité de Duncan (D) et tester la corrélation avec les transports/revenus.
- [ ] Produire la carte choroplèthe finale et rédiger le Chapitre 17.

### Issue #026 — Chapitre 18 : L'indice global de fragmentation scolaire (IFC)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Agrégation de Theil, ANOVA, Gini et polarisation.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de l'indice composite. Contribution relative de chaque composante.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le système est "multi-dimensionnellement structuré".
- **Artefacts générés** : Texte du Chapitre 18.

---

### MILESTONE T1-P5 — Partie V : Décomposition de variance

- **Pistes d'exploration suggérées :**
- [ ] Établir la formule de l'indice composite de fragmentation scolaire et pondérer ses composantes.
- [ ] Rédiger l'analyse détaillée des résultats dans le Chapitre 18.

### Issue #027 — Chapitre 19 : ANOVA simple : public/privé explique-t-il tout ?
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Isolation du facteur "Statut".
- **Périmètre Technique (Ouvert aux contributions)** : Régression OLS unidimensionnelle (IPS ~ statut). Extraction du $R^2$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Formulation prudente (Associations fortes $\neq$ mécanismes causaux).
- **Artefacts générés** : Texte du Chapitre 19.

- **Pistes d'exploration suggérées :**
- [ ] Modèle ANOVA unidimensionnel : IPS ~ secteur (public/privé)
- [ ] Résultat V1 : 35-45% de variance expliquée par le statut
- [ ] Ce que le résidu nous dit (V1)
- [ ] Limites de l'ANOVA simple appliquée à des données scolaires
- [ ] Formulation prudente systématique : associations fortes ≠ mécanismes causaux



### Issue #028 — Chapitre 20 : ANOVA multi-facteurs
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle complet (Statut + Géographie + Type de lycée).
- **Périmètre Technique (Ouvert aux contributions)** : OLS multi-facteurs avec termes d'interactions (ex: privé × ouest). Test d'intégration DVF et transports.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Démontrer que la géographie domine et le statut amplifie.
- **Artefacts générés** : Texte du Chapitre 20, Tableau de décomposition complet.

- **Pistes d'exploration suggérées :**
- [ ] Exécuter les régressions OLS multi-facteurs (interactions privé/géographie) et tester les variables DVF/transports.
- [ ] Exporter le tableau de décomposition complet et rédiger le Chapitre 20.

### Issue #029 — Chapitre 21 : Le modèle multiniveau (HLM)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 14. Structure imbriquée (Lycée $\to$ Ville $\to$ Zone).
- **Périmètre Technique (Ouvert aux contributions)** : Estimation des ICC (Intraclass Correlation Coefficients). $R^2$ marginal vs $R^2$ conditionnel.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Postulat validé analytiquement : "La géographie structure, l'institution filtre".
- **Artefacts générés** : Texte du Chapitre 21, Sorties du modèle.

- **Pistes d'exploration suggérées :**
- [ ] Estimer les ICC (Intraclass Correlation Coefficients) et comparer les R² marginaux et conditionnels.
- [ ] Extraire les sorties du modèle multiniveau pour le texte du Chapitre 21.

### Issue #030 — Chapitre 22 : Vers un modèle causal : DAG statique
**Labels** : `chapitre`, `documentation`, `exploratory`, `difficulty: low`
- **Contexte Analytique** : Modèle 15. Directed Acyclic Graph des déterminants de l'IPS.
- **Périmètre Technique (Ouvert aux contributions)** : Construction du réseau causal (Backdoor criterion). Simulation "do-calculus" : effet d'une neutralisation de variable.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le DAG est une hypothèse formelle, pas une vérité révélée infaillible.
- **Artefacts générés** : Texte du Chapitre 22, Schéma du DAG.

- **Pistes d'exploration suggérées :**
- [ ] Construire formellement le réseau causal (DAG) et simuler l'effet d'une intervention par "do-calculus".
- [ ] Exporter le schéma du DAG et rédiger l'analyse du Chapitre 22.

### Issue #031 — Conclusion du Tome I
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Clôture du Tome I (La Carte et le Territoire).
- **Périmètre Technique (Ouvert aux contributions)** : Synthèse des trouvailles.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Invitation à réfléchir aux politiques.
- **Artefacts générés** : Conclusion du Tome 1.

- **Pistes d'exploration suggérées :**
- [ ] Synthétiser les découvertes majeures et les limites de la première partie.
- [ ] Rédiger le texte de la Conclusion du Tome 1.

### Issue #032 — Annexe A1 : Tableau complet des lycées
**Labels** : `annexe`, `data`, `difficulty: medium`
- **Contexte Analytique** : Données brutes transparentes.
- **Périmètre Technique (Ouvert aux contributions)** : Export CSV.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence totale.
- **Artefacts générés** : Annexe A1.

- **Pistes d'exploration suggérées :**
- [ ] Exporter les données nettoyées des lycées au format CSV.
- [ ] Intégrer cet export pour constituer le Tableau complet de l'Annexe A1.

### Issue #033 — Annexe A2 : Sources de données complètes + licences
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Traçabilité des sources.
- **Périmètre Technique (Ouvert aux contributions)** : Listing exhaustif.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Artefacts générés** : Annexe A2.

- **Pistes d'exploration suggérées :**
- [ ] Dresser l'inventaire exhaustif des jeux de données mobilisés.
- [ ] Présenter ces métadonnées proprement dans l'Annexe A2.

### Issue #034 — Annexe A3 : Méthode de calcul de tous les indices
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Mathématiques appliquées.
- **Périmètre Technique (Ouvert aux contributions)** : Formules LaTeX.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Artefacts générés** : Annexe A3.

- **Pistes d'exploration suggérées :**
- [ ] Convertir la documentation mathématique au format LaTeX.
- [ ] Compiler ces équations pour constituer l'Annexe A3.

### Issue #035 — Annexe A4 : Note sur les licences Open Data
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Cadre légal.
- **Périmètre Technique (Ouvert aux contributions)** : Licences.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Respect du droit.
- **Artefacts générés** : Annexe A4.

- **Pistes d'exploration suggérées :**
- [ ] Recenser les contraintes légales et licences Open Data des jeux de données.
- [ ] Rédiger la note juridique correspondante pour l'Annexe A4.

### Issue #036 — Annexe A5 : Code Python reproductible complet
**Labels** : `annexe`, `code`, `difficulty: medium`
- **Contexte Analytique** : Reproductibilité absolue.
- **Périmètre Technique (Ouvert aux contributions)** : Dépôt de code.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Artefacts générés** : Annexe A5.

- **Pistes d'exploration suggérées :**
- [ ] Rassembler les scripts de nettoyage et de modélisation du Tome 1.
- [ ] Structurer ce dépôt de code pour l'Annexe A5.

### Issue #037 — Annexe A6 : Cartographie complète
**Labels** : `annexe`, `figure`, `difficulty: low`
- **Contexte Analytique** : Visualisation étendue.
- **Périmètre Technique (Ouvert aux contributions)** : Cartes additionnelles.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité.
- **Artefacts générés** : Annexe A6.

- **Pistes d'exploration suggérées :**
- [ ] Regrouper les cartes exploratoires non incluses dans les chapitres principaux.
- [ ] Exporter l'atlas cartographique additionnel pour l'Annexe A6.

### Issue #038 — Annexe A7 : Glossaire des termes statistiques et sociologiques
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Pédagogie conceptuelle.
- **Périmètre Technique (Ouvert aux contributions)** : Définitions.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité.
- **Artefacts générés** : Annexe A7.

- **Pistes d'exploration suggérées :**
- [ ] Compiler les définitions des termes sociologiques et statistiques utilisés.
- [ ] Rédiger le glossaire complet pour l'Annexe A7.

### Issue #039 — Annexe A8 : Bibliographie sélective
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Ancrage académique.
- **Périmètre Technique (Ouvert aux contributions)** : Références.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Humilité scientifique.
- **Artefacts générés** : Annexe A8.

- **Pistes d'exploration suggérées :**
- [ ] Vérifier la mise en forme des références académiques citées dans le texte.
- [ ] Exporter la bibliographie sélective pour l'Annexe A8.

### Issue #040 — Annexe A9 : Comparaison internationale courte
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Mise en perspective.
- **Périmètre Technique (Ouvert aux contributions)** : Synthèse.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité géographique.
- **Artefacts générés** : Annexe A9.

## 🕸️ TOME II — LES RÉSEAUX ET LES MONDES

### MILESTONE T2-INTRO — Pages liminaires & Introduction

- **Pistes d'exploration suggérées :**
- [ ] Réaliser une courte synthèse des travaux comparables à l'étranger.
- [ ] Rédiger cette note de mise en perspective pour l'Annexe A9.

### Issue #041 — Note éthique Tome II + Avant-propos
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Le Tome II introduit la similarité et la théorie des graphes. Il faut s'assurer que "proximité mathématique" ne soit pas confondue avec "entente institutionnelle".
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction Markdown dans `paper_arxiv/tome2/`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La position dans le réseau est une propriété émergente, pas une caractéristique intrinsèque (anti-essentialisme).
- **Artefacts générés** : Avant-propos du Tome II et Note éthique d'ouverture.

- **Pistes d'exploration suggérées :**
- [ ] Note éthique Tome II (position dans le réseau = propriété émergente, pas caractéristique intrinsèque)
- [ ] Avant-propos : "du territoire au réseau" — formulation obligatoire sur les liens de similarité vs flux réels
- [ ] Introduction : nœuds, liens, poids — justification de la fonction de similarité choisie vs alternatives (Jaccard, cosinus)


---

### MILESTONE T2-P1 — Partie I : Topologie du système


### Issue #042 — Chapitre 1 : La CAH comme outil de sociologie scolaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Classification Ascendante Hiérarchique pour diviser l'espace social continu en mondes discrets.
- **Périmètre Technique (Ouvert aux contributions)** : Application de la méthode de Ward. Utilisation de la distance de Mahalanobis. Validation via silhouette score et gap statistic.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La CAH est un algorithme, pas une vérité absolue.
- **Artefacts générés** : Texte du Chapitre 1.

- **Pistes d'exploration suggérées :**
- [ ] Rappel : Classification Ascendante Hiérarchique (méthode de Ward)
- [ ] Distance euclidienne vs distance de Mahalanobis
- [ ] Normalisation des variables : pourquoi les z-scores sont essentiels
- [ ] Choix du nombre de clusters : silhouette, gap statistic, critère de Mojena
- [ ] Résultats V1 : structure en 4-6 clusters stables pour les lycées franciliens
- [ ] Comparaison CAH / k-means / GMM : convergences et divergences
- [ ] **V2** : clustering sur vecteur enrichi (IPS + σ + revenus IRIS + résultats bac + statut)
- [ ] **V2** : comparaison IPS seul vs vecteur enrichi



### Issue #043 — Chapitre 2 : Le dendrogramme comme arbre social
**Labels** : `chapitre`, `figure`, `difficulty: low`
- **Contexte Analytique** : Interprétation de la structure arborescente (Modèle 16).
- **Périmètre Technique (Ouvert aux contributions)** : Tracé du dendrogramme avec le critère de Mojena pour couper l'arbre. Calcul de la profondeur ultramétrique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le dendrogramme n'est pas une hiérarchie de valeur, c'est une mesure de distance.
- **Artefacts générés** : Texte du Chapitre 2, Figure du Dendrogramme.

- **Pistes d'exploration suggérées :**
- [ ] Lecture sociologique du dendrogramme
- [ ] Premier split V1 : homogénéité vs hétérogénéité comme séparation fondamentale
- [ ] Lecture des branches V1 : privé élitiste / public académique / internationaux / scientifiques
- [ ] Hauteurs de fusion comme «ruptures de mondes scolaires» (V1)
- [ ] Le critère de Mojena : détecter les sauts naturels
- [ ] Profondeur ultramétrique V1 : un indice de hiérarchisation sociale
- [ ] **V2** : revenus IRIS ou résultats bac créent-ils une nouvelle dimension de séparation ?



### Issue #044 — Chapitre 3 : Cinq clusters, cinq mondes scolaires
**Labels** : `chapitre`, `figure`, `difficulty: low`
- **Contexte Analytique** : Profilage statistique des 5 mondes isolés.
- **Périmètre Technique (Ouvert aux contributions)** : Extraction des profils moyens pour chaque cluster (IPS, $\sigma$, DVF, IRIS).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les descriptions (Aristocratie, Élites académiques, etc.) doivent rester neutres et statistiques.
- **Artefacts générés** : Texte du Chapitre 3.

- **Pistes d'exploration suggérées :**
- [ ] Cluster 1 : Aristocratie scolaire fermée (privé ouest, IPS > 158, σ < 20)
- [ ] Cluster 2 : Grande bourgeoisie catholique élargie (privé, IPS 153-158, σ 20-25)
- [ ] Cluster 3 : Élites académiques publiques (public, IPS 145-153, σ 27-34)
- [ ] Cluster 4 : Privés urbains mixtes (privé, IPS 145-150, σ 28-32)
- [ ] Cluster 5 : Systèmes internationaux et scientifiques (hors modèle national)
- [ ] Tableau de description de chaque cluster. Carte spatiale des clusters sur l'IDF.
- [ ] Formulation éthique systématique pour chaque cluster
- [ ] **V2** : description analytique enrichie sur toutes les variables (DVF, IRIS, bac)



### Issue #045 — Chapitre 4 : Validation statistique des clusters
**Labels** : `chapitre`, `code`, `validation`, `difficulty: medium`
- **Contexte Analytique** : Les clusters existent-ils vraiment ?
- **Périmètre Technique (Ouvert aux contributions)** : Test de stabilité bootstrap ARI (n=1000). ANOVA post-hoc sur IPS et $\sigma$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Traitement transparent des cas ambigus (lycées aux frontières).
- **Artefacts générés** : Texte du Chapitre 4, Rapport de validation.

- **Pistes d'exploration suggérées :**
- [ ] Silhouette score : cohérence interne des clusters
- [ ] Gap statistic : les clusters existent-ils vraiment ?
- [ ] Stabilité bootstrap (ARI) n=1000 : les clusters survivent-ils à la perturbation ?
- [ ] Séparation statistique : ANOVA post-hoc sur IPS et σ
- [ ] Score de validation global : k optimal consensuel
- [ ] Zones de désaccord entre méthodes : les cas ambigus
- [ ] **V2** : test de robustesse avec sous-échantillons aléatoires (enlever 10% des données)



### Issue #046 — Chapitre 5 : L'ultramétrie
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 32. Le système est-il une hiérarchie parfaite ?
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de la distance cophenétique et de la corrélation ultramétrique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : L'ultramétrie mesure la rigidité du tri social.
- **Artefacts générés** : Texte du Chapitre 5.

- **Pistes d'exploration suggérées :**
- [ ] Propriété ultramétrique : définition formelle
- [ ] Distance cophenétique et corrélation ultramétrique
- [ ] Score de validité ultramétrique : le système est-il vraiment hiérarchique ?
- [ ] «Ponts ultramétriques» V1 : liens qui violent la hiérarchie
- [ ] Signification sociologique : où la logique de classe éclate ?
- [ ] Indice de cohérence arbre/réseau (ARI CAH vs Louvain)
- [ ] Note de prudence : outil descriptif, pas preuve d'une logique nécessaire



### Issue #047 — Chapitre 6 : Détection de communautés Louvain
**Labels** : `chapitre`, `code`, `validation`, `difficulty: medium`
- **Contexte Analytique** : Différence entre hiérarchie (CAH) et communautés (Louvain).
- **Périmètre Technique (Ouvert aux contributions)** : Maximisation de la modularité $Q$. Comparaison CAH vs Louvain via indice ARI.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Révèle des zones de tension structurelle.
- **Artefacts générés** : Texte du Chapitre 6.

- **Pistes d'exploration suggérées :**
- [ ] Principe : maximisation de la modularité Q
- [ ] Différence conceptuelle entre cluster CAH et communauté Louvain
- [ ] Résultats V1 : 4-6 communautés naturelles. Comparaison avec la CAH (ARI, NMI)
- [ ] Ce que la divergence CAH/Louvain révèle : zones de tension structurelle
- [ ] Hiérarchie de Louvain : super-communautés et micro-communautés
- [ ] **V2** : réseau sur IPS seul vs réseau sur vecteur enrichi — comparaison ARI
- [ ] Test de sensibilité résolution : `for r in [0.5, 1.0, 1.5, 2.0]`



### Issue #048 — Chapitre 7 : Louvain multi-couches (multiplex)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Analyse du réseau sur plusieurs strates (social, spatial, académique).
- **Périmètre Technique (Ouvert aux contributions)** : Algorithme Louvain Multiplex. Calcul de l'Indice de fragmentation inter-couches (IFC).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Identification des corridors de lycéens entre mondes.
- **Artefacts générés** : Texte du Chapitre 7.

- **Pistes d'exploration suggérées :**
- [ ] Principe du réseau multiplex (V1)
- [ ] Construction des trois couches de liens (public, privé, international)
- [ ] **V2** : quatrième couche de proximité géographique (distance GPS réelle)
- [ ] Détection de communautés transversales. Blocs «purs» vs blocs hybrides
- [ ] Corridors entre couches : qui traverse les mondes ?
- [ ] Indice de fragmentation inter-couches (IFC) par couche
- [ ] Les divergences topologique/géographique révèlent des effets institutionnels


---

### MILESTONE T2-P2 — Partie II : Réseau de flux et mobilité


### Issue #049 — Chapitre 8 : Construire un réseau de similarité
**Labels** : `chapitre`, `code`, `validation`, `difficulty: medium`
- **Contexte Analytique** : Construction du Graphe de Similarité $W_{ij}$.
- **Périmètre Technique (Ouvert aux contributions)** : Application d'une fonction de noyau exponentiel sur la distance de Mahalanobis. Seuillage et filtrage de densité.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Ce n'est pas un flux physique réel, mais un réseau de potentiel compétitif.
- **Artefacts générés** : Texte du Chapitre 8, Matrice d'Adjacence.

- **Pistes d'exploration suggérées :**
- [ ] Matrice de distances (euclidienne, Mahalanobis). Fonction de similarité exponentielle.
- [ ] Seuillage : densité du réseau vs signal/bruit. Propriétés topologiques.
- [ ] Visualisation : spring layout, force-directed graph
- [ ] **V2** : comparaison avec modèle nul Erdős–Rényi (même densité). Test de significativité de la modularité.
- [ ] Test de sensibilité seuil : `for p in [60, 65, 70, 75, 80]`



### Issue #050 — Chapitre 9 : Centralité
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèles 21 & 22. Qui détient l'influence structurelle ?
- **Périmètre Technique (Ouvert aux contributions)** : Eigenvector, Betweenness, et Closeness centrality (avec poids inversés).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Position mathématique, pas jugement qualitatif.
- **Artefacts générés** : Texte du Chapitre 9.

- **Pistes d'exploration suggérées :**
- [ ] Degré pondéré. Betweenness centrality : les ponts structurels.
- [ ] Closeness centrality (⚠️ poids inversés : `distance = 1/(weight + 1e-6)`)
- [ ] Eigenvector centrality : les hubs d'influence
- [ ] Top 10 lycées par centralité composite (V1)
- [ ] Carte du réseau avec centralité codée visuellement (V1)
- [ ] **V2** : corrélation centralité × résultats bac × revenus IRIS
- [ ] Script `figures/fig3_network_louvain.py`



### Issue #051 — Chapitre 10 : Les ponts entre mondes scolaires
**Labels** : `chapitre`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Lycées situés à l'intersection des clusters sociaux.
- **Périmètre Technique (Ouvert aux contributions)** : Score de pont composite (Betweenness + diversité communautaire).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Un "pont" n'est pas un lycée qui fait consciemment des efforts d'inclusion.
- **Artefacts générés** : Texte du Chapitre 10.

- **Pistes d'exploration suggérées :**
- [ ] Définition opérationnelle du pont (V1)
- [ ] Score de pont composite V1 : betweenness + diversité communautaire + distance ultramétrique
- [ ] Top ponts du système francilien V1 : Lakanal, Hoche, Louis-le-Grand, Henri-IV
- [ ] Lycées frontières entre public d'élite et privé bourgeois
- [ ] Lycées frontières entre monde national et monde international
- [ ] Signification sociologique : institutions qui limitent la fragmentation
- [ ] Note éthique : «ponts analytiques» ≠ pratiques d'admission ou ouverture institutionnelle



### Issue #052 — Chapitre 11 : Flux de mobilité, matrice de Markov
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 24. Mobilité aléatoire simulée.
- **Périmètre Technique (Ouvert aux contributions)** : Normalisation de la matrice de transition $P_{ij}$. Calcul de la distribution stationnaire.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Pure simulation probabiliste.
- **Artefacts générés** : Texte du Chapitre 11.

- **Pistes d'exploration suggérées :**
- [ ] Matrice de transition entre clusters
- [ ] Probabilités de mobilité ascendante / descendante
- [ ] Distribution stationnaire : à quel équilibre tend le système ?
- [ ] Entropie des trajectoires. Durée moyenne dans un cluster (V1)
- [ ] Clusters «pièges» vs clusters «passerelles» (V1)
- [ ] Note de prudence : matrice simulée ≠ matrice observée (sauf données Affelnet)
- [ ] **V2** : calibration partielle avec données Affelnet si disponibles, mesure de l'écart simulé/observé



### Issue #053 — Chapitre 12 : Corridors sociaux : définition et détection
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Détection des autoroutes sociales.
- **Périmètre Technique (Ouvert aux contributions)** : Score de corridor $R_{ab} = F_{ab} / E_{ab}$. Corridors symétriques vs asymétriques ($\Gamma$).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les chemins par défaut du système.
- **Artefacts générés** : Texte du Chapitre 12.

- **Pistes d'exploration suggérées :**
- [ ] Flux observé vs flux attendu (modèle nul d'indépendance)
- [ ] Score de corridor R_ab = F_ab / E_ab
- [ ] Corridors actifs : sur-représentation des transitions. Corridors symétriques vs asymétriques (indice Γ)
- [ ] Top corridors du système francilien — les «autoroutes sociales»
- [ ] Signification V1 : formalisation des «autoroutes sociales» du système scolaire



### Issue #054 — Chapitre 13 : Ascenseurs sociaux vs filtres
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Distinction de l'efficacité verticale des corridors.
- **Périmètre Technique (Ouvert aux contributions)** : Mesure du flux ascendant + gradient positif (Ascenseur) vs flux descendant (Filtre).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Termes d'ingénierie socio-physique.
- **Artefacts générés** : Texte du Chapitre 13.

- **Pistes d'exploration suggérées :**
- [ ] Définition formelle de l'ascenseur (flux ascendant + gradient positif)
- [ ] Définition formelle du filtre (flux descendant + tri social)
- [ ] Corridors ambigus : flux fort mais gradient neutre
- [ ] Distribution spatiale des ascenseurs et filtres. Efficacité des ascenseurs : Δ S moyen (V1)
- [ ] Encadré V1 : les corridors d'élite vs corridors de mobilité sociale descendante



### Issue #055 — Chapitre 14 : Réseau multiplex et analyse multi-couches
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Synthèse de la centralité inter-couches.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de la symétrie de flux selon la couche.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutre.
- **Artefacts générés** : Texte du Chapitre 14.

- **Pistes d'exploration suggérées :**
- [ ] Superposition des couches V1 : social, académique, résidentiel, flux
- [ ] Centralité de chaque couche. Score inter-couches : qui est central dans toutes les couches ?
- [ ] Indice de fragmentation inter-couches (IFC)
- [ ] Symétrie / asymétrie des flux selon les couches
- [ ] Corrélation entre couches : où les logiques se renforcent-elles ?


---

### MILESTONE T2-P3 — Partie III : Structures cachées


### Issue #056 — Chapitre 15 : Distance de Mahalanobis
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Détection des anomalies.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de l'inversion de matrice de covariance. Ellipses de confiance.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Anomalie" = exception statistique pure.
- **Artefacts générés** : Texte du Chapitre 15, Liste des 50 outliers.

- **Pistes d'exploration suggérées :**
- [ ] Top outliers Mahalanobis, ellipses de confiance
- [ ] **Nouveauté** : outliers Mahalanobis vs valeur ajoutée bac atypique (croisement analytique)
- [ ] "Paradoxes analytiques" traités sans jugement



### Issue #057 — Chapitre 16 : Les zones de bascule
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Lycées à la lisière des inversions de gradients.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul du gradient local des effets.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Structure analytique émergente, pas réalité empirique stricte.
- **Artefacts générés** : Texte du Chapitre 16.

- **Pistes d'exploration suggérées :**
- [ ] Gradient local des effets, détection des inversions de gradient
- [ ] Note obligatoire : zones de bascule = structures analytiques émergentes du modèle, pas réalité empirique directe



### Issue #058 — Chapitre 17 : Résidus structurels (SAR + Moran)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèles 26 & 27. Là où la géographie ne suffit plus à expliquer.
- **Périmètre Technique (Ouvert aux contributions)** : Modèle SAR. Calcul des résidus (Blind spots). Indice LISA de Moran.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cartographie des ignorances du modèle.
- **Artefacts générés** : Texte du Chapitre 17, Carte LISA.

- **Pistes d'exploration suggérées :**
- [ ] Modèle SAR de base, calcul des résidus, autocorrélation Moran
- [ ] Score de "blind spot" spatial
- [ ] **Nouveauté** : corrélation résidus × accessibilité transport



### Issue #059 — Chapitre 18 : Classes latentes — les mondes scolaires cachés
**Labels** : `chapitre`, `code`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle GMM (Gaussian Mixture Model).
- **Périmètre Technique (Ouvert aux contributions)** : Estimation des probabilités locales d'appartenance à 5 classes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Révèle la porosité des mondes.
- **Artefacts générés** : Texte du Chapitre 18.

- **Pistes d'exploration suggérées :**
- [ ] Modèle GMM (Gaussian Mixture Model)
- [ ] Latent Class Mixed Model
- [ ] 5 classes latentes détectées — description profils statistiques et sociologiques
- [ ] Zones d'incertitude : établissements multi-appartenance
- [ ] Entropie locale : carte des zones hybrides



### Issue #060 — Chapitre 19 : Frontières sociales floues — le gradient KDE
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Mesure de l'entropie des frontières.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de l'entropie locale $H(x) = -\sum p \log p$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Épaisseur" des frontières.
- **Artefacts générés** : Texte du Chapitre 19.

- **Pistes d'exploration suggérées :**
- [ ] KDE par cluster, probabilités locales d'appartenance
- [ ] Entropie locale H(x) comme mesure de flou
- [ ] Gradient de transition : là où les mondes se mélangent
- [ ] «Épaisseur» des frontières scolaires (concept central)
- [ ] Indice global de flou des frontières F



### Issue #061 — Chapitre 20 : Tension hiérarchie/réseau — points de bascule ultramétriques
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : L'écart entre distance en graphe et distance en arbre.
- **Périmètre Technique (Ouvert aux contributions)** : Mesure du désalignement $|d_{ij} - d^U_{ij}| \times w_{ij}$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Où la mobilité échappe à la hiérarchie ?
- **Artefacts générés** : Texte du Chapitre 20.

- **Pistes d'exploration suggérées :**
- [ ] Mesure de la tension : |d_ij - d^U_ij| × w_ij
- [ ] Lycées «contradictoires» : proches dans le réseau, éloignés dans l'arbre
- [ ] Score de désalignement par lycée
- [ ] Indice global DA : cohérence arbre/réseau
- [ ] Cartographie des points de bascule
- [ ] Signification : là où la mobilité scolaire échappe à la hiérarchie


---

### MILESTONE T2-P4 — Partie IV : Fragmentation et mobilité avancées


### Issue #062 — Chapitre 21 : Pression Ségrégative Locale (PSL)
**Labels** : `chapitre`, `code`, `figure`, `difficulty: low`
- **Contexte Analytique** : Mise à jour avec réseau de flux.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul complet PSL (gravitationnel).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cartographie d'intensité.
- **Artefacts générés** : Texte du Chapitre 21, Carte PSL.

- **Pistes d'exploration suggérées :**
- [ ] Score PSL enrichi avec nouvelles variables
- [ ] Carte PSL sur l'IDF
- [ ] **Nouveauté** : corrélation PSL × accessibilité transport



### Issue #063 — Chapitre 22 : Indice de fragmentation inter-couches (IFC)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Synthèse finale.
- **Périmètre Technique (Ouvert aux contributions)** : Décomposition de l'IFC.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le système d'Île-de-France analysé sous son pire angle.
- **Artefacts générés** : Texte du Chapitre 22.

- **Pistes d'exploration suggérées :**
- [ ] Formule et interprétation
- [ ] Décomposition : IFC public/privé + IPS + géographie
- [ ] IFC par zone (Paris, PC, GC)
- [ ] Indice de mobilité M = 1 - IFC
- [ ] Asymétrie des flux : déséquilibres de mobilité



### Issue #064 — Chapitre 23 : Perméabilité structurelle — un optimum existe-t-il ?
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modélisation des déséquilibres structurels "trop ouvert" vs "trop fermé".
- **Périmètre Technique (Ouvert aux contributions)** : Définition flux $\times$ distance hiérarchique. Indice $\Pi$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le coût structurel d'une mixité forcée sans préparation.
- **Artefacts générés** : Texte du Chapitre 23.

- **Pistes d'exploration suggérées :**
- [ ] Définition de la perméabilité (flux × distance hiérarchique)
- [ ] Trop fermé vs trop ouvert : les deux déséquilibres structurels du système
- [ ] Coût structurel : désorganisation par excès de mixité forcée
- [ ] Indice Π = P_raw / C
- [ ] Perméabilité locale par lycée
- [ ] Lycées «passerelles» vs lycées «verrous»



### Issue #065 — Chapitre 24 : Clusters absorbants et attracteurs dynamiques
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Détection des "trous noirs" scolaires.
- **Périmètre Technique (Ouvert aux contributions)** : Condition spectrale $\rho(T_{Ck}) > 1$. Score $In_k / Out_k$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Démontre la captation des ressources scolaires de la région par des bastions spécifiques.
- **Artefacts générés** : Texte du Chapitre 24, Top clusters absorbants.

- **Pistes d'exploration suggérées :**
- [ ] Définition : flux entrants >> flux sortants
- [ ] Score d'absorption A_k = In_k / Out_k
- [ ] Condition spectrale d'attracteur : ρ(T_Ck) > 1
- [ ] Top clusters absorbants de l'Île-de-France
- [ ] Signification : «puits scolaires» et accumulation des ressources


---

### MILESTONE T2-P5 — Partie V : Spatial et causal


### Issue #066 — Chapitre 25 : Modèle SAR
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Extension spatiale stricte.
- **Périmètre Technique (Ouvert aux contributions)** : SAR avec covariables enrichies. Estimation de $\rho$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Associations spatiales $\neq$ effets causaux.
- **Artefacts générés** : Texte du Chapitre 25.

- **Pistes d'exploration suggérées :**
- [ ] SAR avec covariables enrichies (revenus IRIS, DVF, accessibilité)
- [ ] Estimation de ρ, effets directs vs indirects spatiaux
- [ ] Note obligatoire : associations spatiales ≠ effets causaux



### Issue #067 — Chapitre 26 : Modèle SEM spatial
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle structurel avec variables latentes.
- **Périmètre Technique (Ouvert aux contributions)** : DVF et Accessibilité ajoutés au modèle SEM.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Purement exploratoire.
- **Artefacts générés** : Texte du Chapitre 26.

- **Pistes d'exploration suggérées :**
- [ ] Variables latentes enrichies, R²m vs R²c
- [ ] **Nouveauté** : DVF et accessibilité transport ajoutent-ils du pouvoir explicatif au-delà de l'IPS et IRIS ?



### Issue #068 — Chapitre 27 : GAM non-linéaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les effets ne sont pas droits (splines).
- **Périmètre Technique (Ouvert aux contributions)** : Generalized Additive Models. Tipping points analytiques. (Random Forest placé en annexe).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Associations non-linéaires.
- **Artefacts générés** : Texte du Chapitre 27.

- **Pistes d'exploration suggérées :**
- [ ] GAM avec variables enrichies, effets par splines
- [ ] Note de prudence renforcée : associations non linéaires ≠ identification causale
- [ ] Zones de gradient positif vs négatif, tipping points analytiques
- [ ] ⚠️ Random Forest spatial → `/exploratory/` (pas dans le texte principal)



### Issue #069 — Chapitre 28 : Décomposition des effets indirects
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Effet de quartier vs Effet de réseau.
- **Périmètre Technique (Ouvert aux contributions)** : Extraction des parts de variance.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutre.
- **Artefacts générés** : Texte du Chapitre 28.

- **Pistes d'exploration suggérées :**
- [ ] Effet quartier vs effet réseau
- [ ] Variance quartier / variance réseau
- [ ] **Nouveauté** : l'accessibilité transport modifie-t-elle cet équilibre ?



### Issue #070 — Conclusion Tome II
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Fin du Tome II.
- **Périmètre Technique (Ouvert aux contributions)** : Synthèse des modèles spatiaux.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transition vers le Tome III.
- **Artefacts générés** : Conclusion du Tome 2.

- **Pistes d'exploration suggérées :**
- [ ] Synthétiser les apports et limites des modèles spatiaux développés.
- [ ] Rédiger le texte de la Conclusion du Tome 2.

### Issue #071 — Annexe A1 : Code Python complet
**Labels** : `annexe`, `code`, `difficulty: medium`
- **Contexte Analytique** : Reproductibilité.
- **Périmètre Technique (Ouvert aux contributions)** : Scripts de clustering et graphes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence.
- **Artefacts générés** : Annexe A1.

- **Pistes d'exploration suggérées :**
- [ ] Rassembler les scripts générant les clusters et les réseaux.
- [ ] Structurer ce code Python pour l'Annexe A1 du Tome 2.

### Issue #072 — Annexe A2 : Matrices de distance, similarité, flux
**Labels** : `annexe`, `data`, `difficulty: medium`
- **Contexte Analytique** : Données brutes réseau.
- **Périmètre Technique (Ouvert aux contributions)** : Exports JSON/CSV.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence.
- **Artefacts générés** : Annexe A2.

- **Pistes d'exploration suggérées :**
- [ ] Exporter les matrices mathématiques (distance, flux) sous format lisible (JSON/CSV).
- [ ] Mettre à disposition ces jeux de données via l'Annexe A2.

### Issue #073 — Annexe A3 : Tableau comparatif méthodes de clustering
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Choix algorithmiques.
- **Périmètre Technique (Ouvert aux contributions)** : Benchmarks.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Artefacts générés** : Annexe A3.

- **Pistes d'exploration suggérées :**
- [ ] Rassembler les différents benchmarks de vitesse et de performance algorithmique.
- [ ] Dresser le tableau comparatif final dans l'Annexe A3.

### Issue #074 — Annexe A4 : Résultats complets des modèles
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Inférence.
- **Périmètre Technique (Ouvert aux contributions)** : OLS, SAR, SEM outputs.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence.
- **Artefacts générés** : Annexe A4.

- **Pistes d'exploration suggérées :**
- [ ] Compiler les logs et les résultats statistiques bruts (OLS, SAR, SEM).
- [ ] Structurer ces sorties mathématiques pour l'Annexe A4.

### Issue #075 — Annexe A5 : Note sur les méthodes dans /exploratory/
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Modèles alternatifs.
- **Périmètre Technique (Ouvert aux contributions)** : Random Forest, etc.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence.
- **Artefacts générés** : Annexe A5.

- **Pistes d'exploration suggérées :**
- [ ] Rassembler les résultats des méthodes exploratoires (Random Forest, etc.) non retenues.
- [ ] Rédiger la note méthodologique associée pour l'Annexe A5.

### Issue #076 — Annexe A6 : Cartes supplémentaires
**Labels** : `annexe`, `figure`, `difficulty: low`
- **Contexte Analytique** : Visualisation.
- **Périmètre Technique (Ouvert aux contributions)** : Cartes secondaires.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité.
- **Artefacts générés** : Annexe A6.

- **Pistes d'exploration suggérées :**
- [ ] Regrouper les visualisations géospatiales secondaires générées par les modèles.
- [ ] Exporter ce recueil cartographique pour l'Annexe A6.

### Issue #077 — Annexe A7 : Bibliographie méthodes
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Bibliographie.
- **Périmètre Technique (Ouvert aux contributions)** : Références.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Artefacts générés** : Annexe A7.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger la conclusion du Tome II (5 lycées les plus structurants selon centralité composite)
- [ ] Comparaison internationale courte (Londres, New York — littérature existante)
- [ ] A1 : Code Python complet
- [ ] A2 : Matrices de distance, similarité, flux simulés/observés
- [ ] A3 : Tableau comparatif méthodes de clustering
- [ ] A4 : Résultats complets des modèles
- [ ] A5 : Note sur les méthodes dans `/exploratory/`
- [ ] A6 : Cartes supplémentaires (PSL, centralité, communautés)
- [ ] A7 : Bibliographie méthodes


## 🌀 TOME III — LE TEMPS ET LA RÉFORME

### MILESTONE T3-INTRO — Pages liminaires & Introduction


### Issue #078 — Note éthique et épistémologique Tome III (version renforcée)
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Le Tome III traite du temps, des dynamiques et des métaphores riemanniennes.
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Clause obligatoire de début : "Ce volume propose des cadres dynamiques exploratoires..." Il faut empêcher le lecteur de prendre les projections pour des prédictions.
- **Artefacts générés** : Note éthique T3.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger la note renforcée (cadres exploratoires, non prédictifs, non causaux)
- [ ] Phrase protectrice obligatoire en ouverture : *"Ce volume propose des cadres dynamiques exploratoires…"*
- [ ] Avant-propos : transition "du réseau aux dynamiques", note de limitation explicite sur la granularité des données longitudinales
- [ ] Introduction : présentation transparente du dataset longitudinal (qualité, années manquantes, biais)


---

### MILESTONE T3-P1 — Partie I : Dynamiques temporelles


### Issue #079 — Chapitre 1 : Trajectoires de lycées
**Labels** : `chapitre`, `code`, `figure`, `difficulty: low`
- **Contexte Analytique** : Traquer l'évolution de la valeur $S_{i,t}$ sur plusieurs années.
- **Périmètre Technique (Ouvert aux contributions)** : Score de trajectoire (dérivée moyenne). Corrélation trajectoire $\times$ prix DVF. Script `figures/fig4_trajectories_changepoints.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Identifier les établissements en évolution sociale descendante ou ascendante sans incrimination morale.
- **Artefacts générés** : Texte du Chapitre 1, Figure 4.

- **Pistes d'exploration suggérées :**
- [ ] Définition formelle du score de trajectoire
- [ ] Trois types analytiques : ascendants, déclinants, instables
- [ ] Carte des trajectoires sur l'IDF
- [ ] **Nouveauté** : corrélation trajectoire × évolution prix DVF (polarisation sociale ?)
- [ ] Corrélation trajectoire × données démographiques temporelles INSEE
- [ ] Script `figures/fig4_trajectories_changepoints.py`



### Issue #080 — Chapitre 2 : CAH dynamique
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Évolution de la matrice de clustering.
- **Périmètre Technique (Ouvert aux contributions)** : Matrices de transition inter-temporelles. Indice ARI pour tester si le cluster "Élite" survit dans le temps.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les frontières bougent-elles ?
- **Artefacts générés** : Texte du Chapitre 2.

- **Pistes d'exploration suggérées :**
- [ ] Partitions annuelles, matrice de transition inter-temporelle
- [ ] Stabilité ARI entre années, mobilité de cluster
- [ ] **Nouveauté** : les clusters du Tome II sont-ils stables dans le temps ?



### Issue #081 — Chapitre 3 : L'ultramétrie temporelle
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : La hiérarchie se rigidifie-t-elle avec le temps ?
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de la distance ultramétrique sur 10 ans. Empilement de dendrogrammes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Distinguer l'effet réel de la simple révision du calcul IPS de 2021.
- **Artefacts générés** : Texte du Chapitre 3.

- **Pistes d'exploration suggérées :**
- [ ] Dendrogrammes annuels empilés
- [ ] Distance ultramétrique inter-temporelle, stabilité hiérarchique
- [ ] Note de prudence : distinguer changements réels vs artefacts de la révision IPS 2021



### Issue #082 — Chapitre 4 : Le modèle HMM (régimes cachés)
**Labels** : `chapitre`, `code`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle 35. Le système possède-t-il des "humeurs" latentes ?
- **Périmètre Technique (Ouvert aux contributions)** : Hidden Markov Models sur la série IPS/$\sigma$/Bac. Détection de 4 états latents.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Modèle formel métaphorique.
- **Artefacts générés** : Texte du Chapitre 4.

- **Pistes d'exploration suggérées :**
- [ ] Note de statut épistémologique obligatoire : HMM = cadre exploratoire, pas modélisation robuste au sens strict
- [ ] Variables d'observation : IPS, mixité, résultats bac, prix DVF
- [ ] 4–5 états cachés estimés, matrice de transition, durée moyenne par état



### Issue #083 — Chapitre 5 : HMM couplé au réseau (diffusion des régimes)
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle 36 & 37. Un changement de régime dans Paris se diffuse-t-il via les corridors ?
- **Périmètre Technique (Ouvert aux contributions)** : Graph Neural Network simple ou modèle de diffusion matricielle.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Section expérimentale (`/exploratory/`).
- **Artefacts générés** : Texte du Chapitre 5.

- **Pistes d'exploration suggérées :**
- [ ] Intégration graphe de similarité dans le HMM
- [ ] Note de prudence renforcée : modèle expérimental, résultats = hypothèses exploratoires



### Issue #084 — Chapitre 6 : Dynamique de Theil — évolution de la ségrégation
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : La dérivée de la ségrégation (Modèle 31).
- **Périmètre Technique (Ouvert aux contributions)** : $\Delta T = \Delta T_{within} + \Delta T_{between}$. Calcul de la vitesse $v_T = dT/dt$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Analyser si l'Île-de-France converge vers l'explosion ou vers la stabilité.
- **Artefacts générés** : Texte du Chapitre 6.

- **Pistes d'exploration suggérées :**
- [ ] Série temporelle de T(t)
- [ ] Décomposition dynamique : ΔT = ΔT_within + ΔT_between
- [ ] Paris : hétérogénéité interne maximale, quelle évolution ?
- [ ] Petite couronne : zone de tension, évolution de la polarisation
- [ ] Grande couronne : homogénéité croissante ou décroissante ?
- [ ] Vitesse de fragmentation v_T = dT/dt
- [ ] **V2** : corrélation dynamique Theil × prix DVF



### Issue #085 — Chapitre 7 : Flux de mobilité scolaire — un Sankey dans le temps
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 33. Matérialisation de l'évolution des clusters.
- **Périmètre Technique (Ouvert aux contributions)** : Génération d'une animation Sankey / diagramme de flux temporel.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La "dérive continentale" de l'éducation francilienne.
- **Artefacts générés** : Texte du Chapitre 7.

- **Pistes d'exploration suggérées :**
- [ ] Évolution de la matrice de transition T_t
- [ ] Animation Python conceptuelle 2010-2026 (script fourni)
- [ ] Ouverture / fermeture des corridors dans le temps
- [ ] Émergence et disparition d'ascenseurs sociaux
- [ ] Dérive de T : qu'est-ce qui explique les changements de flux ?


---

### MILESTONE T3-P2 — Partie II : Ruptures et seuils critiques


### Issue #086 — Chapitre 8 : Détection de changepoints (PELT)
**Labels** : `chapitre`, `code`, `figure`, `difficulty: low`
- **Contexte Analytique** : Modèle 34. Trouver les années exactes où le système s'est cassé.
- **Périmètre Technique (Ouvert aux contributions)** : Algorithme PELT (Pruned Exact Linear Time). Corrélation avec les changepoints immobiliers.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Prudence : corrélation $\neq$ causalité.
- **Artefacts générés** : Texte du Chapitre 8.

- **Pistes d'exploration suggérées :**
- [ ] PELT, segmentation binaire, critère AIC/BIC
- [ ] Changepoints sur IPS moyen, σ, Theil, résultats bac
- [ ] **Nouveauté** : coïncidence changepoints scolaires × changepoints DVF immobiliers
- [ ] Note obligatoire : distinguer ruptures réelles vs artefacts révision IPS 2021
- [ ] Test de sensibilité penalty PELT (min_size, pen)



### Issue #087 — Chapitre 9 : Analyse causale des changepoints
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Essayer d'expliquer pourquoi la rupture a eu lieu.
- **Périmètre Technique (Ouvert aux contributions)** : Identification des limites causales (absence de Diff-in-Diff).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cadrage strict des limites du modèle.
- **Artefacts générés** : Texte du Chapitre 9.

- **Pistes d'exploration suggérées :**
- [ ] Note renforcée : associations temporelles, pas effets causaux
- [ ] Ce qu'il faudrait pour une identification causale stricte (diff-in-diff, RD — non disponibles)



### Issue #088 — Chapitre 10 : Phase transitions
**Labels** : `chapitre`, `exploratory`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Modèle 42. Percolation et points critiques.
- **Périmètre Technique (Ouvert aux contributions)** : Condition spectrale de stabilité.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Emprunt fort à la physique statistique. Exiger des "formulations conditionnelles systématiques".
- **Artefacts générés** : Texte du Chapitre 10.

- **Pistes d'exploration suggérées :**
- [ ] Note épistémologique développée : métaphore analytique formalisée, pas loi empirique
- [ ] Condition `ρλ_max(W) ≥ 1` présentée comme condition mathématique sur le modèle
- [ ] Formulations conditionnelles systématiques
- [ ] Résultats "cohérents avec l'hypothèse de fragilisation croissante"



### Issue #089 — Chapitre 11 : Early Warning Signals — prédire les ruptures
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Peut-on savoir si un lycée va s'effondrer socialement ?
- **Périmètre Technique (Ouvert aux contributions)** : Calcul de la variance locale montante, du "critical slowing down".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Limites (faux positifs, sensibilité).
- **Artefacts générés** : Texte du Chapitre 11.

- **Pistes d'exploration suggérées :**
- [ ] Signaux précurseurs d'une transition critique
- [ ] Indicateurs : variance locale, autocorrélation, «critical slowing down»
- [ ] Application aux lycées en frontière
- [ ] Systèmes d'alerte précoce : repérer les lycées «en bascule»
- [ ] Limites : faux positifs, sensibilité aux données
- [ ] Encadré : peut-on prévoir une ségrégation scolaire croissante ?



### Issue #090 — Chapitre 12 : Le DAG inter-temporel — causes et conséquences
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Extension du Modèle 15 au temps $t$.
- **Périmètre Technique (Ouvert aux contributions)** : Inférence causale dynamique, ajout de l'effet inertiel $\alpha$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Expérimentation contrefactuelle in-silico.
- **Artefacts générés** : Texte du Chapitre 12.

- **Pistes d'exploration suggérées :**
- [ ] Extension du DAG statique à une structure dynamique
- [ ] Ultramétrie comme variable causale latente
- [ ] Ruptures ultramétriques comme événements dans le DAG
- [ ] Propagation en cascade : comment un changement de hiérarchie se diffuse
- [ ] Effet mémoriel (inertie) : α dans le modèle dynamique
- [ ] Simulation contrefactuelle : que se passe-t-il si on «casse» un lien causal ?


---

### MILESTONE T3-P3 — Partie III : Géométrie dynamique et modèle final


### Issue #091 — Note préliminaire Partie III
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Introduction du climax théorique de l'Atlas : l'espace de Riemann (modélisation de la dynamique spatio-temporelle).
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Obligation absolue : spécifier que ce sont des langages analytiques, pas des descriptions empiriques directes.
- **Artefacts générés** : Note introductive de la Partie III.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger la note obligatoire (formalismes avancés = langages analytiques, pas descriptions empiriques directement mesurables)



### Issue #092 — Chapitre 13 : L'espace scolaire comme variété riemannienne
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle 48. La topologie sociale n'est pas plate (Espace euclidien), elle est courbée par les privilèges.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul du Tenseur métrique $G_t$. Extraction de la distance non-euclidienne par Isomap.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Métaphore puissante pour montrer que l'ascension sociale demande plus d'énergie que le mobilité sociale descendante.
- **Artefacts générés** : Texte du Chapitre 13.

- **Pistes d'exploration suggérées :**
- [ ] Présentation du formalisme riemannien
- [ ] Chaque lycée comme point, métrique sociale G_t
- [ ] Formulation systématique : "permet de penser X… ne constitue pas une mesure directe"



### Issue #093 — Chapitre 14 : Champ de tensions dynamiques
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Calcul des forces sur chaque établissement (gradient sur l'espace courbe).
- **Périmètre Technique (Ouvert aux contributions)** : Cartographie du champ vectoriel. Calcul $\Phi_{i,t}$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Démontre la force de rappel du déterminisme local.
- **Artefacts générés** : Texte du Chapitre 14.

- **Pistes d'exploration suggérées :**
- [ ] Formalisme du champ de tensions (gradient dans l'espace riemannien)
- [ ] Chaque lycée soumis à des forces structurelles : attraction vers le cluster, répulsion centrifuge
- [ ] Carte du champ de tensions à un instant t
- [ ] Lycées en équilibre vs lycées en tension
- [ ] Formulation : «permet de penser la dynamique structurelle... ne constitue pas une mesure directe»



### Issue #094 — Chapitre 15 : Le modèle unifié
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Synthèse mathématique finale.
- **Périmètre Technique (Ouvert aux contributions)** : Intégration de la fonction de perte multi-composantes $L = L_{HMM} + \lambda_1 L_{GNN} + \lambda_2 L_{ultra} + \lambda_3 L_{flux}$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mettre le code complet dans `/exploratory/`. Ne pas en faire le juge de paix, mais le sommet technique.
- **Artefacts générés** : Texte du Chapitre 15.

- **Pistes d'exploration suggérées :**
- [ ] **Note obligatoire** : `L = L_HMM + λ₁L_GNN + λ₂L_ultra + λ₃L_flux` = outil formel d'exploration, hyperparamètres fixés exploratoirement
- [ ] Ce modèle → `/exploratory/` sur GitHub (pas dans le texte principal comme résultat)
- [ ] Qu'est-ce que ce modèle permet de penser que les modèles séparés ne permettent pas ?
- [ ] Synthèse des trois tomes : de la carte à la dynamique


---

### MILESTONE T3-P4 — Partie IV : Paradoxes et anomalies


### Issue #095 — Note éthique Partie IV
**Labels** : `ethique`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Introduction sur les anomalies paradoxales (Modèle 45).
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Un "lycée sous-performant" est un écart statistique au modèle, pas un jugement sur les équipes pédagogiques.
- **Artefacts générés** : Note éthique Partie IV.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger la note spécifique : "paradoxaux", "sur-performants", "sous-performants" = qualifications relatives à un modèle statistique, pas évaluations de qualité de l'enseignement



### Issue #096 — Chapitre 16 : Lycées paradoxaux positifs (sur-performance sociale)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les lycées qui défient la gravité sociale.
- **Périmètre Technique (Ouvert aux contributions)** : Résidus OLS massifs positifs confirmés par la valeur ajoutée IVAL. Score $P_i$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : On constate le paradoxe sans l'expliquer totalement avec des données macro.
- **Artefacts générés** : Texte du Chapitre 16.

- **Pistes d'exploration suggérées :**
- [ ] Définition formelle avec résultats bac + valeur ajoutée IVAL comme validation externe
- [ ] Score de paradoxalité enrichi
- [ ] Formulation éthique : "performance relative supérieure à ce que leur profil prédirait"
- [ ] Mécanismes non déductibles des données agrégées



### Issue #097 — Chapitre 17 : Paradoxes inversés — le sous-rendement de l'élite
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les lycées qui, vu leur recrutement élitiste, devraient faire bien mieux au bac.
- **Périmètre Technique (Ouvert aux contributions)** : Corrélation avec le score d'entre-soi. Hypothèse de l'effet d'inertie institutionnelle.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Peut-on trop bien trier ses élèves ?" Formulation neutre.
- **Artefacts générés** : Texte du Chapitre 17.

- **Pistes d'exploration suggérées :**
- [ ] Lycées à IPS très élevé mais performance relative faible
- [ ] Hypothèses : saturation, effet sélectivité symbolique, inertie institutionnelle
- [ ] Corrélation entre score d'entre-soi et paradoxe inversé
- [ ] Peut-on «trop bien» trier ses élèves ? (question analytique clé)
- [ ] Carte des paradoxes inversés en Île-de-France
- [ ] **V2** : croisement DVF (dynamique immobilière atypique ?)



### Issue #098 — Chapitre 18 : Trajectoires rares — les outliers de mobilité scolaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Analyser les trajectoires individuelles de lycées qui sautent de cluster.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul anomalie $A(\tau) = -\log P(\tau)$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les marges du déterminisme scolaire.
- **Artefacts générés** : Texte du Chapitre 18.

- **Pistes d'exploration suggérées :**
- [ ] Définition : P(τ_i) ≪ ε
- [ ] Score d'anomalie A(τ_i) = -log P(τ_i)
- [ ] Types : contre-hiérarchiques, «sauts», oscillantes, géographiques
- [ ] Ce que les trajectoires rares révèlent : contournements, réseaux, stratégies
- [ ] Signification : les marges du déterminisme scolaire
- [ ] **V2** : croisement DVF (dynamique immobilière atypique ?)



### Issue #099 — Chapitre 19 : Communes hyper-ségrégées malgré mixité apparente
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les villes qui s'illustrent par une ségrégation intra-muros intense.
- **Périmètre Technique (Ouvert aux contributions)** : Score $HS_c$. Carte IDF des communes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les options (latin, bilangue) ou le privé agissent comme tamis invisible.
- **Artefacts générés** : Texte du Chapitre 19.

- **Pistes d'exploration suggérées :**
- [ ] Paradoxe de la commune «mixte en moyenne»
- [ ] Indice de fausse mixité F_c = M_global - M_interne
- [ ] Score d'hyper-ségrégation masquée HS_c
- [ ] Top communes paradoxales (forte moyenne, forte séparation interne)
- [ ] Mécanismes : filières, options, réputation, recrutement implicite
- [ ] Carte IDF des communes hyper-ségrégées
- [ ] **V2** : croisement DVF (dynamique immobilière atypique ?)



### Issue #100 — Chapitre 20 : Blind spots systémiques
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Ce que tous les modèles (SAR, GMM, Theil) n'arrivent pas à prévoir.
- **Périmètre Technique (Ouvert aux contributions)** : Calcul du score $BS_i$. Consensus d'erreur.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Avouer les ignorances de la machine de l'Atlas.
- **Artefacts générés** : Texte du Chapitre 20.

- **Pistes d'exploration suggérées :**
- [ ] Score BS_i = |R_i| × Σ W_ij |R_j|
- [ ] Consensus multi-modèle d'erreur
- [ ] Zones systématiquement mal expliquées
- [ ] Hypothèses sur variables manquantes : réputation, alumni, dérogations
- [ ] **V2** : croisement DVF (dynamique immobilière atypique ?)


---

### MILESTONE T3-P5 — Partie V : Réforme et simulation


### Issue #101 — Note de cadrage Partie V (obligatoire)
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : "Que se passerait-il si... ?"
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les simulations ne sont PAS des recommandations de politique publique. Les parents s'adapteraient (ex: déménagement, fuite dans le privé), ce que le modèle ignore.
- **Artefacts générés** : Note de Cadrage.

- **Pistes d'exploration suggérées :**
- [ ] Rédiger la note : simulations = scénarios analytiques, pas prédictions ni recommandations de politique publique
- [ ] Préciser que les comportements adaptatifs des acteurs ne sont pas modélisés



### Issue #102 — Chapitre 21 : Simulation réforme — changer la carte scolaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Redistribution in-silico des IPS.
- **Périmètre Technique (Ouvert aux contributions)** : Simulation spatiale non-linéaire. Vérifier si cela déclenche une "transition de phase".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cadrage strict des limites du modèle.
- **Artefacts générés** : Texte du Chapitre 21.

- **Pistes d'exploration suggérées :**
- [ ] Modèle non-linéaire spatial comme outil de simulation
- [ ] Simulation 1 V1 : redistribution des IPS (re-sectorisation)
- [ ] Propagation : la réforme se diffuse-t-elle dans le réseau ?
- [ ] Effets de bord : quels lycées bénéficient, lesquels perdent ?
- [ ] Condition de succès V1 : éviter de déclencher une transition de phase
- [ ] Limites section obligatoire : comportements familiaux statiques, effets adaptatifs potentiellement annulateurs



### Issue #103 — Chapitre 22 : Simulation — neutraliser le privé sélectif
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Contrefactuel : supprimer les 20 lycées les plus fermés de l'algorithme.
- **Périmètre Technique (Ouvert aux contributions)** : Réallocation des flux dans le réseau. Modélisation de l'impact sur les corridors (nouveaux ascenseurs ?).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Exercice purement mathématique analytique. Pas une "fermeture" d'écoles, mais un test de stress de l'équation de Theil.
- **Artefacts générés** : Texte du Chapitre 22.

- **Pistes d'exploration suggérées :**
- [ ] Contrefactuel V1 : que se passe-t-il si on ferme les 20 lycées les plus fermés socialement ?
- [ ] Réallocation des flux dans le réseau
- [ ] Impact sur les clusters : recomposition des mondes scolaires ?
- [ ] Impact sur les corridors : nouveaux ascenseurs sociaux ?
- [ ] Impact sur les goulots : libération de mobilité ?
- [ ] Discussion V1 : est-ce souhaitable ? faisable ? suffisant ? — exercice analytique, pas proposition de politique
- [ ] Note obligatoire : exercice analytique, pas proposition de politique publique



### Issue #104 — Chapitre 23 : Simulation — renforcer les lycées paradoxaux positifs
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modéliser un "label d'excellence" sur la base de la VA au lieu du recrutement social.
- **Périmètre Technique (Ouvert aux contributions)** : Augmentation artificielle du coefficient d'attractivité des "paradoxes positifs" dans le réseau $W$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Risque in-silico de polarisation sociale scolaire progressive mis en évidence.
- **Artefacts générés** : Texte du Chapitre 23.

- **Pistes d'exploration suggérées :**
- [ ] Investir dans les lycées qui sur-performent socialement
- [ ] Impact sur le réseau de mobilité
- [ ] Risque de polarisation sociale scolaire progressive (V1)
- [ ] Effet de labellisation : comment la réputation change les flux
- [ ] Quelle politique de communication accompagne cette stratégie ? (V1)



### Issue #105 — Chapitre 24 : Politiques de mixité : leçons des modèles
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Synthèse théorique des trois simulations.
- **Périmètre Technique (Ouvert aux contributions)** : Analyse de "l'optimum de perméabilité" théorique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mixité forcée vs mixité incitée. "Le risque de la réforme sans modèle".
- **Artefacts générés** : Texte du Chapitre 24.

- **Pistes d'exploration suggérées :**
- [ ] Ce que les modèles disent sur la mixité (V1)
- [ ] La mixité forcée vs la mixité incitée
- [ ] L'optimum de perméabilité : ni trop fermé ni trop ouvert
- [ ] Le rôle des corridors : soutenir les ascenseurs, contester les filtres
- [ ] Les lycées-ponts comme leviers de politique publique
- [ ] Le risque de la réforme sans modèle : déclencher une phase transition non désirée



### Issue #106 — Chapitre 25 : Vers un atlas dynamique
**Labels** : `chapitre`, `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Structuration de l'outil technique (Atlas).
- **Périmètre Technique (Ouvert aux contributions)** : Cartographie des 9 couches de données empilées.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Présenter l'Atlas comme un outil d'aide à la compréhension, pas comme un juge.
- **Artefacts générés** : Texte du Chapitre 25.

- **Pistes d'exploration suggérées :**
- [ ] Les 9 couches de l'atlas
- [ ] Concept d'interactivité (GitHub interactif si développé)
- [ ] Ce que les données actuelles permettent et ne permettent pas encore


---

### MILESTONE T3-P6 — Partie VI : Limites, éthique et ouvertures


### Issue #107 — Chapitre 26 : Limites méthodologiques (le plus important du tome)
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Auto-critique algorithmique de l'Atlas.
- **Périmètre Technique (Ouvert aux contributions)** : Évaluation du "ecological fallacy", des biais de sélection (seulement top 100 ou corpus partiel), de l'absence de données individuelles longitudinales.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le chapitre le plus important. Non-stationnarité du réel vs stationnarité des modèles.
- **Artefacts générés** : Texte du Chapitre 26.

- **Pistes d'exploration suggérées :**
- [ ] IPS comme proxy imparfait
- [ ] Données agrégées et ecological fallacy
- [ ] Absence de données individuelles longitudinales
- [ ] Biais de sélection du corpus (top 100 seulement — implications)
- [ ] Limites des simulations (comportements adaptatifs non modélisés)
- [ ] Non-stationnarité du réel vs stationnarité des modèles
- [ ] Modifications méthodologiques du Ministère (révision IPS 2021)
- [ ] Confusion potentielle artefacts de mesure / changements réels



### Issue #108 — Chapitre 27 : Éthique de la quantification scolaire
**Labels** : `chapitre`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Le danger des mathématiques sociales.
- **Périmètre Technique (Ouvert aux contributions)** : Rédaction théorique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le risque de naturaliser les inégalités. Distinguer "décrire une structure" de "l'accepter comme naturelle". L'IPS peut-il être interprété abusivement ??
- **Artefacts générés** : Texte du Chapitre 27.

- **Pistes d'exploration suggérées :**
- [ ] Le risque de naturaliser les inégalités
- [ ] La mise en données de l'inégalité : pouvoir et contre-pouvoir
- [ ] L'IPS peut-il être interprété abusivement ??
- [ ] Responsabilité du chercheur dans la diffusion
- [ ] Distinction : décrire une structure ≠ l'accepter comme naturelle



### Issue #109 — Chapitre 28 : Ouvertures disciplinaires et comparaisons internationales
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Paris face au reste du monde.
- **Périmètre Technique (Ouvert aux contributions)** : Synthèse de la littérature existante sur Londres, New York, Berlin, Tokyo.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Ne pas faire d'inférence, juste de la bibliographie comparative.
- **Artefacts générés** : Texte du Chapitre 28.

- **Pistes d'exploration suggérées :**
- [ ] Sociologie, géographie sociale, économie, informatique, physique statistique
- [ ] Comparaisons internationales développées (Paris vs Londres, New York, Berlin, Tokyo, Barcelone) — littérature existante uniquement



### Issue #110 — Chapitre 29 : Agenda de recherche
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Les prochaines frontières.
- **Périmètre Technique (Ouvert aux contributions)** : Listing de 10 questions ouvertes et des Data manquantes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Ce qu'un accès aux données individuelles permettrait de faire.
- **Artefacts générés** : Texte du Chapitre 29.

- **Pistes d'exploration suggérées :**
- [ ] 10 questions ouvertes
- [ ] Données nécessaires pour aller plus loin
- [ ] Ce qu'un accès à des données individuelles longitudinales permettrait de faire



### Issue #111 — Conclusion générale de la trilogie
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Clôture de l'Atlas.
- **Périmètre Technique (Ouvert aux contributions)** : Synthèse narrative.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le paradoxe de la méritocratie républicaine face aux données. Sans prescription normative.
- **Artefacts générés** : Conclusion Générale.

- **Pistes d'exploration suggérées :**
- [ ] Ce que l'IDF dit de la France scolaire
- [ ] La ségrégation scolaire comme processus, pas état
- [ ] Le paradoxe de la méritocratie républicaine face aux données
- [ ] Mise en perspective internationale finale
- [ ] Responsabilité collective et leviers d'action (sans prescription normative)



### Issue #112 — Annexe A1 : Code Python complet
**Labels** : `annexe`, `code`, `difficulty: medium`
- **Contexte Analytique** : Reproductibilité du Tome 3.
- **Périmètre Technique (Ouvert aux contributions)** : Scripts dynamiques.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence.
- **Artefacts générés** : Annexe A1.

- **Pistes d'exploration suggérées :**
- [ ] Rassembler les scripts Python dédiés aux séries temporelles et détections de ruptures.
- [ ] Structurer le code dynamique pour l'Annexe A1 du Tome 3.

### Issue #113 — Annexe A2 : Note méthodes
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Choix avancés.
- **Périmètre Technique (Ouvert aux contributions)** : Justifications.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Artefacts générés** : Annexe A2.

- **Pistes d'exploration suggérées :**
- [ ] Réunir les justifications mathématiques des paramètres choisis pour les modèles.
- [ ] Rédiger la note méthodologique justificative dans l'Annexe A2.

### Issue #114 — Annexe A3 : Paramètres estimés des modèles dynamiques
**Labels** : `annexe`, `data`, `difficulty: medium`
- **Contexte Analytique** : Résultats bruts.
- **Périmètre Technique (Ouvert aux contributions)** : HMM, PELT.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence.
- **Artefacts générés** : Annexe A3.

- **Pistes d'exploration suggérées :**
- [ ] Extraire les paramètres estimés par les modèles temporels (HMM, algorithme PELT).
- [ ] Compiler ces valeurs mathématiques dans l'Annexe A3.

### Issue #115 — Annexe A4 : Résultats des simulations de réforme
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Scénarios.
- **Périmètre Technique (Ouvert aux contributions)** : Tableaux de projection.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutre.
- **Artefacts générés** : Annexe A4.

- **Pistes d'exploration suggérées :**
- [ ] Agréger les tableaux de projection issus des simulations de réformes.
- [ ] Mettre en page ces résultats chiffrés pour l'Annexe A4.

### Issue #116 — Annexe A5 : Cartes temporelles et animations
**Labels** : `annexe`, `figure`, `difficulty: low`
- **Contexte Analytique** : Visualisation.
- **Périmètre Technique (Ouvert aux contributions)** : GIFs/Vidéos.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Factuel.
- **Artefacts générés** : Annexe A5.

- **Pistes d'exploration suggérées :**
- [ ] Générer et optimiser les animations (GIFs, vidéos) d'évolution des flux scolaires.
- [ ] Constituer la galerie multimédia de l'Annexe A5.

### Issue #117 — Annexe A6 : Sources longitudinales
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Données temporelles.
- **Périmètre Technique (Ouvert aux contributions)** : Bibliographie data.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Artefacts générés** : Annexe A6.

- **Pistes d'exploration suggérées :**
- [ ] Inventorier les sources de données longitudinales exploitées.
- [ ] Dresser la bibliographie data complète pour l'Annexe A6.

### Issue #118 — Annexe A7 : Index général de la trilogie
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Navigation.
- **Périmètre Technique (Ouvert aux contributions)** : Indexation.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Facilité.
- **Artefacts générés** : Annexe A7.

- **Pistes d'exploration suggérées :**
- [ ] Créer l'indexation globale croisée sur l'ensemble de la trilogie.
- [ ] Générer l'index général final pour l'Annexe A7.

### Issue #119 — Annexe A8 : Bibliographie complète
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Clôture bibliographique.
- **Périmètre Technique (Ouvert aux contributions)** : Références globales.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Artefacts générés** : Annexe A8.

- **Pistes d'exploration suggérées :**
- [ ] Agréger les citations et la littérature scientifique de l'ensemble du projet.
- [ ] Formater la bibliographie exhaustive de l'Annexe A8.

### Issue #120 — Annexe A9 : Glossaire général unifié
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Définitions.
- **Périmètre Technique (Ouvert aux contributions)** : Dictionnaire de termes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Clarté.
- **Artefacts générés** : Annexe A9.

- **Pistes d'exploration suggérées :**
- [ ] Unifier le dictionnaire des termes techniques (code, stats, socio) employés dans les trois tomes.
- [ ] Rédiger le glossaire de référence global dans l'Annexe A9.

### Issue #121 — Annexe A10 : Licences de données
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Légal.
- **Périmètre Technique (Ouvert aux contributions)** : Open Data.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Droit.
- **Artefacts générés** : Annexe A10.

- **Pistes d'exploration suggérées :**
- [ ] Vérifier la conformité légale et recenser l'ensemble des licences Open Data.
- [ ] Rédiger le récapitulatif juridique pour l'Annexe A10.

### Issue #122 — Annexe A11 : Table de correspondance méthode
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Justification.
- **Périmètre Technique (Ouvert aux contributions)** : Table récapitulative.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Académique.
- **Artefacts générés** : Annexe A11.

- **Pistes d'exploration suggérées :**
- [ ] A1 : Code Python complet (HMM, changepoints, simulations, phase transitions) + lien GitHub
- [ ] A2 : Note méthodes `/exploratory/` avec justification (pourquoi non-inclus dans le texte principal)
- [ ] A3 : Paramètres estimés des modèles dynamiques
- [ ] A4 : Résultats des simulations de réforme (tableaux complets)
- [ ] A5 : Cartes temporelles et animations (Python script fourni)
- [ ] A6 : Sources longitudinales, méthode de construction dataset temporel + biais documentés
- [ ] A7 : Index général de la trilogie
- [ ] A8 : Bibliographie complète (3 tomes)
- [ ] A9 : Glossaire général unifié
- [ ] A10 : Licences de données (Etalab, Open Data Commons, conditions réutilisation)
- [ ] A11 : Table de correspondance méthode/justification sociologique complète


---

## 🎨 ISSUES FIGURES SIGNATURE (transversal)


### Issue #123 — Figure 1 : Carte IPS + ségrégation territoriale
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Première image frappante du Tome I.
- **Périmètre Technique (Ouvert aux contributions)** : Taille des points proportionnelle à l'effectif. Gradient Est/Ouest. Intégrer les revenus IRIS en transparence. Sous-panel scatter IPS vs DVF. Script `figures/fig1_map.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Carte factuelle.
- **Artefacts générés** : Figure 1 HD et Caption LaTeX.

- **Pistes d'exploration suggérées :**
- [ ] Collecter les données géographiques (GeoPandas, communes IDF)
- [ ] Intégrer les revenus IRIS en transparence
- [ ] Taille des points ∝ effectif, gradient Est/Ouest visible
- [ ] Sous-panel : scatter IPS communal vs prix médian DVF
- [ ] Script `figures/fig1_map.py` (code complet dans plan_integral_v2.md)
- [ ] Caption arXiv rédigée



### Issue #124 — Figure 2 : Scatter IPS vs σ
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Démonstration visuelle de la "mixité cachée".
- **Périmètre Technique (Ouvert aux contributions)** : Densité KDE en fond, couleurs rouge/bleu (privé/public). Annotations des lycées emblématiques. Script `figures/fig2_scatter_ips_sigma.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Standard Nature/Science.
- **Artefacts générés** : Figure 2 HD et Caption LaTeX.

- **Pistes d'exploration suggérées :**
- [ ] Densité KDE en fond
- [ ] Couleurs rouge/bleu privé/public
- [ ] Annotations cas emblématiques
- [ ] Sous-panel : corrélation σ × DVF
- [ ] Script `figures/fig2_scatter_ips_sigma.py` (code complet dans plan_integral_v2.md)
- [ ] Caption arXiv rédigée



### Issue #125 — Figure 3 : Réseau Louvain
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Le graphe de l'Île-de-France.
- **Périmètre Technique (Ouvert aux contributions)** : Layout force-directed (spring). Taille nœuds proportionnelle à la centralité eigenvector. Épaisseur arêtes proportionnelle à la similarité. Script `figures/fig3_network_louvain.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Clarifier dans la caption que c'est un réseau mathématique, pas physique.
- **Artefacts générés** : Figure 3 HD et Caption LaTeX.

- **Pistes d'exploration suggérées :**
- [ ] Layout force-directed (spring_layout)
- [ ] Taille nœuds ∝ centralité eigenvector
- [ ] Épaisseur arêtes ∝ similarité
- [ ] Annotation top 10 nœuds centraux
- [ ] Script `figures/fig3_network_louvain.py` (code complet dans plan_integral_v2.md)
- [ ] Caption arXiv avec valeur de modularité Q



### Issue #126 — Figure 4 : Trajectoires + changepoints
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : La dynamique dans le temps.
- **Périmètre Technique (Ouvert aux contributions)** : Courbes temporelles colorées par cluster. Changepoints PELT marqués en rouge. Script `figures/fig4_trajectories_changepoints.py`.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Annotations directement dans le graphique (ex: "changement de formule IPS").
- **Artefacts générés** : Figure 4 HD et Caption LaTeX.

- **Pistes d'exploration suggérées :**
- [ ] Courbes temporelles colorées par cluster Louvain
- [ ] Changepoints PELT marqués en rouge
- [ ] Annotation épistémologique directement dans le graphique
- [ ] Script `figures/fig4_trajectories_changepoints.py` (code complet dans plan_integral_v2.md)
- [ ] Caption arXiv rédigée


---

## 📄 ISSUES arXiv et MANIFESTE


### Issue #127 — Paper arXiv (LaTeX)
**Labels** : `documentation`, `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Soumission scientifique.
- **Périmètre Technique (Ouvert aux contributions)** : Compilation de `paper_arxiv/main.tex`. Abstract < 250 mots. Intégration des figures.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Limites explicites inscrites dès l'abstract.
- **Artefacts générés** : PDF final `main.pdf`.

- **Pistes d'exploration suggérées :**
- [ ] Compiler `paper_arxiv/main.tex` (base dans `manifesto.tex`)
- [ ] Intégrer les 4 figures signature
- [ ] Abstract ≤ 250 mots
- [ ] Note de limitation explicite dans l'abstract
- [ ] Vérifier conformité arXiv (format, fonts, références)



### Issue #128 — Robustesse & Sensibilité (checklist globale)
**Labels** : `validation`, `difficulty: medium`
- **Contexte Analytique** : La garantie de solidité des 3 tomes.
- **Périmètre Technique (Ouvert aux contributions)** : Permutation Moran (n=999), MAUP check, sensibilité seuil réseau (p=60,70,80), Bootstrap ARI (n=1000).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Validation stricte.
- **Artefacts générés** : Rapport de robustesse intégré aux annexes.

- **Pistes d'exploration suggérées :**
- [ ] Moran global (permutation CI, n=999)
- [ ] Moran local (LISA, correction Bonferroni)
- [ ] SAR avec différentes matrices de poids (k=4, k=8, inverse distance)
- [ ] ICC (HLM nul) pour justification multi-niveaux
- [ ] MAUP check (analyse à IRIS, commune, département)
- [ ] Sensibilité seuil réseau
- [ ] Sensibilité résolution Louvain
- [ ] Stabilité bootstrap ARI (n=1000)
- [ ] Comparaison modularité observée vs modèle nul
- [ ] Normalisation z-score avant PELT
- [ ] Bootstrap sur Gini, Theil, Duncan (CI n=1000)



