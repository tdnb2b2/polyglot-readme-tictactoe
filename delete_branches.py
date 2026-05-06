import subprocess
import time

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

def delete_branches():
    branches_str = run_command(['git', 'branch', '-r'])
    branches = [b.strip() for b in branches_str.split('\n') if b.strip()]
    for b in branches:
        if 'origin/main' in b or 'origin/HEAD' in b:
            continue
        branch_name = b.replace('origin/', '').strip()
        print(f"Deleting branch {branch_name}...")
        subprocess.run(['git', 'push', 'origin', '--delete', branch_name])
        time.sleep(1)

if __name__ == "__main__":
    delete_branches()
