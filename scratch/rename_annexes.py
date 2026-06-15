import re

with open("ARCHIVE_issues_V4.md", "r", encoding="utf-8") as f:
    content = f.read()

issues = re.split(r"(^### Issue #\d+.*$)", content, flags=re.MULTILINE)
new_content = [issues[0]]

count = 0
for i in range(1, len(issues), 2):
    title = issues[i]
    body = issues[i+1]
    
    if "Annexe" in title:
        if "Synopsis du Chapitre" in body:
            body = body.replace("Synopsis du Chapitre", "Synopsis de l'Annexe")
            count += 1
            
    new_content.append(title)
    new_content.append(body)

with open("ARCHIVE_issues_V4.md", "w", encoding="utf-8") as f:
    f.write("".join(new_content))

print(f"Replaced {count} instances.")
