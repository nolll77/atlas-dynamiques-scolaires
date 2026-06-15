[![FR](https://img.shields.io/badge/Lang-FR-blue.svg)](README.md)
[![EN](https://img.shields.io/badge/Lang-EN-red.svg)](README.en.md)
[![Contributing](https://img.shields.io/badge/Contributing-Guide-green.svg)](CONTRIBUTING.md)
[![Onboarding](https://img.shields.io/badge/Onboarding-Guide-orange.svg)](PARCOURS_COLLABORATEUR.md)

**A reproducible system for the spatio-temporal analysis of schools in the Île-de-France region**

## Overview

This project builds a computational atlas of school dynamics, combining:

- socio-economic data (INSEE, IRIS)
- school data (IPS, baccalaureate results, IVAL)
- real estate data (DVF)
- mobility data (IDF Mobilités)
- fine-grained geography of schools (lat/lon)

The goal is to produce a multi-dimensional, reproducible, and structured representation of the school system, combining:

- spatial statistics
- network analysis
- dynamic models
- variance decomposition
- clustering and temporal segmentation

⚠️ **Scientific Positioning**

This project is:
- descriptive and analytical
- based on structural correlations
- without direct causal interpretation by default
- reproducible (pipeline + tests + tracking)

Any interpretation must respect the methodological framework defined in `docs/CAUSALITY_LIMITS.md`.

## Repository Architecture

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

## Data Used

The master dataset (`master_dataset.parquet`) is built from:

**School Data**
- IPS (Social Position Index)
- baccalaureate results
- IVAL (value added)

**Socio-economic Data**
- INSEE IRIS (median income, unemployment, socio-professional categories)
- temporal demographics

**Spatial Data**
- GPS coordinates of schools
- school zoning

**Real Estate Data**
- DVF (price per m², transactions)

**Mobility**
- IDF Mobilités accessibility

## Scientific Pipeline

The project follows a reproducible logic:
`Ingestion → Cleaning → Feature Engineering → Modeling → Networks → Temporal Analysis → Figures → Paper`

### Analytical Modules

1. **Spatial Analysis**
   - IPS mapping
   - geographic gradients
   - DVF / school correlations

2. **Statistical Decomposition**
   - multi-factor ANOVA
   - explained variance (geography / status / income)
   - fragmentation indices (Theil, Gini, Duncan)

3. **School Networks**
   - similarity graphs
   - Louvain clustering
   - centrality (eigenvector, betweenness, closeness)
   - multiplex networks

4. **Temporal Dynamics**
   - school trajectories
   - dynamic HAC (Hierarchical Agglomerative Clustering)
   - HMM (hidden regimes)
   - changepoints (PELT)

5. **Segregation and Fragmentation**
   - dynamic Theil
   - spatial Gini
   - global fragmentation index (IFC)

## Validation & Tests

Contributions are subject to a strict validation pipeline:

**Mandatory Tests**
- correct Theil decomposition
- stochastic transition matrices
- graph symmetry
- Moran's tests (spatial autocorrelation)
- bootstrap stability of indices
- MAUP validation (multi-scale)

## Code Organization

- `data/` → raw and processed data
- `src/` → main code (pipelines, models)
- `exploratory/` → notebooks and experimental analyses
- `figures/` → visualizations and maps
- `tests/` → validation tests
- `runs/` → experiment tracking
- `config/` → configuration parameters
- `docs/` → documentation
- `paper_arxiv/` → research version (scientific paper)

## Experiment Tracking

Each execution produces a file in `runs/`:

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

## Issues & Contribution System

Each issue corresponds to an autonomous scientific module:

**Standard Cycle**
`Issue → Pull Request → CI Tests → Review → Merge → Scientific Artifacts Generated`

**Statuses**
- `open` : in development
- `in review` : PR open
- `merged` : integrated into the system
- `validated` : passes all tests
- `archived` : frozen for publication

## Scientific Production

The project generates:
- arXiv article (`paper_arxiv/main.tex`)
- scientific figures (Figures 1–4)
- spatial maps
- network graphs
- reproducible statistical analyses

## Key Indicators

- **IPS** (socio-educational level)
- **σ IPS** (internal heterogeneity)
- **Theil** (entropy)
- **Gini** (inequality)
- **Duncan D** (dissimilarity)
- **IFC** (global fragmentation)

## Reproducibility

```bash
make setup
make data
make features
make models
make figures
make paper
```

## License

This project is published under a dual-license regime:
- **Code and pipeline**: [MIT License](LICENSE) (free use, modification, and distribution permitted).
- **Editorial content and figures**: [CC BY 4.0](LICENSE_CONTENT) (mandatory attribution to the original author).

## Vision

This project is not a ranking.

It is a multi-scale analytical structure aimed at:
- describing spatial organizations
- modeling social dynamics
- linking territory, school, and urban structure
- producing reproducible scientific objects

**Editorial Purpose**: The scientific material generated by this repository (data, maps, algorithms) is intended to be interpreted and published in the form of a **sociological trilogy**:

- **Tome I — The Map and the Territory** (Geography and static segregation)
- **Tome II — Networks and Worlds** (Topology, similarities, and communities)
- **Tome III — Time and Reform** (Temporal dynamics and systemic shocks)

## Citation

For any reuse, please cite this project:
> Noel Ching, *Atlas of School Dynamics*, 2026, GitHub.

amaswarm&nbsp;&nbsp;&nbsp;&nbsp;@&nbsp;&nbsp;&nbsp;&nbsp;g&nbsp;&nbsp;m&nbsp;&nbsp;a&nbsp;&nbsp;i&nbsp;&nbsp;l&nbsp;&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;&nbsp;c&nbsp;&nbsp;o&nbsp;&nbsp;m
