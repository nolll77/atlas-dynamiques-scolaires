# Parcours Contributeur : Comment contribuer de A à Z ?

Bienvenue !

Vous souhaitez consacrer un peu de votre temps et de votre expertise à la construction de l'Atlas des Dynamiques Scolaires ? Ce guide détaille étape par étape le fonctionnement de notre collaboration.

## Avant de commencer

Avant de choisir une issue, nous vous recommandons de :

* Lire le README afin de comprendre les objectifs du projet.
* Parcourir les issues ouvertes pour identifier les sujets sur lesquels vous souhaitez contribuer.
* Vérifier qu'aucune Pull Request n'est déjà en cours sur le même sujet.
* Poser vos questions dans les discussions ou directement sur une issue si certains points ne sont pas clairs.

Pour les contributions importantes (nouveau pipeline de données, évolution de l'architecture, ajout d'une nouvelle source de données, etc.), il est préférable d'échanger au préalable afin de valider l'approche retenue.

---

## Étape 1 : Choisir une Issue

Sur la page **Issues** du dépôt GitHub, vous trouverez la liste des tâches ouvertes.

Privilégiez les issues qui ne sont pas encore assignées à un contributeur.

**Attention :** si vous n'êtes pas mainteneur du projet, GitHub ne vous permet généralement pas de vous assigner vous-même une issue.

**Comment faire ?**

Ouvrez simplement l'issue qui vous intéresse et laissez un commentaire, par exemple :

> Bonjour, je suis intéressé(e) pour prendre en charge cette issue.

Un mainteneur pourra alors vous l'assigner officiellement.

---

## Étape 2 : Préparer votre environnement

Une fois l'issue assignée, créez votre propre copie de travail du projet.

### 1. Créez un fork

Cliquez sur le bouton **Fork** en haut à droite du dépôt GitHub afin de créer une copie du projet sur votre propre compte.

### 2. Clonez votre fork

```bash
git clone git@github.com:VOTRE_PSEUDO/atlas-dynamiques-scolaires.git
cd atlas-dynamiques-scolaires
```

### 3. Créez une branche dédiée

Créez une branche spécifique à votre contribution :

```bash
git checkout -b issue-002-pipeline-ips
```

### 4. Installez l'environnement

```bash
make setup
```

---

## Étape 3 : Développer et vérifier (Test-Driven Architecture)

L'Atlas repose sur une architecture pilotée par les tests (Test-Driven Architecture) extrêmement stricte. Avant de commencer à coder, prenez le temps de comprendre comment s'organise la validation :

* Consultez le fichier `CONTRIBUTING.md`.
* Familiarisez-vous avec l'organisation du projet (notamment la distinction entre `src/` et `exploratory/`).
* Lisez attentivement le **[Laboratoire de Validation (Tests)](tests/README.md)**. Il contient la philosophie de développement et les matrices de couverture.

Pour l'implémentation d'une formule algorithmique, le flux de travail est le suivant :

1. **Identification** : Choisissez un test marqué `⚠️ Skipped` dans nos matrices de couverture.
2. **Activation (Rouge ❌)** : Supprimez le tag `@pytest.mark.skip` du test correspondant, puis lancez la commande `make tests`. Le test échouera : c'est le point de départ.
3. **Développement** : Écrivez l'algorithme dans le dossier source approprié (`src/atlas/features/socle_1_mathematiques/` ou `socle_2_dynamique/`).
4. **Validation (Vert ✅)** : Relancez `make tests` jusqu'à ce que votre code passe le test avec succès.

Enfin, enregistrez vos modifications avec des messages de commit explicites (convention Conventional Commits) :

```text
feat: implémentation de la distance de Mahalanobis
```

---

## Étape 4 : Soumettre votre travail (Pull Request)

Une fois votre développement terminé :

### 1. Poussez votre branche

```bash
git push origin votre-branche
```

### 2. Ouvrez une Pull Request

Rendez-vous sur GitHub puis cliquez sur **Compare & pull request**.

### 3. Décrivez votre contribution

Expliquez clairement :

* ce qui a été réalisé ;
* les choix techniques effectués ;
* les éventuels points nécessitant une attention particulière.

---

## Étape 5 : Revue, validation et fusion

Après l'ouverture de votre Pull Request, notre système d'intégration continue (CI) exécutera automatiquement les tests du projet.

Un mainteneur pourra également effectuer une revue de votre code et vous proposer des ajustements ou demander des précisions.

Ces échanges font partie du processus normal de collaboration open source.

Lorsque :

* les tests sont validés ;
* la revue est satisfaisante ;
* les éventuelles remarques ont été traitées ;

votre contribution pourra être fusionnée dans la branche principale du projet.

---

## Merci !

Chaque contribution, même modeste, participe à l'amélioration de l'Atlas des Dynamiques Scolaires.

Merci pour votre temps, votre expertise et votre volonté de contribuer à un projet ouvert, réutilisable et utile à tous.
