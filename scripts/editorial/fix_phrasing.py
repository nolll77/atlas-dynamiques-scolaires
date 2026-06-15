import re

filepath = "ARCHIVE_issues_V4.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# I will find all instances of:
# - [ ] Récupérer les éléments liés à : {pt}
# - [ ] Mettre en forme et livrer le document : {art}

def replace_match(match):
    pt = match.group(1).strip()
    art = match.group(2).strip()
    # Strip trailing periods if they got left behind
    if pt.endswith('.'): pt = pt[:-1]
    if art.endswith('.'): art = art[:-1]
    
    return f"- [ ] Récupérer tous les éléments concernant : {pt} (le périmètre technique).\n- [ ] Formater ça proprement pour livrer le document final : {art} (l'artefact cible)."

pattern = r"- \[ \] Récupérer les éléments liés à : (.*?)\n- \[ \] Mettre en forme et livrer le document : (.*?)(?=\n|$)"

new_content = re.sub(pattern, replace_match, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Phrasing fixed.")
