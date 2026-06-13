# Guide de Contribution (À lire obligatoirement)

Bienvenue dans le dépôt de **l'Atlas des Dynamiques Scolaires**. 

Ce projet open-source est atypique : il se situe à la croisée de la **sociologie quantitative**, de la **géographie spatiale** et du **machine learning**. 
Pour garantir la rigueur scientifique de l'ouvrage final, nous imposons à tous les contributeurs de lire et de respecter les principes d'architecture et d'épistémologie détaillés ci-dessous.

---

## 1. Architecture du Code : `src/` vs `exploratory/`

Vous remarquerez que les issues vous demandent parfois de placer votre code dans `src/` et parfois dans `exploratory/`. Cette séparation n'est pas qu'informatique, elle est **épistémologique**.

### Le dossier `src/` (Le Socle de Certitudes)
- **Quoi ?** Le pipeline de données, le clustering de base, le calcul des index de ségrégation (Gini, Theil, Duncan).
- **Pourquoi ?** C'est le "cœur du réacteur". Ce code manipule des données réelles et indiscutables (ex: la moyenne d'un IPS). Il doit être parfait, incassable, testé via `pytest`, et optimisé.

### Le dossier `exploratory/` (Le Laboratoire R&D)
- **Quoi ?** Les modèles de Markov Cachés (HMM), les Graphes Causaux (DAG), les Réseaux de Neurones Graphiques (GNN), ou la géométrie riemannienne.
- **Pourquoi ?** Il y a une différence majeure entre "constater une moyenne" et "faire tourner un modèle de prédiction probabiliste". Les algorithmes avancés font des paris sur la réalité. En séparant physiquement ce code, nous prouvons notre rigueur scientifique : nous séparons le *socle statique* des *expériences de modélisation dynamique*.
- **Votre liberté :** Quand un ticket vise le dossier `exploratory/`, cela veut dire que vous avez le droit d'expérimenter, de crasher, de tester des hyperparamètres exotiques. C'est de la R&D.

---

## 2. Règle Éthique : Aucune imputation d'intention

L'Atlas décrit des **structures mathématiques**, il ne juge pas les comportements humains.
- Si un algorithme (ex: Louvain ou CAH) isole un groupe de lycées très favorisés, nous le décrivons comme un "cluster statistiquement homogène". 
- **Interdiction stricte :** Vous ne devez jamais écrire dans vos Pull Requests, vos commentaires de code ou vos analyses que *"tel lycée trie ses élèves"* ou *"telle direction exclut les pauvres"*. Le modèle montre des *résultats*, il ne lit pas dans les pensées des acteurs. L'absence de mixité est traitée comme un phénomène systémique (souvent co-produit par le marché immobilier), et non comme une volonté malveillante locale.

---

## 3. Séparation des Rôles : Code vs Narration

Ce dépôt sert à générer le socle mathématique, statistique et visuel d'une **trilogie littéraire**.
- **Votre rôle (Contributeur Technique) :** Vous produisez le code robuste, les modèles mathématiques purs, et les visualisations (cartes, réseaux, graphiques). Vous résolvez le "Périmètre Technique" des issues.
- **Le rôle de l'Auteur Principal :** L'interprétation sociologique finale, la narration, et la rédaction des chapitres de l'ouvrage sont du ressort exclusif de l'auteur. Le "Périmètre Éditorial" défini dans les issues lui est strictement réservé.

---

## 4. Standard de Création des Issues (Règles "Anti-Subordination")

Que ce soit pour ouvrir un ticket sur une nouvelle analyse, un bug, ou une tâche d'infrastructure, **toute nouvelle issue doit obligatoirement respecter ce format standard**. Il garantit le respect de la règle n°3 et évite les malentendus.

**1. Le système de Labels croisés**
Toute issue doit porter deux types d'étiquettes :
- *Labels descriptifs* : `tome-1`, `data`, `network`, `exploratory`, etc.
- *Label de difficulté* : `difficulty: easy` (DevOps, Data cleaning, Dataviz standard), `difficulty: medium` (Statistiques, Clustering), ou `difficulty: hard` (Machine Learning, Modèles probabilistes et spatiaux).

**2. Le Triptyque de Description (Template)**
Ne parlez jamais d'"Objectifs" ou d'"Actions" (qui sonnent comme des ordres). Utilisez ce gabarit exact :

- **Contexte Analytique :** *Pourquoi fait-on cette issue ?* Si l'issue fait appel à des concepts complexes (HMM, Variété Riemannienne, CAH), il est obligatoire de les "vulgariser" ici de manière pédagogique pour qu'un développeur comprenne le but sociologique sans être un expert du domaine.
- **Périmètre Technique (Ouvert aux contributions) :** *Que doit faire la machine ?* Lister clairement les packages Python attendus, les datasets croisés (ex: IPS vs DVF) et le dossier cible (`src/` ou `exploratory/`).
- **Périmètre Éditorial (Réservé à l'Auteur) :** *Que fera l'auteur de ce code ?* Préciser ici la manière dont les résultats seront exploités dans la narration finale, en rappelant les garde-fous éthiques.

---

## 5. Experiment Tracking (MLflow Obligatoire)

Toute issue impliquant la création ou la modification d'un algorithme mathématique (clustering, modèle de Markov, DAG, etc.) doit impérativement utiliser **MLflow** pour enregistrer ses résultats. L'infrastructure est déjà en place (cf. Issue #003).

Dans vos scripts Python, vous devez :
1. Importer `mlflow`.
2. Logger les hyperparamètres avec `mlflow.log_param()` (ex: nombre de clusters, hyperparamètres du modèle).
3. Logger les métriques avec `mlflow.log_metric()` (ex: score de silhouette, modularité).

Un [Template d'Issue GitHub](.github/ISSUE_TEMPLATE/tache_modelisation.md) inclut une checklist que vous devrez valider avant de soumettre votre code.

---

Merci d'avance pour votre expertise technique. En respectant ces règles, vous contribuez à faire de ce projet une référence d'honnêteté intellectuelle et de rigueur open-source !
