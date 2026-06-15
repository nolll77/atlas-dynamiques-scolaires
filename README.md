# Vers un Atlas des Dynamiques Scolaires

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Contributing](https://img.shields.io/badge/Guide-Contribution-green.svg)](CONTRIBUTING.md)
[![Onboarding](https://img.shields.io/badge/Parcours-Collaborateur-orange.svg)](PARCOURS_COLLABORATEUR.md)

**Infrastructure open source de recherche computationnelle sur les dynamiques scolaires.**

Ce projet construit des pipelines de données reproductibles pour analyser les inégalités et structures du système éducatif à partir de données statistiques, géographiques et temporelles.

> ⚠️ Les résultats produits sont des analyses statistiques associatives. Ils ne démontrent pas de causalité et ne doivent pas être interprétés comme des recommandations.

## Ce que produit ce projet

L’Atlas génère :

- des indicateurs de ségrégation scolaire (ex : IPS, distributions socio-économiques),
- des représentations spatiales des dynamiques éducatives,
- des graphes de relations entre établissements,
- des analyses temporelles des évolutions du système scolaire,
- des figures et datasets reproductibles.

## Structure du projet

Le projet est organisé autour de trois axes analytiques :

- **Tome I — Carte et territoire**
  Analyse spatiale et socio-économique des établissements scolaires.
- **Tome II — Réseaux et structures**
  Graphes, communautés et interactions entre établissements.
- **Tome III — Temps et transformations**
  Dynamiques temporelles, réformes et évolutions du système.

## Démarrage rapide

```bash
# Cloner le dépôt
git clone git@github.com:nolll77/atlas-dynamiques-scolaires.git
cd atlas-dynamiques-scolaires

# Installer l'environnement
make setup

# Lancer les tests
make tests

# Générer les figures
make figures
```

## Organisation du code

- `src/atlas/` → code de production
- `exploratory/` → analyses expérimentales
- `config/` → configuration des pipelines
- `tests/` → tests unitaires et validation

## Citer ce projet

Voir [CITATION.cff](CITATION.cff) ou utiliser la fonctionnalité GitHub “Cite this repository”.

## Contribution

Les contributions sont les bienvenues.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour le workflow complet : issues → fork → branche → PR → review. Vous pouvez également suivre notre [Parcours Contributeur pas-à-pas](PARCOURS_COLLABORATEUR.md).

## Licence

Code : [MIT](LICENSE)
Figures et textes : [CC-BY 4.0](LICENSE_CONTENT)

## Philosophie

Ce projet vise à rendre les structures éducatives observables, reproductibles et analysables à partir de données ouvertes et transparentes.
