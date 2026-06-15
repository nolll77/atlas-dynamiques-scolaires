import re

filepath = "ARCHIVE_issues_V4.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

def replace_match(match):
    pt = match.group(1).strip()
    art = match.group(2).strip()
    
    return f"- [ ] Explorer et rassembler les éléments concernant : {pt}.\n- [ ] Mettre au propre ces travaux pour constituer le document : {art}."

pattern = r"- \[ \] Récupérer tous les éléments concernant : (.*?) \(le périmètre technique\)\.\n- \[ \] Formater ça proprement pour livrer le document final : (.*?) \(l'artefact cible\)\."

new_content = re.sub(pattern, replace_match, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Corporate jargon removed.")
