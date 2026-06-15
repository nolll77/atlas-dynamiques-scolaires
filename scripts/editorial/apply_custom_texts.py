import re

custom_texts = {
    "#022": "- [ ] Calculer les z-scores spatiaux (entre-soi) et générer la carte d'Île-de-France.\n- [ ] Rédiger le texte du Chapitre 14 et exporter le script ainsi que le Top 20.",
    "#023": "- [ ] Décomposer mathématiquement la variance (secteur, géographie) et tracer la Courbe de Lorenz.\n- [ ] Intégrer les graphiques et rédiger l'analyse finale dans le Chapitre 15.",
    "#024": "- [ ] Calculer l'indice de Theil aux trois niveaux géographiques et institutionnels.\n- [ ] Dresser le tableau complet de décomposition de la variance pour le Chapitre 16.",
    "#025": "- [ ] Calculer l'indice de dissimilarité de Duncan (D) et tester la corrélation avec les transports/revenus.\n- [ ] Produire la carte choroplèthe finale et rédiger le Chapitre 17.",
    "#026": "- [ ] Établir la formule de l'indice composite de fragmentation scolaire et pondérer ses composantes.\n- [ ] Rédiger l'analyse détaillée des résultats dans le Chapitre 18.",
    "#028": "- [ ] Exécuter les régressions OLS multi-facteurs (interactions privé/géographie) et tester les variables DVF/transports.\n- [ ] Exporter le tableau de décomposition complet et rédiger le Chapitre 20.",
    "#029": "- [ ] Estimer les ICC (Intraclass Correlation Coefficients) et comparer les R² marginaux et conditionnels.\n- [ ] Extraire les sorties du modèle multiniveau pour le texte du Chapitre 21.",
    "#030": "- [ ] Construire formellement le réseau causal (DAG) et simuler l'effet d'une intervention par \"do-calculus\".\n- [ ] Exporter le schéma du DAG et rédiger l'analyse du Chapitre 22.",
    "#031": "- [ ] Synthétiser les découvertes majeures et les limites de la première partie.\n- [ ] Rédiger le texte de la Conclusion du Tome 1.",
    "#032": "- [ ] Exporter les données nettoyées des lycées au format CSV.\n- [ ] Intégrer cet export pour constituer le Tableau complet de l'Annexe A1.",
    "#033": "- [ ] Dresser l'inventaire exhaustif des jeux de données mobilisés.\n- [ ] Présenter ces métadonnées proprement dans l'Annexe A2.",
    "#034": "- [ ] Convertir la documentation mathématique au format LaTeX.\n- [ ] Compiler ces équations pour constituer l'Annexe A3.",
    "#035": "- [ ] Recenser les contraintes légales et licences Open Data des jeux de données.\n- [ ] Rédiger la note juridique correspondante pour l'Annexe A4.",
    "#036": "- [ ] Rassembler les scripts de nettoyage et de modélisation du Tome 1.\n- [ ] Structurer ce dépôt de code pour l'Annexe A5.",
    "#037": "- [ ] Regrouper les cartes exploratoires non incluses dans les chapitres principaux.\n- [ ] Exporter l'atlas cartographique additionnel pour l'Annexe A6.",
    "#038": "- [ ] Compiler les définitions des termes sociologiques et statistiques utilisés.\n- [ ] Rédiger le glossaire complet pour l'Annexe A7.",
    "#039": "- [ ] Vérifier la mise en forme des références académiques citées dans le texte.\n- [ ] Exporter la bibliographie sélective pour l'Annexe A8.",
    "#040": "- [ ] Réaliser une courte synthèse des travaux comparables à l'étranger.\n- [ ] Rédiger cette note de mise en perspective pour l'Annexe A9.",
    "#070": "- [ ] Synthétiser les apports et limites des modèles spatiaux développés.\n- [ ] Rédiger le texte de la Conclusion du Tome 2.",
    "#071": "- [ ] Rassembler les scripts générant les clusters et les réseaux.\n- [ ] Structurer ce code Python pour l'Annexe A1 du Tome 2.",
    "#072": "- [ ] Exporter les matrices mathématiques (distance, flux) sous format lisible (JSON/CSV).\n- [ ] Mettre à disposition ces jeux de données via l'Annexe A2.",
    "#073": "- [ ] Rassembler les différents benchmarks de vitesse et de performance algorithmique.\n- [ ] Dresser le tableau comparatif final dans l'Annexe A3.",
    "#074": "- [ ] Compiler les logs et les résultats statistiques bruts (OLS, SAR, SEM).\n- [ ] Structurer ces sorties mathématiques pour l'Annexe A4.",
    "#075": "- [ ] Rassembler les résultats des méthodes exploratoires (Random Forest, etc.) non retenues.\n- [ ] Rédiger la note méthodologique associée pour l'Annexe A5.",
    "#076": "- [ ] Regrouper les visualisations géospatiales secondaires générées par les modèles.\n- [ ] Exporter ce recueil cartographique pour l'Annexe A6.",
    "#112": "- [ ] Rassembler les scripts Python dédiés aux séries temporelles et détections de ruptures.\n- [ ] Structurer le code dynamique pour l'Annexe A1 du Tome 3.",
    "#113": "- [ ] Réunir les justifications mathématiques des paramètres choisis pour les modèles.\n- [ ] Rédiger la note méthodologique justificative dans l'Annexe A2.",
    "#114": "- [ ] Extraire les paramètres estimés par les modèles temporels (HMM, algorithme PELT).\n- [ ] Compiler ces valeurs mathématiques dans l'Annexe A3.",
    "#115": "- [ ] Agréger les tableaux de projection issus des simulations de réformes.\n- [ ] Mettre en page ces résultats chiffrés pour l'Annexe A4.",
    "#116": "- [ ] Générer et optimiser les animations (GIFs, vidéos) d'évolution des flux scolaires.\n- [ ] Constituer la galerie multimédia de l'Annexe A5.",
    "#117": "- [ ] Inventorier les sources de données longitudinales exploitées.\n- [ ] Dresser la bibliographie data complète pour l'Annexe A6.",
    "#118": "- [ ] Créer l'indexation globale croisée sur l'ensemble de la trilogie.\n- [ ] Générer l'index général final pour l'Annexe A7.",
    "#119": "- [ ] Agréger les citations et la littérature scientifique de l'ensemble du projet.\n- [ ] Formater la bibliographie exhaustive de l'Annexe A8.",
    "#120": "- [ ] Unifier le dictionnaire des termes techniques (code, stats, socio) employés dans les trois tomes.\n- [ ] Rédiger le glossaire de référence global dans l'Annexe A9.",
    "#121": "- [ ] Vérifier la conformité légale et recenser l'ensemble des licences Open Data.\n- [ ] Rédiger le récapitulatif juridique pour l'Annexe A10."
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
        if issue_num in custom_texts:
            # We want to replace the generic "Explorer et rassembler..." lines
            # with the custom text.
            # First, find where "- **Pistes d'exploration suggérées :**" is.
            pattern = r"- \*\*Pistes d'exploration suggérées :\*\*\n- \[ \] Explorer et rassembler.*?(?=\n\n|\Z)"
            
            replacement = f"- **Pistes d'exploration suggérées :**\n{custom_texts[issue_num]}"
            
            # Use re.sub with re.DOTALL so it matches across newlines
            issue = re.sub(pattern, replacement, issue, flags=re.DOTALL)
            
    new_issues.append(issue)

with open(filepath, "w", encoding="utf-8") as f:
    f.write("### Issue".join(new_issues))

print("Applied 35 custom texts.")
