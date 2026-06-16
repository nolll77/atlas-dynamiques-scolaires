#  Socle Mathématique et Algorithmique (Formulaire Complet)

> **GUIDE DE CONSTRUCTION (MANIFESTE DU SOCLE)**
> 
> **Qu'est-ce qu'un Socle (ou Lexique Formel) ?**
> C'est le référentiel absolu et purgé de tout bruit narratif. Il extrait, nettoie et standardise la "moelle technique", mathématique ou algorithmique d'un projet pour la rendre exploitable par des machines (code) ou des pairs (scientifiques).
> 
> **Le Standard des 9 Tags (Le DAG d'Ingénierie Ultime) :**
> Chaque formule doit pouvoir être lue et implémentée comme une fonction autonome et sécurisée grâce à ces 9 clés :
> 1. **Quoi :** La traduction sociologique et concrète de l'équation (interdiction de froideur mathématique).
> 2. **Pourquoi :** L'objectif politique ou interprétatif (à quoi ça sert dans le système).
> 3. **Inputs (Entrées) :** Les données brutes, vecteurs ou matrices nécessaires au calcul.
> 4. **Outputs (Sorties) :** Le format mathématique du résultat retourné.
> 5. **Dépendance Amont :** Prérequis. Quelle autre formule doit obligatoirement être calculée *avant*.
> 6. **Dépendance Aval :** Impact. Quelle(s) formule(s) utiliseront ce résultat *après* (pour le chaînage).
> 7. **Complexité Algorithmique :** Ordre de grandeur informatique (Big O) et implications matérielles.
> 8. **Contraintes & Hypothèses (Assumptions) :** Les postulats théoriques traduits dans le strict contexte matériel de l'étude (ex: les lycées, le public/privé, les flux d'élèves).
> 9. **Limites / Biais (Edge Cases) :** Les situations extrêmes de la vraie vie (géographie, politique locale) où la formule "craque" ou donne des résultats absurdes.
>
> **LA LOI DE L'ANCRAGE TERRAIN :**
> Cette loi s'applique de manière totalitaire à **tous** les tags explicatifs (en particulier le *Quoi* et le *Pourquoi*). La froideur mathématique désincarnée, la "vulgarisation" poétique abstraite ou le jargon purement académique sont **strictement interdits**. Toute abstraction mathématique doit être immédiatement traduite en utilisant exclusivement **les objets réels du terrain étudié** (l'IPS, les élèves, les lycées, la ségrégation, les ghettos, le public/privé). La description doit toujours "situer l'action" dans la réalité physique et sociale du système éducatif.

---

> [!NOTE]
> **VALIDATION ARCHITECTURALE (TDD)**
> L'intégralité des 31 formules de ce manifeste est verrouillée par des tests informatiques.
> 👉 **Voir le suivi :** [Matrice de Couverture à 100% des Formules](../tests/socle_1_mathematiques/MATRICE_DE_COUVERTURE_SOCLE_1.md)
> 👉 **Documentation technique :** [README du Socle 1](../tests/socle_1_mathematiques/README.md)

---


## 0. Fondations Statistiques (Analyse Exploratoire)

### Normalisation (Z-Score) et Indice d'Entre-Soi
**Formule :**

$$
\Huge z = \frac{x - \mu}{\sigma} \quad \text{et} \quad E^* = z_{IPS} - z_{\sigma}
$$

<br>

*   **Quoi :** Ajustement statistique permettant de comparer objectivement la position de n'importe quel lycée par rapport à la moyenne régionale stricte.

