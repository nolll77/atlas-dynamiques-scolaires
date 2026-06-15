# Architecture de Reproductibilité Scientifique

L'Atlas des Dynamiques Scolaires n'est pas qu'un outil de visualisation, c'est une **infrastructure de recherche ouverte**. Dans le domaine académique et scientifique, la validité d'une découverte repose sur sa capacité à être reproduite à l'identique par un pair. 

Pour garantir cette rigueur, nous avons mis en place une architecture de Reproductibilité Scientifique basée sur les standards de l'industrie : **DVC (Data Version Control)**, **MLflow** et **uv**.

Ce document explique le rôle de ces outils et comment les utiliser lors de vos contributions.

---

## 1. La séparation Code / Données (Git vs DVC)

Git est excellent pour gérer les versions du code texte (`.py`, `.md`), mais il est incapable de gérer efficacement de lourds fichiers de données (les bases CSV de l'INSEE, les shapefiles, les modèles entraînés).

C'est ici qu'intervient **DVC**.
- **Git** versionne l'intelligence (l'algorithme).
- **DVC** versionne la matière première (la donnée) et les résultats.

DVC agit exactement comme Git, mais pour les données. Il stocke les métadonnées de hachage dans des fichiers minuscules (`.dvc`), que l'on commite sur Git. Les vraies données lourdes, elles, sont stockées sur un *remote* (Google Drive, S3, etc.). 

Si vous clonez le dépôt, vous tapez :
```bash
dvc pull
```
Et DVC ira chercher la version exacte des données qui correspond au code actuel de votre branche Git. Plus de `donnees_finales_V3_final_pour_de_vrai.csv` !

---

## 2. Le Graphe de Dépendance (`dvc.yaml`)

Au cœur de notre reproductibilité se trouve le fichier `dvc.yaml`. Il définit notre **Pipeline de Données** (DAG - Directed Acyclic Graph).

Il explique à la machine dans quel ordre exécuter le code, et quelles sont les dépendances de chaque étape :

```yaml
# Extrait du dvc.yaml
stages:
  build_master:
    cmd: python -m atlas.data.cleaners build_master
    deps:
      - src/atlas/data/cleaners.py
      - params.yaml
    outs:
      - data/processed/master_dataset.parquet
```

**Que signifie ce bloc ?**
1. L'étape `build_master` crée le fichier `master_dataset.parquet` (`outs`).
2. Elle a besoin du script Python `cleaners.py` et du fichier `params.yaml` (`deps`).
3. **Magie de DVC :** Si vous tapez `dvc repro`, DVC va vérifier les *hashs* des fichiers. Si ni le code `cleaners.py` ni les paramètres n'ont changé depuis la dernière fois, DVC *ne relancera pas le calcul*. Il utilisera le cache. C'est un gain de temps massif sur les gros algorithmes (comme les chaînes de Markov ou la détection de communautés de Louvain).

---

## 3. Le Centre de Commandement : `params.yaml`

La pire erreur en data science est le "hardcoding" (coder des paramètres en dur dans les scripts Python, par exemple : `if ips > 140:`). Cela rend le code illisible, introuvable et impossible à comparer.

Dans l'Atlas, **TOUS** les hyperparamètres, seuils et configurations résident dans le fichier central `params.yaml`.

```yaml
# Extrait du params.yaml
data:
  min_ips_threshold: 140

clustering:
  optimal_k: 5
  bootstrap_n: 1000
```

Si un chercheur veut tester l'hypothèse de l'Atlas avec $K=6$ clusters au lieu de $5$, il n'a pas à fouiller dans 40 scripts Python. Il modifie simplement la valeur dans `params.yaml` et lance :
```bash
dvc repro
```
DVC comprendra que le paramètre a changé, invalidera le cache des étapes concernées, et recalculera tout le modèle automatiquement.

---

## 4. L'Orchestration avec le `Makefile`

Pour simplifier la vie des développeurs, la complexité des commandes est masquée derrière notre `Makefile`.

* `make setup` : Prépare l'environnement complet.
* `make data` : Demande à DVC de reconstruire uniquement le jeu de données maître.
* `make run-all` : Exécute la chaîne complète (Données $\to$ Modèles $\to$ Matrices Mathématiques $\to$ Figures $\to$ Tests unitaires).
* `make tests` : Lance la batterie de tests TDD (Test-Driven Architecture).

---

## 5. Le Suivi Scientifique avec MLflow

Là où DVC gère les "fichiers", **MLflow** gère les "métriques" et les "expériences". 

Lorsque nous ferons tourner de gros modèles (comme l'optimisation des seuils de distance spatiale ou les modèles de basculement non-linéaires), MLflow enregistrera en direct, pour chaque test :
1. Les paramètres utilisés (ceux du `params.yaml`).
2. Les scores obtenus (Indice de Theil, Silhouette Score, etc.).

Vous pouvez visualiser toutes vos expérimentations en tapant :
```bash
make mlflow-ui
```
Cela permet d'avoir une traçabilité scientifique parfaite : *"Quand j'ai mis le paramètre alpha à 0.05 mardi dernier, quel était l'impact exact sur la ségrégation mesurée ?"*

---

## Conclusion : Règles pour les Contributeurs

Pour maintenir l'intégrité de cette infrastructure, merci de respecter ces 3 règles d'or lors de vos développements :

1. **Aucun paramètre en dur.** Si votre algorithme a besoin d'un seuil, d'une graine aléatoire (seed), ou d'une taille d'échantillon, ajoutez ce paramètre dans `params.yaml` et appelez-le dans votre code.
2. **Ne commitez jamais de données sur Git.** Le dossier `data/` est ignoré par Git. Utilisez DVC si de nouvelles données sont générées de façon permanente.
3. **Mettez à jour le pipeline.** Si votre code génère un nouvel output intermédiaire (ex: une nouvelle matrice), ajoutez une étape dans `dvc.yaml` pour que le système la prenne en compte.
