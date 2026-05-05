import os
import subprocess
import json

LANGS = ["c", "cpp", "csharp", "go", "java", "javascript", "kotlin", "php", "python", "ruby", "rust", "scala", "swift", "typescript"]

def test_lang(lang):
    title = f"{lang}: Tic-Tac-Toe: Reset"
    print(f"--- Testing {lang} ---")
    env = os.environ.copy()
    env['ISSUE_TITLE'] = title
    env['REPO'] = 'tdnb2b2/polyglot-readme-tictactoe'
    env['ISSUE_NUMBER'] = '0'
    
    result = subprocess.run(['python3', 'dispatcher.py'], env=env, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"SUCCESS: {lang}")
        return True
    else:
        print(f"FAILED: {lang}")
        print(result.stderr)
        return False

def main():
    failed = []
    for lang in LANGS:
        if not test_lang(lang):
            failed.append(lang)
    
    if failed:
        print(f"\nFAILED LANGUAGES: {', '.join(failed)}")
    else:
        print("\nALL LANGUAGES PASSED RESET TEST.")

if __name__ == '__main__':
    main()