*   **Légende :** 
    *   $z$ : score normalisé *(ex : l'avance ou le retard d'un lycée par rapport à la moyenne académique)*.
    *   $x$ : valeur brute *(ex : l'IPS brut du lycée à 130)*.
    *   $\mu$ : moyenne globale *(ex : l'IPS moyen de tous les lycées de la région, à 105)*.
    *   $\sigma$ : écart-type *(ex : la dispersion de l'IPS en Île-de-France)*.
    *   $E^*$ : Indice d'entre-soi *(ex : un score élevé prouve que le lycée est une bulle fermée)*.
    *   $z_{IPS}$ : IPS normalisé du lycée *(ex : le lycée est dans le Top 1% national)*.
    *   $z_{\sigma}$ : écart-type interne normalisé *(ex : le manque de diversité à l'intérieur même des murs du lycée)*.


*   **Pourquoi :** Mesurer rigoureusement "l'entre-soi" : un lycée fermé a un IPS très haut et un écart-type très bas.

*   **Inputs :** Vecteur des moyennes IPS ($x$), moyenne globale ($\mu$), écart-type ($\sigma$).

*   **Outputs :** Vecteur de scores $E^*$ (scalaire par établissement).

*   **Dépendance Amont :** Aucune (données brutes).

*   **Dépendance Aval :** Distance de Mahalanobis.

*   **Complexité Algorithmique :** O(N) — Calcul ultra-rapide, une simple passe sur la donnée suffit.

*   **Contraintes & Hypothèses (Assumptions) :** Suppose que la répartition des lycées selon l'IPS ressemble à une cloche équilibrée autour de la moyenne, sans quoi la notion même de note "extrême" perd son sens.

*   **Limites / Biais (Edge Cases) :** Le calcul devient aveugle s'il y a un lycée ultra-élitiste avec 100% de CSP+, il va étirer l'écart-type et écraser tous les autres vers la moyenne.

### Distance de Mahalanobis
**Formule :**

$$
\Huge D_M(x) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}
$$

<br>

*   **Quoi :** Détection algorithmique des "lycées ovnis" (ceux dont le profil social ou académique est totalement déconnecté de la norme du système).

*   **Légende :** 
    *   $D_M(x)$ : distance d'anomalie *(ex : à quel point ce lycée est un "OVNI" dans le paysage scolaire)*.
    *   $x$ : vecteur de caractéristiques *(ex : IPS, part de boursiers, taux de mention au bac du lycée)*.
    *   $\mu$ : profil moyen académique *(ex : le portrait-robot du lycée francilien standard)*.
    *   $\Sigma^{-1}$ : matrice corrigeant les redondances *(ex : empêche de compter deux fois la richesse si on a déjà l'IPS et le taux de CSP+)*.


*   **Pourquoi :** Identifier les vrais "outliers" (anomalies statistiques), comme les lycées ultra-élitistes ou exceptionnellement mixtes.

*   **Inputs :** Matrice de features (IPS, CSP+, etc.), Matrice de covariance inverse $\Sigma^{-1}$.

*   **Outputs :** Vecteur de distances (scalaire positif par établissement).

*   **Dépendance Amont :** Normalisation Z-Score.

*   **Dépendance Aval :** Distance Sociale et Similarité ($W_{ij}$).

*   **Complexité Algorithmique :** O(N * D² + D³) — Très rapide sur quelques variables (D), mais l'inversion de matrice fera crasher le serveur si on dépasse les 10 000 dimensions.

*   **Contraintes & Hypothèses (Assumptions) :** Suppose que les variables ont des relations linéaires entre elles (ex: plus l'IPS monte, plus la part de CSP+ monte de façon prévisible).

*   **Limites / Biais (Edge Cases) :** Si deux variables mesurent exactement la même chose (colinéarité parfaite), la matrice devient mathématiquement impossible à inverser et le code plantera.

### Indice de Dissimilarité de Duncan ($D$)
**Formule :**

$$
\Huge D = \frac{1}{2} \sum \left| \frac{priv\acute{e}_i}{Total\_Priv\acute{e}} - \frac{public_i}{Total\_Public} \right|
$$

<br>

*   **Quoi :** Mesure de la fracture sociale évaluant exactement quel pourcentage d'élèves devrait changer de lycée pour que la zone étudiée atteigne une mixité parfaite.

*   **Légende :** 
    *   $D$ : Indice de dissimilarité *(ex : le taux de "séparation pure" entre deux publics)*.
    *   $priv\acute{e}_i$ : effectif privé de la sous-zone $i$ *(ex : les 500 élèves inscrits dans le privé dans le 16ème arrondissement)*.
    *   $Total\_Priv\acute{e}$ : total global du privé *(ex : l'ensemble des élèves du privé à Paris)*.


*   **Pourquoi :** Démontrer que la ségrégation institutionnelle (séparation public/privé) est maximale dans les zones riches.

*   **Inputs :** Effectifs agrégés public/privé par unité géographique (ex: commune).

*   **Outputs :** Scalaire $D \in [0, 1]$ par zone étudiée.

*   **Dépendance Amont :** Aucune.

*   **Dépendance Aval :** Indice de Fragmentation par Établissement ($F_i$).

*   **Complexité Algorithmique :** O(N) — Traversée linéaire très simple.

*   **Contraintes & Hypothèses (Assumptions) :** Le système scolaire est vu de manière fermée : on suppose que pour rééquilibrer la mixité, un élève qui quitte un lycée privé doit obligatoirement être remplacé par un élève du public, dans un jeu de vases communicants stricts.

*   **Limites / Biais (Edge Cases) :** Biais de la petite taille : si on l'applique sur un tout petit quartier avec 3 élèves du privé, la formule hallucine une ségrégation maximale de 100%.

### Indice de Fragmentation par Établissement ($F_i$)
**Formule :**

$$
\Huge F_i = \alpha \cdot B_i + \beta \cdot D_i + \gamma \cdot \Delta Var_i + \delta \cdot R_i
$$

<br>

*   **Quoi :** Score d'alerte identifiant les établissements qui agissent comme des "murs" bloquant la mixité ou des "pompes" aspirant l'élite du territoire.

*   **Légende :** 
    *   $F_i$ : Indice de dangerosité ségrégative *(ex : le niveau de responsabilité de ce lycée spécifique dans la fracture de sa ville)*.
    *   $B_i$ : Rôle de pont *(ex : ce lycée est-il le seul carrefour de mixité du quartier ?)*.
    *   $D_i$ : Isolement local *(ex : à quel point il diffère du collège d'en face)*.
    *   $\Delta Var_i$ : Poids dans l'inégalité globale *(ex : sa part de responsabilité dans le Theil total)*.
    *   $R_i$ : Saut hiérarchique *(ex : son niveau d'inaccessibilité pour les classes moyennes)*.
    *   $\alpha, \beta, \gamma, \delta$ : pondérations politiques.


*   **Pourquoi :** Classer mathématiquement le pouvoir "structurant" (pont) ou "fragmentant" d'un lycée sur l'ensemble du système.

*   **Inputs :** Betweenness $B_i$, Duncan $D_i$, Variance $\Delta Var_i$, Rupture $R_i$.

*   **Outputs :** Scalaire $F_i$ de "dangerosité ségrégative" par lycée.

*   **Dépendance Amont :** Centralité (Bloc 2), Duncan (Bloc 0), Mojena (Bloc 5).

*   **Dépendance Aval :** Aucune (Indice final de restitution).

*   **Complexité Algorithmique :** O(1) pour l'agrégation finale, une fois que tous les inputs ont été calculés au préalable.

*   **Contraintes & Hypothèses (Assumptions) :** On suppose que le rôle de "pont" d'un lycée est la variable structurante dominante qui détermine sa capacité à atténuer ou renforcer la fracture sociale globale.

*   **Limites / Biais (Edge Cases) :** Complètement instable si on modifie arbitrairement les poids (alpha/beta). Un lycée peut passer de "pont" à "danger" juste en changeant un coefficient de 0.1.

---

## 1. Topologie et Distances

### Distance Ultramétrique (Hiérarchie)
**Formule :**

$$
\Huge d_U(i,j) \le \max(d_U(i,k), d_U(k,j))
$$

<br>

*   **Quoi :** Modélisation mathématique stricte mesurant l'épaisseur du "plafond de verre" séparant deux lycées de castes sociales différentes.

*   **Légende :** 
    *   $d_U(i,j)$ : hauteur du plafond de verre séparant deux lycées *(ex : l'impossibilité sociologique pour un élève du lycée $i$ de côtoyer un élève du lycée $j$)*.
    *   $k$ : un lycée intermédiaire *(ex : un lycée de classe moyenne servant de tampon)*.


*   **Pourquoi :** Modéliser la société scolaire comme des strates étanches et mutuellement exclusives.

*   **Inputs :** Dendrogramme issu d'un algorithme de clustering (ex: Ward).

*   **Outputs :** Matrice des distances ultramétriques $NxN$.

*   **Dépendance Amont :** Matrice de distance de base (Mahalanobis ou Euclidienne).

*   **Dépendance Aval :** Critère de Mojena, Tension Ultramétrique.

*   **Complexité Algorithmique :** O(N³) — Faire ça sur 500 lycées prend 1 seconde. Le faire sur 2 millions d'élèves fera exploser la RAM du serveur, il faut utiliser un cluster Cloud pour ça.

*   **Contraintes & Hypothèses (Assumptions) :** La société scolaire fonctionne selon des castes fermées et pyramidales : on présuppose qu'il est impossible pour un lycée ou un élève d'avoir un pied dans la bourgeoisie et un autre dans la classe moyenne.

*   **Limites / Biais (Edge Cases) :** S'il y a des lycées "hybrides" qui n'appartiennent à aucun groupe clair, l'algorithme va les forcer brutalement dans la branche la moins pire, faussant l'architecture.

### Distance Sociale et Similarité (Poids du Graphe)
**Formule :**

$$
\Huge W_{ij} = \exp\left(-\frac{D_{ij}}{\sigma}\right)
$$

<br>

*   **Quoi :** Calcul de la probabilité réelle que des élèves de deux lycées distincts se croisent ou se ressemblent, en fonction du gouffre social qui les sépare.

*   **Légende :** 
    *   $W_{ij}$ : probabilité d'échange entre deux lycées *(ex : les chances réelles que les élèves de ces deux lycées se croisent au sport ou dans les transports)*.
    *   $D_{ij}$ : distance pure *(ex : l'écart d'IPS cumulé à la distance kilométrique)*.
    *   $\sigma$ : paramètre de lissage *(ex : la tolérance globale de la société au mélange)*.


*   **Pourquoi :** Permettre de tracer les arêtes du graphe continu des lycées franciliens (réseau affinitaire).

*   **Inputs :** Matrice de distances euclidiennes ou de Mahalanobis $D_{ij}$, paramètre de lissage $\sigma$.

*   **Outputs :** Matrice d'adjacence pondérée $W_{ij} \in [0, 1]$.

*   **Dépendance Amont :** Distance de Mahalanobis (Bloc 0).

*   **Dépendance Aval :** Modularité Louvain, Centralité, Tension Ultramétrique.

*   **Complexité Algorithmique :** O(N²) — Calculer la distance de chaque lycée avec tous les autres crée une matrice dense qui devient ultra-lourde si N dépasse 50 000.

*   **Contraintes & Hypothèses (Assumptions) :** On postule que la probabilité que deux lycées échangent (flux d'élèves, amitiés) chute de manière purement mécanique et prévisible à mesure que l'écart d'IPS ou de distance kilométrique se creuse.

*   **Limites / Biais (Edge Cases) :** Si le paramètre d'ouverture ($\sigma$) est réglé trop bas, la formule dira que tous les lycées sont totalement isolés les uns des autres (graphe vide). S'il est trop haut, elle dira que tout le monde se côtoie indistinctement (graphe plein).

---

## 2. Théorie des Réseaux et Graphes

### Modularité (Algorithme de Louvain)
**Formule :**

$$
\Huge Q = \frac{1}{2m} \sum_{i,j} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)
$$

<br>

*   **Quoi :** Détection des "bulles sociales" : regroupement aveugle des lycées qui vivent en vase clos et s'échangent des élèves entre eux.

*   **Légende :** 
    *   $Q$ : score de modularité *(ex : le niveau de "tribalisme" du système éducatif)*.
    *   $m$ : masse totale des flux *(ex : l'ensemble des mobilités d'élèves à l'échelle d'une académie)*.
    *   $A_{ij}$ : intensité de la proximité entre lycées *(ex : le nombre d'élèves issus du même collège qui se répartissent entre ces deux lycées)*.
    *   $k_i, k_j$ : attractivité des lycées *(ex : le lycée Henri IV a une masse d'attractivité énorme)*.
    *   $\delta(c_i, c_j)$ : identité de strate sociale *(ex : vaut 1 si les deux lycées sont classés dans la strate "Élite")*.



*   **Pourquoi :** Détecter endogènement les "mondes scolaires" (sans imposer le nombre de clusters à l'avance).

*   **Inputs :** Matrice d'adjacence $A_{ij}$ (poids des liens).

*   **Outputs :** Dictionnaire de partition $\{Lyc\acute{e}e\_i: Cluster\_k\}$, score de modularité $Q_{max}$.

*   **Dépendance Amont :** Distance Sociale et Similarité $W_{ij}$ (Bloc 1).

*   **Dépendance Aval :** Frontière Sociale, Tension Hiérarchie vs Réseau, Modèles Markoviens.

*   **Complexité Algorithmique :** O(N log N) — Très efficace, on peut l'exécuter sur un ordinateur portable même pour un gros réseau d'Île-de-France.

*   **Contraintes & Hypothèses (Assumptions) :** La formule présuppose qu'un "monde social" se définit uniquement par le volume massif d'élèves qui circulent en vase clos entre quelques lycées, ignorant totalement la sociologie ou l'identité de ces élèves.

*   **Limites / Biais (Edge Cases) :** Limite de résolution : les micro-communautés (ex: un groupuscule de 3 lycées très spécifiques) seront aveuglément englouties de force et diluées dans un bloc géant par l'algorithme.

### Centralité d'Intermédiarité (Betweenness)
**Formule :**

$$
\Huge B(i) = \sum_{s \ne i \ne t} \frac{\sigma_{st}(i)}{\sigma_{st}}
$$

<br>

*   **Quoi :** Identification des lycées "passerelles", ces rares établissements par lesquels transitent les mobilités entre des quartiers ou des mondes sociaux différents.

*   **Légende :** 
    *   $B(i)$ : criticité du lycée *(ex : ce lycée est un "goulot d'étranglement", si on le ferme, le Nord et le Sud de la ville ne se mélangeront plus du tout)*.
    *   $\sigma_{st}$ : chemins totaux entre deux mondes *(ex : toutes les routes d'évitement possibles)*.
    *   $\sigma_{st}(i)$ : chemins passant par $i$ *(ex : le nombre de trajectoires qui atterrissent obligatoirement dans ce lycée-carrefour)*.


*   **Pourquoi :** Identifier les "goulets d'étranglement" et les lycées "ponts" structurels entre mondes sociaux.

*   **Inputs :** Graphe relationnel (nœuds et arêtes pondérées).

*   **Outputs :** Vecteur de centralité (score par lycée).

*   **Dépendance Amont :** Distance Sociale et Similarité $W_{ij}$ (Bloc 1).

*   **Dépendance Aval :** Pression Ségrégative Locale, Indice de Fragmentation.

*   **Complexité Algorithmique :** O(V * E) — Très lourd sur les graphes denses. À calculer uniquement après avoir retiré les liens faibles (sparsification), sinon le calcul prendra des jours entiers.

*   **Contraintes & Hypothèses (Assumptions) :** On suppose que les flux d'élèves entre lycées suivent toujours le chemin le plus court dans le réseau de similarité sociale, sans jamais privilégier des stratégies d'évitement ou de proximité géographique.

*   **Limites / Biais (Edge Cases) :** Si le réseau est déconnecté (deux mondes qui ne se parlent absolument jamais), le calcul devient fou et assigne des scores nuls ou infinis aux ponts intermédiaires.

### Tension Hiérarchie vs Réseau (Indice Hybride)
**Formule :**

$$
\Huge T = 1 - ARI \quad \text{(où ARI = Adjusted Rand Index)} \quad
$$

<br>

*   **Quoi :** Mesure du "stress systémique" évaluant le conflit entre la carte scolaire officielle (la hiérarchie d'état) et le vrai réseau d'évitement des familles.

*   **Légende :** 
    *   $T$ : score de tension globale *(ex : le niveau de guerre ouverte entre la sectorisation de l'État et la triche des familles)*.
    *   $ARI$ : score de ressemblance *(ex : à quel point la carte des amitiés ressemble à la pyramide des classes sociales)*.


*   **Pourquoi :** Démontrer que la structure verticale hiérarchisée (CAH) entre en conflit avec la structure relationnelle horizontale (Louvain).

*   **Inputs :** Partition assignée par la CAH, Partition assignée par Louvain.

*   **Outputs :** Scalaire global de tension $T \in [0, 1]$.

*   **Dépendance Amont :** CAH (Bloc 1) et Modularité Louvain (Bloc 2).

*   **Dépendance Aval :** Aucune (Métrique de contrôle final).

*   **Complexité Algorithmique :** O(N) — Simple calcul de comparaison de deux tableaux d'affectation.

*   **Contraintes & Hypothèses (Assumptions) :** L'outil suppose qu'une hiérarchie d'IPS imposée d'en haut (par l'État) et une logique de réseau d'amitiés forgée d'en bas (par les flux d'élèves) peuvent être comparées loyalement sur le même terrain.

*   **Limites / Biais (Edge Cases) :** Si une des méthodes décide de couper le système en 2 blocs massifs, et l'autre en 50 micro-blocs, l'ARI va paniquer mathématiquement et donner un score de tension maximale qui n'a pas de sens sociologique.

---

## 3. Ségrégation et Inégalités Spatiales

### Indice de Theil (Décomposition de l'Entropie)
**Formule :**


$$
\Huge T = \sum_i \frac{x_i}{\mu} \log\left(\frac{x_i}{\mu}\right)
$$

**Décomposition :** 

$$
\Large T = T_{between-zones} + T_{between-lycees} + T_{within-lycees}
$$

<br>

*   **Quoi :** Découpage chirurgical de la ségrégation pour prouver si l'inégalité vient plutôt des écarts entre les villes, ou des écarts entre les lycées d'une même ville.

*   **Légende :** 
    *   $T$ : indice total d'inégalité *(ex : le niveau global de ségrégation de l'Île-de-France)*.
    *   $x_i$ : poids de la zone *(ex : la proportion d'élèves très riches dans ce département)*.
    *   $\mu$ : moyenne globale *(ex : l'idéal égalitaire parfait)*.


*   **Pourquoi :** Prouver que l'inégalité se construit en "poupées russes" (ségrégation territoriale vs institutionnelle vs interne).

*   **Inputs :** Distribution des effectifs sociaux (ex: IPS) avec clés hiérarchiques (Zone > Lycée > Élève).

*   **Outputs :** Scalaires d'inégalité $T_{global}$, $T_{between}$, $T_{within}$.

*   **Dépendance Amont :** Aucune.

*   **Dépendance Aval :** Theil Spatial (Bloc 14), Score Composite $S$ (Bloc 14).

*   **Complexité Algorithmique :** O(N) — Ultra-rapide.

*   **Contraintes & Hypothèses (Assumptions) :** La formule suppose que l'inégalité d'un territoire peut se découper proprement entre l'inégalité de ses communes, plus l'inégalité des lycées dans ces communes, sans qu'aucune "fuite" d'information n'échappe à ces échelons.

*   **Limites / Biais (Edge Cases) :** Le Theil réagit très mal s'il y a des établissements avec un score exactement de 0 (le logarithme de zéro fait crasher le code), il faut toujours lisser en ajoutant un epsilon (+0.0001).

### Pression Ségrégative Locale (PSL)
**Formule :**

$$
\Huge PSL_i = \alpha H_i + \beta D_i + \gamma B_i + \delta C_i
$$

<br>

*   **Quoi :** Diagnostic cartographié évaluant si un établissement est encerclé par une zone de "haute tension" sociale prête à craquer.

*   **Légende :** 
    *   $PSL_i$ : pression sur le lycée *(ex : le risque imminent d'explosion ou de fuite des classes moyennes dans ce lycée)*.
    *   $H_i$ : hétérogénéité spatiale *(ex : le quartier est très contrasté)*.
    *   $D_i$ : distance sociale au centre *(ex : le lycée est très loin de la norme)*.
    *   $B_i$ : rôle de pont *(ex : le lycée doit absorber toutes les tensions)*.
    *   $C_i$ : diversité interne *(ex : la composition hétérogène de ses propres classes)*.
    *   $\alpha, \beta, \gamma, \delta$ : pondérations.


*   **Pourquoi :** Cartographier non pas l'état passif, mais la *tension géographique* (les zones de faille actives du système).

*   **Inputs :** Données géolocalisées, métriques de réseau du Bloc 2.

*   **Outputs :** Score géolocalisé $PSL$ (scalaire par lycée).

*   **Dépendance Amont :** Centralité d'Intermédiarité (Bloc 2).

*   **Dépendance Aval :** Cartographie exploratoire interactive.

*   **Complexité Algorithmique :** O(N log N) — L'utilisation d'un KD-Tree permet de trouver les voisins géographiques instantanément sans vérifier tout le pays pour chaque lycée.

*   **Contraintes & Hypothèses (Assumptions) :** L'outil part du principe qu'empiler plusieurs petites faiblesses géographiques fera toujours moins de dégâts pour un lycée qu'un seul énorme problème, ignorant que la combinaison de tensions peut créer un effet d'étincelle.

*   **Limites / Biais (Edge Cases) :** Si un lycée est physiquement au bord de la carte étudiée (effet de bordure), il n'a pas de voisins d'un côté, et la formule sous-estimera mathématiquement sa pression réelle.

---

## 4. Modèles Causaux Spatiaux (Économétrie)

### Spatial Autoregressive Model (SAR)
**Formule :**

$$
\Huge y = \rho Wy + X\beta + \epsilon
$$

<br>

*   **Quoi :** Détection de l'effet "tache d'huile" : prouver qu'un lycée s'effondre socialement parce que ses voisins immédiats sont eux-mêmes en train de s'effondrer.

*   **Légende :** 
    *   $y$ : variable mesurée *(ex : l'IPS d'un lycée)*.
    *   $\rho$ : effet de contagion *(ex : l'intensité avec laquelle la chute d'un lycée entraîne ses voisins)*.
    *   $W$ : poids du voisinage *(ex : les lycées à moins d'un kilomètre pèsent plus lourd)*.
    *   $X$ : variables locales *(ex : la taille du lycée, l'offre d'options)*.
    *   $\beta$ : impact direct *(ex : l'effet pur d'ouvrir une section internationale)*.
    *   $\epsilon$ : hasard *(ex : l'effet d'une rumeur non mesurable)*.


*   **Pourquoi :** Quantifier la "contagion" de la ségrégation (prouver mathématiquement qu'un lycée est causé en partie par ses voisins).

*   **Inputs :** Vecteur cible $y$ (IPS), covariables $X$, matrice de poids spatiaux géographiques $W$ (standardisée en ligne).

*   **Outputs :** Coefficients des variables $\beta$ et paramètre de contagion spatiale $\rho$.

*   **Dépendance Amont :** Matrice spatiale (coordonnées GPS converties).

*   **Dépendance Aval :** Effets Marginaux Spatiaux, Résidus Spatiaux.

*   **Complexité Algorithmique :** O(N³) — L'estimation par Maximum de Vraisemblance implique le calcul du déterminant d'une matrice massive. À éviter absolument sur plus de 10 000 unités sans approximation spatiale par sparse matrix.

*   **Contraintes & Hypothèses (Assumptions) :** On suppose qu'il y a une contagion directe et instantanée : si le lycée voisin s'effondre, cela m'impacte systématiquement, peu importe mon contexte.

*   **Limites / Biais (Edge Cases) :** Si la matrice de voisinage $W$ n'est pas standardisée à 1 (somme des lignes = 1), le paramètre $\rho$ perd tout son sens et la prédiction peut exploser vers l'infini.

### Effets Marginaux Spatiaux (Propagation)
**Formule :**

$$
\Huge ME = (I - \rho W)^{-1} \beta
$$

<br>

*   **Quoi :** Simulation de "l'onde de choc" : mesurer comment l'ouverture ou la fermeture d'une filière dans un lycée va impacter en cascade tous les lycées environnants.

*   **Légende :** 
    *   $ME$ : onde de choc *(ex : la répercussion en cascade de l'ouverture d'un lycée privé sur tous les lycées publics à 5km à la ronde)*.
    *   $I$ : base neutre.
    *   $\rho$ : coefficient de contagion.
    *   $W$ : carte des voisinages.
    *   $\beta$ : impact de départ.


*   **Pourquoi :** Tracer l'onde de choc causale (ex: "si j'améliore le lycée A, voici comment cela se propage géographiquement jusqu'au lycée B par ricochet").

*   **Inputs :** $\rho$, $W$, $\beta$ (estimés par le modèle SAR).

*   **Outputs :** Matrice des effets marginaux locaux et globaux.

*   **Dépendance Amont :** Modèle SAR (Bloc 4).

*   **Dépendance Aval :** Outil d'aide à la décision politique.

*   **Complexité Algorithmique :** O(N³) — L'inversion totale d'une matrice dense $(I - \rho W)$ nécessite de passer par une série mathématique d'approximation (Taylor/Neumann) si la carte est trop grande.

*   **Contraintes & Hypothèses (Assumptions) :** L'onde de choc se propage à l'infini dans le système spatial en s'atténuant mécaniquement à chaque pas géographique.

*   **Limites / Biais (Edge Cases) :** Si le paramètre de contagion spatiale $\rho$ approche de 1, la matrice s'effondre mathématiquement et l'effet marginal annonce qu'un changement dans 1 seul lycée va faire exploser le système entier.

---

## 5. Algorithmique et Seuils

### Critère de Mojena (Sauts de Rupture CAH)
**Formule :**

$$
\Huge h_k > \bar{h} + \beta \cdot \sigma_h
$$

<br>

*   **Quoi :** Preuve mathématique fixant objectivement le moment précis où un écart d'IPS devient une véritable "fracture de classe" infranchissable.

*   **Légende :** 
    *   $h_k$ : hauteur du mur social *(ex : le fossé séparant la fusion des lycées "Moyens" avec le bloc de l'"Élite")*.
    *   $\bar{h}$ : bruit de fond *(ex : le niveau de ségrégation ordinaire de la ville)*.
    *   $\sigma_h$ : variance des ruptures.
    *   $\beta$ : sévérité *(ex : à partir de quel seuil on considère que c'est une vraie fracture)*.



*   **Pourquoi :** Éviter de choisir le nombre de clusters au doigt mouillé, et prouver mathématiquement l'existence de "plafonds de verre" sociaux abrupts.

*   **Inputs :** Hauteurs des nœuds du dendrogramme $h_k$, constante de sévérité $\beta$ (souvent entre 1.25 et 3).

*   **Outputs :** Seuil de coupure (Nombre de clusters optimal $k$).

*   **Dépendance Amont :** CAH / Distance Ultramétrique (Bloc 1).

*   **Dépendance Aval :** Tout partitionnement ultérieur (Tension Hybride, etc.).

*   **Complexité Algorithmique :** O(N) — Parcours linéaire et instantané du vecteur des longueurs de branches.

*   **Contraintes & Hypothèses (Assumptions) :** L'outil postule que les micro-regroupements d'élèves au quotidien ne sont que du bruit statistique lisse, et que seule une rupture massive de distance signale un vrai "plafond de verre" entre classes sociales.

*   **Limites / Biais (Edge Cases) :** Sur un système socialement très continu et lisse (sans vraie fracture), Mojena va forcer une cassure purement artificielle là où il n'y a qu'une légère montée statistique.

---

## 6. Analyse des Résidus et Modèles Causaux Avancés

### Résidus Spatiaux (Anomalies Structurelles)
**Formule :**

$$
\Huge residu_i = y_i - \hat{y}_i
$$

<br>

*   **Quoi :** Traque des "anomalies politiques" : les lycées qui réussissent miraculeusement ou s'effondrent de manière incompréhensible par rapport à ce que dicte leur adresse.

*   **Légende :** 
    *   $residu_i$ : erreur du modèle face à la réalité *(ex : un lycée qui est beaucoup plus riche que ce que son quartier délabré laisserait présager)*.
    *   $y_i$ : réalité *(ex : l'IPS mesuré)*.
    *   $\hat{y}_i$ : prédiction géographique *(ex : l'IPS que le lycée "devrait" avoir vu son adresse)*.


*   **Pourquoi :** Traquer les anomalies politiques : les "miracles" (trop mixtes) ou les "bunkers" (trop ségrégués) par rapport à ce que la géographie commanderait "normalement".

*   **Inputs :** Valeurs réelles $y_i$, prédictions SAR $\hat{y}_i$.

*   **Outputs :** Vecteur de résidus continus par établissement.

*   **Dépendance Amont :** Modèle SAR (Bloc 4).

*   **Dépendance Aval :** Outils d'audit territorial.

*   **Complexité Algorithmique :** O(N) — Simple soustraction matricielle.

*   **Contraintes & Hypothèses (Assumptions) :** Le modèle spatial qui a généré la prédiction a réussi à capturer 100% de la mécanique géographique évidente.

*   **Limites / Biais (Edge Cases) :** S'il reste de la forte corrélation spatiale dans les résidus, cela signifie qu'il y a un énorme facteur politique caché (ex: financement local occulte) que la formule a raté.

### Inférence Causale par Graphes (DAG & DoWhy)
**Théorème (Backdoor Criterion) :** Pour identifier $P \to Y$, bloquer les chemins non-causaux en conditionnant sur $\{Z, N\}$. Ne pas conditionner sur un Collider $S$.

<br>

*   **Quoi :** Architecture de preuve absolue garantissant que nos conclusions sur les lycées ne sont pas faussées par des variables cachées (comme les stratégies des parents).

*   **Légende :** 
    *   $P$ : cause étudiée *(ex : l'ouverture d'une filière sélective)*.
    *   $Y$ : effet mesuré *(ex : l'augmentation de la ségrégation)*.
    *   $Z, N$ : variables parasites *(ex : le niveau de revenu des parents du quartier, qui explique en fait les deux)*.
    *   $S$ : fausse piste *(Collider)* *(ex : le taux de mention au bac, qui est une conséquence et non une cause)*.


*   **Pourquoi :** Prouver que la méthode d'évaluation du système scolaire est structurellement immunisée contre les biais de sélection statistiques classiques.

*   **Inputs :** Graphe causal défini par l'expert (nœuds, flèches causales).

*   **Outputs :** Formule probabiliste désenchevêtrée (Estimand causal).

*   **Dépendance Amont :** Aucune (Modélisation théorique préalable au code).

*   **Dépendance Aval :** Causal Random Forest ou Propensity Score Matching.

*   **Complexité Algorithmique :** O(V + E) — Parcours de graphe pour trouver les chemins bloqués (très rapide).

*   **Contraintes & Hypothèses (Assumptions) :** Suppose que le chercheur a listé absolument toutes les variables "confondantes" (Unobserved Confounding) existantes et imaginables dans le monde réel.

*   **Limites / Biais (Edge Cases) :** Si on conditionne par erreur sur un "Collider" (une variable qui est l'effet des deux autres, et non la cause), la formule crée mathématiquement une fausse preuve de cause à effet qui n'existe pas dans la vraie vie (Collider Bias).

---

## 7. Dynamique et Topologie Spatiale

### Entropie de Transition (CAH Dynamique)
**Formule :**

$$
\Huge H_i = -\sum_k p_{ik} \log p_{ik}
$$

<br>

*   **Quoi :** Mesure du chaos d'un lycée : distinguer les établissements au destin figé (élite stable) de ceux qui naviguent à vue au gré des réformes.

*   **Légende :** 
    *   $H_i$ : niveau d'imprévisibilité *(ex : le chaos ambiant autour de l'avenir de ce lycée de quartier)*.
    *   $p_{ik}$ : probabilités de destin *(ex : 80% de chances qu'un lycée en cours de paupérisation finisse dans la strate "Ghetto" l'année suivante)*.



*   **Pourquoi :** Distinguer l'élite stable et prévisible (entropie zéro) des zones de déclassement ou d'ascension chaotique (forte incertitude).

*   **Inputs :** Matrice de probabilités de transition markovienne temporelle $p_{ik}$.

*   **Outputs :** Vecteur d'entropie (scalaire par établissement).

*   **Dépendance Amont :** Clustering temporel CAH / Louvain.

*   **Dépendance Aval :** Score composite global.

*   **Complexité Algorithmique :** O(K) — K étant le nombre de clusters, le calcul est quasi instantané.

*   **Contraintes & Hypothèses (Assumptions) :** L'incertitude du futur d'un lycée est parfaitement encodée dans la diversité de ses choix et mouvements passés.

*   **Limites / Biais (Edge Cases) :** Un lycée qui n'a jamais bougé aura une entropie strictement de 0. La formule dira alors que son destin est "tracé dans le marbre" pour l'éternité, même en cas de réforme gouvernementale radicale.

### CAH Contrainte (Distance Pénalisée)
**Formule :**

$$
\Huge D' = D_{social} + \lambda D_{geo}
$$

<br>

*   **Quoi :** Forçage algorithmique fusionnant la distance kilométrique et le gouffre social pour dessiner des "ghettos" physiquement contigus sur la carte.

*   **Légende :** 
    *   $D'$ : distance totale forcée *(ex : l'impossibilité de regrouper deux lycées qui se ressemblent mais qui sont à 100km l'un de l'autre)*.
    *   $D_{social}$ : différence d'IPS pure.
    *   $D_{geo}$ : écart kilométrique.
    *   $\lambda$ : poids de la carte géographique face à la sociologie.


*   **Pourquoi :** Forcer l'algorithme à regrouper des zones à la fois similaires socialement ET adjacentes physiquement (pour prouver l'existence d'îlots territoriaux contigus).

*   **Inputs :** Matrice de distances sociales, matrice de distances spatiales, hyperparamètre de contrainte $\lambda$.

*   **Outputs :** Nouvelle matrice de distance composite.

*   **Dépendance Amont :** Distances Euclidiennes / Géographiques (Bloc 0).

*   **Dépendance Aval :** CAH Modifiée.

*   **Complexité Algorithmique :** O(N²) — Simple combinaison de deux matrices denses de NxN avant de lancer le clustering.

*   **Contraintes & Hypothèses (Assumptions) :** La proximité kilométrique et la proximité sociale peuvent être converties et additionnées dans une seule et même "monnaie d'échange" (grâce au paramètre $\lambda$).

*   **Limites / Biais (Edge Cases) :** Si on ne normalise pas parfaitement les kilomètres géographiques avec les unités d'IPS avant d'additionner, les kilomètres écraseront la sociologie pure et l'algorithme ne regroupera plus les écoles que par simples codes postaux aveugles.

### Densité de Continuité Sociale (KDE & Chevauchement)
**Formule (Overlap) :** $O_{ij} = \int \min(f_i(x), f_j(x)) dx$

<br>

*   **Quoi :** Cartographie des "zones grises" où la frontière entre l'élite scolaire et les classes populaires devient floue et perméable dans la rue.

*   **Légende :** 
    *   $O_{ij}$ : zone de mixité urbaine *(ex : les quelques rues où les élèves favorisés et défavorisés habitent porte à porte)*.
    *   $f_i(x)$ : présence d'une caste *(ex : la concentration massive de cadres dans l'hyper-centre)*.



*   **Pourquoi :** Passer d'une vision de "groupes distincts" rigides à une cartographie continue des tensions, révélant les "frontières scolaires floues".

*   **Inputs :** Fonctions de densité KDE $f_i$ et $f_j$ évaluées sur une grille spatiale 2D.

*   **Outputs :** Matrice de pourcentages de chevauchement inter-clusters $O_{ij} \in [0, 1]$.

*   **Dépendance Amont :** Modèle KDE (Kernel Density Estimation) sur GPS.

*   **Dépendance Aval :** Heatmaps spatiales de tension continue.

*   **Complexité Algorithmique :** Extrêmement lourde. Calculer l'intégrale numérique d'intersection sur une grille spatiale de l'Île-de-France demande une énorme puissance GPU si la grille de pixels est très fine.

*   **Contraintes & Hypothèses (Assumptions) :** L'influence sociale d'un lycée bave géographiquement autour de lui comme une tache d'huile continue sur la carte des quartiers.

*   **Limites / Biais (Edge Cases) :** Si deux mondes distincts sont séparés par un obstacle physique massif ignoré par la formule (ex: le périphérique parisien, la Seine), le modèle KDE croira à tort qu'il y a un fort chevauchement de populations.

---

## 8. Validation Structurelle des Clusters

### Silhouette Score (Cohérence Interne)
**Formule :**

$$
\Huge s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$

<br>

*   **Quoi :** Vérification mathématique pour savoir si les "bulles sociales" découvertes sont vraiment étanches, ou si les élèves naviguent en réalité entre elles.

*   **Légende :** 
    *   $s(i)$ : netteté de l'appartenance sociale *(ex : ce lycée est-il vraiment à sa place au cœur de la strate "Classe moyenne" ?)*.
    *   $a(i)$ : ressemblance avec ses pairs *(ex : à quel point il ressemble aux autres lycées de sa catégorie)*.
    *   $b(i)$ : ressemblance avec les autres *(ex : à quel point il lorgne vers les caractéristiques de l'élite)*.



*   **Pourquoi :** Valider rigoureusement à quel point les "mondes scolaires" sont bien séparés les uns des autres (frontières étanches ou poreuses).

*   **Inputs :** Matrice de distances de base, vecteurs d'appartenance aux clusters.

*   **Outputs :** Score de Silhouette global ou vecteur local $[-1, 1]$.

*   **Dépendance Amont :** Partition CAH ou Louvain (Blocs 1, 2).

*   **Dépendance Aval :** Benchmark et optimisation des hyperparamètres du code.

*   **Complexité Algorithmique :** O(N²) — Le calcul des distances de chaque point vers absolument tout le reste est très lourd sur de gros datasets.

*   **Contraintes & Hypothèses (Assumptions) :** Les vrais "mondes scolaires" sont censés être de forme globalement sphérique et bien compacts dans l'espace des données.

*   **Limites / Biais (Edge Cases) :** Si la société est organisée en longs "filaments" ou structures étirées complexes, le score de Silhouette va mal-noter le système et dire que le clustering est raté, alors qu'il capte une vraie structure sociologique non-sphérique.

### Gap Statistic (Validation Réalité vs Bruit)
**Formule :**

$$
\Huge Gap(k) = E[\log(W_k^*)] - \log(W_k)
$$

<br>

*   **Quoi :** Ultime démonstration algorithmique prouvant que la hiérarchie des lycées (riches, moyens, pauvres) existe réellement et n'est pas une illusion statistique.

*   **Légende :** 
    *   $Gap(k)$ : validation de l'existence des classes *(ex : est-il plus pertinent de diviser les lycées de la ville en 3 ou en 5 castes étanches ?)*.
    *   $E[\log(W_k^*)]$ : rêve égalitaire *(ex : le scénario utopique d'une mixité parfaite tirée au hasard)*.
    *   $\log(W_k)$ : réalité cynique *(ex : la fragmentation ghettoïsée réellement observée)*.



*   **Pourquoi :** Fournir la preuve algorithmique absolue que la stratification sociale observée (en $k$ classes) n'est pas un simple artéfact mathématique.

*   **Inputs :** Matrice de features originelles, distribution nulle générée (simulations aléatoires).

*   **Outputs :** Courbe de la Gap Statistic selon $k$ (le pic donne le vrai nombre de mondes).

*   **Dépendance Amont :** Modèle de clustering de base (K-Means, Ward).

*   **Dépendance Aval :** Justification académique du choix définitif du paramètre $K$.

*   **Complexité Algorithmique :** Massivement lourd. La méthode oblige à relancer le clustering en entier 500 fois de suite sur des données générées au hasard. À exécuter sur des serveurs Cloud.

*   **Contraintes & Hypothèses (Assumptions) :** L'absence totale de classe sociale dans un monde théorique pur correspond à une distribution parfaitement uniforme (un "cube" de bruit statistique).

*   **Limites / Biais (Edge Cases) :** Sur des données de très grande dimension (ex: si on intègre 50 variables sociologiques), le volume géométrique de la boîte de simulation devient si gigantesque (Fléau de la dimension) que la Gap Statistic perd toute capacité de jugement face à la réalité.

---

## 9. Fractures et Tensions Structurelles

### Tension Ultramétrique / Réseau Locale
**Formule :**

$$
\Huge T_i = \sum_j |d_U(i,j) - d_G(i,j)| w_{ij}
$$

<br>

*   **Quoi :** Détection des lycées "schizophrènes", tiraillés entre la case sociale où l'État les range et la réalité des élèves qu'ils brassent quotidiennement.

*   **Légende :** 
    *   $T_i$ : stress du lycée *(ex : un lycée tiraillé entre son statut public officiel et son obsession à imiter les codes du privé)*.
    *   $d_U(i,j)$ : fossé hiérarchique *(ex : l'ordre officiel de l'Académie)*.
    *   $d_G(i,j)$ : réalité des flux *(ex : ce que font vraiment les élèves)*.
    *   $w_{ij}$ : intensité du lien clandestin.


*   **Pourquoi :** Détecter mathématiquement les "Points de Bascule" (les établissements tiraillés entre leur strate sociale assignée et la réalité de leurs interactions locales de voisinage).

*   **Inputs :** Matrice des distances ultramétriques $d_U$, Matrice des chemins de graphe $d_G$, Matrice d'adjacence $w_{ij}$.

*   **Outputs :** Vecteur de "Tension Structurelle" (score de stress géolocalisé par lycée).

*   **Dépendance Amont :** Distance Ultramétrique (Bloc 1) et Graphes (Bloc 2).

*   **Dépendance Aval :** Focalisation de l'investigation qualitative (interview sociologique des lycées ciblés).

*   **Complexité Algorithmique :** O(N²) — La double normalisation et soustraction de matrices gigantesques prend de la mémoire RAM.

*   **Contraintes & Hypothèses (Assumptions) :** Le fossé entre "ce que je devrais fréquenter" (la hiérarchie d'état) et "ceux que je fréquente vraiment" (le réseau affinitaire) est l'origine du stress sociologique d'un établissement.

*   **Limites / Biais (Edge Cases) :** Si la formule de distance ultramétrique produit un blocage avec de trop nombreuses égalités parfaites (ex: 50 lycées ont exactement la même distance ultramétrique de 1.0), le calcul de soustraction de la tension devient extrêmement bruité et perd en résolution.

---

## 10. Modèles de Dynamique et Flux Markoviens

### Matrice de Transition (Modèle de Markov)
**Formule :**

$$
\Huge P_{ij} = P(C_{t+1}=j \mid C_t=i)
$$

<br>

*   **Quoi :** Modélisation des trajectoires de "déclassement" ou "d'ascension" : quelle est la probabilité statistique qu'un lycée pauvre rejoigne l'élite dans 5 ans ?

*   **Légende :** 
    *   $P_{ij}$ : probabilité de déclassement/ascension *(ex : 5% de chance de passer de "Défavorisé" à "Mixte" en une décennie)*.
    *   $C_t$ : état actuel *(ex : statut "Élite" en 2023)*.



*   **Pourquoi :** Démontrer que le système scolaire n'est pas figé statiquement mais est un espace de circulation macroscopique.

*   **Inputs :** Panel longitudinal des trajectoires (Lycée assigné à un cluster au temps $t$ et $t+1$).

*   **Outputs :** Matrice carrée stochastique $P$ (somme des lignes = 1).

*   **Dépendance Amont :** Partitionnement de clusters (Bloc 1, 2) évalué sur l'axe temporel.

*   **Dépendance Aval :** Stationnarité asymptotique, Centralité Markoviene.

*   **Complexité Algorithmique :** O(N) — Simple comptage statistique ultra-rapide des sauts d'une année sur l'autre.

*   **Contraintes & Hypothèses (Assumptions) :** Hypothèse mathématique stricte de "l'amnésie" (Ordre 1) : le système suppose que si tu es dans le cluster A aujourd'hui, peu importe si tu viens du cluster D ou Z l'année précédente, cela n'influence plus ton futur.

*   **Limites / Biais (Edge Cases) :** Si un établissement d'élite disparaît des radars (fermeture administrative) d'une année sur l'autre, il crée un "trou noir" mathématique dans la matrice qui empêchera la somme des probabilités de faire exactement 1.

### Distribution Stationnaire (Stabilité)
**Formule :**

$$
\Huge \pi P = \pi
$$

<br>

*   **Quoi :** Simulation visionnaire révélant à quoi ressemblera le système scolaire francilien dans 50 ans si les politiques de sectorisation ne changent pas d'un iota.

*   **Légende :** 
    *   $\pi$ : l'avenir inéluctable *(ex : la carte scolaire figée telle qu'elle sera dans 50 ans si aucune loi ne change)*.
    *   $P$ : les dynamiques actuelles.
    *   $\lambda=1$ : le point d'équilibre fatal.


*   **Pourquoi :** Révéler mathématiquement le point d'équilibre inéluctable du système à long terme (dans 50 ans) si les politiques de flux ne changent pas d'un iota.

*   **Inputs :** Matrice de transition $P$.

*   **Outputs :** Vecteur de probabilités asymptotiques finales $\pi$.

*   **Dépendance Amont :** Matrice de Transition (Bloc 10).

*   **Dépendance Aval :** Extrapolation pour l'évaluation des politiques publiques.

*   **Complexité Algorithmique :** O(K³) — Résolution algébrique de vecteurs propres (très rapide vu que le nombre de clusters K est petit, ex: K=5 mondes).

*   **Contraintes & Hypothèses (Assumptions) :** Les règles du jeu politique actuelles (la mécanique des flux) resteront strictement figées pour l'éternité, et on laisse tourner le moteur de simulation sans le freiner.

*   **Limites / Biais (Edge Cases) :** Si le système contient un "puits absorbant" absolu (un cluster d'hyper-élite dont historiquement personne n'est jamais ressorti vers le bas), la formule annoncera aveuglément que 100% du système scolaire va finir par tomber dans ce puits avec le temps, ce qui est physiquement impossible.

### Centralité de Transition (Flux Nets)
**Formule :**

$$
\Huge F_i = \sum_j (P_{ij} + P_{ji})
$$

<br>

*   **Quoi :** Identification des "grandes gares de tri" scolaires : les mondes sociaux qui aspirent et recrachent massivement les élèves du système.

*   **Légende :** 
    *   $F_i$ : rôle de pompe ou de passoire *(ex : la strate "Défavorisée" subit-elle une fuite massive de ses meilleurs éléments vers le haut ?)*.
    *   $P_{ij}$ : ceux qui s'enfuient *(ex : les élèves qui partent vers le privé)*.
    *   $P_{ji}$ : ceux qui arrivent *(ex : les relégués d'autres secteurs)*.



*   **Pourquoi :** Classer sociologiquement les zones du système en grandes gares de tri : "attracteurs" (aimants sociaux), "émetteurs" (zones de fuite) ou "passerelles transitoires".

*   **Inputs :** Matrice de transition $P$.

*   **Outputs :** Vecteur de volume macroscopique de flux par cluster.

*   **Dépendance Amont :** Matrice de Transition (Bloc 10).

*   **Dépendance Aval :** Aucune.

*   **Complexité Algorithmique :** O(K) — Additions basiques sur de petites dimensions.

*   **Contraintes & Hypothèses (Assumptions) :** Le volume pur des brassages (entrants + sortants) dicte et reflète la véritable importance "politique" du cluster dans le cœur du système.

*   **Limites / Biais (Edge Cases) :** Ce score est facilement piégeux si lu isolément : il ne distingue absolument pas un cluster "poubelle" qui se vide massivement sans retour, d'un cluster hyper-dynamique qui brasse énormément d'élèves avec un équilibre entrée/sortie parfait (les deux auront un énorme score $F_i$).

### Entropie de Transition (Vitesse de Mobilité)
**Formule :**

$$
\Huge H_i = -\sum_j P_{ij} \log P_{ij}
$$

<br>

*   **Quoi :** Évaluation du niveau de fatalité : prouver si les élèves d'un quartier donné ont une chance de s'échapper vers de multiples horizons ou si leur destin est verrouillé.

*   **Légende :** 
    *   $H_i$ : incertitude du destin *(ex : un lycée de banlieue dont la population change très vite au gré des réformes a une forte entropie)*.
    *   $P_{ij}$ : les différents chemins possibles vers le futur.



*   **Pourquoi :** Quantifier le niveau de "déterminisme" d'un cluster : un $H_i$ proche de 0 signifie que le parcours futur est tracé et inévitable pour ceux qui s'y trouvent.

*   **Inputs :** Lignes vectorielles de la matrice de transition $P$.

*   **Outputs :** Scalaire entropique traduisant l'ouverture de destin pour chaque cluster.

*   **Dépendance Amont :** Matrice de Transition (Bloc 10).

*   **Dépendance Aval :** Modèle Composite $S$ (Bloc 14).

*   **Complexité Algorithmique :** O(K) — Léger coût pour le logarithme.

*   **Contraintes & Hypothèses (Assumptions) :** Nécessite une taille d'échantillon historique massive par cluster pour que les probabilités empiriques observées $P_{ij}$ soient représentatives et ne tendent pas vers zéro par pur hasard statistique.

*   **Limites / Biais (Edge Cases) :** Les clusters ayant très peu d'effectifs historiques vont voir leurs probabilités de fuite surestimées vers certains mondes, forçant l'entropie à afficher un faux sentiment d'ouverture et de chaos.

---

## 11. Réseaux Multiplexes et Mobilité Inter-Couches

### Flux entre Couches ($F_{ab}$)
**Formule :**

$$
\Huge F_{ab} = P(\text{layer}_t=a \to \text{layer}_{t+1}=b)
$$

<br>

*   **Quoi :** Mesure chirurgicale des véritables actes de fuite, comme l'exode du Public vers le Privé ou le passage soudain d'un lycée de ZEP vers un quartier favorisé.

*   **Légende :** 
    *   $F_{ab}$ : le saut institutionnel *(ex : la probabilité qu'un élève abandonne l'école publique pour s'inscrire dans le privé catholique)*.
    *   $layer_t$ : le système d'origine *(ex : l'Éducation Nationale)*.


*   **Pourquoi :** Modéliser la véritable mobilité scolaire en 3D (fusionnant institution, géographie et sociologie de l'élève).

*   **Inputs :** Base de données longitudinale assignant chaque entité (élève/lycée) à un "layer" (strate) explicite.

*   **Outputs :** Tenseur ou matrice croisée de co-occurrences inter-couches.

*   **Dépendance Amont :** Aucune (requête SQL sur base brute).

*   **Dépendance Aval :** Indices de perméabilité, Asymétrie systémique.

*   **Complexité Algorithmique :** O(N) — Nécessite de traiter la base de données brute ligne par ligne (jointure temporelle massive).

*   **Contraintes & Hypothèses (Assumptions) :** Le saut "institutionnel" pur (le fait de changer la variable de couche, ex: passer du public au privé) est l'événement pivot qui définit la vraie mobilité de rupture.

*   **Limites / Biais (Edge Cases) :** Totalement dépendant de la qualité du traçage administratif. Si l'éducation nationale perd la trace d'un identifiant élève (ou s'il change de nom/région), le flux disparait, créant un "mirage de non-mobilité".

### Indice de Fragmentation Inter-Couches (IFC / Perméabilité)
**Formules :** $IFC = \sum_a F_{aa} \quad \text{ou normalisé} \quad IFC^* = \frac{1 - \sum_a F_{aa}}{1 - 1/K}$

<br>

*   **Quoi :** Le verdict final sur l'ascenseur social : un score mesurant l'asphyxie totale de la mobilité entre les différentes castes du système.

*   **Légende :** 
    *   $IFC$ : imperméabilité systémique *(ex : la forteresse institutionnelle qui empêche tout passage entre le lycée professionnel et la voie générale)*.
    *   $F_{aa}$ : l'entre-soi total *(ex : la part gigantesque d'élèves du privé qui y restent de la maternelle jusqu'au bac)*.


*   **Pourquoi :** Prouver mathématiquement la fermeture de l'ascenseur social (un score $IFC \to 1$ signe un blocage total, un effondrement de la mobilité inter-couches).

*   **Inputs :** Matrice de Flux entre Couches $F_{ab}$.

*   **Outputs :** Scalaire global de perméabilité du système entier.

*   **Dépendance Amont :** Flux entre Couches (Bloc 11).

*   **Dépendance Aval :** Modèle de rapport politique.

*   **Complexité Algorithmique :** O(K) — Lecture de la diagonale de la matrice.

*   **Contraintes & Hypothèses (Assumptions) :** Le niveau de fluidité totale "parfaite" dans une société correspondrait à une distribution des élèves où chacun atterrirait dans n'importe quelle couche avec une chance aléatoire parfaitement équitable.

*   **Limites / Biais (Edge Cases) :** Si le Privé représente en réalité 20% des places du système et le Public 80%, la formule normalisée "par le hasard strict $1/K$" (soit 50/50) explose et donne des résultats faux. Il faut obligatoirement ajuster le modèle sur les probabilités marginales réelles des sièges disponibles.

### IFC Pondéré (Distance Sociale Inter-strata)
**Formule :**

$$
\Huge IFC_w = \sum_{a,b} F_{ab} \cdot d_{ab}
$$

<br>

*   **Quoi :** Ajustement de l'ascenseur social pénalisant les sauts "faciles" (entre favorisés) pour valoriser les véritables "miracles scolaires" (de la grande pauvreté vers l'élite).

*   **Légende :** 
    *   $IFC_{weighted}$ : perméabilité corrigée *(ex : passer du public au privé compte double si le passage se fait d'un quartier pauvre vers un quartier ultra-riche)*.
    *   $D(a,b)$ : l'ampleur du gouffre social franchi lors de la fuite.


*   **Pourquoi :** Modérer les volumes par la réalité de l'effort social (le passage d'un "Public favorisé" à un "Privé favorisé" coûte beaucoup moins d'énergie qu'un saut "Public très défavorisé $\to$ Privé d'élite").

*   **Inputs :** Matrice des flux $F_{ab}$, Matrice de distance sémantique/sociale $d_{ab}$ entre les couches.

*   **Outputs :** Scalaire global de fluidité pondérée.

*   **Dépendance Amont :** Flux entre Couches, Distances sociales.

*   **Dépendance Aval :** Aucune.

*   **Complexité Algorithmique :** O(K²) — Produit terme à terme simple sur petites dimensions matricielles.

*   **Contraintes & Hypothèses (Assumptions) :** La violence ou l'héroïsme d'un saut de classe se mesure intégralement par la "distance mathématique sémantique" paramétrée entre deux strates.

*   **Limites / Biais (Edge Cases) :** Complètement dépendant du choix arbitraire des poids : si l'analyste décide qu'aller de "Q1 vers Q4" pèse 10 fois plus lourd qu'un saut "Q3 vers Q4", l'indice final peut être gonflé ou sous-estimé selon la subjectivité humaine qui a configuré $d_{ab}$.

### Asymétrie des Flux (Déséquilibre d'Aspiration)
**Formule :**

$$
\Huge A = \sum_{a,b} |F_{ab} - F_{ba}|
$$

<br>

*   **Quoi :** Détection du siphonnage : prouver mathématiquement que les lycées d'élite aspirent les meilleurs éléments du populaire sans jamais rien rendre en échange.

*   **Légende :** 
    *   $A_{ab}$ : prédation institutionnelle *(ex : le privé aspire 500 excellents élèves du public, mais n'en renvoie que 10 (les cancres) l'année suivante)*.
    *   $F_{ab}$ : le siphonnage vers le haut.
    *   $F_{ba}$ : le rejet vers le bas.


*   **Pourquoi :** Détecter la violence du "siphonnage" d'une strate par une autre (ex: démontrer que le Privé aspire les meilleurs profils du Public sans jamais renvoyer l'équivalent dans l'autre sens).

*   **Inputs :** Matrice de Flux entre Couches $F_{ab}$.

*   **Outputs :** Scalaire d'asymétrie totale (niveau de déséquilibre parasitaire) du système.

*   **Dépendance Amont :** Flux entre Couches.

*   **Dépendance Aval :** Modèles de drainage et génération de Sankey diagrams visuels.

*   **Complexité Algorithmique :** O(K²) — Soustraction matricielle rapide.

*   **Contraintes & Hypothèses (Assumptions) :** Une société ou un système d'éducation parfaitement sain est une société où les échanges entre strates sont bilatéraux, fluides et toujours équilibrés quantitativement.

*   **Limites / Biais (Edge Cases) :** Ce chiffre brut va mathématiquement crier à "l'alerte rouge au siphonnage" si la population totale d'une des couches est de base 10 fois plus grande que l'autre couche, même si la proportion relative des flux est parfaitement saine en termes de ratios de chance.

### Entropie Globale des Flux (Chaos du Réseau)
**Formule :**

$$
\Huge H_{flux} = -\sum_{a,b} F_{ab} \log F_{ab}
$$

<br>

*   **Quoi :** Thermomètre global du chaos : le système éducatif est-il figé comme du béton ou complètement fluide et imprévisible ?

*   **Légende :** 
    *   $H_{global}$ : niveau de panique du système *(ex : si l'entropie est maximale, cela signifie que le marché scolaire est devenu une foire d'empoigne où tout le monde fuit dans toutes les directions)*.
    *   $F_{ab}$ : l'ensemble des mouvements croisés.


*   **Pourquoi :** Évaluer macroscopiquement si le système éducatif est "liquide" (tout communique, forte mobilité croisée) ou s'il est "sclérosé" (les flux suivent des canaux de caste uniques et prévisibles).

*   **Inputs :** Matrice de Flux aplatie en vecteur.

*   **Outputs :** Scalaire global d'entropie du système (son niveau de chaos/liberté).

*   **Dépendance Amont :** Flux entre Couches.

*   **Dépendance Aval :** Score Composite $S$ (Bloc 14).

*   **Complexité Algorithmique :** O(K²) — Évaluation sur chaque cellule des probabilités jointes.

*   **Contraintes & Hypothèses (Assumptions) :** Plus l'entropie générée est forte, plus le système ressemble à un bac à sable parfaitement liquide où n'importe quel élève de base peut potentiellement atterrir n'importe où (incarnation de la mobilité absolue).

*   **Limites / Biais (Edge Cases) :** La formule s'autodétruit et crashe en erreur mathématique bloquante s'il y a une seule cellule du tableau de flux totalement vide (0 flux observé entre couche A et couche Z), car l'opération $0 \cdot \log(0)$ est non définie sans traitement préalable.

---

## 12. Modularité Avancée (Multi-couches et Hiérarchique)

### Modularité Généralisée (Louvain Multi-couches)
**Formule :**

$$
\Huge Q_{multi} = \sum_{\alpha} \sum_{ij} \left( A_{ij}^\alpha - \gamma^\alpha P_{ij}^\alpha \right) \delta(c_i, c_j)
$$

<br>

*   **Quoi :** Clustering en 3D capable de comprendre que le marché scolaire du Public et le marché du Privé se superposent et s'influencent sur la même géographie.

*   **Légende :** 
    *   $Q_{multi}$ : modularité en 3D *(ex : la détection des alliances invisibles entre des lycées publics et privés qui partagent secrètement les mêmes viviers d'élèves bourgeois)*.
    *   $\alpha$ : la couche institutionnelle *(ex : Public vs Privé)*.
    *   $A_{ij}^\alpha$ : intensité des flux au sein du privé.
    *   $\gamma^\alpha$ : niveau de zoom.
    *   $P_{ij}^\alpha$ : hasard de référence.
    *   $\delta(c_i, c_j)$ : identité de groupe *(ex : vaut 1 si c'est un regroupement de lycées prestigieux indépendamment de leur statut)*.



*   **Pourquoi :** Découvrir les "Super-Communautés hybrides" qui transcendent l'opposition binaire institutionnelle et prouver l'existence d'alliances invisibles ou de bassins de vie partagés entre le privé et le public.

*   **Inputs :** Tenseur d'adjacence tridimensionnel $A_{ij}^\alpha$ (le réseau multiplex), hyperparamètre de couplage inter-couche $\omega$ (la force qui relie un même lycée à travers ses différentes dimensions).

*   **Outputs :** Dictionnaire de partition globale (unifiée à travers les couches).

*   **Dépendance Amont :** Matrices de graphes préalablement décomposées par strates.

*   **Dépendance Aval :** Cartographie 3D de la topologie des super-structures.

*   **Complexité Algorithmique :** O(L * N log N) — Assez capricieux en occupation de mémoire (RAM) s'il y a plus de 5 ou 6 "layers" différents analysés en parallèle.

*   **Contraintes & Hypothèses (Assumptions) :** L'identité d'un établissement existe simultanément sur toutes ses dimensions institutionnelles ou sociologiques, reliées par une courroie de transmission constante (omega).

*   **Limites / Biais (Edge Cases) :** Entièrement à la merci de l'hyperparamètre de saut "omega". S'il est forcé à 0, l'algorithme traitera chaque monde comme un silo séparé (aucun intérêt multi-couches). S'il est réglé de manière démesurée, la formule écrasera les subtilités, fusionnera violemment le public et le privé et produira une bouillie analytique.

### Cohésion des Super-Communautés (Résistance Interne)
**Formule :**

$$
\Huge Q_k = \frac{W_{intra}}{W_{total}}
$$

<br>

*   **Quoi :** Calcul du niveau de "repli sur soi" d'un bloc de lycées, évaluant s'ils vivent en totale autarcie par rapport au reste de la région.

*   **Légende :** 
    *   $C_k$ : étanchéité de la super-strate *(ex : la forteresse que représente le bloc de l'élite parisienne)*.
    *   $E_{in}(k)$ : les flux endogames *(ex : les excellents élèves qui naviguent uniquement entre Louis-le-Grand et Henri IV sans jamais en sortir)*.
    *   $E_{out}(k)$ : les très rares fuites vers l'extérieur.
    *   $\lambda$ : pénalité pour éviter de regrouper toute la région en un seul bloc artificiel.



*   **Pourquoi :** Contrôler si l'agrégation pyramidale de l'algorithme (qui a fusionné des micro-mondes scolaires) ne vient pas de forcer artificiellement la création d'alliances politiquement bancales et instables au sommet de l'arbre.

*   **Inputs :** Graphe condensé par blocs d'états (où un méta-nœud = toute une super-communauté).

*   **Outputs :** Vecteur de scores de solidité intrinsèque pour chaque méta-bloc identifié.

*   **Dépendance Amont :** Partition Louvain finalisée (Bloc 2 ou Bloc 12).

*   **Dépendance Aval :** Rétro-validation empirique des modèles multi-couches.

*   **Complexité Algorithmique :** O(V + E) — Parcours très rapide du graphe réduit par la macro-structure.

*   **Contraintes & Hypothèses (Assumptions) :** La "véritable" force sociologique ou l'homogénéité d'une super-communauté se juge exclusivement par sa propension à interagir en vase clos (proportion de flux intra-muros vs extra-muros).

*   **Limites / Biais (Edge Cases) :** La formule est strictement "aveugle aux effets de bords géographiques". Un lycée qui serait hyper-cohérent socialement avec son bloc mais situé aux confins géographiques du cluster (subissant des fuites mécaniques vers d'autres blocs par proximité) fera chuter injustement le score de résilience globale.

---

## 13. Frontières Sociales et Discontinuités

### Score de Frontière Sociale ($FS_{ij}$)
**Formule :**

$$
\Huge FS_{ij} = d_{ij} \cdot (1 - w_{ij}) \cdot \mathbf{1}(c_i \neq c_j)
$$

<br>

*   **Quoi :** Repérage du "gouffre absolu" : les paires de lycées qui sont géographiquement proches mais que tout sépare (IPS, réputation, et flux d'élèves nuls).

*   **Légende :** 
    *   $FS_{ij}$ : le mur de Berlin invisible *(ex : la violence de la rupture éducative entre Paris 17ème et Clichy)*.
    *   $D_{ij}$ : écart sociologique pur.
    *   $\Delta C_{ij}$ : rupture de caste *(ex : indique si les deux lycées géographiquement voisins appartiennent à des strates sociales différentes (vaut 1) ou identiques (vaut 0))*.
    *   $\beta$ : l'importance donnée à la coupure nette.



*   **Pourquoi :** Permettre de cartographier au GPS les véritables "murs de Berlin invisibles", c'est-à-dire les zones de tension extrêmes où deux lycées pourtant physiquement voisins n'ont aucune chance statistique de se mélanger.

*   **Inputs :** Matrice de distances sociales pures $d_{ij}$, matrice d'affinité/similarité probabiliste $w_{ij}$, et vecteur de la partition de clustering.

*   **Outputs :** Matrice "creuse" (Sparse matrix) signalant uniquement la présence de fractures critiques inter-établissements.

*   **Dépendance Amont :** Louvain/Partition (Bloc 2) et Distances Sociales de base (Bloc 1).

*   **Dépendance Aval :** Visualisation spatiale des lignes de fractures et indice de Rigidité.

*   **Complexité Algorithmique :** O(N²) sur papier, mais O(E) si massivement optimisé en utilisant d'abord un filtre "KNN géographique" (pour s'interdire de chercher des fractures sociales entre Paris et Marseille).

*   **Contraintes & Hypothèses (Assumptions) :** Les "murs" infranchissables de la société naissent obligatoirement de la conjonction parfaite d'un énorme gouffre statistique et d'une séparation algorithmique catégorique ("hard clustering").

*   **Limites / Biais (Edge Cases) :** En cas de légère instabilité dans le clustering amont (si un lycée est balancé dans le mauvais monde social par un artefact d'algorithme), la formule "hallucinera" et générera de fausses alarmes de fracture avec tous ses voisins de trottoir directs.

### Rigidité des Frontières (Le Syndrome de la Forteresse)
**Formule :**

$$
\Huge R = 1 - \frac{\text{Flux inter-communautés}}{\text{Flux total}}
$$

<br>

*   **Quoi :** Mesure de "l'enfermement de quartier" évaluant à quel point il est statistiquement impossible pour un élève de s'échapper de sa zone de recrutement d'origine.

*   **Légende :** 
    *   $R_i$ : niveau de blindage du lycée *(ex : un lycée qui a un score de 1 est physiquement entouré d'établissements beaucoup plus pauvres que lui, avec lesquels il refuse le moindre échange d'élèves)*.
    *   $FS_{ij}$ : la solidité du mur avec le voisin.
    *   $N(i)$ : le nombre total de voisins immédiats.


*   **Pourquoi :** Distinguer de manière implacable une simple "zone de transition" relativement poreuse, d'une véritable "forteresse de ségrégation" totalement hermétique au monde extérieur.

*   **Inputs :** Base des volumes de flux agrégés, recoupés au couteau par les partitions communautaires.

*   **Outputs :** Scalaire de rigidité (verrouillage systémique) ou score local de rétention $R \in [0, 1]$.

*   **Dépendance Amont :** Matrice Markov de transition (Bloc 10) et Partitions réseaux (Bloc 2).

*   **Dépendance Aval :** Rapports de fermeture de l'écosystème.

*   **Complexité Algorithmique :** O(K) — Soustraction de ratios à l'échelle des super-clusters (ultra-léger en machine).

*   **Contraintes & Hypothèses (Assumptions) :** La capacité d'une forteresse ou d'une zone géographique à capter, absorber et retenir définitivement sa population est la signature absolue de son niveau de ségrégation ou de consanguinité sociale.

*   **Limites / Biais (Edge Cases) :** L'indice surréagit de manière aveugle et mécanique à la simple *masse physique* des blocs : un monstre territorial (ex: regrouper toute la Banlieue dans un bloc) aura un score de "bunker hermétique" écrasant juste parce qu'il est statistiquement immense et capte mécaniquement le flux, et non pas par volonté réelle de ségrégation active.

---

## 14. Décomposition Spatio-Temporelle des Inégalités

### Theil Spatial par Commune ($T_c$)
**Formule :**

$$
\Huge T_c = \sum_{s \in \text{classes}_{IPS}} \frac{n_{c,s}}{n_c} \log\left(\frac{n_{c,s}/n_c}{p_s}\right)
$$

<br>

*   **Quoi :** Scan territorial révélant quelles communes sont des "monopoles sociaux" (100% de riches ou 100% de pauvres) face à la moyenne francilienne.

*   **Légende :** 
    *   $T_c$ : responsabilité politique du maire *(ex : la part exacte de l'inégalité régionale qui est directement causée par la politique urbaine de la mairie de Versailles)*.
    *   $N_c$ : taille de la ville.
    *   $x_{ic}$ : situation des lycées de cette ville.


*   **Pourquoi :** Permettre la production de heatmaps de ségrégation chirurgicales révélant les véritables "archipels de l'entre-soi" (ces villes fracturées de l'intérieur par des strates sociales qui ne se côtoient jamais).

*   **Inputs :** Effectifs locaux ultra-granulaires par quantile d'IPS $n_{c,s}$, somme des effectifs de la commune $n_c$, proportions globales visées $p_s$.

*   **Outputs :** Vecteur des scores de Theil d'éloignement, mappés géographiquement.

*   **Dépendance Amont :** Indice d'Entropie de Theil de base (Bloc 3).

*   **Dépendance Aval :** Ingestion par modèle économétrique SAR (Bloc 4), Cartographie QGIS/Plotly.

*   **Complexité Algorithmique :** O(N_communes) — Balayage spatial extrêmement véloce.

*   **Contraintes & Hypothèses (Assumptions) :** La ségrégation, sociologiquement, s'éprouve, se subit et s'organise à l'échelle administrative de la *commune*, utilisée ici comme référentiel pivot de comparaison par rapport à la "norme" de la région.

*   **Limites / Biais (Edge Cases) :** Sur les minuscules villages dotés d'un seul et unique groupe scolaire, la formule n'a plus le moindre sens mathématique, subit des effets de seuil violents et crache des valeurs d'entropie absurdes qui pollueront visuellement toute la carte spatiale.

### Polarisation Locale (Le Choc des Extrêmes)
**Formule :**

$$
\Huge P_c = p(Q1) \cdot p(Q4)
$$

<br>

*   **Quoi :** Détection des "chocs thermiques sociaux", ces très rares lycées où la grande bourgeoisie croise la grande précarité de plein fouet.

*   **Légende :** 
    *   $P_i$ : niveau de tension sociale directe *(ex : la violence du choc quand un collège ultra-bourgeois est situé exactement en face d'un lycée d'enseignement professionnel en grande difficulté)*.
    *   $z_i, z_j$ : les IPS extrêmes (l'un très haut, l'autre très bas).
    *   $w_{ij}$ : le fait qu'ils se font face dans la même rue.


*   **Pourquoi :** Mettre immédiatement en lumière la forme de violence sociale la plus crue : les territoires "duaux" (gentrifiés) où la grande richesse côtoie la grande pauvreté sur le même trottoir sans aucun sas de décompression au milieu.

*   **Inputs :** Proportions communales exactes (probabilités d'occurrence) des classes de quartiers (Q1 et Q4).

*   **Outputs :** Vecteur de choc social / polarisation spatiale par localité.

*   **Dépendance Amont :** Discrétisation par quantiles (Binning).

*   **Dépendance Aval :** Isolation des villes sous haute tension sociétale.

*   **Complexité Algorithmique :** O(N) — Produit croisé basique des arrays.

*   **Contraintes & Hypothèses (Assumptions) :** La véritable "bombe à retardement sociologique" ne réside pas dans l'absence de mixité, mais dans la promiscuité géographique suffocante des deux extrémités spectrales de la richesse, créant un ressentiment local.

*   **Limites / Biais (Edge Cases) :** Cette formule mathématique mutile la réalité en ignorant à 100% l'existence de la "classe moyenne" (les Q2 et Q3). Une ville gigantesque exclusivement composée de classes moyennes aura exactement le même score de "0.0" qu'une ville de milliardaires 100% pure, créant des angles morts massifs dans l'analyse de la mixité.

### Décomposition Dynamique Temporelle (L'Évolution du Fracture)
**Formule :**

$$
\Huge \Delta T = \Delta T_{within} + \Delta T_{between}
$$

<br>

*   **Quoi :** Radar du déclassement mesurant en temps réel si l'apartheid scolaire s'accélère à cause de l'embourgeoisement des villes, ou des choix de filières des directeurs d'école.

*   **Légende :** 
    *   $\Delta T$ : l'aggravation du problème *(ex : l'augmentation de la fracture sociale sur les 10 dernières années)*.
    *   $\Delta T_{between}$ : ce qui vient de la gentrification des quartiers.
    *   $\Delta T_{within}$ : ce qui vient de la prolifération des classes de niveaux (filières d'élite) au sein même des lycées.


*   **Pourquoi :** Identifier le vrai moteur de l'aggravation en cours : la ségrégation monte-t-elle parce que des mairies se barricadent contre les autres (ghettoïsation des territoires éloignés), ou parce que les écoles d'une même commune s'étanchent (création de bunkers locaux au bout de la rue) ?

*   **Inputs :** Les scores globaux de l'Indice Theil (Bloc 3) calculés à une année $t$, et à son année de référence antérieure $t-1$.

*   **Outputs :** Séquence de vecteurs delta (la force d'inertie de l'inégalité au fil des ans).

*   **Dépendance Amont :** L'entièreté de la décomposition additive de Theil (Bloc 3).

*   **Dépendance Aval :** Rapports de prospective.

*   **Complexité Algorithmique :** O(N) — Simple soustraction vectorielle des métriques archivées.

*   **Contraintes & Hypothèses (Assumptions) :** Le modèle mathématique suppute par facilité que l'environnement global est démographiquement étanche et fermé : il ignore l'effet perturbateur de l'exode rural, des naissances, ou des migrations de population venues d'une autre région.

*   **Limites / Biais (Edge Cases) :** Si la carte scolaire est réorganisée politiquement par le ministère (ouverture d'un nouveau lycée ou fusion de deux collèges) entre le temps $t$ et $t-1$, l'équation s'effondre techniquement. On ne peut pas soustraire des "ensembles Theil" dont la taille de base (le nombre d'établissements) a magiquement changé sans appliquer des poids de redressement mathématiques ultra-lourds.

### Score Composite Global de Ségrégation ($S$)
**Formule :**

$$
\Huge S = \alpha T + \beta G - \gamma H
$$

<br>

*   **Quoi :** Le "Score du Jugement Dernier", la note finale et systémique combinant l'apartheid spatial, le cumul des richesses et le blocage de l'ascenseur social sur tout le territoire.

*   **Légende :** 
    *   $S$ : L'Indice Macroscopique Final *(ex : le "Thermomètre absolu" de 0 à 100 de la toxicité du système scolaire d'une académie entière)*.
    *   $T_{norm}$ : l'inégalité de base.
    *   $F_{norm}$ : le verrouillage des flux.
    *   $H_{norm}$ : l'effet de meute spatial.
    *   $w_1, w_2, w_3$ : les poids de synthèse.


*   **Pourquoi :** L'objectif ultime, la raison d'être du livre : condenser l'intégralité de la "maladie sociologique" d'un écosystème en un unique verdict chiffré qui fusionne de force la dimension Spatiale, l'Accumulation des ressources et le Vecteur Temps.

*   **Inputs :** Le score Theil Global $T$ (Bloc 3), le Gini classique $G$, l'Entropie des flux réseaux $H$ (Bloc 11), pondérés par des "hyperparamètres doctrinaux" $\alpha, \beta, \gamma$.

*   **Outputs :** Le "Score de Température S" d'un pays ou d'une région.

*   **Dépendance Amont :** Theil (Bloc 3), Entropie de Réseau (Bloc 11), et Calcul d'Inégalité de Gini standard.

*   **Dépendance Aval :** Point culminant de la Trilogie, indexation globale pour la publication.

*   **Complexité Algorithmique :** O(1) — Scalaire instantané (le "Big O" réel a déjà été payé par le cluster en calculant tous les blocs précédents).

*   **Contraintes & Hypothèses (Assumptions) :** Le concepteur postule qu'on peut légitimement réduire la complexité humaine infinie à une addition de trois vecteurs : l'Espace physique, le différentiel de Capital, et le niveau de Liberté de circulation dans le Temps.

*   **Limites / Biais (Edge Cases) :** Ce n'est plus une formule mathématique absolue, mais un "Manifeste Idéologique". Les poids de la formule sont totalement arbitraires : si le sociologue écrit $\alpha=0.9$ et $\gamma=0.1$, il force la machine à admettre que l'Espace géographique a une importance d'écrasement 9 fois supérieure au "droit de changer d'école", ce qui est un choix politique que la formule ne peut ni justifier ni prouver par elle-même.
