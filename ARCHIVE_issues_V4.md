# 🐙 GitHub Issues — Trilogie *Vers un Atlas des Dynamiques Scolaires*

## 🏗️ MILESTONE 0 — Infrastructure & Setup Transversal

### Issue #001 — Structure du dépôt GitHub
**Labels** : `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Déploiement de l'environnement de recherche reproductible pour l'Atlas.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Architecture transparente et documentée.
- **Artefacts générés** : Dépôt structuré, `README.md` bilingue, `MANIFESTO.md`, `DATA_SOURCES.md`, `LICENSE`.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Traitement factuel des sources publiques, sourçage rigoureux.
- **Artefacts générés** : Pipeline de collecte, table maître (`data/processed/master_dataset.parquet`).

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Affirmation de la doctrine descriptive vs normative (aucun jugement moral).
- **Artefacts générés** : `docs/CAUSALITY_LIMITS.md`, `docs/NETWORK_INTERPRETATION.md`, `docs/SOCLE_MATHEMATIQUE.md`, `docs/SOCLE_DYNAMIQUE.md`, `docs/GLOSSAIRE.md`.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Créer `docs/CAUSALITY_LIMITS.md` (template validé dans info_github.md)
  - [ ] Créer `docs/NETWORK_INTERPRETATION.md` (template validé dans info_github.md)
  - [ ] Intégrer `docs/SOCLE_MATHEMATIQUE.md` (Formules statistiques et indices de ségrégation)
  - [ ] Intégrer `docs/SOCLE_DYNAMIQUE.md` (Modèles dynamiques, causaux et temporels)
  - [ ] Intégrer `docs/GLOSSAIRE.md` (Lexique unifié déjà existant)
  - [ ] Vérifier que chaque tome intègre la note éthique modèle



### Issue #004 — Tests unitaires (infrastructure)
**Labels** : `code`, `validation`, `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Validation mathématique des outils de l'Atlas (Modèles 1 à 15).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Garantie de la rigueur algorithmique de la recherche.
- **Artefacts générés** : Suite de tests `tests/` opérationnelle.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] `tests/test_theil_decomposition.py` — Theil_total = Theil_between + Theil_within
  - [ ] `tests/test_graph_construction.py` — symétrie, pas de self-loops
  - [ ] `tests/test_closeness_weights.py` — poids inversés avant calcul closeness
  - [ ] `tests/test_markov_transitions.py` — lignes de transition sommant à 1
  - [ ] `tests/test_moran_permutation.py` — distribution nulle centrée sur 0



### Issue #005 — Experiment tracking (`runs/`)
**Labels** : `infrastructure`, `code`, `difficulty: hard`
- **Contexte Analytique** : Traçabilité des explorations algorithmiques (spécialement pour HMM, Louvain, PELT).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité totale et transparence des essais.
- **Artefacts générés** : Système de logging opérationnel dans le dossier `runs/`.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Définir le format JSON des runs (git_hash, timestamp, config, metrics)
  - [ ] Script d'enregistrement automatique des runs


---

## 🗺️ TOME I — LA CARTE ET LE TERRITOIRE

### MILESTONE T1-INTRO — Pages liminaires & Introduction


### Issue #006 — Note éthique Tome I + Préface générale
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Cadrage de l'approche descriptive et statique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : On décrit des structures spatiales, on ne juge pas les politiques d'établissement. Focus sur les données cartographiques.
- **Artefacts générés** : Note éthique T1, Préface générale de la trilogie (8-12 pages), Avant-propos Tome I.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rédiger note éthique spécifique au Tome I (focus : données cartographiques et statistiques descriptives)
  - [ ] Rédiger préface générale de la trilogie (8–12 pages, version narrative du manifeste)
  - [ ] Rédiger avant-propos du Tome I (passage "classement → structure spatiale", guide de lecture)



### Issue #007 — Introduction générale : Le paradoxe de l'école républicaine
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Exposition du paradoxe central (égalité de droit / inégalité de fait spatialisée).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Présentation factuelle du corpus enrichi, de la méthode Ministère (IPS), justification des ajouts (σ, DVF).
- **Artefacts générés** : Texte de l'Introduction Générale.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : IPS vs capital culturel. Distinction entre statistiques et utilisation politique ou médiatique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Construction statistique de l'IPS (méthode Ministère)
  - Ce que l'IPS capture et ce qu'il efface
  - IPS et capital culturel : distinction bourdieusienne revisitée
  - Comparaison IPS vs revenus médians IRIS (corrélation forte mais imparfaite → effets institutionnels propres)
  - **Nouveauté** : encadré "peut-on corriger l'IPS ?" — indice composite IPS + σ + revenus IRIS
  - Code Python pour reproduire le calcul composite (annexe A5)
  - Encadré : "L'IPS peut-il être interprété abusivement ?institutionnellement ?" (formulation analytique stricte)
  - Encadré : différence IPS / taux de boursiers / PCS
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 1, Code Python (annexe A5).

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la matrice de corrélation statistique entre l'IPS et les revenus médians par IRIS.
  - [ ] Coder la fonction mathématique de l'indice composite (IPS + σ + revenus IRIS) et exporter les scores des lycées.



### Issue #009 — Chapitre 2 : L'écart-type, révélateur de mixité cachée
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : L'écart-type $\sigma$ (Modèle 1) comme mesure vitale de la diversité interne.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Homogénéité" est un fait statistique, pas un jugement moral sur la valeur des élèves ou le projet pédagogique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition statistique et interprétation sociologique de σ
  - Deux lycées même IPS, structures sociales opposées
  - σ comme mesure de diversité interne
  - Cas emblématiques : Saint-Jean de Passy (σ=15,7) vs Henri-IV (σ=32,4)
  - **Nouveauté** : corrélation σ × données DVF immobilières (test exploratoire)
  - Encadré : l'écart-type et la théorie de la ségrégation résidentielle
  - Tableau : top 20 lycées les plus homogènes / les plus hétérogènes
  - Cas emblématiques décrits comme "appartenant à des clusters de forte homogénéité" (note éthique)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 2, Tableaux du Top 20.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer l'écart-type de l'IPS pour chaque lycée afin d'estimer la mixité sociale interne.
  - [ ] Générer le tableau récapitulatif du Top 20 des lycées les plus homogènes et les plus hétérogènes.
  - [ ] Exécuter un test de corrélation exploratoire entre l'écart-type et les données immobilières DVF.



### Issue #010 — Chapitre 3 : Panorama du corpus enrichi
**Labels** : `chapitre`, `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Distribution statistique globale du système scolaire francilien.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mention des "absents du classement" (biais de sélection). Standard Nature/Science pour la Figure 2.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Distribution statistique : IPS, σ, répartition public/privé, géographie
  - Répartition par type (général, technologique, polyvalent, international)
  - Premières corrélations IPS / σ / statut / revenus IRIS / résultats bac
  - **Figure signature 2** : scatter IPS vs σ, couleurs public/privé, densité KDE, annotations, sous-panel DVF
  - Encadré "les absents du classement" (lycées populaires hors corpus, biais de sélection)
  - Script `figures/fig2_scatter_ips_sigma.py`
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 3, Figure Signature 2.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire la distribution statistique de l'IPS, de l'écart-type et de la répartition par secteur (public/privé).
  - [ ] Générer le "scatter plot" (Figure Signature 2) croisant IPS et écart-type, avec colorisation par statut et courbes de densité KDE.


---

### MILESTONE T1-P2 — Partie II : Géographie de l'inégalité


### Issue #011 — Chapitre 4 : La carte de l'élite scolaire francilienne
**Labels** : `chapitre`, `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Spatialisation de la performance (IPS) et des prix de l'immobilier (DVF).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Constat du "croissant de l'ouest" et des "déserts scolaires favorisés". Purement descriptif géographique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Villes surreprésentées : Paris, Neuilly, Versailles, Saint-Germain-en-Laye
  - Histoire du "croissant de l'ouest" (géographie et histoire)
  - Carte choroplèthe des IPS moyens par commune
  - **Nouveauté majeure** : corrélation IPS scolaire × prix DVF (€/m²)
  - Scatter plot IPS communal vs prix médian m²
  - Script `figures/fig1_map.py`
  - Encadré : les arrondissements parisiens (du 6e au 20e, gradient saisissant)
  - Les "déserts scolaires favorisés" : communes aisées sans lycée élite (analyse spécifique)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 4, Figure Signature 1.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la corrélation spatiale entre l'IPS moyen par commune et le prix médian au m² (DVF).
  - [ ] Générer la carte choroplèthe des IPS moyens par commune et le scatter plot correspondant.



### Issue #012 — Chapitre 5 : Les trois couronnes
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Mesurer l'effet pur de la géographie.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les trois couronnes sont-elles trois systèmes distincts ? La géographie explique-t-elle plus que le statut institutionnel ?
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Profil analytique de Paris (hétérogénéité maximale)
  - Profil de la petite couronne (compétition et polarisation)
  - Profil de la grande couronne (homogénéité relative)
  - **Nouveauté** : ANOVA spatiale (zone × statut × revenus IRIS)
  - Décomposition de variance : "géographie explique X%, statut Y%, revenus IRIS Z%"
  - Indice de dissimilarité de Duncan par commune
  - Tableau comparatif des trois zones avec toutes les variables
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 5, Résultats ANOVA.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Réaliser une ANOVA spatiale pour décomposer la variance selon 3 facteurs (zone géographique, statut public/privé, revenus IRIS).
  - [ ] Extraire les pourcentages de variance expliquée et dresser le tableau comparatif complet des trois couronnes.
  - [ ] Calculer l'indice de dissimilarité de Duncan pour chaque commune.



### Issue #013 — Chapitre 6 : La ségrégation invisible
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Le paradoxe de la commune "mixte" contenant des lycées "homogènes".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Fausse mixité" est un écart statistique, pas une accusation de volonté politique locale.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Le paradoxe de la mixité apparente
  - Mécanismes : carte scolaire, dérogations, filières sélectives, réputation
  - **Nouveauté** : indice de "fausse mixité" formalisé `F_c = M_global - M_interne`
  - Test exploratoire : accessibilité transport × niveau de ségrégation (données IDF Mobilités)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 6, Topologie des communes paradoxales.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la formule de l'indice de "fausse mixité" (F_c = M_global - M_interne) et générer les scores communaux.
  - [ ] Tester la corrélation statistique entre l'accessibilité aux transports (IDF Mobilités) et le niveau de ségrégation.



### Issue #014 — Chapitre 7 : Secteur public vs privé, géographie différenciée
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Effet de ségrégation institutionnelle spatialisée.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Analyse neutre de la répartition. Encadré sur le hors contrat comme terra incognita.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Répartition spatiale public/privé
  - Histoire du réseau catholique en Île-de-France
  - Polarisation Δ IPS public/privé par zone
  - **Nouveauté** : corrélation densité privé × prix DVF
  - Encadré : lycées hors contrat (terra incognita statistique)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 7.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la polarisation de l'IPS (delta public/privé) ventilée par zone géographique.
  - [ ] Tester statistiquement la corrélation entre la densité locale d'établissements privés et le prix immobilier (DVF).


