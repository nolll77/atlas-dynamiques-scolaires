#  Socle Mathématique, Dynamique et Causal (Monde B)

> **GUIDE DE CONSTRUCTION (MANIFESTE DU SOCLE DYNAMIQUE)**
> Ce document est l'extension du Socle Mathématique, dédié aux modèles complexes, spatiaux, temporels et causaux (Le "Monde B"). Il capture l'intégration des dynamiques de réseau et d'évolution temporelle.
>
> **LA LOI DE L'ANCRAGE TERRAIN :**
> Il respecte rigoureusement le **Standard des 9 Tags** et la **LOI DE L'ANCRAGE TERRAIN** : aucune poésie abstraite, aucune variance hors-sol, tout est traduit dans les objets de l'étude (lycées, élèves, flux, territoires).

---

### 1. Décomposition des Effets Directs et Indirects (Spatial Lag)
**Formule :**

$$
\Huge Y_i = \alpha X_i + \beta \sum_j W_{ij} X_j + \varepsilon_i
$$
*   **Quoi :** Séparation statistique entre ce que le lycée "produit" seul (effet direct $\alpha$) et ce qu'il "subit" de ses voisins (effet indirect $\beta$).
*   **Légende :** $Y_i$ : variable dépendante (ex: IPS), $\alpha$ : effet direct intrinsèque, $X_i$ : ressources propres, $\beta$ : force de contagion, $W_{ij}$ : matrice spatiale, $X_j$ : ressources des voisins, $\varepsilon_i$ : résidu.
*   **Pourquoi :** Comprendre si un lycée est un acteur autonome de la ségrégation ou s'il est simplement porté par son écosystème territorial.
*   **Inputs :** Caractéristiques du lycée ($X_i$, ex: IPS) et matrice de voisinage ($W$).
*   **Outputs :** Ratios de domination (Ri = $|I_i| / |D_i|$).
*   **Dépendance Amont :** Matrice de voisinage (KNN ou Distance).
*   **Dépendance Aval :** Typologie des établissements (Autonome vs Dépendant).
*   **Complexité Algorithmique :** O(N²) pour la matrice spatiale. Peut saturer la RAM si calculé sur tous les élèves d'un pays au lieu des lycées.
*   **Contraintes & Hypothèses (Assumptions) :** On suppose que l'influence entre deux lycées circule de manière fluide et symétrique, sans barrière invisible qui bloquerait l'effet de quartier.
*   **Limites / Biais (Edge Cases) :** Si un lycée recrute ses élèves à l'échelle nationale (hyper-élite), la formule hallucinera une dépendance locale forte à cause de la géographie, alors que ce lycée ignore totalement son quartier.

---

### 2. Score de Propagation de Ségrégation (SPS) / Hotspots
**Formule :**

$$
\Huge SPS_i = S_i \cdot \sum_j W_{ij} S_j
$$
*   **Quoi :** Mesure de la "contagion" ségrégative d'un lieu vers ses voisins.
*   **Légende :** $SPS_i$ : score de propagation du lycée $i$, $S_i$ : ségrégation propre de $i$, $W_{ij}$ : matrice spatiale, $S_j$ : ségrégation des voisins $j$.
*   **Pourquoi :** Identifier les "hotspots", ces lycées qui ne sont pas seulement inégalitaires, mais qui diffusent activement cette ségrégation autour d'eux.
*   **Inputs :** Score de ségrégation locale ($S_i$, ex: Theil) et matrice de voisinage ($W_{ij}$).
*   **Outputs :** Vecteur de scores $SPS$ par établissement, cartographiable.
*   **Dépendance Amont :** Indice de Theil local.
*   **Dépendance Aval :** Pression de propagation (PP).
*   **Complexité Algorithmique :** O(N) une fois la matrice de voisinage $W$ établie, calcul instantané.
*   **Contraintes & Hypothèses (Assumptions) :** On postule que la proximité géographique entre deux établissements ségrégués aggrave mécaniquement leur fermeture sociale, créant un effet "boule de neige" territorial.
*   **Limites / Biais (Edge Cases) :** Dans des zones géographiquement isolées (ex: lycées ruraux), l'absence de voisins tue artificiellement le score SPS, rendant l'algorithme aveugle à la ségrégation rurale.

---

### 3. Zones de Bascule (Effet local non-linéaire)
**Formule :**

$$
\Huge Bascule_i = \mathbb{1}(\beta_i \times \bar{\beta}_{voisins(i)} < 0)
$$
*   **Quoi :** Détection spatiale des ruptures de régime (où l'impact d'une variable s'inverse par rapport aux voisins).
*   **Légende :** $Bascule_i$ : indicateur booléen (1 si rupture), $\beta_i$ : effet local de la variable sur $i$, $\bar{\beta}_{voisins(i)}$ : effet moyen sur les voisins géographiques.
*   **Pourquoi :** Repérer les lignes de faille urbaines où "plus de mixité" passe d'un effet intégrateur à un effet destructeur selon le quartier.
*   **Inputs :** Modèles OLS locaux par voisinage (Spatial Varying Coefficients).
*   **Outputs :** Booléen et intensité de bascule ($B_i$).
*   **Dépendance Amont :** Modèle linéaire global et KNN spatial.
*   **Dépendance Aval :** Cartographie des "points de retournement".
*   **Complexité Algorithmique :** O(N * K) où l'on entraîne un modèle par lycée sur son micro-voisinage. Relativement lourd mais parallélisable.
*   **Contraintes & Hypothèses (Assumptions) :** On assume que le système scolaire francilien est tellement fragmenté qu'une politique publique (ex: ajout d'une filière) aura des conséquences diamétralement opposées si elle est appliquée à l'Est ou à l'Ouest de Paris.
*   **Limites / Biais (Edge Cases) :** Aux abords d'une frontière administrative étanche (deux académies qui ne se parlent pas), l'outil peut détecter une fausse zone de bascule alors qu'il s'agit d'une simple rupture de sectorisation imposée par l'État.

---

### 4. Modèle Latent Spatial (Analyse des Résidus)
**Formule :**

$$
\Huge r_i = Y_i - \hat{Y}_i = z_{c(i)} + u_i
$$
*   **Quoi :** Utilisation des erreurs prédictives (résidus) pour découvrir des classes sociales "cachées".
*   **Légende :** 
    *   $r_i$ : résidu spatial pour $i$
    *   $Y_i$ : vraie valeur
    *   $\hat{Y}_i$ : prédiction du modèle global
    *   $z_{c(i)}$ : effet du cluster latent $c$
    *   $u_i$ : bruit purement aléatoire
