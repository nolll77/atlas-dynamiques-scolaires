import re

filepath = "ARCHIVE_issues_V4.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

issues = content.split("### Issue")
count = 0
for i in issues[1:]:
    if "- [ ] Explorer et rassembler" in i:
        title = i.split("\n")[0].strip()
        pt_match = re.search(r'\*\*Périmètre Technique[^*]*\*\*\s*:\s*(.*)', i)
        art_match = re.search(r'\*\*Artefacts générés\*\*\s*:\s*(.*)', i)
        pt = pt_match.group(1).strip() if pt_match else "N/A"
        art = art_match.group(1).strip() if art_match else "N/A"
        print(f"Issue: {title}\nPT: {pt}\nArt: {art}\n---")
        count += 1
print(f"Total: {count}")
