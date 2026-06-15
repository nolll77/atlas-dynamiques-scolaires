# Architecture de Reproductibilité Scientifique

L'Atlas des Dynamiques Scolaires n'est pas qu'un outil de visualisation, c'est une **infrastructure de recherche ouverte**. Dans le domaine académique et scientifique, la validité d'une découverte repose sur sa capacité à être reproduite à l'identique par un pair. 

Pour garantir cette rigueur, nous avons mis en place une architecture de Reproductibilité Scientifique basée sur les standards de l'industrie : **DVC (Data Version Control)**, **MLflow** et **uv**.

Ce document explique le rôle de ces outils et comment les utiliser lors de vos contributions.

---

## 1. Gestion des dépendances (`uv` et `pyproject.toml`)

Dans le monde académique, l'utilisation d'un simple fichier `requirements.txt` pose d'énormes problèmes à long terme (les versions des bibliothèques évoluent et finissent par casser le code des années plus tard).

L'Atlas utilise une architecture ultra-moderne basée sur **uv** et le standard **`pyproject.toml`** :

* **Le fichier `uv.lock` (Garantie temporelle)** : C'est le point le plus crucial pour la science. Le fichier `uv.lock` fige l'empreinte exacte (les *hashs*) de chaque sous-bibliothèque utilisée. Si un chercheur clone le dépôt dans 5 ans, `uv` installera l'environnement mathématique au bit près, tel qu'il était aujourd'hui. Il n'y a plus aucun risque qu'une mise à jour casse la reproductibilité.
* **La vitesse de `uv`** : Écrit en Rust, `uv` remplace `pip` et `virtualenv` en étant 10 à 100 fois plus rapide pour résoudre et installer les lourdes dépendances du projet (GeoPandas, scikit-learn, etc.).
* **La centralisation (`pyproject.toml`)** : Toutes les métadonnées, les dépendances et les configurations des outils (Pytest, Ruff, Mypy) sont réunies au même endroit (selon le standard PEP 621), éliminant le chaos des anciens `setup.py` ou `setup.cfg`.
* **Les "Extras" intelligents (`[dev]` et `[docs]`)** : L'installation est modulaire. Un chercheur souhaitant faire tourner les algorithmes n'a pas besoin d'installer les outils lourds servant à construire le site web ou tester le code.

---

## 2. La séparation Code / Données (Git vs DVC)

**Le cauchemar classique** : Dans 95% des laboratoires, les chercheurs s'échangent des fichiers par mail ou sur des clés USB nommés `data_v1.csv`, `data_v2_FINAL.csv`. Quand vient l'heure de publier l'article, personne ne sait *exactement* quel fichier a été utilisé pour générer la Figure 3. Et on ne peut pas mettre 50 Go de données sur GitHub, car Git n'est pas fait pour ça et plante.

**La révolution DVC** : 
DVC fait pour la *Data* ce que Git fait pour le *Code*. Au lieu d'uploader les gros fichiers sur GitHub, DVC les envoie discrètement sur un stockage décentralisé "bon marché" (Google Drive, S3). Sur GitHub, DVC ne laisse qu'un minuscule fichier texte contenant un "hachage" (ex: `master_dataset.parquet.dvc`).

**Résultat magique** : Si dans 2 ans vous faites un `git checkout ancienne_branche`, puis tapez `dvc pull`, DVC ira télécharger *exactement* le bon jeu de données qui correspondait à votre code à la seconde près. C'est la garantie absolue de ne jamais "perdre" la donnée qui a justifié une publication.

---

## 3. Le Graphe de Dépendance (`dvc.yaml`)

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

## 4. Le Centre de Commandement : `params.yaml`

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

## 5. L'Orchestration avec le `Makefile`

Pour simplifier la vie des développeurs, la complexité des commandes est masquée derrière notre `Makefile`.

* `make setup` : Prépare l'environnement complet.
* `make data` : Demande à DVC de reconstruire uniquement le jeu de données maître.
* `make run-all` : Exécute la chaîne complète (Données $\to$ Modèles $\to$ Matrices Mathématiques $\to$ Figures $\to$ Tests unitaires).
* `make tests` : Lance la batterie de tests TDD (Test-Driven Architecture).

---

## 6. Le Suivi Scientifique avec MLflow

**Le cauchemar classique** : Pour trouver le bon seuil de clustering (ex: 5 clusters au lieu de 4), un chercheur lance son algorithme, note le score sur un post-it, change le paramètre, relance, et oublie ce qu'il a fait 3 jours plus tard. *"Comment j'avais fait pour obtenir cette super carte la semaine dernière ?"* $\to$ Perdu à jamais.

**La révolution MLflow** :
C'est un tableau de bord (un *dashboard*) automatisé. Chaque fois que le code tourne (`make run-all`), MLflow agit comme une "boîte noire d'avion". Il enregistre automatiquement : qui a lancé le code, à quelle heure, avec quel commit Git, **tous** les paramètres exacts du `params.yaml`, et les scores mathématiques en sortie (votre Indice de Theil, votre Gini, etc.).

**Résultat magique** : Sur l'interface visuelle de MLflow (accessible en tapant `make mlflow-ui`), vous pouvez sélectionner 5 anciennes exécutions, cliquer sur "Comparer", et MLflow vous sort un graphique croisé vous prouvant mathématiquement que *"C'est quand le paramètre Alpha était à 0.05 que le clustering était le plus stable"*. C'est un registre scientifique infalsifiable.

---

## Conclusion : Le Coffre-Fort Mathématique

Dans les revues scientifiques prestigieuses (qui exigent de plus en plus de garanties computationnelles pour éviter les fraudes), utiliser l'orchestration DVC/MLflow/uv signifie : **"Mon projet n'est pas un script Python jetable, c'est un coffre-fort mathématique auditable de bout en bout."**

Afin de préserver cette infrastructure de recherche, la communauté s'accorde sur 3 principes de co-développement :

1. **Paramétrage centralisé.** Lorsqu'un algorithme requiert un seuil ou une graine aléatoire (seed), la pratique est de l'ajouter dans `params.yaml` afin d'éviter les valeurs écrites en dur dans le code.
2. **Séparation du code et de la donnée.** Le dossier `data/` étant ignoré par Git, l'ajout de nouvelles données permanentes s'effectue naturellement via DVC.
3. **Évolution du pipeline.** Lorsqu'une contribution génère un nouvel output intermédiaire (ex: une nouvelle matrice), il suffit d'ajouter l'étape correspondante dans `dvc.yaml` pour que l'ensemble du système l'intègre.
