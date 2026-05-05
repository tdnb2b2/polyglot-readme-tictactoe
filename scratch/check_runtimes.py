import os
import subprocess

LANGS = [
    'python', 'javascript', 'typescript', 'go', 'rust',
    'java', 'kotlin', 'php', 'ruby', 'csharp', 
    'c', 'cpp', 'scala', 'swift'
]

runners = {
    'python': ['python3', '--version'],
    'javascript': ['node', '--version'],
    'typescript': ['npm', '--version'],
    'go': ['go', 'version'],
    'rust': ['cargo', '--version'],
    'java': ['java', '-version'],
    'kotlin': ['kotlinc', '-version'],
    'php': ['php', '--version'],
    'ruby': ['ruby', '--version'],
    'csharp': ['dotnet', '--version'],
    'c': ['gcc', '--version'],
    'cpp': ['g++', '--version'],
    'scala': ['scala', '-version'],
    'swift': ['swift', '--version']
}

def main():
    for lang in LANGS:
        cmd = runners.get(lang)
        if not cmd:
            print(f"{lang}: No version command")
            continue
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"{lang}: OK ({res.stdout.splitlines()[0] if res.stdout else 'checked'})")
            else:
                print(f"{lang}: FAILED ({res.stderr.splitlines()[0] if res.stderr else 'error'})")
        except Exception as e:
            print(f"{lang}: NOT INSTALLED ({e})")

if __name__ == '__main__':
    main()
