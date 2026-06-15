import os
import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace **Formule :** $...$ with block math
    # Or replace any $...$ that has multiple underscores.
    # The safest is to replace "**Formule :** $...$" with "**Formule :**\n\n$$\n...\n$$"
    
    def replacer(match):
        math_content = match.group(1)
        return f"**Formule :**\n\n$$\n{math_content}\n$$"

    new_content = re.sub(r'\*\*Formule :\*\* \$(.+?)\$', replacer, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)

fix_file('docs/SOCLE_DYNAMIQUE.md')
try:
    fix_file('docs/SOCLE_MATHEMATIQUE.md')
except Exception as e:
    pass

print("Math formatting fixed.")
