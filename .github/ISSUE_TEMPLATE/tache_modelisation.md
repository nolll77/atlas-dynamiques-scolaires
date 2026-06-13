---
name: Tâche de Modélisation (Algorithme / Data)
about: Créer une issue pour un nouveau modèle, clustering, ou pipeline de données
title: "[Modèle] "
labels: ''
assignees: ''
---

## Contexte Analytique
*Pourquoi fait-on cette issue ? Vulgariser l'objectif sociologique ou mathématique ici.*


## Périmètre Technique (Ouvert aux contributions)
*Que doit faire la machine ? Lister les packages Python attendus, les datasets croisés et le dossier cible (src/ ou exploratory/).*


## Périmètre Éditorial (Réservé à l'Auteur)
*Que fera l'auteur de ce code ? Préciser ici la manière dont les résultats seront exploités.*


---
### 🛠 Checklist d'Infrastructure (Obligatoire avant de clore l'issue)
Afin de garantir la reproductibilité et le suivi des expériences :
- [ ] Le code est placé dans le bon répertoire (`src/` ou `exploratory/`).
- [ ] Les dépendances ont été ajoutées via `uv add <package>` si nécessaire.
- [ ] J'ai importé `mlflow` dans mon script Python.
- [ ] J'ai utilisé `mlflow.log_param()` pour enregistrer les paramètres clés de l'algorithme (ex: k clusters).
- [ ] J'ai utilisé `mlflow.log_metric()` ou `mlflow.log_artifact()` pour enregistrer les résultats.
