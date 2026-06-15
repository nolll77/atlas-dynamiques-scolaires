import re

dict_rewrites = {
    "#008": "- [ ] Calculer la matrice de corrélation statistique entre l'IPS et les revenus médians par IRIS.\n- [ ] Coder la fonction mathématique de l'indice composite (IPS + σ + revenus IRIS) et exporter les scores des lycées.",
    "#009": "- [ ] Calculer l'écart-type de l'IPS pour chaque lycée afin d'estimer la mixité sociale interne.\n- [ ] Générer le tableau récapitulatif du Top 20 des lycées les plus homogènes et les plus hétérogènes.\n- [ ] Exécuter un test de corrélation exploratoire entre l'écart-type et les données immobilières DVF.",
    "#010": "- [ ] Extraire la distribution statistique de l'IPS, de l'écart-type et de la répartition par secteur (public/privé).\n- [ ] Générer le \"scatter plot\" (Figure Signature 2) croisant IPS et écart-type, avec colorisation par statut et courbes de densité KDE.",
    "#011": "- [ ] Calculer la corrélation spatiale entre l'IPS moyen par commune et le prix médian au m² (DVF).\n- [ ] Générer la carte choroplèthe des IPS moyens par commune et le scatter plot correspondant.",
    "#012": "- [ ] Réaliser une ANOVA spatiale pour décomposer la variance selon 3 facteurs (zone géographique, statut public/privé, revenus IRIS).\n- [ ] Extraire les pourcentages de variance expliquée et dresser le tableau comparatif complet des trois couronnes.\n- [ ] Calculer l'indice de dissimilarité de Duncan pour chaque commune.",
    "#013": "- [ ] Coder la formule de l'indice de \"fausse mixité\" (F_c = M_global - M_interne) et générer les scores communaux.\n- [ ] Tester la corrélation statistique entre l'accessibilité aux transports (IDF Mobilités) et le niveau de ségrégation.",
    "#014": "- [ ] Calculer la polarisation de l'IPS (delta public/privé) ventilée par zone géographique.\n- [ ] Tester statistiquement la corrélation entre la densité locale d'établissements privés et le prix immobilier (DVF).",
    "#016": "- [ ] Isoler statistiquement le Cluster 1 (IPS > 158, écart-type < 20).\n- [ ] Calculer le score composite d'entre-soi pour ces établissements et exporter les statistiques descriptives.",
    "#017": "- [ ] Extraire les statistiques descriptives du Cluster 2 sur l'ensemble du vecteur de variables (IPS, écart-type, DVF, IRIS, bac).\n- [ ] Générer la liste brute des lycées constituant ce cluster.",
    "#018": "- [ ] Extraire les statistiques descriptives complètes du Cluster 3 (IPS élevé, mixité forte).\n- [ ] Extraire la valeur ajoutée IVAL pour tester statistiquement la corrélation avec l'hétérogénéité sociale.",
    "#019": "- [ ] Extraire les statistiques descriptives complètes du Cluster 4 (IPS, σ, DVF, IRIS, résultats bac).\n- [ ] Générer la liste brute des établissements appartenant à ce cluster pour validation.",
    "#020": "- [ ] Isoler les établissements internationaux et scientifiques (Cluster 5) et extraire leurs caractéristiques statistiques.\n- [ ] Produire le tableau récapitulatif des variables descriptives (IPS, σ, DVF, IRIS, résultats bac).",
    "#021": "- [ ] Extraire les statistiques descriptives des lycées publics favorisés résidentiels.\n- [ ] Générer la carte spatiale positionnant les 5 clusters sur la région Île-de-France.",
    "#027": "- [ ] Modéliser une ANOVA unidimensionnelle (IPS en fonction du statut public/privé).\n- [ ] Extraire le pourcentage de variance expliquée (R²) et générer le tableau des résidus statistiques.",
    "#042": "- [ ] Implémenter la Classification Ascendante Hiérarchique (CAH) avec la méthode de Ward et normalisation en z-scores.\n- [ ] Comparer statistiquement les résultats de la CAH avec l'algorithme k-means et un modèle GMM.\n- [ ] Exécuter le clustering (V2) sur le vecteur enrichi (IPS, écart-type, revenus IRIS, résultats bac, statut).",
    "#043": "- [ ] Générer le dendrogramme complet de la CAH et calculer les hauteurs de fusion.\n- [ ] Appliquer le critère de Mojena pour détecter mathématiquement les sauts de clusters optimaux.\n- [ ] Calculer la profondeur ultramétrique du graphe.",
    "#044": "- [ ] Extraire les tableaux de description statistique pour les 5 clusters validés.\n- [ ] Générer la carte spatiale positionnant les clusters sur la carte d'Île-de-France.",
    "#045": "- [ ] Calculer le silhouette score et la \"gap statistic\" pour valider la robustesse des clusters.\n- [ ] Exécuter un test de stabilité bootstrap (Adjusted Rand Index) sur 1000 itérations.\n- [ ] Réaliser une ANOVA post-hoc sur l'IPS et l'écart-type pour valider la séparation statistique.",
    "#046": "- [ ] Calculer la distance cophenétique et la corrélation ultramétrique du système.\n- [ ] Extraire les \"ponts ultramétriques\" (liens violant la hiérarchie).\n- [ ] Calculer l'Adjusted Rand Index pour évaluer la cohérence entre l'arbre (CAH) et le réseau (Louvain).",
    "#047": "- [ ] Implémenter la détection de communautés avec l'algorithme de Louvain en maximisant la modularité (Q).\n- [ ] Comparer les communautés Louvain avec les clusters CAH (via les métriques ARI et NMI).\n- [ ] Exécuter un test de sensibilité en modifiant la résolution de Louvain (0.5, 1.0, 1.5, 2.0).",
    "#048": "- [ ] Construire un réseau multiplex (multicouches) intégrant les flux, le statut et la distance géographique (GPS).\n- [ ] Détecter les communautés transversales et extraire la liste des corridors inter-couches.\n- [ ] Calculer l'indice de fragmentation inter-couches (IFC) par couche.",
    "#049": "- [ ] Construire la matrice de distances (Mahalanobis et Euclidienne) et seuiller le réseau.\n- [ ] Modéliser un réseau nul d'Erdős–Rényi de même densité pour tester la significativité statistique de la modularité.\n- [ ] Générer la visualisation du graphe avec l'algorithme Force-Directed (Spring Layout).",
    "#050": "- [ ] Calculer les indices de centralité : Eigenvector centrality, Betweenness, et Degré pondéré.\n- [ ] Générer le Top 10 des lycées selon un score composite de centralité.\n- [ ] Produire la visualisation du graphe avec colorisation des nœuds par centralité.",
    "#051": "- [ ] Coder la formule du score de \"pont\" composite (betweenness + diversité communautaire + distance ultramétrique).\n- [ ] Extraire le Top 10 des lycées franchissant les frontières (ponts structurels).",
    "#052": "- [ ] Générer la matrice de transition (Markov) entre les différents clusters.\n- [ ] Estimer mathématiquement la distribution stationnaire du système (équilibre asymptotique).\n- [ ] Calculer l'entropie des trajectoires et la durée de séjour moyenne dans chaque cluster.",
    "#053": "- [ ] Calculer les flux attendus via un modèle nul d'indépendance et générer les scores de corridor (R_ab = F_ab / E_ab).\n- [ ] Identifier statistiquement les corridors sur-représentés (autoroutes sociales) et extraire l'indice d'asymétrie Γ.",
    "#054": "- [ ] Coder les requêtes d'extraction pour isoler les flux ascendants (ascenseurs) et les flux descendants (filtres).\n- [ ] Calculer l'efficacité moyenne des ascenseurs (ΔS moyen) et générer la distribution spatiale.",
    "#055": "- [ ] Fusionner mathématiquement les différentes couches du réseau multiplex (social, académique, résidentiel).\n- [ ] Calculer le score de centralité inter-couches et tester les corrélations de flux entre les dimensions.",
    "#056": "- [ ] Calculer la distance de Mahalanobis pour l'ensemble du jeu de données et extraire les \"outliers\" (anomalies statistiques).\n- [ ] Croiser les valeurs atypiques de Mahalanobis avec les résultats inattendus de valeur ajoutée (IVAL).",
    "#057": "- [ ] Détecter algorithmiquement les inversions de gradient spatial et extraire les coordonnées des \"zones de bascule\".\n- [ ] Générer la carte thermique localisant ces points critiques.",
    "#058": "- [ ] Modéliser le système via un Spatial Autoregressive Model (SAR) et calculer l'autocorrélation de Moran.\n- [ ] Extraire les résidus du modèle pour identifier les \"blind spots\" spatiaux.\n- [ ] Tester la corrélation des résidus avec les données d'accessibilité aux transports.",
    "#059": "- [ ] Entraîner un modèle GMM (Gaussian Mixture Model) et un Latent Class Mixed Model pour extraire 5 classes latentes.\n- [ ] Calculer l'entropie locale de chaque lycée pour quantifier l'incertitude d'appartenance et cartographier les zones hybrides.",
    "#060": "- [ ] Estimer les probabilités locales d'appartenance aux clusters via KDE (Kernel Density Estimation).\n- [ ] Calculer l'indice d'entropie locale H(x) et générer l'indice global de flou des frontières (F).",
    "#061": "- [ ] Calculer le score de tension hiérarchie/réseau (|d_ij - d^U_ij| × w_ij) pour repérer les anomalies topologiques.\n- [ ] Générer l'indice global DA (désalignement) et cartographier les points de bascule ultramétriques.",
    "#062": "- [ ] Coder le calcul de la Pression Ségrégative Locale (PSL) intégrée aux variables DVF et IRIS.\n- [ ] Générer la carte spatiale de la PSL et tester sa corrélation avec l'accessibilité transport.",
    "#063": "- [ ] Coder la fonction de décomposition de l'Indice de Fragmentation Inter-couches (IFC).\n- [ ] Exporter les matrices d'asymétrie des flux et calculer l'indice de mobilité (M = 1 - IFC).",
    "#064": "- [ ] Coder la boucle de calcul estimant l'indice de perméabilité (Π = P_raw / C) pour chaque lycée.\n- [ ] Générer les graphiques de distribution permettant d'isoler statistiquement les \"passerelles\" (ultra-ouverts) et les \"verrous\" (ultra-fermés).",
    "#065": "- [ ] Coder le score d'absorption des clusters (Flux_IN / Flux_OUT).\n- [ ] Valider la condition spectrale (ρ(T_C) > 1) pour identifier les attracteurs dynamiques (puits scolaires).",
    "#066": "- [ ] Entraîner le modèle SAR en incluant les covariables (DVF, revenus IRIS, accessibilité).\n- [ ] Extraire et décomposer les effets spatiaux directs et indirects pour évaluation.",
    "#067": "- [ ] Entraîner le modèle SEM spatial en incluant les variables enrichies (DVF, accessibilité transport).\n- [ ] Extraire et comparer les métriques d'évaluation du modèle (R² marginal vs R² conditionnel).",
    "#068": "- [ ] Entraîner un modèle additif généralisé (GAM) non-linéaire avec splines sur les variables enrichies.\n- [ ] Extraire les points d'inflexion (tipping points analytiques) et générer les graphiques d'effets marginaux.",
    "#069": "- [ ] Calculer la décomposition mathématique de la variance pour séparer l'effet \"quartier\" de l'effet \"réseau\".\n- [ ] Tester statistiquement si l'intégration de la variable \"accessibilité transport\" modifie cet équilibre.",
    "#079": "- [ ] Coder le score longitudinal de \"trajectoire temporelle\" et classer les établissements (ascendants, déclinants, instables).\n- [ ] Générer le script `figures/fig4_trajectories_changepoints.py` et tester la corrélation temporelle avec l'évolution des prix DVF.",
    "#080": "- [ ] Exécuter la CAH dynamique sur chaque année et générer la matrice de transition inter-temporelle.\n- [ ] Calculer la stabilité (Adjusted Rand Index) des clusters d'une année sur l'autre.",
    "#081": "- [ ] Générer la pile de dendrogrammes annuels superposés.\n- [ ] Calculer la distance ultramétrique inter-temporelle pour évaluer la résilience hiérarchique du système.",
    "#082": "- [ ] Entraîner un Hidden Markov Model (HMM) pour détecter les régimes cachés dans les séries temporelles (IPS, résultats, mixité).\n- [ ] Extraire les matrices de transition estimées et la durée moyenne par état caché.",
    "#083": "- [ ] Coupler le modèle HMM avec la structure topologique (Graph Neural Network temporel ou modèle couplé).\n- [ ] Extraire les paramètres de diffusion montrant comment les régimes se propagent géographiquement.",
    "#084": "- [ ] Calculer la série temporelle de l'indice de Theil (T) et sa vitesse de fragmentation (dT/dt).\n- [ ] Extraire la décomposition dynamique (ΔT_within + ΔT_between) et générer les graphiques d'évolution par couronne.",
    "#085": "- [ ] Générer la série chronologique des matrices de transition et produire l'animation dynamique de Sankey.\n- [ ] Extraire les métriques identifiant mathématiquement l'apparition de nouveaux ascenseurs sociaux.",
    "#086": "- [ ] Exécuter l'algorithme de détection de ruptures (PELT) en ajustant les paramètres de pénalité (AIC/BIC).\n- [ ] Isoler les dates critiques (changepoints) et tester la coïncidence avec les ruptures des séries immobilières DVF.",
    "#087": "- [ ] Configurer un modèle exploratoire (Diff-in-Diff ou Regression Discontinuity) sur les changepoints.\n- [ ] Exporter les intervalles de confiance sur les effets temporels estimés.",
    "#088": "- [ ] Calculer la plus grande valeur propre du réseau (ρλ_max) et générer sa série temporelle.\n- [ ] Extraire les fenêtres temporelles critiques où le système s'approche de l'instabilité structurelle (valeur >= 1).",
    "#089": "- [ ] Coder la détection des \"Early Warning Signals\" (variance locale, autocorrélation critique) sur les lycées en frontière.\n- [ ] Modéliser un algorithme prédictif détectant la fragilisation ségrégative d'un établissement.",
    "#090": "- [ ] Construire formellement le Directed Acyclic Graph (DAG) inter-temporel pour inclure les délais et l'inertie.\n- [ ] Simuler mathématiquement une intervention (modification de flux) et en extraire les conséquences en cascade.",
    "#092": "- [ ] Coder la métrique tensorielle représentant l'espace scolaire comme une variété riemannienne (G_t).\n- [ ] Extraire les coordonnées courbées de chaque lycée et générer la visualisation topologique abstraite.",
    "#093": "- [ ] Calculer mathématiquement le gradient dans l'espace riemannien (champ de tensions centrifuge/centripète).\n- [ ] Générer la carte vectorielle montrant les lycées soumis aux pressions d'attraction et de répulsion.",
    "#094": "- [ ] Assembler la fonction de perte composite (Loss = L_HMM + λ₁L_GNN + λ₂L_ultra + λ₃L_flux).\n- [ ] Entraîner le réseau neuronal unifié et extraire les hyperparamètres finaux vers un fichier de configuration.",
    "#096": "- [ ] Créer une fonction de filtrage détectant les établissements ayant un fort score de sur-performance relative.\n- [ ] Générer l'export brut (CSV/JSON) de ces anomalies statistiques avec croisement IVAL.",
    "#097": "- [ ] Coder l'extraction des \"paradoxes inversés\" (IPS ultra-élevé mais sous-rendement en VA).\n- [ ] Tester statistiquement la corrélation de ce sous-rendement avec les dynamiques immobilières locales (DVF).",
    "#098": "- [ ] Calculer l'entropie des trajectoires individuelles (-log P(τ_i)) et isoler les trajectoires outliers de mobilité.\n- [ ] Exporter la liste des établissements ayant des transitions contre-hiérarchiques.",
    "#099": "- [ ] Calculer le score d'hyper-ségrégation masquée (HS_c) combinant une forte moyenne communale et un fort indice de ségrégation interne.\n- [ ] Générer la carte spatiale identifiant les communes \"faussement mixtes\".",
    "#100": "- [ ] Coder la consolidation des erreurs (résidus) multi-modèles pondérées spatialement.\n- [ ] Extraire la liste géographique des \"blind spots\" (zones systématiquement mal prédites).",
    "#102": "- [ ] Initialiser la boucle de simulation de re-sectorisation (redistribution artificielle des IPS locaux).\n- [ ] Extraire la nouvelle configuration du réseau et valider la condition de stabilité de la phase de transition simulée.",
    "#103": "- [ ] Coder le modèle contrefactuel \"suppression des noeuds hyper-sélectifs\" (fermeture simulée du Top 20 fermé).\n- [ ] Relancer l'algorithme de routage des flux et exporter les nouvelles matrices d'accessibilité sociale.",
    "#104": "- [ ] Injecter un bonus attractif simulé sur les lycées paradoxaux positifs.\n- [ ] Extraire l'impact de ce choc sur l'ouverture de nouveaux corridors sociaux dans le modèle probabiliste.",
    "#105": "- [ ] Calculer les seuils critiques (tipping points) de mixité provoquant la bascule des corridors.\n- [ ] Générer un rapport d'optimisation probabiliste comparant les stratégies de régulation de flux.",
    "#106": "- [ ] Compiler l'architecture des couches JSON pour la cartographie web interactive finale.\n- [ ] Générer les tuiles de base géographiques et les calques statistiques (IPS, résidus, clusters).",
    "#107": "- [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur rédige cette analyse méthodologique.*",
    "#108": "- [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur rédige cette analyse éthique.*",
    "#109": "- [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur rédige ces ouvertures disciplinaires.*",
    "#110": "- [ ] *Le contributeur n'a aucune tâche technique assignée. L'Auteur définit l'agenda de recherche.*"
}

