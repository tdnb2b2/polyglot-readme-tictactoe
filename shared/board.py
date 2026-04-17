import random

# Minimalist board rendering matching readme-games style
# Replaced decorative emojis with clean links and text

CELLS = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
LANG_POOL = [
    "Python", "JavaScript", "Go", "Rust", "Ruby", 
    "PHP", "Java", "CPP", "C", "CSharp", 
    "Swift", "Kotlin", "TypeScript", "Scala"
]

def render_board_md(board_state):
    \"\"\"
    board_state: dict mapping "A1" etc to "X", "O", or None
    \"\"\"
    rows = []
    rows.append("| | A | B | C |")
    rows.append("|---|---|---|---|")
    
    for r in ["1", "2", "3"]:
        line = f"| {r} "
        for c in ["A", "B", "C"]:
            key = f"{c}{r}"
            val = board_state.get(key)
            if val == "X":
                line += "| X "
            elif val == "O":
                line += "| O "
            else:
                # Use a random language for the link to demonstrate polyglot nature
                lang = random.choice(LANG_POOL)
                url = f"https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title={lang}:+Tic-Tac-Toe:+Put+{key}"
                line += f"| [___]({url}) "
        line += "|"
        rows.append(line)
        
    return "\n".join(rows)
