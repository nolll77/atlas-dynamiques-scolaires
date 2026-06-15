# Parcours Collaborateur : Comment contribuer de A à Z ?

Bienvenue ! Vous souhaitez donner un peu de votre temps et de votre expertise technique pour construire l'Atlas des Dynamiques Scolaires ? Ce guide détaille étape par étape le fonctionnement de notre collaboration.

## Étape 1 : Choisir une Issue (Ticket)

Sur la page **Issues** de GitHub, vous trouverez la liste des tâches ouvertes. Cherchez celles qui n'ont personne d'assigné (les issues "libres").
* **Attention :** Sur GitHub, vous ne pouvez pas vous assigner une issue vous-même d'un simple clic si vous n'êtes pas administrateur du projet.
* **Comment faire ?** Ouvrez l'issue qui vous intéresse et postez un commentaire disant par exemple : *"Bonjour, je suis intéressé(e) pour prendre en charge cette issue !"*. L'auteur du projet vous l'assignera officiellement en retour.

## Étape 2 : Préparer son environnement

Une fois l'issue assignée, vous devez créer votre propre copie de travail :
1. Cliquez sur le bouton **Fork** en haut à droite du dépôt GitHub pour copier le projet sur votre propre compte.
2. Clonez votre copie sur votre ordinateur :
   ```bash
   git clone git@github.com:VOTRE_PSEUDO/atlas-dynamiques-scolaires.git
   cd atlas-dynamiques-scolaires
   ```
3. Créez une branche dédiée à votre issue (ex: `git checkout -b issue-002-pipeline-ips`).
4. Installez l'environnement avec notre gestionnaire :
   ```bash
   make setup
   ```

## Étape 3 : Coder et vérifier

* Lisez attentivement le [Guide de Contribution (CONTRIBUTING.md)](CONTRIBUTING.md) pour comprendre la philosophie du code (dossiers `src/` vs `exploratory/`) et nos principes de neutralité.
* Écrivez votre code !
* Avant de sauvegarder, vérifiez que tout est au vert :
  ```bash
  make tests
  ```
* Sauvegardez vos changements (Commit) en suivant des messages clairs (ex: `feat: add IPS pipeline`).

## Étape 4 : Soumettre son travail (Pull Request)

1. Poussez votre code sur votre copie GitHub (`git push origin votre-branche`).
2. Allez sur la page du projet principal et cliquez sur **Compare & pull request**.
3. Remplissez le formulaire de la Pull Request en expliquant ce que vous avez fait.

## Étape 5 : La signature du CLA (Accord de contribution)

Dès que vous ouvrez votre première Pull Request, un **robot automatisé (CLA Assistant)** va poster un commentaire. Cet accord légal est indispensable pour intégrer votre code à l'infrastructure open-source tout en protégeant le projet.
* **Que devez-vous faire ?** C'est très simple. Le robot vous demandera de poster un commentaire avec une phrase exacte en anglais, généralement : 
  `I have read the CLA Document and I hereby sign the CLA`
* Copiez-collez cette phrase et postez-la en commentaire. Le robot validera instantanément votre accord.

## Étape 6 : Validation et Fusion

Notre système d'Intégration Continue (CI) va alors tester automatiquement votre code. Si la CI est verte et que la relecture est bonne, votre code sera fusionné dans le projet principal. 

**Merci infiniment pour votre temps et vos compétences !**
