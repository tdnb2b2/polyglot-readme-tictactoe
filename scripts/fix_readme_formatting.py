import re

def fix_readme_spacing(path):
    with open(path, 'r') as f:
        content = f.read()

    # Ensure blank lines around headers
    content = re.sub(r'\n+(### .*)', r'\n\n\1', content)
    
    # Ensure blank lines around board markers
    content = re.sub(r'\n+(<!-- BOARD_.*_START -->)', r'\n\n\1', content)
    content = re.sub(r'(<!-- BOARD_.*_END -->)\n+', r'\1\n\n', content)
    
    # Cleanup: collapse 3+ newlines into 2
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

if __name__ == "__main__":
    fix_readme_spacing('README.md')
    print("README.md spacing fixed.")