---

### MILESTONE T1-P3 — Partie III : Sociologie des établissements


### Issue #015 — Note éthique renforcée Partie III
**Labels** : `ethique`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Préparation au clustering CAH (Création de typologies de lycées).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Un cluster statistique est un groupe mathématique, non une volonté délibérée d'exclusion. Les termes ("Aristocratie", etc.) sont des étiquettes typologiques.
- **Artefacts générés** : Note introductive de la Partie III.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rédiger la note d'ouverture de la Partie III (résultats d'une analyse statistique, aucun jugement sur pratiques internes)
  - [ ] Intégrer la note dans le texte principal



### Issue #016 — Chapitre 8 : L'aristocratie scolaire fermée (Cluster 1)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du premier cluster (IPS > 158, $\sigma$ < 20).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Indicateur de concentration sociale" jamais "ce lycée s'organise pour exclure". Effet systémique, pas intention.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition structurelle : IPS > 158, σ < 20, privé catholique
  - Profil sociologique : bourgeoisie patrimoniale, réseaux familiaux anciens
  - Établissements emblématiques : Saint-Jean de Passy, Saint-Dominique, Massillon, Saint-Louis de Gonzague
  - Score d'entre-soi composite (IPS/σ) : calcul et interprétation formelle
  - Logique de reproduction : de l'école au réseau des grandes écoles
  - Formulation éthique : "indicateur de concentration sociale" jamais "ce lycée s'organise pour exclure"
  - Logique de reproduction comme effet systémique (pas intention individuelle)
  - Encadré : les alumni et les réseaux professionnels
  - Encadré : le rôle des associations de parents d'élèves
  - Enrichissement résultats bac et valeur ajoutée → "paradoxe analytique" si applicable
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 8.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Isoler statistiquement le Cluster 1 (IPS > 158, écart-type < 20).
  - [ ] Calculer le score composite d'entre-soi pour ces établissements et exporter les statistiques descriptives.



### Issue #017 — Chapitre 9 : La grande bourgeoisie catholique élargie (Cluster 2)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du deuxième cluster (IPS 153-158, $\sigma$ 20-25).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Formulation statistique systématique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Profil : IPS 153-158, écart-type 20-25
  - Établissements : Sainte-Marie Neuilly, Notre-Dame du Grandchamp, Blanche de Castille, Madeleine Daniélou
  - Capital scolaire familial : professions libérales, cadres dirigeants
  - Le projet éducatif catholique : entre confessionnalité et excellence académique
  - Différences internes : établissements «vieille bourgeoisie» vs «nouvelle bourgeoisie»
  - Formulation éthique systématique : structures statistiques, pas intentions institutionnelles
  - Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 9.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire les statistiques descriptives du Cluster 2 sur l'ensemble du vecteur de variables (IPS, écart-type, DVF, IRIS, bac).
  - [ ] Générer la liste brute des lycées constituant ce cluster.



### Issue #018 — Chapitre 10 : Les élites académiques publiques (Cluster 3)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du cluster public méritocratique (IPS 145-153, $\sigma$ > 30).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La méritocratie républicaine en acte et le rôle des classes préparatoires (filtre secondaire).
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Profil paradoxal : IPS élevé (145-153), mais mixité forte (σ > 30)
  - Établissements : Henri-IV, Louis-le-Grand, Hoche, Lakanal, Fénelon, Blaise-Pascal
  - La méritocratie républicaine en acte
  - Présence de boursiers, recrutement académique national
  - L'effet réseau : concours d'entrée implicites, classes préparatoires
  - Écart-type comme indicateur de diversité réelle : qui sont les élèves ?
  - Encadré : les classes préparatoires comme filtre social secondaire
  - Enrichissement : valeur ajoutée IVAL — paradoxe analytique si applicable
  - Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 10.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire les statistiques descriptives complètes du Cluster 3 (IPS élevé, mixité forte).
  - [ ] Extraire la valeur ajoutée IVAL pour tester statistiquement la corrélation avec l'hétérogénéité sociale.



### Issue #019 — Chapitre 11 : Les privés intermédiaires ouverts (Cluster 4)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse du cluster hybride (IPS 145-152, $\sigma$ 28-32).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Constat d'ouverture relative.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Profil : IPS 145-152, écart-type 28-32
  - Établissements : Charles Péguy, Notre-Dame de la Providence, Rambam, Montalembert
  - Des établissements privés qui recrutent dans des milieux plus variés
  - Proximité avec les publics parisiens : un positionnement hybride
  - Hypothèses : localisation, tradition, offre pédagogique
  - Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 11.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire les statistiques descriptives complètes du Cluster 4 (IPS, σ, DVF, IRIS, résultats bac).
  - [ ] Générer la liste brute des établissements appartenant à ce cluster pour validation.



### Issue #020 — Chapitre 12 : Les élites internationales et scientifiques (Cluster 5)
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse de l'écologie scolaire singulière (ex: Saclay, Saint-Germain-en-Laye).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Position hors logique nationale classique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Établissements : École Jeannine Manuel, Lycée international de Saint-Germain-en-Laye, Lycée franco-allemand, Blaise-Pascal, Vallée de Chevreuse
  - Capital culturel mondialisé vs capital technoscientifique
  - Recrutement : expatriés, ingénieurs, chercheurs, hauts fonctionnaires internationaux
  - Position atypique dans le système : hors logique nationale classique
  - Encadré : le bassin de Paris-Saclay — une écologie scolaire singulière
  - Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 12.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Isoler les établissements internationaux et scientifiques (Cluster 5) et extraire leurs caractéristiques statistiques.
  - [ ] Produire le tableau récapitulatif des variables descriptives (IPS, σ, DVF, IRIS, résultats bac).



### Issue #021 — Chapitre 13 : Les lycées publics favorisés résidentiels
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Analyse des lycées de quartier aisés.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Synthèse neutre des 5 mondes scolaires.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Établissements : Lycée Alain, Louis de Broglie, La Bruyère, Louis Pasteur Neuilly
  - Profil : bons bassins résidentiels, public local favorisé
  - Mixité modérée, stabilité sociale
  - Rôle dans la hiérarchie locale : entre «lycée de quartier aisé» et «lycée d'excellence»
  - Comparaison avec Cluster 3 (public académique) et Cluster 1 (privé fermé)
  - Description analytique sur toutes les variables (IPS, σ, DVF, IRIS, résultats bac)
  - Carte spatiale des 5 clusters sur l'IDF + formulation éthique transversale
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 13, Carte spatiale IDF des 5 mondes.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire les statistiques descriptives des lycées publics favorisés résidentiels.
  - [ ] Générer la carte spatiale positionnant les 5 clusters sur la région Île-de-France.


---

### MILESTONE T1-P4 — Partie IV : Mesures de la ségrégation


### Issue #022 — Chapitre 14 : Construire un score d'entre-soi social
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 12. L'agrégation de l'IPS et de l'inverse de la dispersion.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Limites de l'indice brut précisées.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Indice IPS/σ : formule, calcul, interprétation sociologique.
  - - Top 20 lycées les plus «fermés» socialement — formulation éthique obligatoire.
  - - Top 20 lycées les plus «ouverts» relativement à leur niveau.
  - - Corrélation score d'entre-soi / secteur / géographie.
  - - Limites de l'indice brut.
  - - *V2* : indice normalisé par z-scores (IPS et inverse de σ). Carte spatiale IDF. Script Python annexe A5.

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 14, Script de calcul, Top 20 "Ouverts" / "Fermés".

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer les z-scores spatiaux (entre-soi) et générer la carte d'Île-de-France.
  - [ ] Exporter le script ainsi que le Top 20.

### Issue #023 — Chapitre 15 : L'indice de Gini des lycées franciliens
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 9. Gini de la distribution des IPS.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Application d'un standard mathématique universel.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Application de l'indice de Gini à la distribution des IPS en Île-de-France.
  - - Décomposition public/privé : Gini within (dans chaque secteur) et between (entre secteurs).
  - - Décomposition géographique (Paris/PC/GC). Courbe de Lorenz de l'IPS scolaire.
  - - *V2* : comparaison nationale (Lyon, Marseille si données disponibles).
  - - Encadré comparatif international court (Londres, Berlin) basé sur la littérature existante.

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 15, Courbe de Lorenz.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Décomposer mathématiquement la variance (secteur, géographie) et tracer la Courbe de Lorenz.
  - [ ] Livrer les graphiques formatés pour le Chapitre 15.

