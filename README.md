# Atlas des Dynamiques Scolaires

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![FR](https://img.shields.io/badge/Lang-FR-blue.svg)](README.md)
[![EN](https://img.shields.io/badge/Lang-EN-red.svg)](README.en.md)
[![Contributing](https://img.shields.io/badge/Guide-Contribution-green.svg)](CONTRIBUTING.md)
[![Onboarding](https://img.shields.io/badge/Parcours-Collaborateur-orange.svg)](PARCOURS_COLLABORATEUR.md)

**Un système reproductible d’analyse spatio-temporelle des établissements scolaires en Île-de-France**

## Présentation

Ce projet construit un atlas computationnel des dynamiques scolaires, combinant :

- données socio-économiques (INSEE, IRIS)
- données scolaires (IPS, résultats bac, IVAL)
- données immobilières (DVF)
- données de mobilité (IDF Mobilités)
- géographie fine des établissements (lat/lon)

L’objectif est de produire une représentation multi-dimensionnelle, reproductible et structurée du système scolaire, en combinant :

- statistiques spatiales
- analyse de réseaux
- modèles dynamiques
- décomposition de variance
- clustering et segmentation temporelle

> **Positionnement scientifique**
> 
> Ce projet est :
> - descriptif et analytique
> - basé sur des corrélations structurelles
> - sans interprétation causale directe par défaut
> - reproductible (pipeline + tests + tracking)
> 
> Toute interprétation doit respecter le cadre méthodologique défini dans [docs/CAUSALITY_LIMITS.md](docs/CAUSALITY_LIMITS.md).

## Architecture du dépôt

```text
.
├── archives/
│
├── config/
│   └── analysis.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── docs/
│   ├── CAUSALITY_LIMITS.md
│   ├── NETWORK_INTERPRETATION.md
│   ├── SOCLE_1_MATHEMATIQUES.md
│   ├── SOCLE_2_DYNAMIQUE.md
│   └── GLOSSAIRE.md
│
├── exploratory/
│   └── notebooks/
│
├── figures/
│
├── paper_arxiv/
│
├── runs/
│   └── (experiment tracking MLflow - généré localement, ignoré par git)
│
├── scripts/
│
├── src/
│   └── atlas/
│
├── tests/
│   ├── README.md
│   ├── socle_1_mathematiques/
│   └── socle_2_dynamique/
│
├── MANIFESTO.md
├── README.md
└── Makefile
```

## Données utilisées

Le dataset maître (`master_dataset.parquet`) est construit à partir de :

**Données scolaires**
- IPS (Indice de Position Sociale)
- résultats au baccalauréat
- IVAL (valeur ajoutée)

**Données socio-économiques**
- INSEE IRIS (revenus médians, chômage, CSP)
- démographie temporelle

**Données spatiales**
- coordonnées GPS des établissements
- sectorisation scolaire

**Données immobilières**
- DVF (prix au m², transactions)

**Mobilité**
- accessibilité IDF Mobilités

## Pipeline scientifique

Le projet suit une logique reproductible :

Ingestion → Nettoyage → Feature Engineering → Modélisation → Réseaux → Analyse temporelle → Figures → Paper

## Modules analytiques

**1. Analyse spatiale**
- cartographie IPS
- gradients géographiques
- corrélations DVF / école

**2. Décomposition statistique**
- ANOVA multi-facteurs
- variance expliquée (géographie / statut / revenu)
- indices de fragmentation (Theil, Gini, Duncan)

**3. Réseaux scolaires**
- graphes de similarité
- Louvain clustering
- centralité (eigenvector, betweenness, closeness)
- multiplex networks

**4. Dynamique temporelle**
- trajectoires d’établissements
- CAH dynamique
- HMM (régimes cachés)
- changepoints (PELT)

**5. Ségrégation et fragmentation**
- Theil dynamique
- Gini spatial
- indice global de fragmentation (IFC)

👉 **[Lire le document d'Architecture : Approche Machine Learning & Algorithmique (White-Box ML)](docs/APPROCHE_MACHINE_LEARNING.md)**

## Validation & tests

L'intégration algorithmique repose sur une architecture de validation par les tests (**Test-Driven Architecture**). Toutes les formules théoriques du projet possèdent un test d'intégrité (actif ou en attente) :

- 👉 **[Lire le document d'explication : Pourquoi les tests sont-ils Ignorés (Jaunes) ?](tests/README.md)**
- 👉 **[Preuve de Couverture 100% : Socle 1 (Mathématiques)](tests/socle_1_mathematiques/MATRICE_DE_COUVERTURE_SOCLE_1.md)**
- 👉 **[Preuve de Couverture 100% : Socle 2 (Dynamique)](tests/socle_2_dynamique/MATRICE_DE_COUVERTURE_SOCLE_2.md)**

## Organisation du code

- `data/` → données brutes et transformées
- `src/` → code principal (pipelines, modèles)
- `exploratory/` → notebooks et analyses expérimentales
- `figures/` → visualisations et cartes
- `tests/` → tests de validation
- `runs/` → suivi des expériences
- `config/` → paramètres de configuration
- `docs/` → documentation
- `paper_arxiv/` → version recherche (papier scientifique)

## Experiment tracking

Chaque exécution produit un fichier dans `runs/` :

```json
{
  "git_hash": "abc123",
  "timestamp": "2026-06-15",
  "config": {},
  "metrics": {
    "theil": 0.42,
    "gini": 0.31,
    "modularity": 0.67
  }
}
```

## Issues & système de contribution

Chaque issue correspond à un module scientifique autonome :

**Cycle standard**
Issue → Pull Request → Tests CI → Review → Merge → Artefacts scientifiques générés

**Statuts**
- `open` : en développement
- `in review` : PR ouverte
- `merged` : intégré au système
- `validated` : passe tous les tests
- `archived` : figé pour publication

## Production scientifique

Le projet génère :

- article arXiv (`paper_arxiv/main.tex`)
- figures scientifiques (Figures 1–4)
- cartes spatiales
- graphes de réseau
- analyses statistiques reproductibles

## Principaux indicateurs
- IPS (niveau socio-scolaire)
- σ IPS (hétérogénéité interne)
- Theil (entropie)
- Gini (inégalité)
- Duncan D (dissimilarité)
- IFC (fragmentation globale)

## Reproductibilité Scientifique

Afin de pallier la fragilité historique des environnements analytiques (fichiers `requirements.txt` obsolètes, données volatiles), l'Atlas adopte les standards d'ingénierie les plus stricts, dignes des laboratoires de pointe en Machine Learning. Ce triptyque garantit une reproductibilité absolue :

- **Ingénierie logicielle (`uv` & `pyproject.toml`)** : L'utilisation de `uv` (100x plus rapide que `pip`) couplé au fichier `uv.lock` gèle l'environnement au bit près. Même cloné dans 5 ans, le système s'installera à l'identique. Les dépendances sont centralisées via le standard PEP 621.
- **Versionnage des données (DVC)** : DVC fait pour la Data ce que Git fait pour le code. Il relie chaque commit à une version exacte (hachée et décentralisée) des lourdes bases de données utilisées.
- **Tracking des expérimentations (MLflow)** : Fini les résultats de recherche perdus sur des carnets. MLflow enregistre automatiquement l'historique de chaque exécution : il mémorise quels réglages exacts ont été utilisés pour obtenir tel résultat mathématique (ex: Indice de Theil), rendant chaque découverte transparente et auditable.

👉 **[Lire le guide de Reproductibilité Scientifique](docs/REPRODUCTIBILITE_SCIENTIFIQUE.md)**


## Licence

Ce projet distingue trois types de contenus, soumis à des licences spécifiques :

- **Code source** (`src/`, `tests/`, `pipelines/`, `scripts/`) : [MIT License](LICENSE) (usage libre, modification et distribution autorisées).
- **Données** : Les données sources proviennent d'organismes publics (INSEE, DEPP, Etalab DVF, etc.) et restent soumises à leurs licences respectives (Licence Ouverte, ODbL, etc.). Le projet ne revendique aucune propriété sur ces données.
- **Contenu éditorial et figures** (`docs/`, `figures/`, `paper_arxiv/`) : [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE_CONTENT). Toute réutilisation nécessite l'attribution à l'auteur original.

## Vision

Ce projet n’est pas un classement.

C’est une structure analytique multi-échelle visant à :

- décrire des organisations spatiales
- modéliser des dynamiques sociales
- relier territoire, école et structure urbaine
- produire des objets scientifiques reproductibles

**Finalité éditoriale** : Le matériau scientifique généré par ce dépôt (données, cartes, algorithmes) a pour vocation d'être interprété et publié sous la forme d'une **trilogie sociologique** :

- **Tome I — La Carte et le Territoire** (Géographie et ségrégation statique)
- **Tome II — Les Réseaux et les Mondes** (Topologie, similarités et communautés)
- **Tome III — Le Temps et la Réforme** (Dynamiques temporelles et chocs systémiques)

## Citation

Pour toute réutilisation, merci de citer ce projet :
> Noel Ching, *Atlas des Dynamiques Scolaires*, 2026, GitHub.

amaswarm&nbsp;&nbsp;&nbsp;&nbsp;@&nbsp;&nbsp;&nbsp;&nbsp;g&nbsp;&nbsp;m&nbsp;&nbsp;a&nbsp;&nbsp;i&nbsp;&nbsp;l&nbsp;&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;&nbsp;c&nbsp;&nbsp;o&nbsp;&nbsp;m
