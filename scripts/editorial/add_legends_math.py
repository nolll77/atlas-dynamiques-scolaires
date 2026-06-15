import os

legends = {
    "### Normalisation (Z-Score) et Indice d'Entre-Soi": r"*   **Légende :** $z$ : score normalisé, $x$ : valeur brute, $\mu$ : moyenne globale, $\sigma$ : écart-type. $E^*$ : Indice d'entre-soi, $z_{IPS}$ : IPS normalisé du lycée, $z_{\sigma}$ : écart-type interne normalisé du lycée.",
    "### Distance de Mahalanobis": r"*   **Légende :** $D_M(x)$ : Distance de Mahalanobis, $x$ : vecteur de caractéristiques de l'établissement, $\mu$ : barycentre (moyenne), $\Sigma^{-1}$ : inverse de la matrice de covariance.",
    "### Indice de Dissimilarité de Duncan ($D$)": r"*   **Légende :** $D$ : Indice de dissimilarité, $priv\acute{e}_i$ : effectif privé de la sous-zone $i$, $Total\_Priv\acute{e}$ : total global du privé.",
    "### Indice de Fragmentation par Établissement ($F_i$)": r"*   **Légende :** $F_i$ : Indice composite, $B_i$ : Betweenness centrality, $D_i$ : score de Duncan local, $\Delta Var_i$ : contribution à la variance globale, $R_i$ : saut de rupture (Mojena), $\alpha, \beta, \gamma, \delta$ : pondérations.",
    "### Distance Ultramétrique (Hiérarchie)": r"*   **Légende :** $d_U(i,j)$ : distance ultramétrique (hauteur de fusion dans l'arbre) entre les lycées $i$ et $j$. $k$ : un troisième lycée quelconque.",
    "### Distance Sociale et Similarité (Poids du Graphe)": r"*   **Légende :** $W_{ij}$ : poids d'affinité ou probabilité de lien entre $i$ et $j$, $D_{ij}$ : distance (Euclidienne ou Mahalanobis) entre $i$ et $j$, $\sigma$ : hyperparamètre de lissage (ouverture du graphe).",
    "### Modularité (Algorithme de Louvain)": r"*   **Légende :** $Q$ : score de modularité, $m$ : masse totale des arêtes du graphe, $A_{ij}$ : poids de l'arête entre $i$ et $j$, $k_i, k_j$ : somme des poids (degrés) des nœuds $i$ et $j$, $\delta(c_i, c_j)$ : vaut 1 si $i$ et $j$ sont dans le même cluster, 0 sinon.",
    "### Centralité d'Intermédiarité (Betweenness)": r"*   **Légende :** $B(i)$ : centralité du lycée $i$, $\sigma_{st}$ : nombre total de chemins les plus courts entre $s$ et $t$, $\sigma_{st}(i)$ : nombre de ces chemins qui passent par $i$.",
    "### Tension Hiérarchie vs Réseau (Indice Hybride)": r"*   **Légende :** $T$ : score de tension globale, $ARI$ : Adjusted Rand Index comparant la similitude entre la classification hiérarchique (CAH) et celle du réseau (Louvain).",
    "### Indice de Theil (Décomposition de l'Entropie)": r"*   **Légende :** $T$ : indice de Theil total, $x_i$ : proportion de la métrique pour l'unité $i$, $\mu$ : moyenne globale.",
    "### Pression Ségrégative Locale (PSL)": r"*   **Légende :** $PSL_i$ : pression sur le lycée $i$, $H_i$ : hétérogénéité spatiale, $D_i$ : distance sociale au centre, $B_i$ : Betweenness, $C_i$ : diversité, $\alpha, \beta, \gamma, \delta$ : pondérations.",
    "### Spatial Autoregressive Model (SAR)": r"*   **Légende :** $y$ : variable dépendante (ex: IPS), $\rho$ : coefficient de contagion spatiale, $W$ : matrice de voisinage (poids géographiques), $X$ : matrice des variables explicatives, $\beta$ : vecteurs des effets directs, $\epsilon$ : erreur résiduelle.",
    "### Effets Marginaux Spatiaux (Propagation)": r"*   **Légende :** $ME$ : matrice des effets marginaux, $I$ : matrice identité, $\rho$ : coefficient spatial, $W$ : matrice de voisinage, $\beta$ : coefficients initiaux.",
    "### Critère de Mojena (Sauts de Rupture CAH)": r"*   **Légende :** $h_k$ : hauteur du $k$-ième nœud dans le dendrogramme, $\bar{h}$ : hauteur moyenne de tous les nœuds, $\sigma_h$ : écart-type des hauteurs, $\beta$ : constante de sévérité.",
    "### Résidus Spatiaux (Anomalies Structurelles)": r"*   **Légende :** $residu_i$ : erreur géolocalisée, $y_i$ : valeur réelle observée pour $i$, $\hat{y}_i$ : valeur prédite par le modèle SAR.",
    "### Inférence Causale par Graphes (DAG & DoWhy)": r"*   **Légende :** $P$ : cause étudiée, $Y$ : effet mesuré, $Z, N$ : variables de confusion bloquant le chemin 'Backdoor', $S$ : Collider (variable à ne pas bloquer).",
    "### Entropie de Transition (CAH Dynamique)": r"*   **Légende :** $H_i$ : entropie de trajectoire pour le lycée $i$, $p_{ik}$ : probabilité historique que le lycée $i$ transite vers le cluster $k$.",
    "### CAH Contrainte (Distance Pénalisée)": r"*   **Légende :** $D'$ : distance composite finale, $D_{social}$ : distance sociologique pure, $D_{geo}$ : distance kilométrique, $\lambda$ : force de la contrainte géographique.",
    "### Densité de Continuité Sociale (KDE & Chevauchement)": r"*   **Légende :** $O_{ij}$ : aire de chevauchement entre clusters $i$ et $j$, $f_i(x)$ : fonction de densité (KDE) du cluster $i$ en un point $x$ de la carte.",
    "### Silhouette Score (Cohérence Interne)": r"*   **Légende :** $s(i)$ : score de silhouette du point $i$, $a(i)$ : distance moyenne de $i$ aux autres points de son propre cluster, $b(i)$ : distance moyenne de $i$ aux points du cluster voisin le plus proche.",
    "### Gap Statistic (Validation Réalité vs Bruit)": r"*   **Légende :** $Gap(k)$ : statistique de Gap pour $k$ clusters, $E[\log(W_k^*)]$ : log-dispersion attendue sous simulation aléatoire uniforme, $\log(W_k)$ : log-dispersion réelle observée.",
    "### Tension Ultramétrique / Réseau Locale": r"*   **Légende :** $T_i$ : tension pour le lycée $i$, $d_U(i,j)$ : distance dans l'arbre hiérarchique, $d_G(i,j)$ : distance dans le graphe communautaire, $w_{ij}$ : poids du lien.",
    "### Matrice de Transition (Modèle de Markov)": r"*   **Légende :** $P_{ij}$ : probabilité de passer de l'état $i$ à l'état $j$, $C_t$ : état (cluster) au temps $t$.",
    "### Distribution Stationnaire (Stabilité)": r"*   **Légende :** $\pi$ : vecteur de la distribution asymptotique finale (état stable), $P$ : matrice de transition, $\lambda=1$ : valeur propre principale sous-entendue.",
    "### Centralité de Transition (Flux Nets)": r"*   **Légende :** $F_i$ : masse de flux impliquant l'état $i$, $P_{ij}$ : flux sortant de $i$ vers $j$, $P_{ji}$ : flux entrant dans $i$ depuis $j$.",
    "### Entropie de Transition (Vitesse de Mobilité)": r"*   **Légende :** $H_i$ : score d'incertitude de fuite depuis l'état $i$, $P_{ij}$ : probabilité conditionnelle d'aller de $i$ vers $j$.",
    "### Flux entre Couches ($F_{ab}$)": r"*   **Légende :** $F_{ab}$ : probabilité empirique d'un saut de la couche $a$ vers la couche $b$, $layer_t$ : strate institutionnelle au temps $t$.",
    "### Indice de Fragmentation Inter-Couches (IFC / Perméabilité)": r"*   **Légende :** $IFC$ : somme de la diagonale (immobilité), $F_{aa}$ : maintien dans la même couche, $IFC^*$ : indice normalisé, $K$ : nombre total de couches.",
    "### IFC Pondéré (Distance Sociale Inter-strata)": r"*   **Légende :** $IFC_w$ : perméabilité pondérée par la sévérité du saut, $F_{ab}$ : flux observé, $d_{ab}$ : distance sémantique ou sociale entre couche $a$ et couche $b$.",
    "### Asymétrie des Flux (Déséquilibre d'Aspiration)": r"*   **Légende :** $A$ : asymétrie totale du système, $F_{ab}$ : flux aller, $F_{ba}$ : flux retour inverse.",
    "### Entropie Globale des Flux (Chaos du Réseau)": r"*   **Légende :** $H_{flux}$ : entropie globale du réseau multiplex, $F_{ab}$ : probabilité globale de la transition $a \to b$.",
    "### Modularité Généralisée (Louvain Multi-couches)": r"*   **Légende :** $Q_{multi}$ : modularité multi-couches, $\alpha$ : indice de la couche, $A_{ij}^\alpha$ : poids arête dans couche $\alpha$, $\gamma^\alpha$ : résolution, $P_{ij}^\alpha$ : modèle aléatoire nul, $\delta(c_i, c_j)$ : identité de cluster.",
    "### Cohésion des Super-Communautés (Résistance Interne)": r"*   **Légende :** $C_k$ : cohésion du cluster $k$, $E_{in}(k)$ : somme des liens internes à $k$, $E_{out}(k)$ : somme des liens fuyant $k$, $\lambda$ : pénalité de taille.",
    "### Score de Frontière Sociale ($FS_{ij}$)": r"*   **Légende :** $FS_{ij}$ : score de frontière entre points géographiques $i$ et $j$, $D_{ij}$ : distance sociale pure, $\Delta C_{ij}$ : rupture de cluster (0 ou 1), $\beta$ : poids.",
    "### Rigidité des Frontières (Le Syndrome de la Forteresse)": r"*   **Légende :** $R_i$ : rigidité autour du lycée $i$, $FS_{ij}$ : frontières avec les voisins $j$, $w_{ij}$ : poids géographique d'adjacence.",
    "### Theil Spatial par Commune ($T_c$)": r"*   **Légende :** $T_c$ : indice de Theil pour la commune $c$, $T_{c, inter}$ : ségrégation entre les lycées de la commune, $T_{c, intra}$ : ségrégation à l'intérieur des classes des lycées de la commune.",
    "### Polarisation Locale (Le Choc des Extrêmes)": r"*   **Légende :** $P_c$ : polarisation, $Q1$ : effectifs du quart le plus pauvre, $Q4$ : effectifs du quart le plus riche, $\bar{M}_c$ : classe moyenne.",
    "### Décomposition Dynamique Temporelle (L'Évolution du Fracture)": r"*   **Légende :** $\Delta S$ : variation temporelle de la ségrégation, $\Delta Structure$ : part due aux changements institutionnels, $\Delta Demographie$ : part due aux changements de la population.",
    "### Score Composite Global de Ségrégation ($S$)": r"*   **Légende :** $S$ : score macroscopique global, $\omega_k$ : poids de chaque sous-indice, $I_k$ : les différents indices (Theil, Modularité, IFC, etc.)."
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
        
        # Inject legend immediately after the "Quoi :" line, or "Pourquoi :" line
        if line.strip().startswith("*   **Quoi :**") and current_section in legends:
            new_lines.append(legends[current_section] + "\n")
            # Remove from dict so we don't inject twice if there's an issue
            del legends[current_section]
            
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

process_file('docs/SOCLE_MATHEMATIQUE.md')
