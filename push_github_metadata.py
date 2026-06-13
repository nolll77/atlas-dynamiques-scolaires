import os
import subprocess
import time
import re

# 1. Création des labels
LABELS = [
    ("tome 1 : la carte", "1D76DB", "Tome I"),
    ("tome 2 : les réseaux", "0E8A16", "Tome II"),
    ("tome 3 : le temps", "D93F0B", "Tome III"),
    ("partie", "FBCA04", "Ouverture de partie"),
    ("chapitre", "F9D0C4", "Chapitre classique"),
    ("statut: draft", "D4C5F9", "Brouillon"),
    ("statut: review", "006B75", "En relecture"),
    ("statut: complet", "0E8A16", "Terminé"),
    ("data", "1D76DB", "Traitement de données"),
    ("figure", "B60205", "Génération de figure"),
]

def create_labels():
    print("🏷️ Création des labels sur GitHub...")
    for name, color, desc in LABELS:
        try:
            subprocess.run(
                ["gh", "label", "create", name, "-c", color, "-d", desc],
                check=True,
                capture_output=True
            )
            print(f"  ✅ Label '{name}' créé.")
        except subprocess.CalledProcessError as e:
            # Si le label existe déjà, ça renvoie une erreur, on ignore
            print(f"  ℹ️ Label '{name}' existe déjà ou erreur.")
        time.sleep(0.5)

# 2. Création des issues
def create_issues():
    filepath = "/Users/nolll/.gemini/antigravity/brain/63b5031e-a8aa-45bb-a63d-d7062717de7d/github_issues.md"
    if not os.path.exists(filepath):
        print("❌ Fichier github_issues.md introuvable.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex pour capturer la structure de chaque issue
    # Format: ### Issue #001 — Titre ou ### Issue #017b — Titre
    
    issues_raw = re.split(r'### Issue #\d+[a-z]* — ', content)
    
    print(f"🗃️ Parsage de {len(issues_raw)-1} issues potentielles...")
    
    for raw in issues_raw[1:]: # On ignore le premier split qui est l'en-tête du fichier
        lines = raw.strip().split('\n')
        title = lines[0].strip()
        
        labels = []
        body = []
        in_body = False
        
        for line in lines[1:]:
            if line.startswith("**Labels:**"):
                labels_str = line.replace("**Labels:**", "").strip()
                # Les labels sont souvent séparés par des virgules et ont des backticks
                labels_str = labels_str.replace("`", "")
                labels = [l.strip() for l in labels_str.split(',')]
            elif line.startswith("**Body / Checklist:**") or line.startswith("**Body:**") or in_body:
                in_body = True
                if not line.startswith("**Body"):
                    body.append(line)
        
        body_text = "\n".join(body).strip()
        
        print(f"Création de l'issue: {title}")
        
        cmd = ["gh", "issue", "create", "--title", title, "--body", body_text]
        for lbl in labels:
            if lbl:
                cmd.extend(["--label", lbl])
                
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"  ✅ Créée avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Erreur sur '{title}': {e.stderr.decode('utf-8', errors='ignore')}")
            
        time.sleep(1.5) # Anti-rate limit GitHub (1.5s entre chaque issue)

if __name__ == "__main__":
    create_labels()
    create_issues()
    print("\n🚀 Terminé !")
