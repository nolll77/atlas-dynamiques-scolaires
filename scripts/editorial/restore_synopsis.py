import re

plan_path = "/Users/nolll/.gemini/antigravity/brain/63b5031e-a8aa-45bb-a63d-d7062717de7d/plan_integral_v2.md"
with open(plan_path, "r", encoding="utf-8") as f:
    plan_lines = f.readlines()

bullets_db = []
current_title = None
bullets = []

for line in plan_lines:
    line_clean = line.strip()
    
    m_chap = re.match(r'^\*\*Chapitre \d+ — (.*)\*\*', line_clean)
    m_conc = re.match(r'^### (Conclusion.*)', line_clean)
    m_ann = re.match(r'^- (A\d+ : (.*))', line_clean)
    
    if m_chap or m_conc or m_ann:
        if current_title:
            bullets_db.append((current_title, bullets))
        
        if m_chap:
            current_title = m_chap.group(1).strip()
            bullets = []
        elif m_conc:
            current_title = m_conc.group(1).strip()
            bullets = []
        elif m_ann:
            current_title = "Annexe " + m_ann.group(1).strip()
            # For annexes, the line itself is the synopsis if there are no sub-bullets
            bullets = [m_ann.group(2).strip()]
            
    elif current_title and line_clean.startswith('- '):
        # If we see a bullet, and we are in an annexe, it means the annexe has sub-bullets? No, annexes don't have sub-bullets.
        # But if they did, we would append. Actually for annexes we don't want to append other unrelated bullets.
        if "Annexe" not in current_title:
            bullets.append(line_clean)

if current_title:
    bullets_db.append((current_title, bullets))

def find_bullets(issue_title):
    if "Conclusion du Tome I" in issue_title:
        for t, b in bullets_db:
            if "Conclusion du Tome I" in t: return b
    if "Conclusion Tome II" in issue_title or "Conclusion du Tome II" in issue_title:
        for t, b in bullets_db:
            if "Conclusion du Tome II" in t: return b
    if "Conclusion générale" in issue_title or "Conclusion du Tome III" in issue_title:
        for t, b in bullets_db:
            if "Conclusion générale" in t or "Conclusion du Tome III" in t: return b
            
    m = re.search(r'(Annexe A\d+)', issue_title)
    if m:
        ann_id = m.group(1)
        issue_num_match = re.search(r'#(\d+)', issue_title)
        if not issue_num_match: return []
        num = int(issue_num_match.group(1))
        
        tome = 1
        if num > 60 and num < 100: tome = 2
        if num > 100: tome = 3
        
        occurrences = [b for t, b in bullets_db if t.startswith(ann_id)]
        if tome == 1 and len(occurrences) >= 1: return occurrences[0]
        if tome == 2 and len(occurrences) >= 2: return occurrences[1]
        if tome == 3 and len(occurrences) >= 3: return occurrences[2]
        return []
        
    if "Chapitre" in issue_title:
        title_part = issue_title.split(":")[-1].strip().lower()
        for t, b in bullets_db:
            if title_part in t.lower() or t.lower() in title_part:
                return b
        chap_num_match = re.search(r'Chapitre (\d+)', issue_title)
        if chap_num_match:
            cnum = chap_num_match.group(1)
            for t, b in bullets_db:
                words1 = set(title_part.replace("'", " ").split())
                words2 = set(t.replace("'", " ").lower().split())
                if len(words1.intersection(words2)) > 2:
                    return b
    return []

archive_path = "ARCHIVE_issues_V4.md"
with open(archive_path, "r", encoding="utf-8") as f:
    archive_lines = f.readlines()

new_archive_lines = []
i = 0
count = 0
while i < len(archive_lines):
    line = archive_lines[i]
    new_archive_lines.append(line)
    
    if line.strip().startswith("- **Périmètre Éditorial") or line.strip().startswith("- **Artefacts générés**"):
        # We might have an issue with missing "Périmètre Éditorial" (like some annexes only have Artefacts générés)
        # We need to ensure we only insert ONCE per issue.
        # Let's see if we already inserted for this issue. We can do the insertion logic after checking for 'Artefacts générés' ONLY IF 'Périmètre Éditorial' is NOT present, or right after 'Périmètre Éditorial' if it is present.
        
        # ACTUALLY, for Annexes, there is NO Périmètre Éditorial !
        # Look at Issue #032:
        # ### Issue #032 — Annexe A1 : Tableau complet des lycées
        # **Labels** : `annexe`, `data`, `difficulty: medium`
        # - **Artefacts générés** : Annexe A1.
        
        pass # Handle this differently

    i += 1

# Let's do a better replacement approach: block by block
import re
with open(archive_path, "r", encoding="utf-8") as f:
    content = f.read()

issues = re.split(r'(^### Issue #\d+.*$)', content, flags=re.MULTILINE)
new_content = [issues[0]]

for j in range(1, len(issues), 2):
    title = issues[j]
    body = issues[j+1]
    
    if "Synopsis" not in body:
        matched_bullets = find_bullets(title)
        if matched_bullets:
            # Insert synopsis before "Artefacts générés" or at the end of the metadata block
            synopsis_text = "\n- **Synopsis du Chapitre (Réflexions de l'Auteur) :**\n"
            for b in matched_bullets:
                b_clean = re.sub(r'^- A\d+ : ', '', b).strip()
                synopsis_text += "  - " + b_clean + "\n"
                
            if "- **Artefacts générés**" in body:
                body = body.replace("- **Artefacts générés**", synopsis_text.strip() + "\n\n- **Artefacts générés**")
            elif "- **Périmètre de cohérence technique" in body:
                body = body.replace("- **Périmètre de cohérence technique", synopsis_text.strip() + "\n\n- **Périmètre de cohérence technique")
            else:
                body += "\n" + synopsis_text.strip() + "\n"
            count += 1
            print(f"Restored synopsis for {title.strip()} ({len(matched_bullets)} bullets)")
    
    new_content.append(title)
    new_content.append(body)

with open("ARCHIVE_issues_V4.md", "w", encoding="utf-8") as f:
    f.write("".join(new_content))

print(f"Total restored: {count}")
