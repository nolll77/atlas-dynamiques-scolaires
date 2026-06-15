import os

legends = {
    "### 1. Décomposition des Effets Directs et Indirects (Spatial Lag)": r"*   **Légende :** $Y_i$ : variable dépendante (ex: IPS), $\alpha$ : effet direct intrinsèque, $X_i$ : ressources propres, $\beta$ : force de contagion, $W_{ij}$ : matrice spatiale, $X_j$ : ressources des voisins, $\varepsilon_i$ : résidu.",
    "### 2. Score de Propagation de Ségrégation (SPS) / Hotspots": r"*   **Légende :** $SPS_i$ : score de propagation du lycée $i$, $S_i$ : ségrégation propre de $i$, $W_{ij}$ : matrice spatiale, $S_j$ : ségrégation des voisins $j$.",
    "### 3. Zones de Bascule (Effet local non-linéaire)": r"*   **Légende :** $Bascule_i$ : indicateur booléen (1 si rupture), $\beta_i$ : effet local de la variable sur $i$, $\bar{\beta}_{voisins(i)}$ : effet moyen sur les voisins géographiques.",
    "### 4. Modèle Latent Spatial (Analyse des Résidus)": r"*   **Légende :** $r_i$ : résidu spatial pour $i$, $Y_i$ : vraie valeur, $\hat{Y}_i$ : prédiction du modèle global, $z_{c(i)}$ : effet du cluster latent $c$, $u_i$ : bruit purement aléatoire.",
    "### 5. Modèle d'Équations Structurelles Spatial (SEM)": r"*   **Légende :** $Y$ : vecteur cible, $X\beta$ : effets des variables explicatives, $\rho$ : coefficient de corrélation spatiale, $W$ : matrice des poids spatiaux, $\varepsilon$ : terme d'erreur structurel.",
    "### 6. SEM Spatial Multi-Niveaux (Élève → Lycée → Zone)": r"*   **Légende :** $Y_{ijk}$ : score de l'élève $i$ au lycée $j$ en zone $k$, $X_{ijk}\beta$ : caractéristiques individuelles, $u_{jk}$ : effet aléatoire du lycée, $v_k$ : effet de la zone territoriale, $\rho W v_k$ : influence des zones voisines.",
    "### 7. Graphe Acyclique Dirigé Inter-Temporel (DAG 2010→2026)": r"*   **Légende :** $Y_t$ : état au temps $t$, $Y_{t-1}$ : état passé (inertie), $X_t$ : variables contemporaines, $WY_{t-1}$ : état passé des voisins (contagion retardée).",
    "### 8. Trajectoires de Clusters (Sankey des flux structurels)": r"*   **Légende :** $P_{ab}$ : probabilité de transition, $C(t)=a$ : appartenance au monde $a$ en année $t$, $C(t+1)=b$ : atterrissage dans le monde $b$ l'année suivante.",
    "### 9. Détection de Ruptures Structurelles (Changepoints Temporels)": r"*   **Légende :** $d_t$ : magnitude de la rupture, $ARI$ : Adjusted Rand Index comparant les partitions de deux années successives, $D_t$ : distance entre matrices d'embeddings $Z_t$.",
    "### 10. Ultramétrie Temporelle (Géométrie Hiérarchique Évolutive)": r"*   **Légende :** $\Delta_t$ : déformation de l'arbre, $d(D_t, D_{t-1})$ : distance entre dendrogrammes successifs, $U$ : indice global de stabilité hiérarchique.",
    "### 11. Simulation de Mobilité Sociale (La dynamique du lycée)": r"*   **Légende :** $S_i(t)$ : prestige latent, $\alpha X_i$ : atouts internes, $\beta W S$ : gravité du voisinage, $\gamma C_i$ : contraintes territoriales, $\varepsilon_i$ : chocs externes aléatoires.",
    "### 12. Frontières Scolaires \"Dures\" (Cut Edges & Betweenness)": r"*   **Légende :** $F_{ij}$ : score de frontière, $BC_{ij}$ : centralité d'intermédiarité de l'arête, $w_{ij}$ : similarité sociale entre $i$ et $j$.",
    "### 13. Corridors Sociaux (Mobilité entre Clusters)": r"*   **Légende :** $R_{ab}$ : intensité du corridor, $T_{ab}$ : flux réels observés, $E_{ab}$ : flux attendus par hasard absolu, $C_{ab}$ : ratio ajusté par les populations marginales $p_a, p_b$.",
    "### 14. Fragmentation Territoriale (Moran sur Clusters)": r"*   **Légende :** $I_k$ : Indice de Moran catégoriel, $x_k$ : indicateur d'appartenance au cluster $k$, $W$ : matrice géographique, $F_{territorial}$ : fragmentation globale.",
    "### 15. Frontières Sociales Floues (Gradient KDE & Entropie)": r"*   **Légende :** $H(x)$ : entropie au point géographique $x$, $P_k(x)$ : probabilité lissée par noyau d'appartenir au cluster $k$ à cet endroit.",
    "### 16. Indice d'Accord des 3 Critères (Cohérence Structurelle)": r"*   **Légende :** $C_i$ : cohérence du lycée, $\tilde{S}_i$ : score social standardisé, $\tilde{A}_i$ : score académique, $\tilde{F}_i$ : score d'attractivité (flux).",
    "### 17. K Optimal Consensuel (Robustesse du Clustering)": r"*   **Légende :** $C(k)$ : score de consensus pour $k$ classes, $S(k)$ : Silhouette, $G(k)$ : Gap Statistic, $B(k)$ : inertie de coude, $S_{stab}$ : stabilité bootstrap.",
    "### 18. Analyse des Divergences Algorithmiques": r"*   **Légende :** $A_i$ : incertitude d'assignation du lycée $i$, $C_i^{(m)}$ : classe prédite par l'algorithme $m$, $F$ : taux global de désaccord systémique.",
    "### 19. Validation Ultramétrique et Ponts Structurels": r"*   **Légende :** $B_{ij}$ : score de pont, $d_{ij}$ : distance réelle dans le réseau, $d_{ij}^U$ : distance théorique dans l'arbre hiérarchique, $V$ : taux de violation des inégalités d'arbre.",
    "### 20. Modèle Unifié et \"Super-Goulots Systémiques\" (HMM + GNN + DAG)": r"*   **Légende :** $SG_{ij}$ : dangerosité du goulot, $B_{ij}$ : scores de pont selon les modèles Temporels (HMM), Réseau (GNN), Hiérarchiques (U) et Causaux (C).",
    "### 21. Perméabilité Structurelle Optimale (\"Le point Goldilocks\")": r"*   **Légende :** $\Pi$ : perméabilité globale, $P_{raw}$ : intensité brute des flux transgressant la hiérarchie, $C$ : coût du chaos ou désordre perçu.",
    "### 22. Modèle Causal de l'Indice de Fragmentation (IFC)": r"*   **Légende :** $IFC_{ij}$ : fragmentation locale, $\beta_k$ : effets causaux directs, $X_k$ : variables de sélectivité/transport, $u_j$ : effet aléatoire de l'académie, $\epsilon_{ij}$ : résidu individuel.",
    "### 23. Détection des Blocs Scolaires Multi-Couches": r"*   **Légende :** $B^*$ : partition optimale, $W$ : similarité d'IPS, $T$ : matrice des flux réels, $D^U$ : distance hiérarchique, $\lambda$ : poids accordé à l'ordre hiérarchique.",
    "### 24. Les Super-Ponts Inter-Blocs": r"*   **Légende :** $SP_{ij}$ : criticité du super-pont, $P_{ij}$ : flux réels d'élèves, $C_{ij}^{(bet)}$ : centralité Betweenness, $U_{ij}$ : saut ultramétrique (audace sociale du pont).",
    "### 25. Hyper-ségrégation Masquée (Illusion de Mixité)": r"*   **Légende :** $F_c$ : fausse mixité, $\text{Var}_{global}$ : hétérogénéité apparente de la ville, $\text{Var}_{interne}$ : (absence de) mixité au sein des lycées, $HS_c$ : hyper-ségrégation totale.",
    "### 26. Dérive Temporelle de la Mobilité (Matrice T)": r"*   **Légende :** $\Delta T_t$ : changement de tuyauterie d'une année à l'autre, $X_k$ : variables macro, $T_{t-1}$ : inertie des flux, $Z_t$ : chocs exogènes (ex: nouvelle ligne de métro).",
    "### 27. Indice d'Autonomie Scolaire (IAS)": r"*   **Légende :** $IAS_i$ : capacité d'affranchissement, $A_i$ : attractivité lointaine, $S_i$ : constance de l'IPS, $F_i$ : sélectivité, $C_i$ : poids du recrutement sectorisé imposé.",
    "### 28. Décomposition des Effets Indirects (Quartier vs Réseau)": r"*   **Légende :** $Y_i$ : position du lycée, $E_i^{quartier}$ : composante purement kilométrique, $E_i^{\text{r\acute{e}seau}}$ : composante via les transports/filières, $\epsilon_i$ : non-expliqué.",
    "### 29. Causalité des Hotspots (Asymétrie Causale : Cause vs Effet)": r"*   **Légende :** $H_{i,t}$ : tension du hotspot $i$, $C_i^{out}$ : capacité de $i$ à contaminer le reste du réseau, $C_i^{in}$ : vulnérabilité de $i$ face aux crises des autres.",
    "### 30. Modèle Causal Spatial Non-Linéaire (GAM + Spatial RF)": r"*   **Légende :** $s_k$ : fonction de lissage (spline) permettant les effets non-linéaires, $\rho W Y$ : contagion spatiale, $u(s_i)$ : processus gaussien captant le bruit géolocalisé.",
    "### 31. Tipping Points et Instabilité Structurelle": r"*   **Légende :** $\nabla Y_i$ : gradient (pente) de l'effet d'une variable, $\Delta sign$ : point de basculement, $\rho \lambda_{max}(W)$ : condition spectrale de résonance du réseau.",
    "### 32. Classification des Mondes Scolaires Cachés (Latent Class)": r"*   **Légende :** $P(Y_i|X_i)$ : probabilité du profil du lycée, $Z_i=k$ : assignation au \"Monde caché\" $k$, $\beta_{Z_i}$ : règles sociologiques spécifiques au monde $k$.",
    "### 33. Blind Spots et Frontières Non-Modélisées": r"*   **Légende :** $BS_i$ : anomalie du lycée $i$, $R_i$ : résidu du modèle, $B_{ij}$ : intensité de la frontière occulte entre $i$ et $j$.",
    "### 35. Décomposition Totale de Variance (ICC + Spatial ICC)": r"*   **Légende :** $\sigma^2_{zone}$ : fatalité du quartier, $\sigma^2_{school}$ : responsabilité propre du proviseur/lycée, $\sigma^2_{spatial}$ : effet de meute (voisinage).",
    "### 36. Clusters Absorbants (Attracteurs de Réseau)": r"*   **Légende :** $A_k$ : force gravitationnelle du cluster $k$, $In_k$ : flux entrant depuis d'autres mondes, $Out_k$ : flux fuyant vers d'autres mondes, $\rho(T)$ : rayon spectral de stabilité.",
    "### 37. Trajectoires Rares (Outliers Séquentiels)": r"*   **Légende :** $P(\tau_i)$ : probabilité qu'un élève suive cette trajectoire $\tau$, $A(\tau)$ : étrangeté absolue du parcours (souvent lié à l'évitement scolaire).",
    "### 38. Distorsion Spatiale des Flux (Sankey Géographique)": r"*   **Légende :** $\tilde{T}_{ij}$ : flux d'élèves pénalisé par la distance, $\lambda$ : friction kilométrique, $D$ : indice de distorsion montrant si les flux violent la géographie.",
    "### 39. Causalité des Changepoints (Réforme vs Démographie)": r"*   **Légende :** $\tau_k$ : probabilité que la rupture soit due à la réforme $k$, $Z$ : variables inobservées (bruit macro-économique).",
    "### 40. Ruptures Ultramétriques Causales (DAG Temporel)": r"*   **Légende :** $\Delta_{ij}(t)$ : changement de distance hiérarchique entre $i$ et $j$ au temps $t$, $P_{ij}$ : choc de flux, $X_{ij}$ : dégradation relative d'attractivité.",
    "### 41. Carte Continue des Trajectoires (Ascension vs Déclin)": r"*   **Légende :** $\vec{V}(x,y)$ : vecteur de force au point $x,y$, $\nabla S$ : pente de déclassement social, $\nabla A$ : pente d'attractivité.",
    "### 42. Transition de Phase (Seuil Critique et Effondrement)": r"*   **Légende :** $\lambda_{max}$ : plus grande valeur propre de la matrice jacobienne du réseau, dictant si une crise locale reste locale ou embrase toute la région.",
    "### 43. Analyse des Corridors Asymétriques (Ascenseurs vs Filtres)": r"*   **Légende :** $Asym_{ab}$ : ratio d'inégalité des échanges, $T_{ab}$ : ceux qui montent, $T_{ba}$ : ceux qui descendent (ou inversement).",
    "### 44. Corridors d'Élite vs Déclassement (Gradient Directionnel)": r"*   **Légende :** $Grad_{ab}$ : pente sociologique du transfert, $S_a, S_b$ : richesses respectives des mondes de départ et d'arrivée.",
    "### 45. Détection des Lycées Paradoxaux (Déviations Résiduelles)": r"*   **Légende :** $Dev_i$ : degré d'anomalie du lycée $i$, $S_i$ : statut social réel, $f(A_i, F_i)$ : statut théorique calculé d'après sa sélection et son attractivité.",
    "### 46. Champ Dynamique Unifié (Tensions et Déviations)": r"*   **Légende :** $\Phi_i$ : potentiel énergétique total du lycée $i$ dans le système, intégrant sa tension réseau $T_i$ et son anomalie institutionnelle $Dev_i$."
}

def process_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    current_section = None
    
    for line in lines:
        if line.startswith("### "):
            current_section = line.strip()
            
        new_lines.append(line)
        
        # Inject legend immediately after the "*   **Quoi :**" line
        if line.strip().startswith("*   **Quoi :**") and current_section in legends:
            new_lines.append(legends[current_section] + "\n")
            del legends[current_section]
            
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

process_file('docs/SOCLE_DYNAMIQUE.md')
