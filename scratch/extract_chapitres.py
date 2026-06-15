import re

with open("ARCHIVE_issues_V4.md", "r") as f:
    text = f.read()

issues = text.split("### Issue")
output = []
for i in issues[1:]:
    if "- [ ] Explorer et rassembler" not in i and "Chapitre" in i.split("\n")[0]:
        title = i.split("\n")[0].strip()
        pistes_match = re.search(r"- \*\*Pistes d'exploration suggérées :\*\*\n(.*?)(?=\n\n|\Z)", i, re.DOTALL)
        if pistes_match:
            pistes = pistes_match.group(1).strip()
            output.append(f"Title: {title}\nPistes:\n{pistes}\n---\n")

with open("scratch/chapitres_to_rewrite.txt", "w") as f:
    f.write("".join(output))

print(f"Extracted {len(output)} issues.")
