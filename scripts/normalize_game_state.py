#!/usr/bin/env python3
import json
import shutil
import sys
from datetime import datetime

def normalize_logs(logs):
    norm = []
    for entry in logs:
        if isinstance(entry, dict) and "player" in entry and "cell" in entry:
            norm.append({"player": entry["player"], "cell": entry["cell"]})
        elif isinstance(entry, str):
            s = entry.strip()
            if s.lower() == "draw":
                norm.append({"player": None, "cell": None})
            elif "->" in s:
                parts = [part.strip() for part in s.split("->", 1)]
                if len(parts) == 2:
                    norm.append({"player": parts[0], "cell": parts[1]})
    return norm

def main(game_state_path):
    with open(game_state_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Check if data is a dict (game_state.json is a dict of lang_key -> state)
    # The prompt sample assumes 'log' is at the top level, but in this repo it's per language.
    # I should check both cases.
    
    if "log" in data or "logs" in data:
        # Top level log
        logs = data.get("log", data.get("logs", []))
        data["log"] = normalize_logs(logs)
    else:
        # Per language log
        for lang in data:
            if isinstance(data[lang], dict):
                logs = data[lang].get("log", data[lang].get("logs", []))
                data[lang]["log"] = normalize_logs(logs)

    backup = f"{game_state_path}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}"
    shutil.copy2(game_state_path, backup)
    
    with open(game_state_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Normalized {game_state_path}; backup at {backup}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/normalize_game_state.py path/to/game_state.json")
        sys.exit(1)
    main(sys.argv[1])
