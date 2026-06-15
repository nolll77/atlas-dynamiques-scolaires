import re

with open('ARCHIVE_issues_V4.md', 'r', encoding='utf-8') as f:
    content = f.read()

issues = content.split('### Issue')
new_issues = [issues[0]]

for issue in issues[1:]:
    # Find the synopsis block
    synopsis_pattern = r'\n- \*\*Synopsis du Chapitre \(Ligne directrice\) :\*\*\n(.*?)(?=\n\n- \*\*Périmètre de cohérence technique)'
    match = re.search(synopsis_pattern, issue, flags=re.DOTALL)
    
    if match:
        synopsis_content = match.group(1).rstrip()
        # Remove the synopsis block from its original place
        issue = re.sub(synopsis_pattern + r'\n\n', '\n', issue, flags=re.DOTALL)
        
        # Build the new metadata block to insert BEFORE 'Artefacts générés'
        new_synopsis_block = f"- **Synopsis du Chapitre (Réflexions de l'Auteur)** :\n{synopsis_content}\n"
        
        # Insert before '- **Artefacts générés**'
        issue = re.sub(r'(- \*\*Artefacts générés\*\* :.*?\n)', new_synopsis_block + r'\1', issue)
        
    new_issues.append(issue)

with open('ARCHIVE_issues_V4.md', 'w', encoding='utf-8') as f:
    f.write("### Issue".join(new_issues))

print("Moved synopsis blocks to metadata section!")
