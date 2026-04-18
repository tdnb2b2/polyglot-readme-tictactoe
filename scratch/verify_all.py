import os
import json
import subprocess
import shutil

LANGUAGES = {
    'python':     (['python3', 'game.py'], 'implementations/python'),
    'javascript': (['node',    'game.js'], 'implementations/javascript'),
    'typescript': (['npx', 'ts-node', 'game.ts'], 'implementations/typescript'),
    'go':         (['go', 'run', 'game.go'], 'implementations/go'),
    'rust':       (['./target/release/game'], 'implementations/rust'),
    'java':       (['java', 'Game'], 'implementations/java'),
    'kotlin':     (['java', '-jar', 'Game.jar'], 'implementations/kotlin'),
    'php':        (['php',     'game.php'], 'implementations/php'),
    'ruby':       (['ruby',    'game.rb'], 'implementations/ruby'),
    'csharp':     (['dotnet', 'run', '--no-build'], 'implementations/csharp'),
    'c':          (['./game'], 'implementations/c'),
    'cpp':        (['./game'], 'implementations/cpp'),
    'scala':      (['scala',   'Game.scala'], 'implementations/scala'),
    'swift':      (['swift',   'game.swift'], 'implementations/swift'),
}

def verify_lang(lang, cmd, impl_dir):
    print(f"--- Verifying {lang} ---")
    state_path = os.path.join(impl_dir, 'current_state.json')
    
    # 1. Reset
    env = os.environ.copy()
    env['ACTION'] = 'reset'
    env['CELL'] = ''
    
    # Initialize state
    with open(state_path, 'w') as f:
        json.dump({
            'board': [['','',''],['','',''],['','','']],
            'turn': 'X',
            'winner': None,
            'log': []
        }, f)

    try:
        subprocess.run(cmd, env=env, cwd=impl_dir, check=True, capture_output=True)
    except Exception as e:
        return False, f"Reset failed: {e}"

    # 2. Put B2 (expect board[1][1] = 'X')
    env['ACTION'] = 'put'
    env['CELL'] = 'B2'
    try:
        subprocess.run(cmd, env=env, cwd=impl_dir, check=True, capture_output=True)
    except Exception as e:
        return False, f"Put B2 failed: {e}"

    with open(state_path, 'r') as f:
        state = json.load(f)
    
    if state['board'][1][1] != 'X':
        return False, f"Expected board[1][1] to be 'X', got '{state['board'][1][1]}'"

    # 3. Put A1 (expect board[0][0] = 'O')
    env['ACTION'] = 'put'
    env['CELL'] = 'A1'
    try:
        subprocess.run(cmd, env=env, cwd=impl_dir, check=True, capture_output=True)
    except Exception as e:
        return False, f"Put A1 failed: {e}"

    with open(state_path, 'r') as f:
        state = json.load(f)

    if state['board'][0][0] != 'O':
        return False, f"Expected board[0][0] to be 'O', got '{state['board'][0][0]}'"

    print(f"PASS: {lang}")
    return True, ""

def main():
    results = {}
    for lang, (cmd, impl_dir) in LANGUAGES.items():
        # Check if dir exists
        full_dir = os.path.join(os.getcwd(), impl_dir)
        if not os.path.exists(full_dir):
            results[lang] = (False, "Directory not found")
            continue
        
        # Check if binary needs building (Quick check)
        if lang == 'rust' and not os.path.exists(os.path.join(full_dir, 'target/release/game')):
            print(f"Building {lang}...")
            subprocess.run(['cargo', 'build', '--release'], cwd=full_dir)
        elif lang == 'c' and not os.path.exists(os.path.join(full_dir, 'game')):
            print(f"Building {lang}...")
            subprocess.run(['gcc', 'game.c', '-o', 'game'], cwd=full_dir)
        elif lang == 'cpp' and not os.path.exists(os.path.join(full_dir, 'game')):
            print(f"Building {lang}...")
            subprocess.run(['g++', 'game.cpp', '-o', 'game'], cwd=full_dir)
        elif lang == 'java' and not os.path.exists(os.path.join(full_dir, 'Game.class')):
            print(f"Building {lang}...")
            subprocess.run(['javac', '-cp', '.:lib/*', 'Game.java'], cwd=full_dir)
        elif lang == 'kotlin' and not os.path.exists(os.path.join(full_dir, 'Game.jar')):
            print(f"Kotlin verification skipped: Jar missing. Try manual build.")
            results[lang] = (False, "Jar missing")
            continue

        ok, msg = verify_lang(lang, cmd, impl_dir)
        results[lang] = (ok, msg)
        
        # Cleanup
        state_path = os.path.join(impl_dir, 'current_state.json')
        if os.path.exists(state_path):
            os.remove(state_path)

    print("\n--- Final Results ---")
    all_pass = True
    for lang, (ok, msg) in results.items():
        status = "OK" if ok else f"FAIL: {msg}"
        print(f"{lang:12} : {status}")
        if not ok: all_pass = False
    
    if all_pass:
        print("\nAll systems go! Coordinate mapping is consistent across all languages.")
    else:
        print("\nVerification failed for some languages.")

if __name__ == "__main__":
    main()
