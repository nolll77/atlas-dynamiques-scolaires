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

## 3. Les statuts "Skipped" tracent la feuille de route

Cette approche structure la suite de tests en **catalogue d'implémentation**. Chaque test ignoré cartographie une fonction mathématique restant à coder.

Voici le flux de travail (workflow) standard pour l'implémentation :

1. **Identification** : Consulter les [Matrices de Couverture](README.md) et repérer une formule mathématique avec le statut `⚠️ Skipped` (par exemple, la *Distance de Mahalanobis*).
2. **Activation** : Dans le code du test correspondant, supprimer l'étiquette `@pytest.mark.skip`.
3. **Validation de l'échec (Red)** : Exécuter les tests localement (`make tests`). Le test échoue logiquement ❌ puisque l'algorithme n'existe pas encore.
4. **Implémentation (Green)** : Écrire l'algorithme en Python dans le dossier source approprié (`src/atlas/features/socle_1_mathematiques/` ou `socle_2_dynamique/`) jusqu'à ce que la sortie mathématique valide le test (✅).
5. **Intégration (Refactor)** : Ouvrir une *Pull Request*. La Matrice de Couverture passe au statut "✅ Implémenté".

Ce processus garantit que l'algorithme intégré respecte strictement la théorie sociologique : le test agit comme un filet de sécurité structurel.

## 4. Exemple de cycle de développement : La Distance de Mahalanobis

Voici l'application directe de ce flux de travail.

**Étape 1 : L'identification (Jaune ⚠️)**  
Dans le fichier `tests/socle_1_mathematiques/test_00_statistiques.py`, le test est structuré à l'avance :
```python
@pytest.mark.skip(reason="À implémenter")
def test_distance_mahalanobis():
    # Le test contient les données en entrée (inputs) 
    # et le résultat mathématique exact attendu (outputs).
    assert calculer_mahalanobis(x, covariance) == resultat_attendu
```

**Étape 2 : L'activation (Rouge ❌)**  
La ligne `@pytest.mark.skip` est retirée. La commande `make tests` est exécutée.
L'algorithme `calculer_mahalanobis` n'existant pas encore dans le code source, le test échoue (Red).

**Étape 3 : L'implémentation algorithmique (Le Code Source)**  
L'algorithme est codé dans le dossier `src/atlas/features/socle_1_mathematiques/` :
```python
def calculer_mahalanobis(x, covariance):
    # Implémentation réelle de l'équation avec numpy / scipy
    return resultat
```

**Étape 4 : La validation (Vert ✅)**  
L'exécution de `make tests` valide le calcul. L'algorithme produit exactement la valeur théorique attendue. Le test passe au vert. 
Le code est prêt pour l'intégration via *Pull Request*.
