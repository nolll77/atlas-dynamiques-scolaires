import re

filepath = "ARCHIVE_issues_V4.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace in Artefacts générés
content = re.sub(
    r"Texte du Chapitre ([0-9]+)", 
    r"Sorties analytiques (graphes, data, scripts) pour le Chapitre \1", 
    content
)

# Replace in the checkboxes (where I manually wrote "Rédiger le texte...")
content = re.sub(
    r"Rédiger le texte du Chapitre ([0-9]+) et exporter", 
    r"Exporter", 
    content
)
content = re.sub(
    r"Intégrer les graphiques et rédiger l'analyse finale dans le Chapitre ([0-9]+)", 
    r"Livrer les graphiques formatés pour le Chapitre \1", 
    content
)
content = re.sub(
    r"Produire la carte choroplèthe finale et rédiger le Chapitre ([0-9]+)", 
    r"Produire la carte choroplèthe finale pour le Chapitre \1", 
    content
)
content = re.sub(
    r"Rédiger l'analyse détaillée des résultats dans le Chapitre ([0-9]+)", 
    r"Consolider les résultats statistiques pour le Chapitre \1", 
    content
)
content = re.sub(
    r"Exporter le tableau de décomposition complet et rédiger le Chapitre ([0-9]+)", 
    r"Exporter le tableau de décomposition complet pour le Chapitre \1", 
    content
)
content = re.sub(
    r"Extraire les sorties du modèle multiniveau pour le texte du Chapitre ([0-9]+)", 
    r"Extraire les sorties du modèle multiniveau pour le Chapitre \1", 
    content
)
content = re.sub(
    r"Exporter le schéma du DAG et rédiger l'analyse du Chapitre ([0-9]+)", 
    r"Exporter le schéma du DAG pour le Chapitre \1", 
    content
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced Texte du Chapitre successfully.")
