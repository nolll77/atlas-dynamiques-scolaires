# Comprendre notre architecture : La validation par les tests (Test-Driven Architecture)

Bienvenue dans le laboratoire de validation de l'Atlas. Si vous explorez notre dépôt, vous avez sans doute remarqué deux choses inhabituelles :
1. Nous possédons une vaste suite de tests automatisés couvrant des dizaines de formules sociologiques et mathématiques.
2. Pourtant, la quasi-totalité de ces tests sont volontairement marqués comme "Ignorés" (`⚠️ Skipped`) dans notre intégration continue (CI). 

Ce document vous explique pourquoi ce choix n'est pas une erreur, mais le fondement même de notre méthode de développement et de votre future contribution.

## 1. La théorie précède le code

Dans un projet scientifique comme l'Atlas, l'erreur algorithmique n'est pas permise. Pour garantir une fiabilité absolue, nous appliquons les principes de la **Test-Driven Architecture (Architecture pilotée par les tests)** :

* **L'exigence (Le Manifeste)** : Avant d'écrire la moindre ligne de code, l'auteur a formellement défini 63 axiomes et formules sociologiques dans les manifestes théoriques (31 pour le Socle 1, 32 pour le Socle 2).
* **Le moule (Le Test)** : Nous avons ensuite traduit chacune de ces formules théoriques en un "test unitaire" strict. Ce test définit informatiquement les entrées (données) et la sortie mathématique exacte attendue.
* **Le vide (L'Algorithme)** : À l'heure actuelle, la majorité de ces algorithmes *n'ont pas encore été codés*. L'Atlas dispose de ses tests (les gardes-fous), mais attend ses algorithmes (le moteur). Seules quelques fondations comme l'Indice de Theil ou l'Entre-Soi sont déjà finalisées.

## 2. Pourquoi "Ignorer" (Skipper) les tests ?

Si nous laissions la suite de tests s'exécuter normalement aujourd'hui, le "robot" de GitHub chercherait à tester des algorithmes qui n'existent pas encore. Résultat : une immense croix rouge ❌ permanente s'afficherait sur notre dépôt.

Une telle erreur bloquerait le travail de tous les développeurs et donnerait la fausse impression que le projet est "cassé" ou instable.

Pour contourner ce problème, nous avons placé l'étiquette `@pytest.mark.skip` sur tous les tests orphelins. Le robot de GitHub comprend ainsi le message : *"Le test existe, il est légitime, mais ne l'exécute pas pour l'instant"*. Le dépôt reste propre, avec une belle validation verte globale ✅, tout en conservant une trace exacte de ce qu'il reste à construire.

## 3. Les "Skipped" sont votre feuille de route (To-Do List)

Cette approche transforme notre suite de tests en un véritable **catalogue d'appels à contribution**. Chaque test ignoré (jaune) est une mission qui n'attend qu'un développeur pour lui donner vie.

Voici très concrètement comment contribuer à l'Atlas :

1. **Choisissez votre mission** : Consultez nos [Matrices de Couverture](README.md) et repérez une formule mathématique marquée d'un statut `⚠️ Skipped` (par exemple, la *Distance de Mahalanobis*).
2. **Réveillez le test** : Dans le code du test correspondant, supprimez simplement l'étiquette `@pytest.mark.skip`.
3. **Observez l'échec (Red)** : Exécutez les tests localement (`make tests`). Le test va logiquement échouer ❌ puisque l'algorithme n'existe pas encore.
4. **Implémentez (Green)** : Écrivez l'algorithme en Python dans le dossier source approprié (`src/atlas/features/socle_1_mathematiques/` ou `socle_2_dynamique/`) jusqu'à ce que le test valide vos calculs et passe au vert ✅.
5. **Soumettez (Refactor)** : Ouvrez une *Pull Request*. La Matrice de Couverture gagnera alors un nouveau statut "✅ Implémenté" grâce à vous !

En suivant ce processus, vous avez la **garantie absolue** que le code que vous intégrez respecte parfaitement la théorie sociologique : le test était là bien avant vous, agissant comme un filet de sécurité intransigeant.

## 4. Exemple concret : La Distance de Mahalanobis

Voici très exactement ce que vit un développeur qui s'attaque à une formule de l'Atlas.

**Étape 1 : Le repérage (Jaune ⚠️)**  
Dans le fichier `tests/socle_1_mathematiques/test_00_statistiques.py`, le développeur trouve la fonction de test préparée à l'avance :
```python
@pytest.mark.skip(reason="À implémenter")
def test_distance_mahalanobis():
    # Le test contient déjà les données factices (inputs) 
    # et le résultat mathématique exact attendu (outputs).
    assert calculer_mahalanobis(x, covariance) == resultat_attendu
```

**Étape 2 : Le passage à l'acte (Rouge ❌)**  
Le développeur efface simplement la ligne `@pytest.mark.skip`. Il tape `make tests` dans son terminal.
Le système cherche la fonction `calculer_mahalanobis` dans le code source, ne la trouve pas, et fait échouer le test (Red). C'est le signal de départ.

**Étape 3 : Le développement (Le Code Source)**  
Le développeur se rend dans le dossier `src/atlas/features/socle_1_mathematiques/` et écrit le véritable code algorithmique :
```python
def calculer_mahalanobis(x, covariance):
    # Implémentation réelle de l'équation avec numpy / scipy
    return resultat
```

**Étape 4 : La victoire (Vert ✅)**  
Il relance `make tests`. Cette fois, son code source produit exactement la valeur validée par la théorie. Le test passe au vert. 
Il peut fièrement soumettre son code : la rigueur scientifique est sauvée !
