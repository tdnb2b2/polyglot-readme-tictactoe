import os
import subprocess

# Try to get token from env
token = os.environ.get('GITHUB_TOKEN')
if not token:
    # If not in env, check if we can get it via gh auth or just skip
    print("No GITHUB_TOKEN found in environment.")
    exit(1)

repo = "tdnb2b2/polyglot-readme-tictactoe"
url = f"https://{token}@github.com/{repo}.git"

try:
    print(f"Pushing to {repo}...")
    subprocess.run(["git", "push", "--force", url, "main"], check=True)
    print("Push successful.")
except Exception as e:
    print(f"Push failed: {e}")
    exit(1)
