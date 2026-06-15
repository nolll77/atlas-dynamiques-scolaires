import re

filepath = "ARCHIVE_issues_V4.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace any occurrence of "Transparence" or "Transparence totale" after "Périmètre Éditorial & Éthique"
# Some lines might be exactly "**Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence."
# or "**Périmètre Éditorial & Éthique (Réservé à l'Auteur)** : Transparence totale."

def replacer(match):
    prefix = match.group(1)
    return f"{prefix}Reproductibilité de la recherche."

# Pattern to match the specific line and capture the prefix up to the colon + space
pattern = r"(\*\*Périmètre Éditorial & Éthique[^:]*:\s*)Transparence(?: totale)?\.?"

new_content = re.sub(pattern, replacer, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Replaced Transparence with Reproductibilité de la recherche.")
