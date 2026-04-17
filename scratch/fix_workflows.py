import os

LANGUAGES = {
    "python": {"runner": "ubuntu-latest", "setup": "actions/setup-python@v5", "version_key": "python-version", "version": "3.12"},
    "javascript": {"runner": "ubuntu-latest", "setup": "actions/setup-node@v4", "version_key": "node-version", "version": "20"},
    "typescript": {"runner": "ubuntu-latest", "setup": "actions/setup-node@v4", "version_key": "node-version", "version": "20"},
    "go": {"runner": "ubuntu-latest", "setup": "actions/setup-go@v5", "version_key": "go-version", "version": "1.21"},
    "rust": {"runner": "ubuntu-latest", "setup": "actions-rs/toolchain@v1", "version_key": "toolchain", "version": "stable"},
    "java": {"runner": "ubuntu-latest", "setup": "actions/setup-java@v4", "version_key": "java-version", "version": "17", "extra": "distribution: 'temurin'"},
    "kotlin": {"runner": "ubuntu-latest", "setup": "actions/setup-java@v4", "version_key": "java-version", "version": "17", "extra": "distribution: 'temurin'"},
    "php": {"runner": "ubuntu-latest", "setup": "shivammathur/setup-php@v2", "version_key": "php-version", "version": "8.2"},
    "ruby": {"runner": "ubuntu-latest", "setup": "ruby/setup-ruby@v1", "version_key": "ruby-version", "version": "3.2"},
    "csharp": {"runner": "ubuntu-latest", "setup": "actions/setup-dotnet@v4", "version_key": "dotnet-version", "version": "8.0"},
    "cpp": {"runner": "ubuntu-latest", "setup": None},
    "c": {"runner": "ubuntu-latest", "setup": None},
    "scala": {"runner": "ubuntu-latest", "setup": "actions/setup-java@v4", "version_key": "java-version", "version": "17", "extra": "distribution: 'temurin'"},
    "swift": {"runner": "macos-latest", "setup": None},
}

TEMPLATE = """name: {name} Tic-Tac-Toe
on:
  issues:
    types: [opened]

jobs:
  play:
    runs-on: {runner}
    if: "${{{{ contains(github.event.issue.title, '{name}: Tic-Tac-Toe:') }}}}"
    permissions:
      contents: write
      issues: write
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install dependencies
        run: pip install requests

{setup_steps}
      - name: Play Game
        run: python3 dispatcher.py run
        env:
          GITHUB_TOKEN: ${{{{ secrets.GITHUB_TOKEN }}}}
          ISSUE_TITLE: ${{{{ github.event.issue.title }}}}
          ISSUE_NUMBER: ${{{{ github.event.issue.number }}}}
          REPO: ${{{{ github.repository }}}}
          LANGUAGE_OVERRIDE: {lang_key}

      - name: Keep workspace warm
        if: always()
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add game_state.json
          git commit -m "game({lang_key}): update state" || echo "No changes"
          git push origin main || echo "Push failed"
"""

def generate():
    for lang, info in LANGUAGES.items():
        name = lang.capitalize() if lang != 'cpp' else 'Cpp'
        if lang == 'csharp': name = 'C#'
        if lang == 'cpp': name = 'C++'
        if lang == 'javascript': name = 'JavaScript'
        if lang == 'typescript': name = 'TypeScript'
        
        setup_steps = ""
        if info["setup"]:
            setup_steps += f"      - name: Setup {name}\n"
            setup_steps += f"        uses: {info['setup']}\n"
            setup_steps += f"        with:\n"
            setup_steps += f"          {info['version_key']}: '{info['version']}'\n"
            if "extra" in info:
                setup_steps += f"          {info['extra']}\n"
        
        content = TEMPLATE.format(
            name=name,
            lang_key=lang,
            runner=info["runner"],
            setup_steps=setup_steps
        )
        
        filename = f".github/workflows/{lang}.yml"
        os.makedirs(".github/workflows", exist_ok=True)
        with open(filename, "w") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate()
