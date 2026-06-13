import os
import subprocess
import time
import re

def ensure_labels():
    labels = ["code", "ethique", "exploratory", "annexe", "infrastructure", "chapitre", "figure", "documentation"]
    for lbl in labels:
        subprocess.run(["gh", "label", "create", lbl, "-f"], capture_output=True)

def create_issues_ordered():
    ensure_labels()
    filepath = "/Users/nolll/.gemini/antigravity/brain/63b5031e-a8aa-45bb-a63d-d7062717de7d/github_issues.md"
    if not os.path.exists(filepath):
        print("❌ Fichier github_issues.md introuvable.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    issues_to_create = []
    current_milestone = "Général"
    
    current_issue = None
    
    for line in lines:
        line_clean = line.strip()
        
        # Détection du jalon (Tome)
        if "MILESTONE" in line_clean:
            if "T1" in line_clean or "TOME I" in line_clean:
                current_milestone = "Tome I"
            elif "T2" in line_clean or "TOME II" in line_clean:
                current_milestone = "Tome II"
            elif "T3" in line_clean or "TOME III" in line_clean:
                current_milestone = "Tome III"
            elif "MILESTONE 0" in line_clean:
                current_milestone = "Setup"
            elif "Paper" in line_clean or "Publication" in line_clean:
                current_milestone = "Publication"
            continue
            
        # Détection du début d'une issue
        match = re.match(r'^### Issue #(\d+[a-z]*) — (.*)', line_clean)
        if match:
            # Si on était en train de lire une issue, on la sauvegarde
            if current_issue:
                issues_to_create.append(current_issue)
                
            issue_num = match.group(1)
            issue_name = match.group(2)
            
            # Formatage propre et lisible pour l'UX GitHub
            formatted_title = f"[{current_milestone}] #{issue_num} — {issue_name}"
            
            current_issue = {
                "title": formatted_title,
                "labels": [],
                "body": []
            }
            continue
            
        if current_issue:
            if line_clean.startswith("**Labels**") or line_clean.startswith("**Labels:**"):
                labels_str = line_clean.split(":", 1)[1].strip()
                labels_str = labels_str.replace("`", "")
                current_issue["labels"] = [l.strip() for l in labels_str.split(',') if l.strip()]
            else:
                current_issue["body"].append(line_clean)

    # N'oublions pas la dernière issue !
    if current_issue:
        issues_to_create.append(current_issue)

    # ---------------------------------------------------------
    # LA MAGIE UX : ON INVERSE LA LISTE !
    # ---------------------------------------------------------
    # GitHub affiche les issues les plus "récentes" en haut.
    # En poussant la #103 en premier, et la #001 en dernier, 
    # la #001 se retrouvera tout en haut de la liste par défaut !
    issues_to_create.reverse()

    print(f"🗃️ {len(issues_to_create)} issues trouvées. Création en ordre inversé (du {issues_to_create[0]['title']} vers le #001)...")
    
    for issue in issues_to_create:
        title = issue["title"]
        if not any(x in title for x in ["#085"]):
            continue
            
        body_text = "\n".join(issue["body"]).strip()
        
        cmd = ["gh", "issue", "create", "--title", title, "--body", body_text]
        for lbl in issue["labels"]:
            if lbl:
                cmd.extend(["--label", lbl])
                
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"  ✅ Créée : {title}")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Erreur sur '{title}': {e.stderr.decode('utf-8', errors='ignore')}")
            
        time.sleep(1.5)

if __name__ == "__main__":
    create_issues_ordered()
    print("\n🚀 Terminé ! Tout est parfait et ordonné.")