*   **Pourquoi :** Traquer la ségrégation invisible. Ce que les modèles classiques n'expliquent pas (le bruit) est souvent le signal des arrangements discrets entre familles (réputations, évitements).
*   **Inputs :** Vecteur des résidus d'un modèle explicatif ($r_i$).
*   **Outputs :** Clusters latents spatiaux (Gaussian Mixture Model).
*   **Dépendance Amont :** Régression standard (ex: OLS).
*   **Dépendance Aval :** Cartographie du signal latent.
*   **Complexité Algorithmique :** O(I * K * N) pour le GMM sur l'espace spatial, gérable sur des milliers de lycées.
*   **Contraintes & Hypothèses (Assumptions) :** La formule présuppose que l'incapacité d'une machine à prédire le comportement social d'un établissement prouve l'existence de stratégies de contournement occultes (privé hors contrat, options d'excellence invisibles).
*   **Limites / Biais (Edge Cases) :** Si la base de données gouvernementale est simplement mal renseignée pour un quartier pauvre, l'algorithme hallucine la présence d'une stratégie sociale machiavélique là où il y a juste un bug administratif.

---

### 5. Modèle d'Équations Structurelles Spatial (SEM)
**Formule :**

$$
\Huge Y = X\beta + \rho WY + \varepsilon
$$
*   **Quoi :** Modélisation simultanée des causes internes et de la contagion par le voisinage.
*   **Légende :** $Y$ : vecteur cible, $X\beta$ : effets des variables explicatives, $\rho$ : coefficient de corrélation spatiale, $W$ : matrice des poids spatiaux, $\varepsilon$ : terme d'erreur structurel.
*   **Pourquoi :** Démontrer que le niveau social d'un lycée est organiquement lié au niveau de ceux qui l'entourent (effet "spillover").
*   **Inputs :** Variables internes ($X$) et variables laggées spatialement ($WY$).
*   **Outputs :** Intensité de contagion ($\rho$).
*   **Dépendance Amont :** Construction robuste de la matrice spatiale ($W$).
*   **Dépendance Aval :** Part spatiale de la variance ($R^2_{spatial}$).
*   **Complexité Algorithmique :** Élevée pour les vrais estimateurs ML spatial (Maximum de Vraisemblance), mais approximable par OLS laggé en O(N³).
*   **Contraintes & Hypothèses (Assumptions) :** On suppose qu'un lycée n'est jamais une île isolée : son prestige ou sa chute est continuellement contaminé par la réputation des établissements qui l'encerclent physiquement.
*   **Limites / Biais (Edge Cases) :** Si le "voisinage" est défini par un cercle kilométrique strict, la formule devient aveugle aux lycées de banlieue desservis par une ligne de RER directe vers Paris, dont les vrais voisins sont à 20 kilomètres.

---

### 6. SEM Spatial Multi-Niveaux (Élève → Lycée → Zone)
**Formule :**

$$
\Huge Y_{ijk} = X_{ijk}\beta + u_{jk} + v_k + \rho Wv_k + \varepsilon_{ijk}
$$
*   **Quoi :** Emboîtement causal à 3 échelles : la classe sociale de l'élève, la politique du lycée, et le territoire environnant.
*   **Légende :** $Y_{ijk}$ : score de l'élève $i$ au lycée $j$ en zone $k$, $X_{ijk}\beta$ : caractéristiques individuelles, $u_{jk}$ : effet aléatoire du lycée, $v_k$ : effet de la zone territoriale, $\rho W v_k$ : influence des zones voisines.
*   **Pourquoi :** Prouver que la ségrégation est un mille-feuille où les actions individuelles se heurtent à la structure de l'établissement et à la pesanteur du quartier.
*   **Inputs :** Données micro (élèves) et méso (lycées/zones).
*   **Outputs :** Décomposition de la variance (ICC spatial).
*   **Dépendance Amont :** Données exhaustives intra-établissement.
*   **Dépendance Aval :** Typologie des systèmes (Cloisonné vs Territorial).
*   **Complexité Algorithmique :** Très lourde. Résoudre des modèles mixtes (MixedLM) avec des centaines de milliers d'élèves nécessite une convergence itérative puissante.
*   **Contraintes & Hypothèses (Assumptions) :** Le modèle assume que l'inégalité d'un individu se décompose parfaitement en "briques" additionnables : sa part de responsabilité propre, celle de son proviseur, et celle de la mairie de son quartier.
*   **Limites / Biais (Edge Cases) :** L'outil s'effondre si les lycéens franchissent massivement les frontières des "zones" (ex: fuite vers le centre-ville) : le niveau territorial ($v_k$) ne voudrait plus rien dire.

---

### 7. Graphe Acyclique Dirigé Inter-Temporel (DAG 2010→2026)
**Formule :**

$$
\Huge Y_t = \alpha Y_{t-1} + \beta X_t + \gamma WY_{t-1} + \varepsilon_t
$$
*   **Quoi :** Chaînage causal chronologique pour analyser la ségrégation comme une trajectoire historique.
*   **Légende :** $Y_t$ : état au temps $t$, $Y_{t-1}$ : état passé (inertie), $X_t$ : variables contemporaines, $WY_{t-1}$ : état passé des voisins (contagion retardée).
*   **Pourquoi :** Mesurer l'inertie du système : un lycée ghettoïsé en 2010 a-t-il une chance statistique d'échapper à son destin en 2026 ?
*   **Inputs :** Panels de données longitudinales sur 15 ans.
*   **Outputs :** Causalité temporelle, vitesse de propagation ($V$).
*   **Dépendance Amont :** Jointures parfaites des identifiants (UAI) lycées sur 15 ans.
*   **Dépendance Aval :** Causalité DoWhy, simulations contrefactuelles.
*   **Complexité Algorithmique :** O(T * N), dépend du nombre d'années, très rapide.
*   **Contraintes & Hypothèses (Assumptions) :** L'outil suppose qu'un établissement scolaire traîne l'héritage de sa réputation passée d'année en année, et que seule une rupture politique majeure peut dévier cette trajectoire mathématique.
*   **Limites / Biais (Edge Cases) :** Les fusions administratives de lycées ou les changements de nom sur la période temporelle vont créer des trous noirs statistiques dans le graphe, faussant la mémoire du système.

---

### 8. Trajectoires de Clusters (Sankey des flux structurels)
**Formule :**

$$
\Huge P_{ab}(t \to t+1) = P(C(t)=a \to C(t+1)=b)
$$
*   **Quoi :** Matrice de transition mesurant la probabilité pour un lycée de changer de "monde social" d'une époque à l'autre.
*   **Légende :** $P_{ab}$ : probabilité de transition, $C(t)=a$ : appartenance au monde $a$ en année $t$, $C(t+1)=b$ : atterrissage dans le monde $b$ l'année suivante.
*   **Pourquoi :** Visualiser la fluidité du système : l'élite s'élargit-elle ou s'enferme-t-elle ? Les classes moyennes s'effondrent-elles vers le bas ?
*   **Inputs :** Partitions de clusters (ex: Louvain ou KMeans) calculées pour chaque année indépendante.
*   **Outputs :** Diagrammes de flux (Sankey) et entropie des transitions ($H$).
*   **Dépendance Amont :** Algorithmes de clustering stabilisés (les mêmes graines d'aléatoire).
*   **Dépendance Aval :** Visualisation spatio-temporelle.
*   **Complexité Algorithmique :** O(K²) pour la matrice de transition. Très léger.
*   **Contraintes & Hypothèses (Assumptions) :** On part du principe qu'un lycée qui passe du cluster "Populaire" au cluster "Classe Moyenne" représente une véritable ascension sociologique globale, et non un simple glissement démographique des riverains.
*   **Limites / Biais (Edge Cases) :** Si les définitions des clusters (les seuils de richesse) glissent mécaniquement avec l'inflation économique dans le temps, la matrice affichera une fausse explosion de mobilité sociale.

---

### 9. Détection de Ruptures Structurelles (Changepoints Temporels)
**Formule :**

$$
\Huge d_t = 1 - \text{ARI}(C_t, C_{t-1}) \quad \text{ou} \quad D_t = \|Z_t - Z_{t-1}\|
$$
*   **Quoi :** Algorithme mesurant les "séismes" dans la composition du système éducatif.
*   **Légende :** $d_t$ : magnitude de la rupture, $ARI$ : Adjusted Rand Index comparant les partitions de deux années successives, $D_t$ : distance entre matrices d'embeddings $Z_t$.
*   **Pourquoi :** Démontrer que la ségrégation n'évolue pas de manière lisse, mais procède par "chocs" brutaux (ex: une réforme, une crise démographique) qui redessinent la carte scolaire.
*   **Inputs :** Partitions de clusters $C_t$ ou matrices d'embeddings $Z_t$ sur plusieurs années.
*   **Outputs :** Dates de ruptures $\tau$ (Changepoints) et segmentation PELT.
*   **Dépendance Amont :** Modèle de clustering annuel stabilisé.
*   **Dépendance Aval :** Analyse causale historique.
*   **Complexité Algorithmique :** Légère pour le calcul de l'ARI. Modérée si on utilise une optimisation PELT pour ruptures multiples.
*   **Contraintes & Hypothèses (Assumptions) :** On suppose qu'une baisse soudaine de similarité entre les clusters de 2015 et 2016 correspond à un vrai bouleversement sociologique, et non à un artefact statistique dû au renouvellement naturel d'une cohorte d'élèves.
*   **Limites / Biais (Edge Cases) :** Si les effectifs d'élèves chutent drastiquement une année, la structure mathématique change, provoquant une fausse alarme de rupture systémique.

---

### 10. Ultramétrie Temporelle (Géométrie Hiérarchique Évolutive)
**Formule :**

$$
\Huge \Delta_t = d(D_t, D_{t-1}) \quad \text{et l'Indice Global} \quad U = 1 - \frac{1}{T}\sum_t \Delta_t
$$
*   **Quoi :** Empilement de dendrogrammes (arbres de classification) année par année pour filmer le mouvement de la "distance sociale" entre les lycées.
*   **Légende :** $\Delta_t$ : déformation de l'arbre, $d(D_t, D_{t-1})$ : distance entre dendrogrammes successifs, $U$ : indice global de stabilité hiérarchique.
*   **Pourquoi :** Visualiser l'ossature profonde de la reproduction sociale : à quel point la hiérarchie entre l'élite et le populaire est-elle figée dans le temps ($U \approx 1$) ou mouvante ?
*   **Inputs :** Distances ultramétriques (cophenetic) issues de CAH annuelles.
*   **Outputs :** Taux de stabilité hiérarchique $U$ et animations d'arbres.
*   **Dépendance Amont :** Arbres CAH (Ward).
*   **Dépendance Aval :** Visualisation des dendrogrammes dynamiques.
*   **Complexité Algorithmique :** O(N³) par année pour la CAH, computationnellement lourd sur de grands datasets.
*   **Contraintes & Hypothèses (Assumptions) :** La méthode assume que le système scolaire fonctionne comme un arbre généalogique où la "hauteur de fusion" entre deux lycées dicte l'épaisseur du mur social qui les sépare.
*   **Limites / Biais (Edge Cases) :** L'algorithme est instable (effet "flip-flop") : un lycée qui passe d'une moyenne de 12.0 à 12.1 peut basculer d'une branche primaire à une autre, créant un faux "tremblement de terre" dans la géométrie de l'arbre.

---

### 11. Simulation de Mobilité Sociale (La dynamique du lycée)
**Formule :**

$$
\Huge S_i(t+1) = S_i(t) + \alpha X_i(t) + \beta W S(t) - \gamma C_i(t) + \varepsilon_i(t)
$$
*   **Quoi :** Équation de mouvement où un lycée "grimpe" ou "chute" dans le prestige scolaire comme une particule dans un champ de forces.
*   **Légende :** $S_i(t)$ : prestige latent, $\alpha X_i$ : atouts internes, $\beta W S$ : gravité du voisinage, $\gamma C_i$ : contraintes territoriales, $\varepsilon_i$ : chocs externes aléatoires.
*   **Pourquoi :** Prouver mathématiquement qu'un établissement n'est pas maître de son destin : sa réussite ($\alpha X$) est freinée par les contraintes territoriales ($\gamma C$) et tiraillée par la concurrence ou la déchéance de ses voisins ($\beta W S$).
*   **Inputs :** Score de prestige latent $S_i$, ressources $X_i$, voisinage $W S$, contraintes $C_i$.
*   **Outputs :** Trajectoire continue du lycée et Vitesse moyenne de déclassement/ascension ($V_i$).
*   **Dépendance Amont :** Calcul robuste du prestige $S$ et des variables de contraintes $C$.
*   **Dépendance Aval :** Modèle prédictif de déclassement.
*   **Complexité Algorithmique :** Ultra-rapide (O(N) par itération) pour simuler, mais l'estimation des coefficients empiriques peut être ardue.
*   **Contraintes & Hypothèses (Assumptions) :** Le modèle assimile le marché scolaire francilien à une bourse où le capital social d'un lycée est négocié chaque rentrée, réagissant mécaniquement aux fluctuations du quartier.
*   **Limites / Biais (Edge Cases) :** Incapable de modéliser l'effet d'une rumeur locale dévastatrice ou l'arrivée d'un nouveau proviseur, qui sont des chocs hors-variables ($\varepsilon_i$ massif).

---

### 12. Frontières Scolaires "Dures" (Cut Edges & Betweenness)
**Formule :**

$$
\Huge F_{ij} = BC_{ij} \cdot (1 - w_{ij})
$$
*   **Quoi :** Algorithme de détection des "ponts de fragilité" dans le réseau scolaire.
*   **Légende :** $F_{ij}$ : score de frontière, $BC_{ij}$ : centralité d'intermédiarité de l'arête, $w_{ij}$ : similarité sociale entre $i$ et $j$.
*   **Pourquoi :** Cartographier les "lignes de faille" : identifier les liens géographiques qui, s'ils sautent, cassent définitivement la mixité sociale et scindent le territoire en ghettos isolés.
*   **Inputs :** Graphe des lycées $G=(V,E)$ pondéré par la similarité $w_{ij}$.
*   **Outputs :** Score de frontière $F_{ij}$ pour chaque arête.
*   **Dépendance Amont :** Centralité d'intermédiarité ($BC$) via NetworkX.
*   **Dépendance Aval :** Cartographie des lignes de faille.
*   **Complexité Algorithmique :** O(V \cdot E) avec l'algorithme de Brandes pour la betweenness.
*   **Contraintes & Hypothèses (Assumptions) :** L'outil suppose que la cohésion républicaine ne tient que grâce à un nombre infime de connexions, et que le système est au bord du morcellement absolu.
*   **Limites / Biais (Edge Cases) :** Dans les zones hyper-denses (Paris intra-muros), le graphe est tellement saturé de connexions que l'algorithme peine à isoler un seul "pont" critique, noyant les frontières dans le bruit de la densité.

---

### 13. Corridors Sociaux (Mobilité entre Clusters)
**Formule :**

$$
\Huge R_{ab} = \frac{T_{ab}}{E_{ab}} \quad \text{et} \quad C_{ab} = R_{ab} \cdot \min(p_a, p_b)
$$
*   **Quoi :** Matrice isolant les flux d'élèves ou les transferts de similarité anormalement élevés entre deux "mondes sociaux" différents.
*   **Légende :** $R_{ab}$ : intensité du corridor, $T_{ab}$ : flux réels observés, $E_{ab}$ : flux attendus par hasard absolu, $C_{ab}$ : ratio ajusté par les populations marginales $p_a, p_b$.
*   **Pourquoi :** Identifier les "ascenseurs sociaux" ou "toboggans de déclassement" : ces canaux souterrains par lesquels la mixité transite miraculeusement.
*   **Inputs :** Matrice de transition $T_{ab}$ comparée au flux théorique sous hypothèse d'indépendance $E_{ab}$.
*   **Outputs :** Scores de corridor $C_{ab}$ (intensité de la "tuyauterie" secrète).
*   **Dépendance Amont :** Graphe orienté ou matrice de transitions temporelles de clusters.
*   **Dépendance Aval :** Visualisation Sankey des fuites systémiques.
*   **Complexité Algorithmique :** O(K²) où K est le petit nombre de clusters. Instantané.
*   **Contraintes & Hypothèses (Assumptions) :** On postule qu'un flux traversant deux clusters n'est jamais un accident démographique, mais la preuve d'un "tunnel de contournement" institutionnalisé.
*   **Limites / Biais (Edge Cases) :** Si les deux clusters sont minuscules (ex: deux lycées ultra-élitistes s'échangeant 5 élèves), le ratio $R_{ab}$ explosera artificiellement, créant l'illusion d'une autoroute migratoire.

---

### 14. Fragmentation Territoriale (Moran sur Clusters)
**Formule :**

$$
\Huge I_k = \frac{(x_k - \bar{x})^T W (x_k - \bar{x})}{\sum (x_k - \bar{x})^2} \quad \text{et} \quad F_{territorial} = 1 - I_{Moran}
$$
*   **Quoi :** Mesure de la "ghettoïsation spatiale" des clusters sociaux.
*   **Légende :** $I_k$ : Indice de Moran catégoriel, $x_k$ : indicateur d'appartenance au cluster $k$, $W$ : matrice géographique, $F_{territorial}$ : fragmentation globale.
*   **Pourquoi :** Prouver que la ségrégation n'est pas qu'un phénomène abstrait de notes, mais une réalité géographique (des blocs physiques de lycées populaires collés les uns aux autres).
*   **Inputs :** Indicatrices de cluster ($x_k \in \{0,1\}$) et matrice spatiale W.
*   **Outputs :** Indice d'auto-corrélation spatiale catégoriel (Moran global et local).
*   **Dépendance Amont :** Bibliothèques spatiales (PySAL, ESDA).
*   **Dépendance Aval :** Cartographie LISA des clusters territoriaux.
*   **Complexité Algorithmique :** O(N²) calcul matriciel spatial.
*   **Contraintes & Hypothèses (Assumptions) :** L'outil suppose que l'éloignement physique empêche la mixité : si les lycées riches sont tous géographiquement compactés à l'Ouest de Paris, le système est territorialement fracturé.
*   **Limites / Biais (Edge Cases) :** En plein centre-ville, où un lycée privé d'élite est situé littéralement au bout de la rue d'un lycée public défavorisé, l'indice de Moran y verra une mixité spatiale exceptionnelle, alors que la ségrégation y est absolue.

---

### 15. Frontières Sociales Floues (Gradient KDE & Entropie)
**Formule :**

$$
\Huge H(x) = -\sum_k P_k(x) \log P_k(x) \quad \text{et} \quad F_t = \int H_t(x) dx
$$
*   **Quoi :** Carte d'entropie qui remplace la ligne de fracture "pure et dure" par des "zones d'incertitude et de mélange" via l'estimation par noyau KDE.
*   **Légende :** $H(x)$ : entropie au point géographique $x$, $P_k(x)$ : probabilité lissée par noyau d'appartenir au cluster $k$ à cet endroit.
*   **Pourquoi :** Visualiser la ségrégation comme un nuage de gaz plutôt que comme un mur de briques : traquer les zones "grises" où le système hésite, se mélange, et offre de vraies opportunités de mixité.
*   **Inputs :** Coordonnées spatiales (x, y) et Kernel Density Estimation $f_k(x)$ par cluster.
*   **Outputs :** Heatmap d'entropie $H(x)$ (carte des zones grises) et animation temporelle.
*   **Dépendance Amont :** Scipy/Sklearn KernelDensity.
*   **Dépendance Aval :** Interpolation Plotly Mapbox et Matplotlib Animation.
*   **Complexité Algorithmique :** O(N \cdot M) où M est la résolution de la grille (ex: 100x100). Très lourd visuellement si la grille est fine.
*   **Contraintes & Hypothèses (Assumptions) :** On suppose qu'un élève vivant dans une zone d'entropie maximale a le pouvoir effectif d'hésiter entre les deux mondes.
*   **Limites / Biais (Edge Cases) :** Le lissage excessif du noyau (bandwidth trop grand) peut créer des zones de "mélange théorique" virtuel par-dessus des fleuves, des forêts ou des barrières physiques, là où aucun lycée n'existe réellement.

---

### 16. Indice d'Accord des 3 Critères (Cohérence Structurelle)
**Formule :**

$$
\Huge C_i = 1 - \frac{\text{Var}(\tilde{S}_i, \tilde{A}_i, \tilde{F}_i)}{3}
$$
*   **Quoi :** Mesure de l'alignement entre le niveau social ($S$), la performance ($A$) et l'attractivité ($F$) d'un lycée.
*   **Légende :** $C_i$ : cohérence du lycée, $\tilde{S}_i$ : score social standardisé, $\tilde{A}_i$ : score académique, $\tilde{F}_i$ : score d'attractivité (flux).
*   **Pourquoi :** Identifier les "anomalies du système" (les lycées paradoxaux qui réussissent sans le bon profil social, ou qui échouent malgré l'entre-soi bourgeois) par rapport aux blocs scolaires cohérents.
*   **Inputs :** Scores Z-standardisés : social $\tilde{S}_i$, académique $\tilde{A}_i$, flux $\tilde{F}_i$.
*   **Outputs :** Indice de cohérence $C_i \in [0,1]$ et cartographie spatiale.
*   **Dépendance Amont :** Standardisation Scaler.
*   **Dépendance Aval :** Analyse des divergences.
*   **Complexité Algorithmique :** O(N), calcul direct par variance locale.
*   **Contraintes & Hypothèses :** On suppose qu'un lycée "normal" dans un système inégalitaire parfait a ses trois variables parfaitement corrélées.
*   **Limites / Biais :** Si les trois critères sont faux/bruités dans la même direction, l'algorithme y verra une "harmonie" parfaite alors que c'est une erreur de mesure.

---

### 17. K Optimal Consensuel (Robustesse du Clustering)
**Formule :**

$$
\Huge C(k) = \alpha S(k) + \beta G(k) + \gamma B(k) + \delta S_{stab}(k)
$$
*   **Quoi :** Vote multi-critères (Silhouette, Gap Statistic, Inertie, Bootstrap) pour choisir le nombre "réaliste" de classes sociales.
*   **Légende :** $C(k)$ : score de consensus pour $k$ classes, $S(k)$ : Silhouette, $G(k)$ : Gap Statistic, $B(k)$ : inertie de coude, $S_{stab}$ : stabilité bootstrap.
*   **Pourquoi :** Éviter de choisir un $k$ arbitraire ou mathématiquement instable. Prouver que la segmentation retenue est la vraie ossature de la société, résiliente aux perturbations.
*   **Inputs :** Data spatio-sociale et boucle sur $k \in [2, 15]$.
*   **Outputs :** Nombre de clusters optimal $k^*$.
*   **Dépendance Amont :** K-Means et algorithmes de validation.
*   **Dépendance Aval :** Tous les algorithmes de réseaux (Louvain, CAH).
*   **Complexité Algorithmique :** Lourde, nécessite de faire tourner des K-Means bootstrapés des centaines de fois.
*   **Contraintes & Hypothèses :** On postule que la vérité sociale est celle qui résiste le mieux au bruitage informatique (Stabilité Bootstrap).
*   **Limites / Biais :** Les pondérations $\alpha, \beta, \gamma, \delta$ restent fixées par l'analyste, gardant une subjectivité dans le calcul du consensus.

---

### 18. Analyse des Divergences Algorithmiques
**Formule :**

$$
\Huge A_i = \text{Entropie}(\{C_i^{(m)}\}_m) \quad \text{et Indice Global} \quad F = 1 - \frac{1}{N}\sum A_i
$$
*   **Quoi :** Repérage des établissements qui sont classés différemment selon qu'on utilise KMeans, CAH, Louvain ou GMM.
*   **Légende :** $A_i$ : incertitude d'assignation du lycée $i$, $C_i^{(m)}$ : classe prédite par l'algorithme $m$, $F$ : taux global de désaccord systémique.
*   **Pourquoi :** Les divergences entre IA ne sont pas des bugs, ce sont des marqueurs de "zones frontières" ou de "lycées de transition" où plusieurs logiques sociales s'affrontent.
*   **Inputs :** Partitions issues d'algorithmes de géométrie (KMeans), de hiérarchie (CAH) et de graphe (Louvain).
*   **Outputs :** Heatmap d'entropie (Désaccord).
*   **Dépendance Amont :** Pipeline d'IA multiples en parallèle.
*   **Dépendance Aval :** Typologie des hybrides sociaux.
*   **Complexité Algorithmique :** Dépend du modèle le plus lourd (GMM/CAH).
*   **Contraintes & Hypothèses :** On suppose que l'incertitude mathématique équivaut à une incertitude sociologique réelle.
*   **Limites / Biais :** Certains algorithmes (comme Louvain) ont une part d'aléatoire inhérente ; un désaccord peut n'être qu'un artefact d'initialisation (Random Seed).

---

### 19. Validation Ultramétrique et Ponts Structurels
**Formule :**

$$
\Huge B_{ij} = d_{ij} - d_{ij}^U \quad \text{et Violation} \quad V = \sum \max(0, d_{ij} - \max(d_{ik}, d_{kj}))
$$
*   **Quoi :** Détection des "arêtes" géographiques qui relient deux lycées censés être séparés par un gouffre dans le dendrogramme social.
*   **Légende :** $B_{ij}$ : score de pont, $d_{ij}$ : distance réelle dans le réseau, $d_{ij}^U$ : distance théorique dans l'arbre hiérarchique, $V$ : taux de violation des inégalités d'arbre.
*   **Pourquoi :** Identifier les "exceptions scolaires" : les ponts ultramétriques révèlent quand le système de reproduction en arbre est piraté ou court-circuité par le réseau physique de la ville.
*   **Inputs :** Matrice de distance empirique $D$ et ultramétrique $D^U$ (cophenetic).
*   **Outputs :** Matrice de Ponts $B$ et Score de Hiérarchie $C$.
*   **Dépendance Amont :** Arbre CAH (Ward).
*   **Dépendance Aval :** Superposition de graphes et d'arbres.
*   **Complexité Algorithmique :** O(N³) pour le test triadique des inégalités ultramétriques.
*   **Contraintes & Hypothèses :** On postule que la société *devrait* être un arbre parfait (ultramétrique) et que chaque déviation est un canal de mobilité anormale.
*   **Limites / Biais :** L'algorithme de Ward force la création d'un arbre même si les données sont purement circulaires ou aléatoires, fabriquant des hiérarchies factices qui génèrent ensuite de "faux ponts".

---

### 20. Modèle Unifié et "Super-Goulots Systémiques" (HMM + GNN + DAG)
**Formule :**

$$
\Huge SG_{ij} = \alpha B_{ij}^{\text{HMM}} + \beta B_{ij}^{\text{GNN}} + \gamma B_{ij}^{U} + \delta B_{ij}^{C}
$$
*   **Quoi :** Modèle génératif colossal fusionnant le temps (Hidden Markov Model), le réseau (GNN), la hiérarchie (Ultramétrie) et l'inférence causale (DAG) pour isoler les goulets d'étranglement suprêmes.
*   **Légende :** $SG_{ij}$ : dangerosité du goulot, $B_{ij}$ : scores de pont selon les modèles Temporels (HMM), Réseau (GNN), Hiérarchiques (U) et Causaux (C).
*   **Pourquoi :** Trouver les quelques lycées ou trajets qui constituent les véritables "verrous structurels" du système éducatif national (ceux qui contrôlent toute la mobilité).
*   **Inputs :** Trajectoires sur 15 ans $X_t$, Matrices de Voisinage, Dendrogrammes, Graphes causaux.
*   **Outputs :** Cartographie des Super-Goulots $SG_{ij}$ et états cachés $Z_t$.
*   **Dépendance Amont :** L'intégralité des briques du Monde B.
*   **Dépendance Aval :** Simulation macro-économique de réforme publique.
*   **Complexité Algorithmique :** Extrême. L'optimisation conjointe d'un tel système multi-couches nécessite une descente de gradient sur architecture GPU (PyTorch/TensorFlow).
*   **Contraintes & Hypothèses :** On considère que le système scolaire est gouverné par des "états cachés" invisibles (ex: l'aura secrète d'une filière d'élite) et que l'algorithme EM de la HMM saura les révéler.
*   **Limites / Biais :** L'optimisation d'une équation à 5 couches génératives souffrira inévitablement de minima locaux et du fléau de la dimensionnalité, risquant de produire des super-goulots ininterprétables.

---

### 21. Perméabilité Structurelle Optimale ("Le point Goldilocks")
**Formule :**

$$
\Huge \Pi = \frac{P_{raw}}{C+\epsilon} \quad \text{avec} \quad P_{raw} = \sum_{i \neq j} T_{ij} \cdot d_{ij}^U \quad \text{et} \quad C = \sum_{i,j} |d_{ij}^U - E[d^U]|
$$
*   **Quoi :** Évaluation de l'équilibre parfait entre la circulation réelle des élèves (mobilité/flux) et le maintien d'une lisibilité du système (hiérarchie).
*   **Légende :** $\Pi$ : perméabilité globale, $P_{raw}$ : intensité brute des flux transgressant la hiérarchie, $C$ : coût du chaos ou désordre perçu.
*   **Pourquoi :** Démontrer qu'un système idéal n'est ni totalement fermé (ségrégation pure) ni totalement explosé (mixité désorganisée où plus aucune filière ne veut rien dire), mais à un point d'équilibre $\Pi^* = \text{argmax}(\text{mobilité} - \lambda \cdot \text{désordre})$.
*   **Inputs :** Matrice de transition des flux ($T$) et distance ultramétrique ($D^U$).
*   **Outputs :** Score de perméabilité $\Pi$ global et local (par lycée).
*   **Dépendance Amont :** Arbre CAH (pour $D^U$) et matrice Markov (pour $T$).
*   **Dépendance Aval :** Cartographie des "lycées passerelles" vs "lycées isolants".
*   **Complexité Algorithmique :** Légère, simple aggrégation de matrices déjà calculées.
*   **Contraintes & Hypothèses :** Suppose que l'excès de mixité sans structure produit une illisibilité que les familles fuiront (vers le privé), justifiant l'existence d'un optimum.
*   **Limites / Biais :** L'optimisation dépend totalement du paramètre $\lambda$ (pénalité de désordre) qui est choisi arbitrairement par le modélisateur.

---

### 22. Modèle Causal de l'Indice de Fragmentation (IFC)
**Formule :**

$$
\Huge \text{IFC}_{ij} = \beta_0 + \beta_1 X_{1,ij} + \beta_2 X_{2,ij} + \beta_3 X_{3,ij} + \beta_4 X_{4,ij} + u_j + \epsilon_{ij}
$$
*   **Quoi :** Modèle multiniveau rattaché à un DAG pour désenchevêtrer les causes de la fragmentation scolaire (IFC).

*   **Légende :** 
    *   $IFC_{ij}$ : fragmentation locale
    *   $\beta_k$ : effets causaux directs
    *   $X_k$ : variables de sélectivité/transport
    *   $u_j$ : effet aléatoire de l'académie
    *   $\epsilon_{ij}$ : résidu individuel.

*   **Pourquoi :** L'IFC n'est pas qu'un symptôme. Il est l'effet :
    *   de l'IPS ($X_1$)
    *   de la sélectivité ($X_2$)
    *   de l'offre ($X_3$)
    *   du transport ($X_4$)
    *   sous l'effet parapluie du territoire ($u_j$).

*   **Inputs :** Données croisées lycées / zones académiques.

*   **Outputs :** Coefficients causaux directs $\partial IFC / \partial X_k$ et effet structurel territorial $Var(u_j)$.

*   **Dépendance Amont :** Graphe causal dirigé (DAG) avec `dowhy`.

*   **Dépendance Aval :** Simulation contrefactuelle, par exemple $do(X_2 = x)$.

*   **Complexité Algorithmique :** Lourde, régression mixte (`statsmodels.mixedlm`).

*   **Contraintes & Hypothèses :** On suppose le "Backdoor criterion" vérifié, c'est-à-dire l'absence de variables confondantes non observées majeures au niveau du quartier.

*   **Limites / Biais :** La colinéarité extrême entre IPS ($X_1$) et Sélectivité ($X_2$) rend difficile l'isolation pure de la "sélectivité".

---

### 23. Détection des Blocs Scolaires Multi-Couches
**Formule :**

$$
\Huge B^* = \text{argmax}(W + T - \lambda D^U)
$$
*   **Quoi :** Identification des "continents sociaux" en fusionnant la similarité d'IPS ($W$), la tuyauterie des flux ($T$) et l'éloignement dans l'arbre social ($D^U$).
*   **Légende :** $B^*$ : partition optimale, $W$ : similarité d'IPS, $T$ : matrice des flux réels, $D^U$ : distance hiérarchique, $\lambda$ : poids accordé à l'ordre hiérarchique.
*   **Pourquoi :** Dépasser les communes administratives. Trouver les vrais "territoires vécus" par les élèves.
*   **Inputs :** Les 3 matrices $W, T, D^U$.
*   **Outputs :** Partition en blocs $B_k$ via Spectral Clustering.
*   **Dépendance Amont :** Matrice d'affinité combinée $S = W + T - 0.5 \cdot D^U$.
*   **Dépendance Aval :** Analyse des frontières semi-perméables entre blocs.
*   **Complexité Algorithmique :** O(N³) pour le Spectral Clustering sur la matrice dense des lycées.
*   **Contraintes & Hypothèses :** On assume que le comportement des parents obéit à ces 3 forces conjointes.
*   **Limites / Biais :** Le poids relatif des 3 matrices est fixé à la main.

---

### 24. Les Super-Ponts Inter-Blocs
**Formule :**

$$
\Huge SP_{ij} = \frac{P_{ij} \cdot C_{ij}^{(bet)} \cdot U_{ij}}{\sum_{k,l} P_{kl}}
$$
*   **Quoi :** Détection des arêtes hyper-critiques qui lient non pas deux lycées, mais deux *Mondes* (Blocs).
*   **Légende :** $SP_{ij}$ : criticité du super-pont, $P_{ij}$ : flux réels d'élèves, $C_{ij}^{(bet)}$ : centralité Betweenness, $U_{ij}$ : saut ultramétrique (audace sociale du pont).
*   **Pourquoi :** Trouver le "Golden Gate" de la mobilité scolaire. Ce sont les points névralgiques du système qui, s'ils tombent, scindent la société en deux.
*   **Inputs :** Flux réels $P_{ij}$, Centralité $C_{bet}$, Distance hiérarchique $U_{ij}$.
*   **Outputs :** Matrice de super-ponts et extraction du 99e centile.
*   **Dépendance Amont :** Algorithme des blocs scolaires et Betweenness Centrality (`networkx`).
*   **Dépendance Aval :** Cartographie des "ascenseurs sociaux concentrés".
*   **Complexité Algorithmique :** Rapide une fois la betweenness calculée.
*   **Contraintes & Hypothèses :** Un super-pont exige une violation de l'ultramétrie : il doit relier l'improbable.
*   **Limites / Biais :** Très sensible aux faibles effectifs. Un transfert isolé de 3 élèves entre Neuilly et Aubervilliers va faire exploser $U_{ij}$ et créer un faux super-pont si on ne met pas de seuil minimal de flux.

---

### 25. Hyper-ségrégation Masquée (Illusion de Mixité)
**Formule :**

$$
\Huge F_c = Var_{global}(IPS_c) - \sum_{i \in c} Var_{interne}(IPS_i) \quad \text{et} \quad HS_c = (-F_c) \cdot S_c
$$

*   **Quoi :** Détection des communes qui "paraissent" mixtes (bonne moyenne, bonne variance globale) mais qui sont en réalité des archipels d'écoles pures et isolées (variance interne très faible).

*   **Légende :** 
    *   $F_c$ : fausse mixité
    *   $Var_{global}$ : hétérogénéité apparente de la ville
    *   $Var_{interne}$ : (absence de) mixité au sein des lycées
    *   $HS_c$ : hyper-ségrégation totale.

*   **Pourquoi :** Détruire le mythe des "villes mixtes" où le public et le privé cohabitent géographiquement mais s'ignorent scolairement.

*   **Inputs :** IPS des élèves par établissement et par commune.

*   **Outputs :** Score d'Hyper-Ségrégation cachée $HS_c$.

*   **Dépendance Amont :** Agrégation micro-données élèves.

*   **Dépendance Aval :** Cartographie géospatiale de l'illusion statistique.

*   **Complexité Algorithmique :** O(N), GroupBy très rapide.

*   **Contraintes & Hypothèses :** On suppose que la vraie mixité se vit dans les murs du lycée, pas dans les rues de la commune.
*   **Limites / Biais :** Si la commune ne possède qu'un seul grand lycée polyvalent, l'équation s'effondre mathématiquement (elle ne peut pas avoir de fausse mixité inter-établissements).

---

### 26. Dérive Temporelle de la Mobilité (Matrice T)
**Formule :**

$$
\Huge \Delta T_t = \alpha X_1 + \beta X_2 + \gamma X_3 + \delta T_{t-1} + \eta Z_t
$$
*   **Quoi :** Équation de dynamique modélisant l'évolution de la tuyauterie du système (les flux de transition) au fil du temps.
*   **Légende :** $\Delta T_t$ : changement de tuyauterie d'une année à l'autre, $X_k$ : variables macro, $T_{t-1}$ : inertie des flux, $Z_t$ : chocs exogènes (ex: nouvelle ligne de métro).
*   **Pourquoi :** La ségrégation est path-dependent (dépendante de son passé). Prouver l'inertie $I = \text{corr}(T_t, T_{t+1})$.
*   **Inputs :** Matrices $T$ annuelles, vecteurs de variables socio-politiques $X$.
*   **Outputs :** Tenseur de dérive et détection de points de bascule structurelle $|T_{t+1} - T_t| > \theta$.
*   **Dépendance Amont :** Séries temporelles longues (Panel data).
*   **Dépendance Aval :** Prédiction causale des effets de réformes.
*   **Complexité Algorithmique :** Lourde (Régression panel dynamique).
*   **Contraintes & Hypothèses :** On assume que le système a une "mémoire" ($\delta T_{t-1}$).
*   **Limites / Biais :** Les changements de sectorisation géographique créent des chocs exogènes énormes ($Z_t$) qui noient parfois la lente dérive sociologique endogène.

---

### 27. Indice d'Autonomie Scolaire (IAS)
**Formule :**

$$
\Huge IAS_i = \alpha A_i + \beta S_i + \gamma F_i - \delta C_i
$$
*   **Quoi :** Modèle structurel distinguant les lycées qui font leur propre loi (Hubs ou Enclaves) de ceux qui subissent la démographie locale.
*   **Légende :** $IAS_i$ : capacité d'affranchissement, $A_i$ : attractivité lointaine, $S_i$ : constance de l'IPS, $F_i$ : sélectivité, $C_i$ : poids du recrutement sectorisé imposé.
*   **Pourquoi :** Dépasser le simple clivage "Public vs Privé".
*   **Inputs :** Attractivité hors-zone ($A$), stabilité IPS ($S$), contrôle des flux ($F$), dépendance quartier ($C$).
*   **Outputs :** Score IAS par lycée et clustering (1D KMeans) en 3 catégories.
*   **Dépendance Amont :** Analyse des flux croisés avec la géographie (Corrélation IPS_lycée vs IPS_quartier).
*   **Dépendance Aval :** Carte de dépendance territoriale.
*   **Complexité Algorithmique :** O(N), rapide.
*   **Contraintes & Hypothèses :** On suppose qu'un lycée ne veut qu'une chose : s'affranchir de la gravité de son territoire pour sélectionner les meilleurs.
*   **Limites / Biais :** Les lycées de centre-ville ultra-favorisé ont un IAS qui semble faible car leur recrutement "local" est déjà exceptionnel (le territoire est déjà élitiste).

---

### 28. Décomposition des Effets Indirects (Quartier vs Réseau)
**Formule :**

$$
\Huge Y_i = E_i^{quartier} + E_i^{\text{reseau}} + \epsilon_i \quad \text{et l'interaction} \quad E_i^{indirect} = E_i^{quartier} \times E_i^{\text{reseau}}
$$
*   **Quoi :** Modèle spatial multiniveau isolant ce qui vient du "sol" (voisinage) et ce qui vient des "câbles" (connexions).
*   **Légende :** $Y_i$ : position du lycée, $E_i^{quartier}$ : composante purement kilométrique, $E_i^{\text{reseau}}$ : composante via les transports/filières, $\epsilon_i$ : non-expliqué.
*   **Pourquoi :** Démontrer que le réseau scolaire peut soit agir comme amortisseur de la fatalité territoriale, soit comme amplificateur de la ségrégation de quartier.
*   **Inputs :** Matrice géographique vs Matrice de flux/graphe.
*   **Outputs :** Ratios de variance expliquée ($R^2_{quartier}$ vs $R^2_{\text{reseau}}$).
*   **Dépendance Amont :** Modèle spatial autorégressif (SAR) double.
*   **Dépendance Aval :** Cartographie conceptuelle des dominations (Paris=Réseau, Grande Couronne=Quartier).
*   **Complexité Algorithmique :** Modérée à lourde.
*   **Contraintes & Hypothèses :** On suppose que "sol" et "câbles" sont deux espaces mathématiquement indépendants avant leur interaction.
*   **Limites / Biais :** En Île-de-France, le réseau de transport dicte le réseau scolaire, ce qui rend l'effet "Quartier" (desserte SNCF) et l'effet "Réseau" difficiles à scinder purement.

---

### 29. Causalité des Hotspots (Asymétrie Causale : Cause vs Effet)
**Formule :**

$$
\Huge \quad \text{Équation de panel :} \quad H_{i,t+1} = \alpha H_{i,t} + \beta \sum_j W_{ij} H_{j,t} + \gamma X_{i,t} + \epsilon_{i,t} \quad \text{. Score causal net :} \quad C_i = C_i^{out} - C_i^{in} \quad \text{avec} \quad C_i^{out} = \sum_j \frac{\partial Y_j}{\partial H_i} \quad \text{et} \quad C_i^{in} = \sum_j \frac{\partial H_i}{\partial Y_j} \quad \text{.} \quad
$$
*   **Quoi :** Test de temporalité et de pouvoir prédictif pour déterminer si un hotspot ségrégué est la *source* de l'inégalité environnante ou le *produit* d'une dégradation de son voisinage.
*   **Légende :** $H_{i,t}$ : tension du hotspot $i$, $C_i^{out}$ : capacité de $i$ à contaminer le reste du réseau, $C_i^{in}$ : vulnérabilité de $i$ face aux crises des autres.
*   **Pourquoi :** Sortir du constat descriptif (Monde A) pour prouver qu'il existe des "lycées structurants" (qui imposent leur loi, $C_i > 0$) et des "territoires captifs" (qui subissent la loi des autres, $C_i < 0$).
*   **Inputs :** Séries temporelles d'IPS, matrice spatiale $W_{ij}$.
*   **Outputs :** Cartographie en 3 classes (Hotspots-causes, Hotspots-effets, Hotspots-hybrides/rétroaction).
*   **Dépendance Amont :** Modèle spatial dynamique (Spatial Panel Model).
*   **Dépendance Aval :** Simulation d'interventions politiques (cibler les causes, pas les effets).
*   **Complexité Algorithmique :** Lourde (Régression panel spatial avec instruments).
*   **Contraintes & Hypothèses :** Suppose que la causalité laisse une trace dans la précédence temporelle (principe de Granger).
*   **Limites / Biais :** Les réformes brutales de sectorisation peuvent créer des "chocs" artificiels qui brouillent la détection de l'inertie endogène.

---

### 30. Modèle Causal Spatial Non-Linéaire (GAM + Spatial RF)
**Formule :**

$$
\Huge Y_i = \sum_k s_k(X_{ik}) + \rho \sum_j W_{ij} Y_j + u(s_i) + \epsilon_i \quad \text{avec un champ spatial} \quad u(s_i) \sim GP(0, K(s_i,s_j)) \quad \text{.} \quad
$$
*   **Quoi :** Modèle estimant des effets causaux qui varient dans l'espace et de manière non-linéaire (effets seuils), tout en purgeant l'autocorrélation spatiale.
*   **Légende :** $s_k$ : fonction de lissage (spline) permettant les effets non-linéaires, $\rho W Y$ : contagion spatiale, $u(s_i)$ : processus gaussien captant le bruit géolocalisé.
*   **Pourquoi :** Prouver que le système scolaire n'est pas additif (Monde A linéaire) : l'effet du privé ou de l'IPS n'est pas constant, il "sature" ou a des effets plafonds.
*   **Inputs :** Variables scolaires $X_{ik}$, graphe de réseau $W$, coordonnées géographiques $s_i$.
*   **Outputs :** Fonctions de lissage (splines) pour chaque variable et champ spatial résiduel.
*   **Dépendance Amont :** GAM (Generalized Additive Models) et Processus Gaussiens.
*   **Dépendance Aval :** Cartographie des effets non-linéaires (changement de signe des gradients).
*   **Complexité Algorithmique :** Très lourde (Optimisation spline + krigeage).
*   **Contraintes & Hypothèses :** Nécessite une spécification minutieuse des splines pour éviter l'overfitting local.
*   **Limites / Biais :** Difficile d'isoler ce qui relève de la non-linéarité pure ($s_k$) de l'effet réseau ($\rho W Y$) sans un volume massif de données.

---

### 31. Tipping Points et Instabilité Structurelle
**Formule :**

$$
\Huge \quad \text{Changement de signe} \quad \Delta sign(\nabla Y_i) \quad \text{avec} \quad \nabla Y_i = \frac{\partial Y_i}{\partial IPS_i} \quad \text{. Condition critique d'instabilité :} \quad \rho \lambda_{max}(W) \ge 1 \quad \text{.} \quad
$$
*   **Quoi :** Détection des "zones de bascule", les points d'inflexion exacts où le gradient s'inverse (ex: où un point d'IPS supplémentaire ne protège plus, mais accélère la fuite).
*   **Légende :** $\nabla Y_i$ : gradient (pente) de l'effet d'une variable, $\Delta sign$ : point de basculement, $\rho \lambda_{max}(W)$ : condition spectrale de résonance du réseau.
*   **Pourquoi :** Identifier les "zones de rupture" où de très petites variations (une réforme mineure) vont déclencher des changements d'état massifs par effet de propagation.
*   **Inputs :** Dérivées du modèle GAM spatial (Modèle 30).
*   **Outputs :** Score de bascule $T_i$ et cartographie des "Tipping points" scolaires.
*   **Dépendance Amont :** Calcul des valeurs propres de la matrice réseau ($\lambda_{max}(W)$).
*   **Dépendance Aval :** Simulation de "réformes critiques" vs "réformes neutres".
*   **Complexité Algorithmique :** Complexe (calcul analytique des dérivées spatiales).
*   **Contraintes & Hypothèses :** Suppose que le basculement local déclenche une onde de choc à travers tout le réseau via le multiplicateur $(I - \rho W)^{-1}$.
*   **Limites / Biais :** Le seuil de basculement est ultra-sensible au calibrage mathématique de la matrice $W$.

---

### 32. Classification des Mondes Scolaires Cachés (Latent Class)
**Formule :**

$$
\Huge P(Y_i | X_i) = \sum_{k=1}^K P(Z_i=k) P(Y_i | X_i, Z_i=k) \quad \text{avec un modèle mixte} \quad Y_i = \beta_{Z_i} X_i + u_{Z_i} + \epsilon_i \quad \text{. Entropie} \quad H_i = \text{entropy}(P(Z_i)) \quad \text{.} \quad
$$
*   **Quoi :** Découverte de variables latentes $Z_i$ révélant la coexistence de différents "Régimes" (Monde élite autonome, concurrentiel, territorial, transition, fragmenté).
*   **Légende :** $P(Y_i|X_i)$ : probabilité du profil du lycée, $Z_i=k$ : assignation au \"Monde caché\" $k$, $\beta_{Z_i}$ : règles sociologiques spécifiques au monde $k$.
*   **Pourquoi :** Le système n'est pas un continuum social simple ; c'est une superposition de mondes qui ont chacun leurs propres règles de gravité sociale.
*   **Inputs :** Attractivité, IPS, flux, dépendance territoriale.
*   **Outputs :** Probabilité d'appartenance à chaque "Monde" pour chaque lycée, et entropie (incertitude).
*   **Dépendance Amont :** Latent Class Mixed Models (LCMM).
*   **Dépendance Aval :** Cartographie de l'entropie pour trouver les "zones de transition" ou de conflit entre mondes.
*   **Complexité Algorithmique :** Algorithme EM très coûteux sur données mixtes.
*   **Contraintes & Hypothèses :** Fixation algorithmique du nombre $K$ (on postule 5 mondes, mais cela doit être prouvé par critère BIC).
*   **Limites / Biais :** Les zones très hétérogènes (entropie maximale) risquent d'être forcées arbitrairement dans une classe.

---

### 33. Blind Spots et Frontières Non-Modélisées
**Formule :**

$$
\Huge \quad \text{Index} \quad BS_i = |R_i| \cdot \sum_j W_{ij} |R_j| \quad \text{et indice de frontière invisible} \quad B_{ij} = |R_i - R_j| \cdot W_{ij} \quad \text{. Autocorrélation via Indice de Moran} \quad I_R \quad \text{.} \quad
$$
*   **Quoi :** Analyse spatiale des "échecs" systématiques des modèles prédictifs (les résidus structurés).
*   **Légende :** $BS_i$ : anomalie du lycée $i$, $R_i$ : résidu du modèle, $B_{ij}$ : intensité de la frontière occulte entre $i$ et $j$.
*   **Pourquoi :** Traiter les anomalies mathématiques comme des preuves sociologiques. Un modèle qui se trompe fortement *et* de manière spatialement corrélée révèle la présence d'une force occulte (ex: contournement de carte invisible).
*   **Inputs :** Résidus $R_i$ issus des différents modèles (GAM, RF, LCMM).
*   **Outputs :** Heatmap des erreurs systémiques et lignes de fracture invisibles ($B_{ij}$).
*   **Dépendance Amont :** Indice de Moran global et local (LISA).
*   **Dépendance Aval :** Fusion systémique en 4 couches.
*   **Complexité Algorithmique :** Rapide une fois les résidus obtenus.
*   **Contraintes & Hypothèses :** On considère que toute erreur auto-corrélée est un signal, et non du bruit blanc.
*   **Limites / Biais :** Peut confondre une "vraie" anomalie sociologique avec une simple erreur de géocodage massif des données.

---

### 34. Fusion Systémique en 4 Couches (Le Jumeau Numérique)
*   **Quoi :** Superposition conceptuelle liant : Les Mondes Latents (Régimes) $\rightarrow$ Les Blocs (Structure) $\rightarrow$ Les Blind Spots (Inconnu structuré) $\rightarrow$ Les Frontières et Super-Ponts (Réseau).
*   **Pourquoi :** Fournir le diagnostic structurel complet et l'explication unifiée du système scolaire francilien (c'est l'architecture logicielle finale de l'Atlas).
*   **Dépendance Amont :** Tous les algorithmes du Monde B (Modèles 16 à 33).
*   **Dépendance Aval :** Tableau de bord final et récit éditorial global.

---

### 35. Décomposition Totale de Variance (ICC + Spatial ICC)
**Formule :**

$$
\Huge \text{Var}(Y) = \sigma^2_{zone} + \sigma^2_{school} + \sigma^2_{spatial} + \sigma^2_{resid} \quad \text{avec un Indice de Structuration Globale} \quad SCI = \text{ICC}_{zone} + \text{ICC}_{school} + \text{ICC}_{spatial} \quad \text{.} \quad
$$
*   **Quoi :** Isoler précisément d'où vient l'inégalité : du "quartier" (zone), du "lycée" (institution), du "voisinage" (diffusion/contagion spatiale), ou du résidu (le bruit / blind spot).
*   **Légende :** $\sigma^2_{zone}$ : fatalité du quartier, $\sigma^2_{school}$ : responsabilité propre du proviseur/lycée, $\sigma^2_{spatial}$ : effet de meute (voisinage).
*   **Pourquoi :** Répondre définitivement au débat public : "Le problème vient-il du ghetto géographique, du choix de l'école, ou de l'effet de mode du réseau local ?".
*   **Inputs :** Modèle hiérarchique complet avec processus gaussien spatial.
*   **Outputs :** Ratios de corrélation intra-classe (ICC) stricts.
*   **Dépendance Amont :** ANOVA spatiale multiniveau.
*   **Dépendance Aval :** Typologie des systèmes (Territorial vs Hiérarchique vs Réseau).
*   **Complexité Algorithmique :** Modérée (estimation de variance MCMC ou REML).
*   **Contraintes & Hypothèses :** Supposer une additivité des variances (bien qu'il y ait interaction via $\text{Cov}(u_{zone}, v_{school})$).
*   **Limites / Biais :** Très sensible à la définition de la "zone" (MAUP : Modifiable Areal Unit Problem).

---

### 36. Clusters Absorbants (Attracteurs de Réseau)
**Formule :**

$$
\Huge \sum_{i \notin C_k, j \in C_k} T_{ij} \gg \sum_{i \in C_k, j \notin C_k} T_{ij} \quad \text{. Score d'absorption :} \quad A_k = \frac{In_k}{Out_k} + \epsilon \quad \text{. Centralité propre (Rayon spectral) :} \quad \rho(T_{C_k}) > 1 \quad \text{.} \quad
$$
*   **Quoi :** Détection de groupes d'établissements qui agissent comme des trous noirs dans le réseau de mobilité (attirent massivement, ne laissent pas repartir).
*   **Légende :** $A_k$ : force gravitationnelle du cluster $k$, $In_k$ : flux entrant depuis d'autres mondes, $Out_k$ : flux fuyant vers d'autres mondes, $\rho(T)$ : rayon spectral de stabilité.
*   **Pourquoi :** Dépasser le clustering statique pour trouver les "puits structurels" qui déforment tout le système par leur gravité et stabilisent les trajectoires de l'élite.
*   **Inputs :** Matrice des flux $T_{ij}$, partition des clusters $C_k$.
*   **Outputs :** Vecteur des scores d'absorption $A_k$ et dérivée temporelle $\frac{dA_k}{dt}$.
*   **Dépendance Amont :** Graphes orientés, Eigenvector Centrality.
*   **Dépendance Aval :** Causalité : $A_k \rightarrow \Delta T_{jk}$ (le puits modifie la structure future).
*   **Complexité Algorithmique :** O(N³) pour le calcul du rayon spectral de sous-matrices.
*   **Contraintes & Hypothèses :** On suppose que le système scolaire n'est pas à l'équilibre, mais en phase d'accumulation vers certains nœuds.
*   **Limites / Biais :** Les clusters géographiquement fermés en bordure d'académie sembleront "absorbants" simplement parce que les élèves ne peuvent pas fuir l'académie voisine (bruit de frontière administrative).

---

### 37. Trajectoires Rares (Outliers Séquentiels)
**Formule :**

$$
\Huge P(\tau_i) = \prod_t P(s_{t+1} \mid s_t) \quad \text{. Score d'anomalie :} \quad A(\tau_i) = -\log P(\tau_i) \quad \text{. Centralité de transition rare :} \quad O_i = \sum_t \frac{1}{T_{s_t s_{t+1}}} \quad \text{.} \quad
$$
*   **Quoi :** Repérage des trajectoires d'élèves qui violent les chaînes de Markov standard (ex: sauts longue distance, ascensions impossibles, chutes brutales).
*   **Légende :** $P(\tau_i)$ : probabilité qu'un élève suive cette trajectoire $\tau$, $A(\tau)$ : étrangeté absolue du parcours (souvent lié à l'évitement scolaire).
*   **Pourquoi :** Une trajectoire rare n'est pas une "exception statistique" à ignorer, c'est la signature d'un réseau occulte (contournement institutionnel, réseau privé, filière secrète).
*   **Inputs :** Historique longitudinal des élèves $\tau_i = (s_{i1}, s_{i2}, ..., s_{iT})$.
*   **Outputs :** Classification des anomalies (Contre-hiérarchique, Sauté, Oscillant, Long-range jump).
*   **Dépendance Amont :** Modèle de Markov caché (HMM) de base pour le système.
*   **Dépendance Aval :** Extraction de la sous-structure latente : $\tau_i \sim \sum_k \pi_k P_k(\tau)$.
*   **Complexité Algorithmique :** O(T * N) pour scorer N élèves sur T pas de temps.
*   **Contraintes & Hypothèses :** Tout écart sévère à la norme est considéré comme le résultat d'une stratégie sociale, et non du pur hasard.
*   **Limites / Biais :** Les déménagements de famille en cours de scolarité créent des "trajectoires rares" géographiques qui n'ont rien à voir avec de l'évitement scolaire.

---

### 38. Distorsion Spatiale des Flux (Sankey Géographique)
**Formule :**

$$
\Huge \quad \text{Flux spatialisé :} \quad \tilde{T}_{ij} = T_{ij} \cdot e^{-\lambda d_{ij}} \quad \text{. Indice de Distorsion :} \quad D = \frac{\sum T_{ij}}{\sum \tilde{T}_{ij}} \quad \text{. Tension spatiale :} \quad \Delta = \text{Var}(T_{ij}) - \text{Var}(\tilde{T}_{ij}) \quad \text{.} \quad
$$
*   **Quoi :** Superposition du réseau de flux (Sankey) sur la géographie physique pour mesurer à quel point les élèves ignorent la proximité pour s'inscrire loin.
*   **Légende :** $\tilde{T}_{ij}$ : flux d'élèves pénalisé par la distance, $\lambda$ : friction kilométrique, $D$ : indice de distorsion montrant si les flux violent la géographie.
*   **Pourquoi :** Prouver l'existence d'une géométrie "déformée" de la ségrégation : un $D$ élevé prouve que le marché scolaire est déconnecté de la carte locale, régi par la hiérarchie pure.
*   **Inputs :** Matrice de flux $T_{ij}$, Matrice de distances physiques $d_{ij}$.
*   **Outputs :** Graphe pondéré $G=(V,\tilde{T},s)$ et détection des Corridors Sociaux $C_{ij} = T_{ij} \cdot \mathbf{1}(d_{ij} > \delta)$.
*   **Dépendance Amont :** Coordonnées géographiques précises (Lat/Lon) et Matrice O-D.
*   **Dépendance Aval :** Visualisation cartographique 3D Sankey-Map.
*   **Complexité Algorithmique :** O(N²) calcul rapide de distances euclidiennes ou haversine.
*   **Contraintes & Hypothèses :** On applique une pénalité exponentielle $e^{-\lambda d}$ pour l'effort physique du transport.
*   **Limites / Biais :** L'équation ignore la vraie topologie des transports (RER, métro). Un flux à 15 km en RER A est sociologiquement plus "proche" qu'un flux à 5 km sans ligne directe.

---

### 39. Causalité des Changepoints (Réforme vs Démographie)
**Formule :**

$$
\Huge Y_t = \alpha Y_{t-1} + \beta R_t + \gamma D_t + \delta P_t + \epsilon_t \quad \text{. Causalité spatiale des ruptures :} \quad \Delta Y_{i,t} = \rho \sum_j W_{ij} \Delta Y_{j,t} \quad \text{.} \quad
$$
*   **Quoi :** Démêlage économétrique des points de rupture ($\tau^* = \text{argmax}_t \Delta L(t)$) pour isoler le vrai choc exogène (Réforme) de la dérive endogène (Démographie) ou de la réallocation (Privé).
*   **Légende :** $\tau_k$ : probabilité que la rupture soit due à la réforme $k$, $Z$ : variables inobservées (bruit macro-économique).
*   **Pourquoi :** Montrer que certaines politiques prétendument "révolutionnaires" ne font que surfer sur des vagues démographiques, tandis que des réformes invisibles fracturent vraiment le système.
*   **Inputs :** Vecteurs temporels $R_t$ (réformes), $D_t$ (démographie), $P_t$ (privé).
*   **Outputs :** Test causal $C_t = \text{Var}(\Delta Y_t)_{post} - \text{Var}(\Delta Y_t)_{pre}$.
*   **Dépendance Amont :** Détection des changepoints (PELT, Modèle 9).
*   **Dépendance Aval :** Cartographie des ruptures causales.
*   **Complexité Algorithmique :** Estimation de panels dynamiques.
*   **Contraintes & Hypothèses :** Suppose que les réformes sont des chocs "Dirac" (impulsions) et la démographie une onde lente.
*   **Limites / Biais :** La croissance du privé agit souvent comme une conséquence des réformes publiques (effet de fuite), ce qui crée une forte endogénéité entre $R_t$ et $P_t$.

---

### 40. Ruptures Ultramétriques Causales (DAG Temporel)
**Formule :**

$$
\Huge \quad \text{Intensité de rupture :} \quad R_t = d(U_t, U_{t-1}) \quad \text{. DAG temporel :} \quad Y_{t+1} = f(Y_t, X_t, U_t, W_t) + \epsilon \quad \text{.} \quad
$$
*   **Quoi :** Introduction de la hiérarchie latente ($U_t$) comme véritable nœud causal. Un changement de dendrogramme n'est pas qu'un symptôme, c'est un agent infectieux qui se propage : $\Delta Y_{i,t} = \rho \sum_j W_{ij} \Delta U_t$.
*   **Légende :** $\Delta_{ij}(t)$ : changement de distance hiérarchique entre $i$ et $j$ au temps $t$, $P_{ij}$ : choc de flux, $X_{ij}$ : dégradation relative d'attractivité.
*   **Pourquoi :** Prouver que la structure invisible de l'élite contrôle l'évolution de la masse : quand l'élite resserre son entre-soi (fusion/fragmentation ultramétrique), cela déclenche une onde de choc causale sur tous les autres.
*   **Inputs :** Matrices ultramétriques historiques $U_t$.
*   **Outputs :** Typologie des séismes : Fragmentation, Fusion, Re-ranking, Reconfiguration réseau.
*   **Dépendance Amont :** Indice global d'ultramétrie (Modèle 10).
*   **Dépendance Aval :** Preuve d'intervention $P(Y_{t+1} \mid \text{do}(R_t)) \neq P(Y_{t+1})$.
*   **Complexité Algorithmique :** Très lourde (calcul de distances entre arbres sur séries longues).
*   **Contraintes & Hypothèses :** On part du principe que l'information hiérarchique ruisselle de haut en bas et dicte les anticipations des parents.
*   **Limites / Biais :** L'instabilité algorithmique naturelle des arbres CAH d'une année sur l'autre générera énormément de bruit, imitant des "séismes" là où il n'y a que de la variance d'échantillonnage.

---

### 41. Carte Continue des Trajectoires (Ascension vs Déclin)
**Formule :**

$$
\Huge \Delta S_{i,t} = S_{i,t} - S_{i,t-1} \quad \text{. Indice de dynamique spatiale :} \quad T_i = \frac{\bar{\Delta S_i}}{\text{Var}(\Delta S_i) + \epsilon} \quad \text{. Champ} \quad T(s) = f(\bar{\Delta S}, \text{Var}(\Delta S)) \quad \text{.} \quad
$$
*   **Quoi :** Projection spatiale des lycées non plus comme des "niveaux fixes", mais comme des vecteurs de vitesse (qui monte, qui chute, qui vibre).
*   **Légende :** $\vec{V}(x,y)$ : vecteur de force au point $x,y$, $\nabla S$ : pente de déclassement social, $\nabla A$ : pente d'attractivité.
*   **Pourquoi :** Les familles choisissent l'école sur son "momentum", pas sur son état présent. Un lycée moyen en ascension est plus attractif qu'un bon lycée en chute libre.
*   **Inputs :** Scores synthétiques longitudinaux $S_{i,t}$.
*   **Outputs :** Catégorisation en 3 régimes : Ascendants ($T_i \gg 0$), Déclins ($T_i \ll 0$), Frontières Instables ($T_i \approx 0$).
*   **Dépendance Amont :** Différentiation temporelle et interpolation spatiale (KDE/IDW).
*   **Dépendance Aval :** Couplage avec les flux $T_i \approx g(\sum_j T_{ji,t})$.
*   **Complexité Algorithmique :** Légère, O(N) sur l'agrégation, puis O(N²) pour l'interpolation de la carte continue.
*   **Contraintes & Hypothèses :** L'instabilité (variance élevée) est interprétée sociologiquement comme une "zone critique de compétition" et non comme une mauvaise qualité des données.
*   **Limites / Biais :** Le plafond de verre ($S_i$ borné) rend impossible l'ascension mathématique continue des lycées déjà au sommet de l'élite, les classant artificiellement comme "stagnants" ou "déclinants".

---

### 42. Transition de Phase (Seuil Critique et Effondrement)
**Formule :**

$$
\Huge \quad \text{Pression} \quad \Pi_t = \alpha \text{Inej}_t + \beta \text{Seg}_t + \gamma \text{Dem}_t + \delta \text{Priv}_t \quad \text{. Bascule} \quad S_{t+1} = S_t + f(\Pi_t) \quad \text{avec} \quad f(\Pi) = \frac{1}{1 + e^{-k(\Pi - \Pi_c)}} \quad \text{. Effondrement} \quad P(Z_{t+1}=\text{effondré} \mid \Pi_t) = \sigma(\Pi_t - \Pi_c) \quad \text{. Condition réseau} \quad \rho \lambda_{max}(W) \ge 1 \quad \text{.} \quad
$$
*   **Quoi :** Modèle de physique statistique prouvant que le système éducatif ne dérive pas lentement, mais "craque" d'un coup lorsqu'un seuil critique de pression ($\Pi_c$) est dépassé.
*   **Légende :** $\lambda_{max}$ : plus grande valeur propre de la matrice jacobienne du réseau, dictant si une crise locale reste locale ou embrase toute la région.
*   **Pourquoi :** Démontrer que la stabilité apparente d'une carte scolaire est souvent une illusion avant l'effondrement (phase transition), marqué par une variance explosive et une séparation brutale en blocs fermés.
*   **Inputs :** Séries temporelles de pression ($\Pi_t$), matrice d'amplification réseau $W$.
*   **Outputs :** État du système $Z_t \in \{\text{stable}, \text{effondré}\}$ et cartographie des zones critiques.
*   **Dépendance Amont :** Indices de Theil, Gini, et IPS dynamiques.
*   **Dépendance Aval :** Simulation de choc de réforme ou d'ouverture d'un lycée privé.
*   **Complexité Algorithmique :** Estimation de fonction sigmoïde sur séries temporelles, rapide.
*   **Contraintes & Hypothèses :** On suppose que le système absorbe la pression silencieusement jusqu'à un point de non-retour mathématique.
*   **Limites / Biais :** Estimer la valeur exacte du seuil $\Pi_c$ sur des données historiques bruitées est très incertain.

---

### 43. Analyse des Corridors Asymétriques (Ascenseurs vs Filtres)
**Formule :**

$$
\Huge \quad \text{Asymétrie} \quad A_{ij} = T_{ij} - T_{ji} \quad \text{. Indice} \quad \Gamma_{ij} = \frac{T_{ij} - T_{ji}}{T_{ij} + T_{ji} + \epsilon} \quad \text{. Ascenseur social :} \quad \Gamma_{ij} > \theta \text{ et } S_j - S_i > 0 \quad \text{. Filtre social :} \quad \Gamma_{ij} < -\theta \text{ et } S_j - S_i < 0 \quad \text{.} \quad
$$
*   **Quoi :** Classification directionnelle des flux pour prouver que la mobilité scolaire n'est pas un libre-échange neutre, mais une "tuyauterie" polarisée (certains tubes montent, d'autres descendent).
*   **Légende :** $Asym_{ab}$ : ratio d'inégalité des échanges, $T_{ab}$ : ceux qui montent, $T_{ba}$ : ceux qui descendent (ou inversement).
*   **Pourquoi :** Montrer que le système est asymétrique : les "ascenseurs" connectent des mondes éloignés pour une minorité, tandis que les "filtres" relèguent massivement les élèves vers la périphérie.
*   **Inputs :** Matrice des flux $T_{ij}$, prestige/sélectivité $S_i$.
*   **Outputs :** Matrice d'asymétrie $\Gamma$ et typologie (Ascenseurs, Filtres, Neutres).
*   **Dépendance Amont :** Algorithmes de graphes orientés.
*   **Dépendance Aval :** Visualisation spatiale des canaux de tri.
*   **Complexité Algorithmique :** O(V + E), très rapide.
*   **Contraintes & Hypothèses :** Suppose qu'un flux asymétrique descendant n'est jamais un "choix", mais toujours le résultat d'un filtre ou d'une contrainte.
*   **Limites / Biais :** De très faibles flux asymétriques (ex: 2 élèves dans un sens, 0 dans l'autre) produiront un score $\Gamma = 1$, créant des "micro-ascenseurs" insignifiants si on n'applique pas un seuil de volume minimal.

---

### 44. Corridors d'Élite vs Déclassement (Gradient Directionnel)
**Formule :**

$$
\Huge \quad \text{Gradient} \quad \Delta S_{ij} = S_j - S_i \quad \text{. Corridor d'élite :} \quad C^{elite}_{ij} = T_{ij} \cdot \mathbf{1}(\Delta S_{ij} > \theta) \quad \text{. Déclassement :} \quad C^{down}_{ij} = T_{ij} \cdot \mathbf{1}(\Delta S_{ij} < -\theta) \quad \text{. Efficacité} \quad E_{elite} = \frac{\sum C^{elite}}{\sum T} \quad \text{.} \quad
$$
*   **Quoi :** Filtrage macro-structurel du système pour peser précisément le volume de l'élitisme face au volume du déclassement.
*   **Légende :** $Grad_{ab}$ : pente sociologique du transfert, $S_a, S_b$ : richesses respectives des mondes de départ et d'arrivée.
*   **Pourquoi :** Mesurer si le système global est ouvert (forte mobilité ascendante structurée) ou fermé (domination des corridors de déclassement et reproduction locale).
*   **Inputs :** Flux pondérés par la distance sociale $\Delta S_{ij}$.
*   **Outputs :** Scores d'efficacité $E_{elite}$ et $E_{down}$.
*   **Dépendance Amont :** Couplage avec la distance géographique $d_{ij}$.
*   **Dépendance Aval :** Diagnostic final de la polarisation du système éducatif.
*   **Complexité Algorithmique :** Agrégation matricielle basique, instantanée.
*   **Contraintes & Hypothèses :** On considère le gradient $S_j - S_i$ comme une mesure absolue de gain ou de perte sociale, indépendamment du ressenti de l'élève.
*   **Limites / Biais :** Les lycées situés aux extrêmes du système (très pauvres ou très riches) subissent des effets plafonds : ils ne peuvent mathématiquement que générer des corridors "vers le haut" ou "vers le bas" respectivement.

---

### 45. Détection des Lycées Paradoxaux (Déviations Résiduelles)
**Formule :**

$$
\Huge \quad \text{Performance attendue} \quad \hat{R}(S_i) \quad \text{. Résidu} \quad \epsilon_i = R_i - \hat{R}(S_i) \quad \text{. Score paradoxal standardisé} \quad P_i = Z_i^R - Z_i^S \quad \text{. Tension systémique} \quad \tau_{i,t} = R_{i,t} - E[R \mid S_{i,t}] \quad \text{.} \quad
$$
*   **Quoi :** Modèle isolant les lycées qui brisent le déterminisme : ceux qui sur-performent avec un public défavorisé (paradoxe ascendant) et ceux qui sous-performent avec un public d'élite (paradoxe inversé).
*   **Légende :** $Dev_i$ : degré d'anomalie du lycée $i$, $S_i$ : statut social réel, $f(A_i, F_i)$ : statut théorique calculé d'après sa sélection et son attractivité.
*   **Pourquoi :** Montrer que le système possède des failles et des "ascenseurs locaux" invisibles dans les moyennes globales, mais aussi des rentes de situation inefficaces.
*   **Inputs :** Scores de réussite ($R_i$), indices de position sociale ($S_i$).
*   **Outputs :** Vecteur de scores $P_i$ et cartographie des anomalies (Heatmap de sur-performance).
*   **Dépendance Amont :** Régression linéaire/polynomiale de $R$ sur $S$.
*   **Dépendance Aval :** Injection dans la métrique de courbure sociale (Modèle 48).
*   **Complexité Algorithmique :** Régression locale (LOESS/GAM), très rapide.
*   **Contraintes & Hypothèses :** La sous-performance d'un lycée d'élite est mesurable mathématiquement, même si elle est masquée par un taux brut de 100% au bac.
*   **Limites / Biais :** L'effet taille de la cohorte peut créer de faux paradoxes (très forte variance sur des petits lycées).

---

### 46. Champ Dynamique Unifié (Tensions et Déviations)
**Formule :**

$$
\Huge \quad \text{Champ latent} \quad \Phi_{i,t} = \alpha S_{i,t} + \beta R_{i,t} + \gamma H_{i,t} \quad \text{. Déviation connectée} \quad D_{i,t} = \tau_{i,t} \cdot H_{i,t} \quad \text{. Évolution} \quad \Phi_{i,t+1} = \Phi_{i,t} + f(D_{i,t}) + \rho \sum W_{ij} \Phi_{j,t} \quad \text{.} \quad
$$
*   **Quoi :** Fusion des trois forces du système (Structure Sociale, Performance, Réseau) en un seul champ de forces continu.
*   **Légende :** $\Phi_i$ : potentiel énergétique total du lycée $i$ dans le système, intégrant sa tension réseau $T_i$ et son anomalie institutionnelle $Dev_i$.
*   **Pourquoi :** Démontrer que la "déviation" d'un lycée n'a d'impact systémique que si elle est propagée par le réseau ($\tau \cdot H$). Un lycée paradoxal isolé ne change rien au système.
*   **Inputs :** Statut ($S$), Performance ($R$), Centralité de réseau ($H$), Matrice spatiale ($W$).
*   **Outputs :** Cartographie du champ latent $\Phi$ et détection des zones de tension structurelle.
*   **Dépendance Amont :** Calcul des flux $T_{ij}$, scores paradoxaux $P_i$.
*   **Dépendance Aval :** Théorie des champs appliqués à la géométrie sociale.
*   **Complexité Algorithmique :** Résolution d'équations de champ, O(N²) par pas de temps.
*   **Contraintes & Hypothèses :** L'énergie du système est fermée : une sur-performance locale aspire nécessairement des ressources ailleurs.
*   **Limites / Biais :** L'étalonnage des poids $\alpha, \beta, \gamma$ exige des techniques de machine learning (ex: ACP pondérée) pour éviter l'arbitraire.

---

### 47. L'Atlas Analytique Multi-Couches
**Formule :**

$$
\Huge \quad \text{Superposition des 9 tensors d'état :} \quad S_i \quad \text{(Fondation),} \quad R_i \quad \text{(Éducatif),} \quad T_{ij} \quad \text{(Flux),} \quad \tau_i \quad \text{(Déviations),} \quad \Gamma_{ij} \quad \text{(Asymétrie),} \quad d_U(i,j) \quad \text{(Ultramétrie),} \quad t \quad \text{(Dynamique),} \quad \Phi_i \quad \text{(Tensions),} \quad \Pi_t \quad \text{(Transitions).} \quad
$$
*   **Quoi :** Le "SIG" (Système d'Information Géographique) théorique du projet, superposant toutes les métriques en un seul cube de données conceptuel.
*   **Pourquoi :** Montrer visuellement qu'un lycée n'est pas un point sur une carte, mais un vecteur traversé par 9 dimensions causales interagissant entre elles.
*   **Inputs :** L'intégralité des variables calculées par les 46 modèles précédents.
*   **Outputs :** Dashboard matriciel et structure de la base de données finale (DataFrame multi-index).
*   **Dépendance Amont :** Exécution complète de toute l'arborescence algorithmique.
*   **Dépendance Aval :** Géométrie Riemannienne Sociale (Modèle 48).
*   **Complexité Algorithmique :** Stockage tensoriel lourd.
*   **Contraintes & Hypothèses :** Toutes les couches doivent être normalisées et projetées sur le même repère spatial (CRS spatial).
*   **Limites / Biais :** Invisualisable en 2D classique, nécessite des réductions de dimensionnalité (t-SNE/UMAP) pour l'exploration.

---

### 48. Géométrie Riemannienne Sociale (Espace non-Euclidien)
**Formule :**

$$
\Huge \quad \text{Vecteur} \quad x_i = (S_i, R_i, H_i) \quad \text{. Métrique tensorielle} \quad d_{ij}^2 = (x_i - x_j)^T G_t (x_i - x_j) \quad \text{. Tenseur métrique} \quad G_t = f(\text{Seg}_t, \text{Flux}_t) \quad \text{. Courbure} \quad K_t = \nabla G_t \quad \text{. Géodésique} \quad \gamma_i = \text{argmin} \int d_{ij}(t) \quad \text{.} \quad
$$
*   **Quoi :** Le stade ultime de la conceptualisation "Monde B" : modéliser le système scolaire exactement comme la Relativité Générale d'Einstein. La masse (les inégalités) déforme l'espace (la carte scolaire), créant une courbure (la ségrégation) qui dicte les orbites (les trajectoires de mobilité).
*   **Pourquoi :** Prouver mathématiquement que la "distance" entre un lycée REP de banlieue et Henri IV à Paris n'est pas de 5 kilomètres (espace euclidien plat), mais s'apparente à une distance intersidérale due à la courbure infinie de l'espace social à cet endroit.
*   **Inputs :** Le Tenseur d'état $G_t$.
*   **Outputs :** Cartographie de la courbure spatiale $K_t$ (détection des "trous noirs scolaires" et des "déchirures d'espace").
*   **Dépendance Amont :** Tenseur multi-couches de l'Atlas.
*   **Dépendance Aval :** Preuve absolue de l'absence de "libre choix" dans un espace contraint.
*   **Complexité Algorithmique :** Géométrie différentielle discrète complexe.
*   **Contraintes & Hypothèses :** Les acteurs du système ne se déplacent pas en ligne droite, ils suivent passivement les géodésiques dictées par la métrique sociale.
*   **Limites / Biais :** Requiert un très haut niveau d'abstraction. L'implémentation nécessitera des approximations via Manifold Learning (Isomap, t-SNE) pour la visualisation.