### Issue #024 — Chapitre 16 : L'indice de Theil : ségrégation décomposable
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 10. Indice d'entropie décomposable spatialement et institutionnellement.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Objectivation rigoureuse des parts de variance.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Formule et interprétation sociologique du Theil.
  - - Theil global francilien.
  - - Décomposition V1 : within zones / between zones / within lycées / between lycées.
  - - Theil public vs privé.
  - - Quelle dimension explique le plus d'inégalité ? Tableau synthétique de décomposition.
  - - *V2* : décomposition supplémentaire avec revenus IRIS (troisième niveau d'analyse).
  - - Test unitaire `test_theil_decomposition.py` : Theil_total = Theil_between + Theil_within.

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 16, Tableau de décomposition de variance.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer l'indice de Theil aux trois niveaux géographiques et institutionnels.
  - [ ] Dresser le tableau complet de décomposition de la variance pour le Chapitre 16.

### Issue #025 — Chapitre 17 : L'indice de dissimilarité spatial (Duncan D)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 11. Dissimilarité entre "classes favorisées" et "classes populaires" par commune.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mise en évidence des paradoxes locaux.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Duncan D par ville. Carte choroplèthe de D en Île-de-France.
  - - Corrélation D / richesse communale (V1).
  - - Les villes les plus ségrégées entre public et privé.
  - - Les villes les moins ségrégées : que nous apprennent-elles ? (V1)
  - - *V2* : corrélation D × accessibilité transport (temps de trajet gares/RER).

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 17, Carte choroplèthe de $D$.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer l'indice de dissimilarité de Duncan (D) et tester la corrélation avec les transports/revenus.
  - [ ] Produire la carte choroplèthe finale pour le Chapitre 17.

### Issue #026 — Chapitre 18 : L'indice global de fragmentation scolaire (IFC)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Agrégation de Theil, ANOVA, Gini et polarisation.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le système est "multi-dimensionnellement structuré".
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Construction d'un indice composite : Theil + ANOVA + polarisation + hétérogénéité.
  - - Calcul et résultat pour l'Île-de-France.
  - - Contribution relative de chaque composante (V1).
  - - Comparaison avec d'autres régions françaises / si données disponibles (Lyon, Marseille, Bordeaux).
  - - Interprétation V1 : système «modérément fragmenté» mais «multi-dimensionnellement structuré».

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 18.

---

### MILESTONE T1-P5 — Partie V : Décomposition de variance

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Établir la formule de l'indice composite de fragmentation scolaire et pondérer ses composantes.
  - [ ] Consolider les résultats statistiques pour le Chapitre 18.

### Issue #027 — Chapitre 19 : ANOVA simple : public/privé explique-t-il tout ?
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Isolation du facteur "Statut".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Formulation prudente (Associations fortes $\neq$ mécanismes causaux).
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Modèle ANOVA unidimensionnel : IPS ~ secteur (public/privé)
  - Résultat V1 : 35-45% de variance expliquée par le statut
  - Ce que le résidu nous dit (V1)
  - Limites de l'ANOVA simple appliquée à des données scolaires
  - Formulation prudente systématique : associations fortes ≠ mécanismes causaux
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 19.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Modéliser une ANOVA unidimensionnelle (IPS en fonction du statut public/privé).
  - [ ] Extraire le pourcentage de variance expliquée (R²) et générer le tableau des résidus statistiques.



### Issue #028 — Chapitre 20 : ANOVA multi-facteurs
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle complet (Statut + Géographie + Type de lycée).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Démontrer que la géographie domine et le statut amplifie.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Modèle complet V1 : public/privé + zone + type de lycée + interactions.
  - - Interactions significatives V1 : privé × ouest parisien, scientifique × Saclay.
  - - Hiérarchie des facteurs : géographie domine, statut amplifie (V1).
  - - Tableau de décomposition V1.
  - - *V2* : intégration variables DVF + accessibilité transport. Comparaison modèle simple vs modèle complet : gain de variance expliquée.

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 20, Tableau de décomposition complet.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Exécuter les régressions OLS multi-facteurs (interactions privé/géographie) et tester les variables DVF/transports.
  - [ ] Exporter le tableau de décomposition complet pour le Chapitre 20.

### Issue #029 — Chapitre 21 : Le modèle multiniveau (HLM)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 14. Structure imbriquée (Lycée $\to$ Ville $\to$ Zone).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Postulat validé analytiquement : "La géographie structure, l'institution filtre".
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Structure imbriquée : lycée → ville → zone (V1).
  - - ICC par niveau (V1).
  - - Part de variance expliquée par le contexte spatial.
  - - Résultat central V1 : *«la géographie structure, l'institution filtre»*.
  - - R² marginal vs R² conditionnel.
  - - Encadré V1 : effets fixes vs effets aléatoires dans l'analyse scolaire.
  - - *V2* : covariables niveau 2 enrichies : revenus médians IRIS, prix DVF, accessibilité transport.

- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 21, Sorties du modèle.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Estimer les ICC (Intraclass Correlation Coefficients) et comparer les R² marginaux et conditionnels.
  - [ ] Extraire les sorties du modèle multiniveau pour le Chapitre 21.

### Issue #030 — Chapitre 22 : Vers un modèle causal : DAG statique
**Labels** : `chapitre`, `documentation`, `exploratory`, `difficulty: low`
- **Contexte Analytique** : Modèle 15. Directed Acyclic Graph des déterminants de l'IPS.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le DAG est une hypothèse formelle, pas une vérité révélée infaillible.
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 22, Schéma du DAG.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Construire formellement le réseau causal (DAG) et simuler l'effet d'une intervention par "do-calculus".
  - [ ] Exporter le schéma du DAG pour le Chapitre 22.

### Issue #031 — Conclusion du Tome I
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Clôture du Tome I (La Carte et le Territoire).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Invitation à réfléchir aux politiques.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Synthèse des structures identifiées. Ce que la carte et le classement cachent.
  - - Limites de l'approche statique → transition vers le Tome II.
  - - Position de l'IDF dans un contexte comparatif (2–3 pages, littérature existante).
  - - Encadré : données disponibles, données manquantes, ce qui serait nécessaire.

- **Artefacts générés** : Conclusion du Tome 1.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Synthétiser les découvertes majeures et les limites de la première partie.
  - [ ] Rédiger le texte de la Conclusion du Tome 1.

### Issue #032 — Annexe A1 : Tableau complet des lycées
**Labels** : `annexe`, `data`, `difficulty: medium`
- **Contexte Analytique** : Données brutes transparentes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Tableau complet lycées (IPS, σ, secteur, ville, score entre-soi, revenus IRIS, résultats bac)

- **Artefacts générés** : Annexe A1.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Exporter les données nettoyées des lycées au format CSV.
  - [ ] Intégrer cet export pour constituer le Tableau complet de l'Annexe A1.

### Issue #033 — Annexe A2 : Sources de données complètes + licences
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Traçabilité des sources.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Sources de données complètes (data.gouv.fr, INSEE, DVF Etalab, IDF Mobilités, IGN) + licences

- **Artefacts générés** : Annexe A2.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Dresser l'inventaire exhaustif des jeux de données mobilisés.
  - [ ] Présenter ces métadonnées proprement dans l'Annexe A2.

### Issue #034 — Annexe A3 : Méthode de calcul de tous les indices
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Mathématiques appliquées.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Méthode de calcul de tous les indices (Gini, Theil, Duncan, IFC, score d'entre-soi)

- **Artefacts générés** : Annexe A3.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Convertir la documentation mathématique au format LaTeX.
  - [ ] Compiler ces équations pour constituer l'Annexe A3.

### Issue #035 — Annexe A4 : Note sur les licences Open Data
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Cadre légal.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Respect du droit.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Note sur les licences Open Data (Etalab, Open Data Commons, conditions réutilisation)

- **Artefacts générés** : Annexe A4.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Recenser les contraintes légales et licences Open Data des jeux de données.
  - [ ] Rédiger la note juridique correspondante pour l'Annexe A4.

### Issue #036 — Annexe A5 : Code Python reproductible complet
**Labels** : `annexe`, `code`, `difficulty: medium`
- **Contexte Analytique** : Reproductibilité absolue.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Code Python reproductible + lien GitHub

- **Artefacts générés** : Annexe A5.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rassembler les scripts de nettoyage et de modélisation du Tome 1.
  - [ ] Structurer ce dépôt de code pour l'Annexe A5.

### Issue #037 — Annexe A6 : Cartographie complète
**Labels** : `annexe`, `figure`, `difficulty: low`
- **Contexte Analytique** : Visualisation étendue.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Cartographie complète

- **Artefacts générés** : Annexe A6.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Regrouper les cartes exploratoires non incluses dans les chapitres principaux.
  - [ ] Exporter l'atlas cartographique additionnel pour l'Annexe A6.

### Issue #038 — Annexe A7 : Glossaire des termes statistiques et sociologiques
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Pédagogie conceptuelle.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Glossaire des termes statistiques et sociologiques

- **Artefacts générés** : Annexe A7.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Compiler les définitions des termes sociologiques et statistiques utilisés.
  - [ ] Rédiger le glossaire complet pour l'Annexe A7.

### Issue #039 — Annexe A8 : Bibliographie sélective
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Ancrage académique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Humilité scientifique.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Bibliographie sélective (sociologie éducation, géographie sociale, ségrégation urbaine)

- **Artefacts générés** : Annexe A8.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Vérifier la mise en forme des références académiques citées dans le texte.
  - [ ] Exporter la bibliographie sélective pour l'Annexe A8.

### Issue #040 — Annexe A9 : Comparaison internationale courte
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Mise en perspective.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité géographique.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Comparaison internationale courte (tableau synthétique, 5–6 métropoles)

- **Artefacts générés** : Annexe A9.

## 🕸️ TOME II — LES RÉSEAUX ET LES MONDES

### MILESTONE T2-INTRO — Pages liminaires & Introduction

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Réaliser une courte synthèse des travaux comparables à l'étranger.
  - [ ] Rédiger cette note de mise en perspective pour l'Annexe A9.

### Issue #041 — Note éthique Tome II + Avant-propos
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Le Tome II introduit la similarité et la théorie des graphes. Il faut s'assurer que "proximité mathématique" ne soit pas confondue avec "entente institutionnelle".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La position dans le réseau est une propriété émergente, pas une caractéristique intrinsèque (anti-essentialisme).
- **Artefacts générés** : Avant-propos du Tome II et Note éthique d'ouverture.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Note éthique Tome II (position dans le réseau = propriété émergente, pas caractéristique intrinsèque)
  - [ ] Avant-propos : "du territoire au réseau" — formulation obligatoire sur les liens de similarité vs flux réels
  - [ ] Introduction : nœuds, liens, poids — justification de la fonction de similarité choisie vs alternatives (Jaccard, cosinus)


---

### MILESTONE T2-P1 — Partie I : Topologie du système


### Issue #042 — Chapitre 1 : La CAH comme outil de sociologie scolaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Classification Ascendante Hiérarchique pour diviser l'espace social continu en mondes discrets.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La CAH est un algorithme, pas une vérité absolue.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Rappel : Classification Ascendante Hiérarchique (méthode de Ward)
  - Distance euclidienne vs distance de Mahalanobis
  - Normalisation des variables : pourquoi les z-scores sont essentiels
  - Choix du nombre de clusters : silhouette, gap statistic, critère de Mojena
  - Résultats V1 : structure en 4-6 clusters stables pour les lycées franciliens
  - Comparaison CAH / k-means / GMM : convergences et divergences
  - **V2** : clustering sur vecteur enrichi (IPS + σ + revenus IRIS + résultats bac + statut)
  - **V2** : comparaison IPS seul vs vecteur enrichi
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 1.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Implémenter la Classification Ascendante Hiérarchique (CAH) avec la méthode de Ward et normalisation en z-scores.
  - [ ] Comparer statistiquement les résultats de la CAH avec l'algorithme k-means et un modèle GMM.
  - [ ] Exécuter le clustering (V2) sur le vecteur enrichi (IPS, écart-type, revenus IRIS, résultats bac, statut).



### Issue #043 — Chapitre 2 : Le dendrogramme comme arbre social
**Labels** : `chapitre`, `figure`, `difficulty: low`
- **Contexte Analytique** : Interprétation de la structure arborescente (Modèle 16).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le dendrogramme n'est pas une hiérarchie de valeur, c'est une mesure de distance.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Lecture sociologique du dendrogramme
  - Premier split V1 : homogénéité vs hétérogénéité comme séparation fondamentale
  - Lecture des branches V1 : privé élitiste / public académique / internationaux / scientifiques
  - Hauteurs de fusion comme «ruptures de mondes scolaires» (V1)
  - Le critère de Mojena : détecter les sauts naturels
  - Profondeur ultramétrique V1 : un indice de hiérarchisation sociale
  - **V2** : revenus IRIS ou résultats bac créent-ils une nouvelle dimension de séparation ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 2, Figure du Dendrogramme.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Générer le dendrogramme complet de la CAH et calculer les hauteurs de fusion.
  - [ ] Appliquer le critère de Mojena pour détecter mathématiquement les sauts de clusters optimaux.
  - [ ] Calculer la profondeur ultramétrique du graphe.



### Issue #044 — Chapitre 3 : Cinq clusters, cinq mondes scolaires
**Labels** : `chapitre`, `figure`, `difficulty: low`
- **Contexte Analytique** : Profilage statistique des 5 mondes isolés.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les descriptions (Aristocratie, Élites académiques, etc.) doivent rester neutres et statistiques.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Cluster 1 : Aristocratie scolaire fermée (privé ouest, IPS > 158, σ < 20)
  - Cluster 2 : Grande bourgeoisie catholique élargie (privé, IPS 153-158, σ 20-25)
  - Cluster 3 : Élites académiques publiques (public, IPS 145-153, σ 27-34)
  - Cluster 4 : Privés urbains mixtes (privé, IPS 145-150, σ 28-32)
  - Cluster 5 : Systèmes internationaux et scientifiques (hors modèle national)
  - Tableau de description de chaque cluster. Carte spatiale des clusters sur l'IDF.
  - Formulation éthique systématique pour chaque cluster
  - **V2** : description analytique enrichie sur toutes les variables (DVF, IRIS, bac)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 3.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire les tableaux de description statistique pour les 5 clusters validés.
  - [ ] Générer la carte spatiale positionnant les clusters sur la carte d'Île-de-France.



### Issue #045 — Chapitre 4 : Validation statistique des clusters
**Labels** : `chapitre`, `code`, `validation`, `difficulty: medium`
- **Contexte Analytique** : Les clusters existent-ils vraiment ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Traitement transparent des cas ambigus (lycées aux frontières).
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Silhouette score : cohérence interne des clusters
  - Gap statistic : les clusters existent-ils vraiment ?
  - Stabilité bootstrap (ARI) n=1000 : les clusters survivent-ils à la perturbation ?
  - Séparation statistique : ANOVA post-hoc sur IPS et σ
  - Score de validation global : k optimal consensuel
  - Zones de désaccord entre méthodes : les cas ambigus
  - **V2** : test de robustesse avec sous-échantillons aléatoires (enlever 10% des données)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 4, Rapport de validation.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer le silhouette score et la "gap statistic" pour valider la robustesse des clusters.
  - [ ] Exécuter un test de stabilité bootstrap (Adjusted Rand Index) sur 1000 itérations.
  - [ ] Réaliser une ANOVA post-hoc sur l'IPS et l'écart-type pour valider la séparation statistique.



### Issue #046 — Chapitre 5 : L'ultramétrie
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 32. Le système est-il une hiérarchie parfaite ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : L'ultramétrie mesure la rigidité du tri social.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Propriété ultramétrique : définition formelle
  - Distance cophenétique et corrélation ultramétrique
  - Score de validité ultramétrique : le système est-il vraiment hiérarchique ?
  - «Ponts ultramétriques» V1 : liens qui violent la hiérarchie
  - Signification sociologique : où la logique de classe éclate ?
  - Indice de cohérence arbre/réseau (ARI CAH vs Louvain)
  - Note de prudence : outil descriptif, pas preuve d'une logique nécessaire
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 5.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la distance cophenétique et la corrélation ultramétrique du système.
  - [ ] Extraire les "ponts ultramétriques" (liens violant la hiérarchie).
  - [ ] Calculer l'Adjusted Rand Index pour évaluer la cohérence entre l'arbre (CAH) et le réseau (Louvain).



### Issue #047 — Chapitre 6 : Détection de communautés Louvain
**Labels** : `chapitre`, `code`, `validation`, `difficulty: medium`
- **Contexte Analytique** : Différence entre hiérarchie (CAH) et communautés (Louvain).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Révèle des zones de tension structurelle.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Principe : maximisation de la modularité Q
  - Différence conceptuelle entre cluster CAH et communauté Louvain
  - Résultats V1 : 4-6 communautés naturelles. Comparaison avec la CAH (ARI, NMI)
  - Ce que la divergence CAH/Louvain révèle : zones de tension structurelle
  - Hiérarchie de Louvain : super-communautés et micro-communautés
  - **V2** : réseau sur IPS seul vs réseau sur vecteur enrichi — comparaison ARI
  - Test de sensibilité résolution : `for r in [0.5, 1.0, 1.5, 2.0]`
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 6.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Implémenter la détection de communautés avec l'algorithme de Louvain en maximisant la modularité (Q).
  - [ ] Comparer les communautés Louvain avec les clusters CAH (via les métriques ARI et NMI).
  - [ ] Exécuter un test de sensibilité en modifiant la résolution de Louvain (0.5, 1.0, 1.5, 2.0).



### Issue #048 — Chapitre 7 : Louvain multi-couches (multiplex)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Analyse du réseau sur plusieurs strates (social, spatial, académique).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Identification des corridors de lycéens entre mondes.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Principe du réseau multiplex (V1)
  - Construction des trois couches de liens (public, privé, international)
  - **V2** : quatrième couche de proximité géographique (distance GPS réelle)
  - Détection de communautés transversales. Blocs «purs» vs blocs hybrides
  - Corridors entre couches : qui traverse les mondes ?
  - Indice de fragmentation inter-couches (IFC) par couche
  - Les divergences topologique/géographique révèlent des effets institutionnels
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 7.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Construire un réseau multiplex (multicouches) intégrant les flux, le statut et la distance géographique (GPS).
  - [ ] Détecter les communautés transversales et extraire la liste des corridors inter-couches.
  - [ ] Calculer l'indice de fragmentation inter-couches (IFC) par couche.


---

### MILESTONE T2-P2 — Partie II : Réseau de flux et mobilité


### Issue #049 — Chapitre 8 : Construire un réseau de similarité
**Labels** : `chapitre`, `code`, `validation`, `difficulty: medium`
- **Contexte Analytique** : Construction du Graphe de Similarité $W_{ij}$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Ce n'est pas un flux physique réel, mais un réseau de potentiel compétitif.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Matrice de distances (euclidienne, Mahalanobis). Fonction de similarité exponentielle.
  - Seuillage : densité du réseau vs signal/bruit. Propriétés topologiques.
  - Visualisation : spring layout, force-directed graph
  - **V2** : comparaison avec modèle nul Erdős–Rényi (même densité). Test de significativité de la modularité.
  - Test de sensibilité seuil : `for p in [60, 65, 70, 75, 80]`
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 8, Matrice d'Adjacence.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Construire la matrice de distances (Mahalanobis et Euclidienne) et seuiller le réseau.
  - [ ] Modéliser un réseau nul d'Erdős–Rényi de même densité pour tester la significativité statistique de la modularité.
  - [ ] Générer la visualisation du graphe avec l'algorithme Force-Directed (Spring Layout).



### Issue #050 — Chapitre 9 : Centralité
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèles 21 & 22. Qui détient l'influence structurelle ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Position mathématique, pas jugement qualitatif.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Degré pondéré. Betweenness centrality : les ponts structurels.
  - Closeness centrality (⚠️ poids inversés : `distance = 1/(weight + 1e-6)`)
  - Eigenvector centrality : les hubs d'influence
  - Top 10 lycées par centralité composite (V1)
  - Carte du réseau avec centralité codée visuellement (V1)
  - **V2** : corrélation centralité × résultats bac × revenus IRIS
  - Script `figures/fig3_network_louvain.py`
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 9.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer les indices de centralité : Eigenvector centrality, Betweenness, et Degré pondéré.
  - [ ] Générer le Top 10 des lycées selon un score composite de centralité.
  - [ ] Produire la visualisation du graphe avec colorisation des nœuds par centralité.



### Issue #051 — Chapitre 10 : Les ponts entre mondes scolaires
**Labels** : `chapitre`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Lycées situés à l'intersection des clusters sociaux.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Un "pont" n'est pas un lycée qui fait consciemment des efforts d'inclusion.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition opérationnelle du pont (V1)
  - Score de pont composite V1 : betweenness + diversité communautaire + distance ultramétrique
  - Top ponts du système francilien V1 : Lakanal, Hoche, Louis-le-Grand, Henri-IV
  - Lycées frontières entre public d'élite et privé bourgeois
  - Lycées frontières entre monde national et monde international
  - Signification sociologique : institutions qui limitent la fragmentation
  - Note éthique : «ponts analytiques» ≠ pratiques d'admission ou ouverture institutionnelle
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 10.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la formule du score de "pont" composite (betweenness + diversité communautaire + distance ultramétrique).
  - [ ] Extraire le Top 10 des lycées franchissant les frontières (ponts structurels).



### Issue #052 — Chapitre 11 : Flux de mobilité, matrice de Markov
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 24. Mobilité aléatoire simulée.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Pure simulation probabiliste.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Matrice de transition entre clusters
  - Probabilités de mobilité ascendante / descendante
  - Distribution stationnaire : à quel équilibre tend le système ?
  - Entropie des trajectoires. Durée moyenne dans un cluster (V1)
  - Clusters «pièges» vs clusters «passerelles» (V1)
  - Note de prudence : matrice simulée ≠ matrice observée (sauf données Affelnet)
  - **V2** : calibration partielle avec données Affelnet si disponibles, mesure de l'écart simulé/observé
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 11.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Générer la matrice de transition (Markov) entre les différents clusters.
  - [ ] Estimer mathématiquement la distribution stationnaire du système (équilibre asymptotique).
  - [ ] Calculer l'entropie des trajectoires et la durée de séjour moyenne dans chaque cluster.



### Issue #053 — Chapitre 12 : Corridors sociaux : définition et détection
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Détection des autoroutes sociales.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les chemins par défaut du système.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Flux observé vs flux attendu (modèle nul d'indépendance)
  - Score de corridor R_ab = F_ab / E_ab
  - Corridors actifs : sur-représentation des transitions. Corridors symétriques vs asymétriques (indice Γ)
  - Top corridors du système francilien — les «autoroutes sociales»
  - Signification V1 : formalisation des «autoroutes sociales» du système scolaire
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 12.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer les flux attendus via un modèle nul d'indépendance et générer les scores de corridor (R_ab = F_ab / E_ab).
  - [ ] Identifier statistiquement les corridors sur-représentés (autoroutes sociales) et extraire l'indice d'asymétrie Γ.



### Issue #054 — Chapitre 13 : Ascenseurs sociaux vs filtres
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Distinction de l'efficacité verticale des corridors.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Termes d'ingénierie socio-physique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition formelle de l'ascenseur (flux ascendant + gradient positif)
  - Définition formelle du filtre (flux descendant + tri social)
  - Corridors ambigus : flux fort mais gradient neutre
  - Distribution spatiale des ascenseurs et filtres. Efficacité des ascenseurs : Δ S moyen (V1)
  - Encadré V1 : les corridors d'élite vs corridors de mobilité sociale descendante
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 13.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder les requêtes d'extraction pour isoler les flux ascendants (ascenseurs) et les flux descendants (filtres).
  - [ ] Calculer l'efficacité moyenne des ascenseurs (ΔS moyen) et générer la distribution spatiale.



### Issue #055 — Chapitre 14 : Réseau multiplex et analyse multi-couches
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Synthèse de la centralité inter-couches.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutre.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Superposition des couches V1 : social, académique, résidentiel, flux
  - Centralité de chaque couche. Score inter-couches : qui est central dans toutes les couches ?
  - Indice de fragmentation inter-couches (IFC)
  - Symétrie / asymétrie des flux selon les couches
  - Corrélation entre couches : où les logiques se renforcent-elles ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 14.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Fusionner mathématiquement les différentes couches du réseau multiplex (social, académique, résidentiel).
  - [ ] Calculer le score de centralité inter-couches et tester les corrélations de flux entre les dimensions.


---

### MILESTONE T2-P3 — Partie III : Structures cachées


### Issue #056 — Chapitre 15 : Distance de Mahalanobis
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Détection des anomalies.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Anomalie" = exception statistique pure.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Top outliers Mahalanobis, ellipses de confiance
  - **Nouveauté** : outliers Mahalanobis vs valeur ajoutée bac atypique (croisement analytique)
  - "Paradoxes analytiques" traités sans jugement
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 15, Liste des 50 outliers.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la distance de Mahalanobis pour l'ensemble du jeu de données et extraire les "outliers" (anomalies statistiques).
  - [ ] Croiser les valeurs atypiques de Mahalanobis avec les résultats inattendus de valeur ajoutée (IVAL).



### Issue #057 — Chapitre 16 : Les zones de bascule
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Lycées à la lisière des inversions de gradients.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Structure analytique émergente, pas réalité empirique stricte.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Gradient local des effets, détection des inversions de gradient
  - Note obligatoire : zones de bascule = structures analytiques émergentes du modèle, pas réalité empirique directe
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 16.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Détecter algorithmiquement les inversions de gradient spatial et extraire les coordonnées des "zones de bascule".
  - [ ] Générer la carte thermique localisant ces points critiques.



### Issue #058 — Chapitre 17 : Résidus structurels (SAR + Moran)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèles 26 & 27. Là où la géographie ne suffit plus à expliquer.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cartographie des ignorances du modèle.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Modèle SAR de base, calcul des résidus, autocorrélation Moran
  - Score de "blind spot" spatial
  - **Nouveauté** : corrélation résidus × accessibilité transport
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 17, Carte LISA.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Modéliser le système via un Spatial Autoregressive Model (SAR) et calculer l'autocorrélation de Moran.
  - [ ] Extraire les résidus du modèle pour identifier les "blind spots" spatiaux.
  - [ ] Tester la corrélation des résidus avec les données d'accessibilité aux transports.



### Issue #059 — Chapitre 18 : Classes latentes — les mondes scolaires cachés
**Labels** : `chapitre`, `code`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle GMM (Gaussian Mixture Model).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Révèle la porosité des mondes.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Modèle GMM (Gaussian Mixture Model)
  - Latent Class Mixed Model
  - 5 classes latentes détectées — description profils statistiques et sociologiques
  - Zones d'incertitude : établissements multi-appartenance
  - Entropie locale : carte des zones hybrides
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 18.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Entraîner un modèle GMM (Gaussian Mixture Model) et un Latent Class Mixed Model pour extraire 5 classes latentes.
  - [ ] Calculer l'entropie locale de chaque lycée pour quantifier l'incertitude d'appartenance et cartographier les zones hybrides.



### Issue #060 — Chapitre 19 : Frontières sociales floues — le gradient KDE
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Mesure de l'entropie des frontières.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Épaisseur" des frontières.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - KDE par cluster, probabilités locales d'appartenance
  - Entropie locale H(x) comme mesure de flou
  - Gradient de transition : là où les mondes se mélangent
  - «Épaisseur» des frontières scolaires (concept central)
  - Indice global de flou des frontières F
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 19.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Estimer les probabilités locales d'appartenance aux clusters via KDE (Kernel Density Estimation).
  - [ ] Calculer l'indice d'entropie locale H(x) et générer l'indice global de flou des frontières (F).



### Issue #061 — Chapitre 20 : Tension hiérarchie/réseau — points de bascule ultramétriques
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : L'écart entre distance en graphe et distance en arbre.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Où la mobilité échappe à la hiérarchie ?
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Mesure de la tension : |d_ij - d^U_ij| × w_ij
  - Lycées «contradictoires» : proches dans le réseau, éloignés dans l'arbre
  - Score de désalignement par lycée
  - Indice global DA : cohérence arbre/réseau
  - Cartographie des points de bascule
  - Signification : là où la mobilité scolaire échappe à la hiérarchie
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 20.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer le score de tension hiérarchie/réseau (|d_ij - d^U_ij| × w_ij) pour repérer les anomalies topologiques.
  - [ ] Générer l'indice global DA (désalignement) et cartographier les points de bascule ultramétriques.


---

### MILESTONE T2-P4 — Partie IV : Fragmentation et mobilité avancées


### Issue #062 — Chapitre 21 : Pression Ségrégative Locale (PSL)
**Labels** : `chapitre`, `code`, `figure`, `difficulty: low`
- **Contexte Analytique** : Mise à jour avec réseau de flux.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cartographie d'intensité.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Score PSL enrichi avec nouvelles variables
  - Carte PSL sur l'IDF
  - **Nouveauté** : corrélation PSL × accessibilité transport
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 21, Carte PSL.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder le calcul de la Pression Ségrégative Locale (PSL) intégrée aux variables DVF et IRIS.
  - [ ] Générer la carte spatiale de la PSL et tester sa corrélation avec l'accessibilité transport.



### Issue #063 — Chapitre 22 : Indice de fragmentation inter-couches (IFC)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Synthèse finale.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le système d'Île-de-France analysé sous son pire angle.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Formule et interprétation
  - Décomposition : IFC public/privé + IPS + géographie
  - IFC par zone (Paris, PC, GC)
  - Indice de mobilité M = 1 - IFC
  - Asymétrie des flux : déséquilibres de mobilité
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 22.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la fonction de décomposition de l'Indice de Fragmentation Inter-couches (IFC).
  - [ ] Exporter les matrices d'asymétrie des flux et calculer l'indice de mobilité (M = 1 - IFC).



### Issue #064 — Chapitre 23 : Perméabilité structurelle — un optimum existe-t-il ?
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modélisation des déséquilibres structurels "trop ouvert" vs "trop fermé".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le coût structurel d'une mixité forcée sans préparation.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition de la perméabilité (flux × distance hiérarchique)
  - Trop fermé vs trop ouvert : les deux déséquilibres structurels du système
  - Coût structurel : désorganisation par excès de mixité forcée
  - Indice Π = P_raw / C
  - Perméabilité locale par lycée
  - Lycées «passerelles» vs lycées «verrous»
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 23.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la boucle de calcul estimant l'indice de perméabilité (Π = P_raw / C) pour chaque lycée.
  - [ ] Générer les graphiques de distribution permettant d'isoler statistiquement les "passerelles" (ultra-ouverts) et les "verrous" (ultra-fermés).



### Issue #065 — Chapitre 24 : Clusters absorbants et attracteurs dynamiques
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Détection des "trous noirs" scolaires.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Démontre la captation des ressources scolaires de la région par des bastions spécifiques.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition : flux entrants >> flux sortants
  - Score d'absorption A_k = In_k / Out_k
  - Condition spectrale d'attracteur : ρ(T_Ck) > 1
  - Top clusters absorbants de l'Île-de-France
  - Signification : «puits scolaires» et accumulation des ressources
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 24, Top clusters absorbants.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder le score d'absorption des clusters (Flux_IN / Flux_OUT).
  - [ ] Valider la condition spectrale (ρ(T_C) > 1) pour identifier les attracteurs dynamiques (puits scolaires).


---

### MILESTONE T2-P5 — Partie V : Spatial et causal


### Issue #066 — Chapitre 25 : Modèle SAR
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Extension spatiale stricte.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Associations spatiales $\neq$ effets causaux.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - SAR avec covariables enrichies (revenus IRIS, DVF, accessibilité)
  - Estimation de ρ, effets directs vs indirects spatiaux
  - Note obligatoire : associations spatiales ≠ effets causaux
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 25.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Entraîner le modèle SAR en incluant les covariables (DVF, revenus IRIS, accessibilité).
  - [ ] Extraire et décomposer les effets spatiaux directs et indirects pour évaluation.



### Issue #067 — Chapitre 26 : Modèle SEM spatial
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle structurel avec variables latentes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Purement exploratoire.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Variables latentes enrichies, R²m vs R²c
  - **Nouveauté** : DVF et accessibilité transport ajoutent-ils du pouvoir explicatif au-delà de l'IPS et IRIS ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 26.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Entraîner le modèle SEM spatial en incluant les variables enrichies (DVF, accessibilité transport).
  - [ ] Extraire et comparer les métriques d'évaluation du modèle (R² marginal vs R² conditionnel).



### Issue #068 — Chapitre 27 : GAM non-linéaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les effets ne sont pas droits (splines).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Associations non-linéaires.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - GAM avec variables enrichies, effets par splines
  - Note de prudence renforcée : associations non linéaires ≠ identification causale
  - Zones de gradient positif vs négatif, tipping points analytiques
  - ⚠️ Random Forest spatial → `/exploratory/` (pas dans le texte principal)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 27.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Entraîner un modèle additif généralisé (GAM) non-linéaire avec splines sur les variables enrichies.
  - [ ] Extraire les points d'inflexion (tipping points analytiques) et générer les graphiques d'effets marginaux.



### Issue #069 — Chapitre 28 : Décomposition des effets indirects
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Effet de quartier vs Effet de réseau.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutre.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Effet quartier vs effet réseau
  - Variance quartier / variance réseau
  - **Nouveauté** : l'accessibilité transport modifie-t-elle cet équilibre ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 28.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la décomposition mathématique de la variance pour séparer l'effet "quartier" de l'effet "réseau".
  - [ ] Tester statistiquement si l'intégration de la variable "accessibilité transport" modifie cet équilibre.



### Issue #070 — Conclusion Tome II
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Fin du Tome II.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transition vers le Tome III.
- **Synopsis du Chapitre (Réflexions de l'Auteur) :**
  - - Des structures cachées à la structure réelle. Ce que le réseau révèle que le territoire ne montrait pas.
  - - Les 5 lycées les plus structurants selon la centralité composite.
  - - Comparaison internationale courte : réseaux scolaires de Londres et New York (littérature existante).
  - - Transition vers le Tome III.

- **Artefacts générés** : Conclusion du Tome 2.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Synthétiser les apports et limites des modèles spatiaux développés.
  - [ ] Rédiger le texte de la Conclusion du Tome 2.

### Issue #071 — Annexe A1 : Code Python complet
**Labels** : `annexe`, `code`, `difficulty: medium`
- **Contexte Analytique** : Reproductibilité.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Code Python complet (CAH, Louvain, réseau, SAR, GAM, toutes les figures) + lien GitHub

- **Artefacts générés** : Annexe A1.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rassembler les scripts générant les clusters et les réseaux.
  - [ ] Structurer ce code Python pour l'Annexe A1 du Tome 2.

### Issue #072 — Annexe A2 : Matrices de distance, similarité, flux
**Labels** : `annexe`, `data`, `difficulty: medium`
- **Contexte Analytique** : Données brutes réseau.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Matrices de distance, similarité, flux simulés et flux observés (Affelnet partiels)

- **Artefacts générés** : Annexe A2.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Exporter les matrices mathématiques (distance, flux) sous format lisible (JSON/CSV).
  - [ ] Mettre à disposition ces jeux de données via l'Annexe A2.

### Issue #073 — Annexe A3 : Tableau comparatif méthodes de clustering
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Choix algorithmiques.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur scientifique.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Tableau comparatif méthodes de clustering sur le dataset enrichi

- **Artefacts générés** : Annexe A3.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rassembler les différents benchmarks de vitesse et de performance algorithmique.
  - [ ] Dresser le tableau comparatif final dans l'Annexe A3.

### Issue #074 — Annexe A4 : Résultats complets des modèles
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Inférence.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Résultats complets des modèles statistiques

- **Artefacts générés** : Annexe A4.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Compiler les logs et les résultats statistiques bruts (OLS, SAR, SEM).
  - [ ] Structurer ces sorties mathématiques pour l'Annexe A4.

### Issue #075 — Annexe A5 : Note sur les méthodes dans /exploratory/
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Modèles alternatifs.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Note sur les méthodes dans `/exploratory/` avec justification du choix de non-inclusion

- **Artefacts générés** : Annexe A5.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rassembler les résultats des méthodes exploratoires (Random Forest, etc.) non retenues.
  - [ ] Rédiger la note méthodologique associée pour l'Annexe A5.

### Issue #076 — Annexe A6 : Cartes supplémentaires
**Labels** : `annexe`, `figure`, `difficulty: low`
- **Contexte Analytique** : Visualisation.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutralité.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Cartes supplémentaires (PSL, centralité, communautés multi-couches)

- **Artefacts générés** : Annexe A6.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Regrouper les visualisations géospatiales secondaires générées par les modèles.
  - [ ] Exporter ce recueil cartographique pour l'Annexe A6.

### Issue #077 — Annexe A7 : Bibliographie méthodes
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Bibliographie.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Bibliographie méthodes (network science, spatial econometrics, sociologie computationnelle)

- **Artefacts générés** : Annexe A7.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Clause obligatoire de début : "Ce volume propose des cadres dynamiques exploratoires..." Il faut empêcher le lecteur de prendre les projections pour des prédictions.
- **Artefacts générés** : Note éthique T3.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rédiger la note renforcée (cadres exploratoires, non prédictifs, non causaux)
  - [ ] Phrase protectrice obligatoire en ouverture : *"Ce volume propose des cadres dynamiques exploratoires…"*
  - [ ] Avant-propos : transition "du réseau aux dynamiques", note de limitation explicite sur la granularité des données longitudinales
  - [ ] Introduction : présentation transparente du dataset longitudinal (qualité, années manquantes, biais)


---

### MILESTONE T3-P1 — Partie I : Dynamiques temporelles


### Issue #079 — Chapitre 1 : Trajectoires de lycées
**Labels** : `chapitre`, `code`, `figure`, `difficulty: low`
- **Contexte Analytique** : Traquer l'évolution de la valeur $S_{i,t}$ sur plusieurs années.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Identifier les établissements en évolution sociale descendante ou ascendante sans incrimination morale.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition formelle du score de trajectoire
  - Trois types analytiques : ascendants, déclinants, instables
  - Carte des trajectoires sur l'IDF
  - **Nouveauté** : corrélation trajectoire × évolution prix DVF (polarisation sociale ?)
  - Corrélation trajectoire × données démographiques temporelles INSEE
  - Script `figures/fig4_trajectories_changepoints.py`
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 1, Figure 4.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder le score longitudinal de "trajectoire temporelle" et classer les établissements (ascendants, déclinants, instables).
  - [ ] Générer le script `figures/fig4_trajectories_changepoints.py` et tester la corrélation temporelle avec l'évolution des prix DVF.



### Issue #080 — Chapitre 2 : CAH dynamique
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Évolution de la matrice de clustering.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les frontières bougent-elles ?
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Partitions annuelles, matrice de transition inter-temporelle
  - Stabilité ARI entre années, mobilité de cluster
  - **Nouveauté** : les clusters du Tome II sont-ils stables dans le temps ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 2.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Exécuter la CAH dynamique sur chaque année et générer la matrice de transition inter-temporelle.
  - [ ] Calculer la stabilité (Adjusted Rand Index) des clusters d'une année sur l'autre.



### Issue #081 — Chapitre 3 : L'ultramétrie temporelle
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : La hiérarchie se rigidifie-t-elle avec le temps ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Distinguer l'effet réel de la simple révision du calcul IPS de 2021.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Dendrogrammes annuels empilés
  - Distance ultramétrique inter-temporelle, stabilité hiérarchique
  - Note de prudence : distinguer changements réels vs artefacts de la révision IPS 2021
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 3.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Générer la pile de dendrogrammes annuels superposés.
  - [ ] Calculer la distance ultramétrique inter-temporelle pour évaluer la résilience hiérarchique du système.



### Issue #082 — Chapitre 4 : Le modèle HMM (régimes cachés)
**Labels** : `chapitre`, `code`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle 35. Le système possède-t-il des "humeurs" latentes ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Modèle formel métaphorique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Note de statut épistémologique obligatoire : HMM = cadre exploratoire, pas modélisation robuste au sens strict
  - Variables d'observation : IPS, mixité, résultats bac, prix DVF
  - 4–5 états cachés estimés, matrice de transition, durée moyenne par état
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 4.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Entraîner un Hidden Markov Model (HMM) pour détecter les régimes cachés dans les séries temporelles (IPS, résultats, mixité).
  - [ ] Extraire les matrices de transition estimées et la durée moyenne par état caché.



### Issue #083 — Chapitre 5 : HMM couplé au réseau (diffusion des régimes)
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle 36 & 37. Un changement de régime dans Paris se diffuse-t-il via les corridors ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Section expérimentale (`/exploratory/`).
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Intégration graphe de similarité dans le HMM
  - Note de prudence renforcée : modèle expérimental, résultats = hypothèses exploratoires
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 5.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coupler le modèle HMM avec la structure topologique (Graph Neural Network temporel ou modèle couplé).
  - [ ] Extraire les paramètres de diffusion montrant comment les régimes se propagent géographiquement.



### Issue #084 — Chapitre 6 : Dynamique de Theil — évolution de la ségrégation
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : La dérivée de la ségrégation (Modèle 31).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Analyser si l'Île-de-France converge vers l'explosion ou vers la stabilité.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Série temporelle de T(t)
  - Décomposition dynamique : ΔT = ΔT_within + ΔT_between
  - Paris : hétérogénéité interne maximale, quelle évolution ?
  - Petite couronne : zone de tension, évolution de la polarisation
  - Grande couronne : homogénéité croissante ou décroissante ?
  - Vitesse de fragmentation v_T = dT/dt
  - **V2** : corrélation dynamique Theil × prix DVF
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 6.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la série temporelle de l'indice de Theil (T) et sa vitesse de fragmentation (dT/dt).
  - [ ] Extraire la décomposition dynamique (ΔT_within + ΔT_between) et générer les graphiques d'évolution par couronne.



### Issue #085 — Chapitre 7 : Flux de mobilité scolaire — un Sankey dans le temps
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modèle 33. Matérialisation de l'évolution des clusters.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : La "dérive continentale" de l'éducation francilienne.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Évolution de la matrice de transition T_t
  - Animation Python conceptuelle 2010-2026 (script fourni)
  - Ouverture / fermeture des corridors dans le temps
  - Émergence et disparition d'ascenseurs sociaux
  - Dérive de T : qu'est-ce qui explique les changements de flux ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 7.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Générer la série chronologique des matrices de transition et produire l'animation dynamique de Sankey.
  - [ ] Extraire les métriques identifiant mathématiquement l'apparition de nouveaux ascenseurs sociaux.


---

### MILESTONE T3-P2 — Partie II : Ruptures et seuils critiques


### Issue #086 — Chapitre 8 : Détection de changepoints (PELT)
**Labels** : `chapitre`, `code`, `figure`, `difficulty: low`
- **Contexte Analytique** : Modèle 34. Trouver les années exactes où le système s'est cassé.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Prudence : corrélation $\neq$ causalité.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - PELT, segmentation binaire, critère AIC/BIC
  - Changepoints sur IPS moyen, σ, Theil, résultats bac
  - **Nouveauté** : coïncidence changepoints scolaires × changepoints DVF immobiliers
  - Note obligatoire : distinguer ruptures réelles vs artefacts révision IPS 2021
  - Test de sensibilité penalty PELT (min_size, pen)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 8.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Exécuter l'algorithme de détection de ruptures (PELT) en ajustant les paramètres de pénalité (AIC/BIC).
  - [ ] Isoler les dates critiques (changepoints) et tester la coïncidence avec les ruptures des séries immobilières DVF.



### Issue #087 — Chapitre 9 : Analyse causale des changepoints
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Essayer d'expliquer pourquoi la rupture a eu lieu.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cadrage strict des limites du modèle.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Note renforcée : associations temporelles, pas effets causaux
  - Ce qu'il faudrait pour une identification causale stricte (diff-in-diff, RD — non disponibles)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 9.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Configurer un modèle exploratoire (Diff-in-Diff ou Regression Discontinuity) sur les changepoints.
  - [ ] Exporter les intervalles de confiance sur les effets temporels estimés.



### Issue #088 — Chapitre 10 : Phase transitions
**Labels** : `chapitre`, `exploratory`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Modèle 42. Percolation et points critiques.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Emprunt fort à la physique statistique. Exiger des "formulations conditionnelles systématiques".
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Note épistémologique développée : métaphore analytique formalisée, pas loi empirique
  - Condition `ρλ_max(W) ≥ 1` présentée comme condition mathématique sur le modèle
  - Formulations conditionnelles systématiques
  - Résultats "cohérents avec l'hypothèse de fragilisation croissante"
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 10.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer la plus grande valeur propre du réseau (ρλ_max) et générer sa série temporelle.
  - [ ] Extraire les fenêtres temporelles critiques où le système s'approche de l'instabilité structurelle (valeur >= 1).



### Issue #089 — Chapitre 11 : Early Warning Signals — prédire les ruptures
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Peut-on savoir si un lycée va s'effondrer socialement ?
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Limites (faux positifs, sensibilité).
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Signaux précurseurs d'une transition critique
  - Indicateurs : variance locale, autocorrélation, «critical slowing down»
  - Application aux lycées en frontière
  - Systèmes d'alerte précoce : repérer les lycées «en bascule»
  - Limites : faux positifs, sensibilité aux données
  - Encadré : peut-on prévoir une ségrégation scolaire croissante ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 11.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la détection des "Early Warning Signals" (variance locale, autocorrélation critique) sur les lycées en frontière.
  - [ ] Modéliser un algorithme prédictif détectant la fragilisation ségrégative d'un établissement.



### Issue #090 — Chapitre 12 : Le DAG inter-temporel — causes et conséquences
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Extension du Modèle 15 au temps $t$.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Expérimentation contrefactuelle in-silico.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Extension du DAG statique à une structure dynamique
  - Ultramétrie comme variable causale latente
  - Ruptures ultramétriques comme événements dans le DAG
  - Propagation en cascade : comment un changement de hiérarchie se diffuse
  - Effet mémoriel (inertie) : α dans le modèle dynamique
  - Simulation contrefactuelle : que se passe-t-il si on «casse» un lien causal ?
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 12.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Construire formellement le Directed Acyclic Graph (DAG) inter-temporel pour inclure les délais et l'inertie.
  - [ ] Simuler mathématiquement une intervention (modification de flux) et en extraire les conséquences en cascade.


---

### MILESTONE T3-P3 — Partie III : Géométrie dynamique et modèle final


### Issue #091 — Note préliminaire Partie III
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Introduction du climax théorique de l'Atlas : l'espace de Riemann (modélisation de la dynamique spatio-temporelle).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Obligation absolue : spécifier que ce sont des langages analytiques, pas des descriptions empiriques directes.
- **Artefacts générés** : Note introductive de la Partie III.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rédiger la note obligatoire (formalismes avancés = langages analytiques, pas descriptions empiriques directement mesurables)



### Issue #092 — Chapitre 13 : L'espace scolaire comme variété riemannienne
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Modèle 48. La topologie sociale n'est pas plate (Espace euclidien), elle est courbée par les privilèges.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Métaphore puissante pour montrer que l'ascension sociale demande plus d'énergie que le mobilité sociale descendante.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Présentation du formalisme riemannien
  - Chaque lycée comme point, métrique sociale G_t
  - Formulation systématique : "permet de penser X… ne constitue pas une mesure directe"
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 13.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la métrique tensorielle représentant l'espace scolaire comme une variété riemannienne (G_t).
  - [ ] Extraire les coordonnées courbées de chaque lycée et générer la visualisation topologique abstraite.



### Issue #093 — Chapitre 14 : Champ de tensions dynamiques
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Calcul des forces sur chaque établissement (gradient sur l'espace courbe).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Démontre la force de rappel du déterminisme local.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Formalisme du champ de tensions (gradient dans l'espace riemannien)
  - Chaque lycée soumis à des forces structurelles : attraction vers le cluster, répulsion centrifuge
  - Carte du champ de tensions à un instant t
  - Lycées en équilibre vs lycées en tension
  - Formulation : «permet de penser la dynamique structurelle... ne constitue pas une mesure directe»
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 14.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer mathématiquement le gradient dans l'espace riemannien (champ de tensions centrifuge/centripète).
  - [ ] Générer la carte vectorielle montrant les lycées soumis aux pressions d'attraction et de répulsion.



### Issue #094 — Chapitre 15 : Le modèle unifié
**Labels** : `chapitre`, `exploratory`, `difficulty: medium`
- **Contexte Analytique** : Synthèse mathématique finale.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mettre le code complet dans `/exploratory/`. Ne pas en faire le juge de paix, mais le sommet technique.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - **Note obligatoire** : `L = L_HMM + λ₁L_GNN + λ₂L_ultra + λ₃L_flux` = outil formel d'exploration, hyperparamètres fixés exploratoirement
  - Ce modèle → `/exploratory/` sur GitHub (pas dans le texte principal comme résultat)
  - Qu'est-ce que ce modèle permet de penser que les modèles séparés ne permettent pas ?
  - Synthèse des trois tomes : de la carte à la dynamique
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 15.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Assembler la fonction de perte composite (Loss = L_HMM + λ₁L_GNN + λ₂L_ultra + λ₃L_flux).
  - [ ] Entraîner le réseau neuronal unifié et extraire les hyperparamètres finaux vers un fichier de configuration.


---

### MILESTONE T3-P4 — Partie IV : Paradoxes et anomalies


### Issue #095 — Note éthique Partie IV
**Labels** : `ethique`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Introduction sur les anomalies paradoxales (Modèle 45).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Un "lycée sous-performant" est un écart statistique au modèle, pas un jugement sur les équipes pédagogiques.
- **Artefacts générés** : Note éthique Partie IV.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rédiger la note spécifique : "paradoxaux", "sur-performants", "sous-performants" = qualifications relatives à un modèle statistique, pas évaluations de qualité de l'enseignement



### Issue #096 — Chapitre 16 : Lycées paradoxaux positifs (sur-performance sociale)
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les lycées qui défient la gravité sociale.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : On constate le paradoxe sans l'expliquer totalement avec des données macro.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition formelle avec résultats bac + valeur ajoutée IVAL comme validation externe
  - Score de paradoxalité enrichi
  - Formulation éthique : "performance relative supérieure à ce que leur profil prédirait"
  - Mécanismes non déductibles des données agrégées
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 16.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Créer une fonction de filtrage détectant les établissements ayant un fort score de sur-performance relative.
  - [ ] Générer l'export brut (CSV/JSON) de ces anomalies statistiques avec croisement IVAL.



### Issue #097 — Chapitre 17 : Paradoxes inversés — le sous-rendement de l'élite
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les lycées qui, vu leur recrutement élitiste, devraient faire bien mieux au bac.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : "Peut-on trop bien trier ses élèves ?" Formulation neutre.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Lycées à IPS très élevé mais performance relative faible
  - Hypothèses : saturation, effet sélectivité symbolique, inertie institutionnelle
  - Corrélation entre score d'entre-soi et paradoxe inversé
  - Peut-on «trop bien» trier ses élèves ? (question analytique clé)
  - Carte des paradoxes inversés en Île-de-France
  - **V2** : croisement DVF (dynamique immobilière atypique ?)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 17.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder l'extraction des "paradoxes inversés" (IPS ultra-élevé mais sous-rendement en VA).
  - [ ] Tester statistiquement la corrélation de ce sous-rendement avec les dynamiques immobilières locales (DVF).



### Issue #098 — Chapitre 18 : Trajectoires rares — les outliers de mobilité scolaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Analyser les trajectoires individuelles de lycées qui sautent de cluster.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les marges du déterminisme scolaire.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Définition : P(τ_i) ≪ ε
  - Score d'anomalie A(τ_i) = -log P(τ_i)
  - Types : contre-hiérarchiques, «sauts», oscillantes, géographiques
  - Ce que les trajectoires rares révèlent : contournements, réseaux, stratégies
  - Signification : les marges du déterminisme scolaire
  - **V2** : croisement DVF (dynamique immobilière atypique ?)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 18.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer l'entropie des trajectoires individuelles (-log P(τ_i)) et isoler les trajectoires outliers de mobilité.
  - [ ] Exporter la liste des établissements ayant des transitions contre-hiérarchiques.



### Issue #099 — Chapitre 19 : Communes hyper-ségrégées malgré mixité apparente
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Les villes qui s'illustrent par une ségrégation intra-muros intense.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les options (latin, bilangue) ou le privé agissent comme tamis invisible.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Paradoxe de la commune «mixte en moyenne»
  - Indice de fausse mixité F_c = M_global - M_interne
  - Score d'hyper-ségrégation masquée HS_c
  - Top communes paradoxales (forte moyenne, forte séparation interne)
  - Mécanismes : filières, options, réputation, recrutement implicite
  - Carte IDF des communes hyper-ségrégées
  - **V2** : croisement DVF (dynamique immobilière atypique ?)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 19.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer le score d'hyper-ségrégation masquée (HS_c) combinant une forte moyenne communale et un fort indice de ségrégation interne.
  - [ ] Générer la carte spatiale identifiant les communes "faussement mixtes".



### Issue #100 — Chapitre 20 : Blind spots systémiques
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Ce que tous les modèles (SAR, GMM, Theil) n'arrivent pas à prévoir.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Avouer les ignorances de la machine de l'Atlas.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Score BS_i = |R_i| × Σ W_ij |R_j|
  - Consensus multi-modèle d'erreur
  - Zones systématiquement mal expliquées
  - Hypothèses sur variables manquantes : réputation, alumni, dérogations
  - **V2** : croisement DVF (dynamique immobilière atypique ?)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 20.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder la consolidation des erreurs (résidus) multi-modèles pondérées spatialement.
  - [ ] Extraire la liste géographique des "blind spots" (zones systématiquement mal prédites).


---

### MILESTONE T3-P5 — Partie V : Réforme et simulation


### Issue #101 — Note de cadrage Partie V (obligatoire)
**Labels** : `documentation`, `ethique`, `difficulty: low`
- **Contexte Analytique** : "Que se passerait-il si... ?"
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Les simulations ne sont PAS des recommandations de politique publique. Les parents s'adapteraient (ex: déménagement, fuite dans le privé), ce que le modèle ignore.
- **Artefacts générés** : Note de Cadrage.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rédiger la note : simulations = scénarios analytiques, pas prédictions ni recommandations de politique publique
  - [ ] Préciser que les comportements adaptatifs des acteurs ne sont pas modélisés



### Issue #102 — Chapitre 21 : Simulation réforme — changer la carte scolaire
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Redistribution in-silico des IPS.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Cadrage strict des limites du modèle.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Modèle non-linéaire spatial comme outil de simulation
  - Simulation 1 V1 : redistribution des IPS (re-sectorisation)
  - Propagation : la réforme se diffuse-t-elle dans le réseau ?
  - Effets de bord : quels lycées bénéficient, lesquels perdent ?
  - Condition de succès V1 : éviter de déclencher une transition de phase
  - Limites section obligatoire : comportements familiaux statiques, effets adaptatifs potentiellement annulateurs
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 21.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Initialiser la boucle de simulation de re-sectorisation (redistribution artificielle des IPS locaux).
  - [ ] Extraire la nouvelle configuration du réseau et valider la condition de stabilité de la phase de transition simulée.



### Issue #103 — Chapitre 22 : Simulation — neutraliser le privé sélectif
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Contrefactuel : supprimer les 20 lycées les plus fermés de l'algorithme.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Exercice purement mathématique analytique. Pas une "fermeture" d'écoles, mais un test de stress de l'équation de Theil.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Contrefactuel V1 : que se passe-t-il si on ferme les 20 lycées les plus fermés socialement ?
  - Réallocation des flux dans le réseau
  - Impact sur les clusters : recomposition des mondes scolaires ?
  - Impact sur les corridors : nouveaux ascenseurs sociaux ?
  - Impact sur les goulots : libération de mobilité ?
  - Discussion V1 : est-ce souhaitable ? faisable ? suffisant ? — exercice analytique, pas proposition de politique
  - Note obligatoire : exercice analytique, pas proposition de politique publique
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 22.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Coder le modèle contrefactuel "suppression des noeuds hyper-sélectifs" (fermeture simulée du Top 20 fermé).
  - [ ] Relancer l'algorithme de routage des flux et exporter les nouvelles matrices d'accessibilité sociale.



### Issue #104 — Chapitre 23 : Simulation — renforcer les lycées paradoxaux positifs
**Labels** : `chapitre`, `code`, `difficulty: medium`
- **Contexte Analytique** : Modéliser un "label d'excellence" sur la base de la VA au lieu du recrutement social.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Risque in-silico de polarisation sociale scolaire progressive mis en évidence.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Investir dans les lycées qui sur-performent socialement
  - Impact sur le réseau de mobilité
  - Risque de polarisation sociale scolaire progressive (V1)
  - Effet de labellisation : comment la réputation change les flux
  - Quelle politique de communication accompagne cette stratégie ? (V1)
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 23.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Injecter un bonus attractif simulé sur les lycées paradoxaux positifs.
  - [ ] Extraire l'impact de ce choc sur l'ouverture de nouveaux corridors sociaux dans le modèle probabiliste.



### Issue #105 — Chapitre 24 : Politiques de mixité : leçons des modèles
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Synthèse théorique des trois simulations.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Mixité forcée vs mixité incitée. "Le risque de la réforme sans modèle".
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Ce que les modèles disent sur la mixité (V1)
  - La mixité forcée vs la mixité incitée
  - L'optimum de perméabilité : ni trop fermé ni trop ouvert
  - Le rôle des corridors : soutenir les ascenseurs, contester les filtres
  - Les lycées-ponts comme leviers de politique publique
  - Le risque de la réforme sans modèle : déclencher une phase transition non désirée
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 24.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Calculer les seuils critiques (tipping points) de mixité provoquant la bascule des corridors.
  - [ ] Générer un rapport d'optimisation probabiliste comparant les stratégies de régulation de flux.



### Issue #106 — Chapitre 25 : Vers un atlas dynamique
**Labels** : `chapitre`, `infrastructure`, `difficulty: hard`
- **Contexte Analytique** : Structuration de l'outil technique (Atlas).
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Présenter l'Atlas comme un outil d'aide à la compréhension, pas comme un juge.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Les 9 couches de l'atlas
  - Concept d'interactivité (GitHub interactif si développé)
  - Ce que les données actuelles permettent et ne permettent pas encore
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 25.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Compiler l'architecture des couches JSON pour la cartographie web interactive finale.
  - [ ] Générer les tuiles de base géographiques et les calques statistiques (IPS, résidus, clusters).


---

### MILESTONE T3-P6 — Partie VI : Limites, éthique et ouvertures


### Issue #107 — Chapitre 26 : Limites méthodologiques (le plus important du tome)
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Auto-critique algorithmique de l'Atlas.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le chapitre le plus important. Non-stationnarité du réel vs stationnarité des modèles.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - IPS comme proxy imparfait
  - Données agrégées et ecological fallacy
  - Absence de données individuelles longitudinales
  - Biais de sélection du corpus (top 100 seulement — implications)
  - Limites des simulations (comportements adaptatifs non modélisés)
  - Non-stationnarité du réel vs stationnarité des modèles
  - Modifications méthodologiques du Ministère (révision IPS 2021)
  - Confusion potentielle artefacts de mesure / changements réels
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 26.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur rédige cette analyse méthodologique.*



### Issue #108 — Chapitre 27 : Éthique de la quantification scolaire
**Labels** : `chapitre`, `ethique`, `difficulty: low`
- **Contexte Analytique** : Le danger des mathématiques sociales.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le risque de naturaliser les inégalités. Distinguer "décrire une structure" de "l'accepter comme naturelle". L'IPS peut-il être interprété abusivement ??
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Le risque de naturaliser les inégalités
  - La mise en données de l'inégalité : pouvoir et contre-pouvoir
  - L'IPS peut-il être interprété abusivement ??
  - Responsabilité du chercheur dans la diffusion
  - Distinction : décrire une structure ≠ l'accepter comme naturelle
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 27.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur rédige cette analyse éthique.*



### Issue #109 — Chapitre 28 : Ouvertures disciplinaires et comparaisons internationales
**Labels** : `chapitre`, `difficulty: medium`
- **Contexte Analytique** : Paris face au reste du monde.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Ne pas faire d'inférence, juste de la bibliographie comparative.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - Sociologie, géographie sociale, économie, informatique, physique statistique
  - Comparaisons internationales développées (Paris vs Londres, New York, Berlin, Tokyo, Barcelone) — littérature existante uniquement
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 28.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur rédige ces ouvertures disciplinaires.*



### Issue #110 — Chapitre 29 : Agenda de recherche
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Les prochaines frontières.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Ce qu'un accès aux données individuelles permettrait de faire.
- **Synopsis du Chapitre (Réflexions de l'Auteur)** :
  - 10 questions ouvertes
  - Données nécessaires pour aller plus loin
  - Ce qu'un accès à des données individuelles longitudinales permettrait de faire
- **Artefacts générés** : Sorties analytiques (graphes, data, scripts) pour le Chapitre 29.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur définit l'agenda de recherche.*



### Issue #111 — Conclusion générale de la trilogie
**Labels** : `chapitre`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Clôture de l'Atlas.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Le paradoxe de la méritocratie républicaine face aux données. Sans prescription normative.
- **Artefacts générés** : Conclusion Générale.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Ce que l'IDF dit de la France scolaire
  - [ ] La ségrégation scolaire comme processus, pas état
  - [ ] Le paradoxe de la méritocratie républicaine face aux données
  - [ ] Mise en perspective internationale finale
  - [ ] Responsabilité collective et leviers d'action (sans prescription normative)



### Issue #112 — Annexe A1 : Code Python complet
**Labels** : `annexe`, `code`, `difficulty: medium`
- **Contexte Analytique** : Reproductibilité du Tome 3.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Code Python complet + lien GitHub

- **Artefacts générés** : Annexe A1.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Rassembler les scripts Python dédiés aux séries temporelles et détections de ruptures.
  - [ ] Structurer le code dynamique pour l'Annexe A1 du Tome 3.

### Issue #113 — Annexe A2 : Note méthodes
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Choix avancés.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Note sur les méthodes `/exploratory/` avec justification

- **Artefacts générés** : Annexe A2.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Réunir les justifications mathématiques des paramètres choisis pour les modèles.
  - [ ] Rédiger la note méthodologique justificative dans l'Annexe A2.

### Issue #114 — Annexe A3 : Paramètres estimés des modèles dynamiques
**Labels** : `annexe`, `data`, `difficulty: medium`
- **Contexte Analytique** : Résultats bruts.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Reproductibilité de la recherche.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Paramètres estimés des modèles dynamiques

- **Artefacts générés** : Annexe A3.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Extraire les paramètres estimés par les modèles temporels (HMM, algorithme PELT).
  - [ ] Compiler ces valeurs mathématiques dans l'Annexe A3.

### Issue #115 — Annexe A4 : Résultats des simulations de réforme
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Scénarios.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Neutre.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Résultats des simulations (tableaux complets)

- **Artefacts générés** : Annexe A4.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Agréger les tableaux de projection issus des simulations de réformes.
  - [ ] Mettre en page ces résultats chiffrés pour l'Annexe A4.

### Issue #116 — Annexe A5 : Cartes temporelles et animations
**Labels** : `annexe`, `figure`, `difficulty: low`
- **Contexte Analytique** : Visualisation.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Factuel.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Sources longitudinales, méthode de construction dataset temporel

- **Artefacts générés** : Annexe A5.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Générer et optimiser les animations (GIFs, vidéos) d'évolution des flux scolaires.
  - [ ] Constituer la galerie multimédia de l'Annexe A5.

### Issue #117 — Annexe A6 : Sources longitudinales
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Données temporelles.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Index général de la trilogie

- **Artefacts générés** : Annexe A6.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Inventorier les sources de données longitudinales exploitées.
  - [ ] Dresser la bibliographie data complète pour l'Annexe A6.

### Issue #118 — Annexe A7 : Index général de la trilogie
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Navigation.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Facilité.
- **Synopsis de l'Annexe (Réflexions de l'Auteur) :**
  - Bibliographie complète (3 tomes)

- **Artefacts générés** : Annexe A7.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Créer l'indexation globale croisée sur l'ensemble de la trilogie.
  - [ ] Générer l'index général final pour l'Annexe A7.

### Issue #119 — Annexe A8 : Bibliographie complète
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Clôture bibliographique.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Rigueur.
- **Artefacts générés** : Annexe A8.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Agréger les citations et la littérature scientifique de l'ensemble du projet.
  - [ ] Formater la bibliographie exhaustive de l'Annexe A8.

### Issue #120 — Annexe A9 : Glossaire général unifié
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Définitions.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Clarté.
- **Artefacts générés** : Annexe A9.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Unifier le dictionnaire des termes techniques (code, stats, socio) employés dans les trois tomes.
  - [ ] Rédiger le glossaire de référence global dans l'Annexe A9.

### Issue #121 — Annexe A10 : Licences de données
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Légal.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Droit.
- **Artefacts générés** : Annexe A10.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Vérifier la conformité légale et recenser l'ensemble des licences Open Data.
  - [ ] Rédiger le récapitulatif juridique pour l'Annexe A10.

### Issue #122 — Annexe A11 : Table de correspondance méthode
**Labels** : `annexe`, `documentation`, `difficulty: low`
- **Contexte Analytique** : Justification.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Académique.
- **Artefacts générés** : Annexe A11.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Carte factuelle.
- **Artefacts générés** : Figure 1 HD et Caption LaTeX.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Collecter les données géographiques (GeoPandas, communes IDF)
  - [ ] Intégrer les revenus IRIS en transparence
  - [ ] Taille des points ∝ effectif, gradient Est/Ouest visible
  - [ ] Sous-panel : scatter IPS communal vs prix médian DVF
  - [ ] Script `figures/fig1_map.py` (code complet dans plan_integral_v2.md)
  - [ ] Caption arXiv rédigée



### Issue #124 — Figure 2 : Scatter IPS vs σ
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Démonstration visuelle de la "mixité cachée".
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Standard Nature/Science.
- **Artefacts générés** : Figure 2 HD et Caption LaTeX.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Densité KDE en fond
  - [ ] Couleurs rouge/bleu privé/public
  - [ ] Annotations cas emblématiques
  - [ ] Sous-panel : corrélation σ × DVF
  - [ ] Script `figures/fig2_scatter_ips_sigma.py` (code complet dans plan_integral_v2.md)
  - [ ] Caption arXiv rédigée



### Issue #125 — Figure 3 : Réseau Louvain
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : Le graphe de l'Île-de-France.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Clarifier dans la caption que c'est un réseau mathématique, pas physique.
- **Artefacts générés** : Figure 3 HD et Caption LaTeX.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Layout force-directed (spring_layout)
  - [ ] Taille nœuds ∝ centralité eigenvector
  - [ ] Épaisseur arêtes ∝ similarité
  - [ ] Annotation top 10 nœuds centraux
  - [ ] Script `figures/fig3_network_louvain.py` (code complet dans plan_integral_v2.md)
  - [ ] Caption arXiv avec valeur de modularité Q



### Issue #126 — Figure 4 : Trajectoires + changepoints
**Labels** : `figure`, `code`, `difficulty: low`
- **Contexte Analytique** : La dynamique dans le temps.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Annotations directement dans le graphique (ex: "changement de formule IPS").
- **Artefacts générés** : Figure 4 HD et Caption LaTeX.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Limites explicites inscrites dès l'abstract.
- **Artefacts générés** : PDF final `main.pdf`.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
  - [ ] Compiler `paper_arxiv/main.tex` (base dans `manifesto.tex`)
  - [ ] Intégrer les 4 figures signature
  - [ ] Abstract ≤ 250 mots
  - [ ] Note de limitation explicite dans l'abstract
  - [ ] Vérifier conformité arXiv (format, fonts, références)



### Issue #128 — Robustesse & Sensibilité (checklist globale)
**Labels** : `validation`, `difficulty: medium`
- **Contexte Analytique** : La garantie de solidité des 3 tomes.
- **Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Validation stricte.
- **Artefacts générés** : Rapport de robustesse intégré aux annexes.

- **Périmètre de cohérence technique (Ouvert aux contributions) :**
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



