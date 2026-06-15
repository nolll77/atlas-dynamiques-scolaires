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

## Étape 3 : Développer et vérifier

Avant de commencer à coder, prenez le temps de lire le guide de contribution.

* Consultez le fichier `CONTRIBUTING.md`.
* Familiarisez-vous avec l'organisation du projet (notamment la distinction entre `src/` et `exploratory/`).
* Respectez les principes de qualité, de reproductibilité et de neutralité du projet.

Développez ensuite votre solution.

Avant chaque envoi, vérifiez que tout fonctionne correctement :

```bash
make tests
```

Enfin, enregistrez vos modifications avec des messages de commit explicites :

```text
feat: add IPS pipeline
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

## Étape 5 : Signature du CLA (Accord de contribution)

Lors de votre première Pull Request, un robot automatisé (CLA Assistant) publiera un commentaire vous invitant à signer l'accord de contribution du projet.

La procédure est simple : il vous sera demandé de publier une phrase précise en commentaire, par exemple :

```text
I have read the CLA Document and I hereby sign the CLA
```

Une fois ce commentaire publié, le robot validera automatiquement votre accord.

### Pourquoi cet accord ?

Le projet est développé sous licence MIT. Cela signifie que le code source est librement accessible et réutilisable par tous, dans les conditions prévues par cette licence.

Le CLA complète ce cadre en garantissant que les contributions intégrées au projet peuvent être utilisées, maintenues, distribuées et faire l'objet d'évolutions futures sans incertitude juridique.

Concrètement :

* Votre contribution est intégrée à une infrastructure open source accessible à tous.
* Les utilisateurs du projet peuvent réutiliser ce code conformément à la licence MIT.
* Les mainteneurs disposent des droits nécessaires pour maintenir et faire évoluer le projet dans la durée.
* Vous restez identifié comme contributeur via l'historique Git et les mécanismes habituels de reconnaissance des projets open source.

Les contributions intégrées au projet participent à la construction d'une infrastructure open source publiée sous licence MIT. Cette infrastructure peut être librement utilisée et réutilisée par tous, y compris les contributeurs, les mainteneurs, les chercheurs, les associations, les entreprises ou les citoyens, conformément aux conditions de cette licence.

---

## Étape 6 : Revue, validation et fusion

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
