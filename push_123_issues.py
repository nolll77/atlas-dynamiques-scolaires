import os
import subprocess
import time
import re

def extract_unique_labels(filepath):
    unique_labels = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("**Labels:**"):
                labels_str = line.split(":", 1)[1].strip().replace("`", "")
                for l in labels_str.split(","):
                    if l.strip():
                        unique_labels.add(l.strip())
    return list(unique_labels)

def ensure_labels(filepath):
    labels = extract_unique_labels(filepath)
    print(f"🏷️ Labels détectés : {labels}")
    for lbl in labels:
        # Create or update label. Using -f forces update if it exists.
        subprocess.run(["gh", "label", "create", lbl, "-f"], capture_output=True)

def create_issues_ordered():
    filepath = "ARCHIVE_issues_V3_detaillees.md"
    if not os.path.exists(filepath):
        print(f"❌ Fichier {filepath} introuvable.")
        return

    ensure_labels(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    issues_to_create = []
    current_issue = None
    
    for line in lines:
        line_clean = line.strip()
        
        # Skip milestone headers as we'll use the title directly
        if line_clean.startswith("## MILESTONE : "):
            continue
            
        match = re.match(r'^### Issue — (.*)', line_clean)
        if match:
            if current_issue:
                issues_to_create.append(current_issue)
                
            issue_title = match.group(1).strip()
            
            current_issue = {
                "title": issue_title,
                "labels": [],
                "body": []
            }
            continue
            
        if current_issue:
            if line_clean.startswith("**Labels:**"):
                labels_str = line_clean.split(":", 1)[1].strip()
                current_issue["labels"] = [l.strip() for l in labels_str.split(',') if l.strip()]
            else:
                current_issue["body"].append(line_clean)

    if current_issue:
        issues_to_create.append(current_issue)

    # REVERSE THE LIST FOR GITHUB DISPLAY
    issues_to_create.reverse()

    print(f"🗃️ {len(issues_to_create)} issues trouvées. Création en ordre inversé...")
    
    for issue in issues_to_create:
        title = issue["title"]
        body_text = "\n".join(issue["body"]).strip()
        
        cmd = ["gh", "issue", "create", "--title", title, "--body", body_text]
        for lbl in issue["labels"]:
            if lbl:
                cmd.extend(["--label", lbl])
                
        try:
            print(f"Création de : {title}...")
            # We wait 2 seconds between API calls to avoid rate limits
            time.sleep(2)
            res = subprocess.run(cmd, check=True, capture_output=True)
            print(f"  ✅ Succès.")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Erreur sur '{title}': {e.stderr.decode('utf-8', errors='ignore')}")

if __name__ == "__main__":
    create_issues_ordered()
    print("\n🚀 Terminé ! Toutes les issues V3 ont été injectées sur GitHub.")
