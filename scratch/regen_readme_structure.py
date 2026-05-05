import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(ROOT, 'README.md')

LANGS = [
    ("c", "C"),
    ("cpp", "C++"),
    ("csharp", "C#"),
    ("go", "Go"),
    ("java", "Java"),
    ("javascript", "JavaScript"),
    ("kotlin", "Kotlin"),
    ("php", "PHP"),
    ("python", "Python"),
    ("ruby", "Ruby"),
    ("rust", "Rust"),
    ("scala", "Scala"),
    ("swift", "Swift"),
    ("typescript", "TypeScript")
]

def main():
    content = "# 🕹️ Polyglot Tic-Tac-Toe on GitHub README\n\n"
    content += "A playable Tic-Tac-Toe game on GitHub README, implemented in multiple programming languages! Make moves by creating issues.\n\n"
    content += "---\n\n"
    content += "## 🛠️ Individual Boards\n\n"

    for lang_key, lang_display in LANGS:
        content += f"### {lang_display}\n\n"
        content += f"<!-- BOARD_{lang_key.upper()}_START -->\n"
        content += f"<!-- BOARD_{lang_key.upper()}_END -->\n\n"

    with open(README_PATH, 'w') as f:
        f.write(content)
    print("README structure regenerated with correct order.")

if __name__ == '__main__':
    main()
