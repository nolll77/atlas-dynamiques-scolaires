# Atlas des Dynamiques Scolaires

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
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
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── src/
│   ├── ingestion/
│   ├── features/
│   ├── models/
│   ├── network/
│   ├── temporal/
│   └── utils/
│
├── exploratory/
│   ├── notebooks/
│   └── experiments/
│
├── figures/
│
├── tests/
│
├── runs/
│   └── (experiment tracking JSON)
│
├── config/
│   └── analysis.yaml
│
├── docs/
│   ├── CAUSALITY_LIMITS.md
│   ├── SOCLE_MATHEMATIQUE.md
│   ├── NETWORK_INTERPRETATION.md
│   └── GLOSSAIRE.md
│
├── manifesto/
│
├── paper_arxiv/
│   └── main.tex
│
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

## Validation & tests

Les contributions sont soumises à un pipeline de validation strict :

- **Tests obligatoires**
- décomposition Theil correcte
- matrices de transition stochastiques
- symétrie des graphes
- tests de Moran (spatial autocorrelation)
- stabilité bootstrap des indices
- validation MAUP (multi-échelle)

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
Issue → Pull Request → Tests CI → Review → Merge → Dataset enrichi

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

## Reproductibilité

```bash
make setup
make data
make features
make models
make figures
make paper
```

## Licence

MIT License — usage libre avec citation du projet.

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