filepath = "ARCHIVE_issues_V4.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

issues = content.split("### Issue")
new_issues = [issues[0]]

for issue in issues[1:]:
    issue_num_match = re.match(r'^\s*(#[0-9]{3})', issue)
    if issue_num_match:
        issue_num = issue_num_match.group(1)
        
        # We need to find the "- **Pistes d'exploration suggérées :**" block
        pattern = r"- \*\*Pistes d'exploration suggérées :\*\*\n(.*?)(?=\n\n|\Z)"
        match = re.search(pattern, issue, flags=re.DOTALL)
        
        if match:
            old_pistes = match.group(1).strip()
            
            # Convert checkboxes to bullet points in the old pistes
            synopsis_bullets = re.sub(r'^- \[ \]', '  -', old_pistes, flags=re.MULTILINE)
            
            # Check if this issue is in our custom dictionary
            if issue_num in dict_rewrites:
                # Append both the synopsis and the new technical checkboxes
                replacement = (
                    f"- **Synopsis du Chapitre (Ligne directrice) :**\n"
                    f"{synopsis_bullets}\n\n"
                    f"- **Cahier des charges Data-Science (Ouvert aux contributions) :**\n"
                    f"{dict_rewrites[issue_num]}"
                )
            else:
                # If it's not in the dictionary (e.g. it's an Annexe), we just rename the title 
                # to Cahier des charges Data-Science, and keep the original technical boxes.
                replacement = (
                    f"- **Cahier des charges Data-Science (Ouvert aux contributions) :**\n"
                    f"{old_pistes}"
                )
            
            issue = re.sub(pattern, replacement, issue, flags=re.DOTALL)
            
    new_issues.append(issue)

with open(filepath, "w", encoding="utf-8") as f:
    f.write("### Issue".join(new_issues))

print("Applied V3 massive rewrite: Kept synopsis + added technical tasks.")
