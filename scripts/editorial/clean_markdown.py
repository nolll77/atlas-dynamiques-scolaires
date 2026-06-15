import re

with open('ARCHIVE_issues_V4.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the redundant line
content = re.sub(r'- \*\*Périmètre Technique \(Ouvert aux contributions\)\*\* : .*?\n', '', content)

# 2. Indent the checkboxes
content = re.sub(r'\n- \[ \]', '\n  - [ ]', content)

with open('ARCHIVE_issues_V4.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("Cleaned up ARCHIVE_issues_V4.md!")
