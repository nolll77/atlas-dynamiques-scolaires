import os

def fix_line(line):
    content = line[len("**Formule :** "):].strip()
    parts = content.split('$')
    
    math_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            math_parts.append(part.strip())
        else:
            text = part.strip()
            if text:
                math_parts.append(f"\\quad \\text{{{text}}} \\quad")
                
    joined_math = " ".join(math_parts)
    return "**Formule :**\n\n$$\n\\Huge " + joined_math + "\n$$\n"

def process_file(orig, dest):
    if not os.path.exists(orig):
        return
    with open(orig, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if line.startswith("**Formule :** "):
            new_lines.append(fix_line(line))
        else:
            new_lines.append(line)
            
    with open(dest, 'w') as f:
        f.writelines(new_lines)
    print(f"Fixed {dest}")

process_file('original_dynamique.md', 'docs/SOCLE_DYNAMIQUE.md')
process_file('original_mathematique.md', 'docs/SOCLE_MATHEMATIQUE.md')
