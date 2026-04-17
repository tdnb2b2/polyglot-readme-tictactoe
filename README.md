# 🎮 polyglot-readme-tictactoe

> **Tic-Tac-Toe playable directly on this README — in 14 programming languages.**  
> Each language runs its own independent board, powered by GitHub Actions.  
> Click ➕ to make a move. The corresponding language implementation processes your move and updates this README.

---

## How to Play

1. Pick a language board below
2. Click any **➕** cell — it opens a pre-filled GitHub Issue
3. Submit the issue — GitHub Actions runs that language's implementation
4. The board updates automatically within ~30 seconds
5. Players alternate: ❌ goes first, then ⭕

**Move format:** `<Language>: Tic-Tac-Toe: Put <Cell>` (e.g. `Python: Tic-Tac-Toe: Put B2`)

---

## 🐍 Python

<!-- PYTHON_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Python+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Python+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Python+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Python+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Python+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Python+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Python+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Python+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Python+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Python+board)
<!-- PYTHON_END -->

<details>
<summary>📄 Python implementation snippet</summary>

```python
import json, os

# Read the simplified state
with open('current_state.json', 'r') as f:
    s = json.load(f)

cell   = os.environ.get('CELL', '').upper()
action = os.environ.get('ACTION', 'put')

if action == 'reset':
    s = {"board": [["","",""],["","",""],["","",""]], "turn": "X", "winner": None, "log": []}
elif cell and not s["winner"]:
    # Apply Tic-Tac-Toe logic...
    pass

# Write it back
with open('current_state.json', 'w') as f:
    json.dump(s, f, indent=2)
```

</details>

---

## 🌐 JavaScript

<!-- JAVASCRIPT_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+JavaScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+JavaScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+JavaScript+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+JavaScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+JavaScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+JavaScript+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+JavaScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+JavaScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+JavaScript+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Reset&body=Reset+JavaScript+board)
<!-- JAVASCRIPT_END -->

<details>
<summary>📄 JavaScript implementation snippet</summary>

```javascript
const fs = require('fs');
const s = JSON.parse(fs.readFileSync('current_state.json'));
const cell = (process.env.CELL || "").toUpperCase();
const action = process.env.ACTION || "put";

if (action === 'reset') {
    s.board = [["","",""],["","",""],["","",""]];
    s.turn = "X"; s.winner = null; s.log = [];
} else if (cell && !s.winner) {
    // Apply logic...
}
fs.writeFileSync('current_state.json', JSON.stringify(s, null, 2));
```

</details>

---

## 🔷 TypeScript

<!-- TYPESCRIPT_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+TypeScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+TypeScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+TypeScript+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+TypeScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+TypeScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+TypeScript+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+TypeScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+TypeScript+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+TypeScript+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Reset&body=Reset+TypeScript+board)
<!-- TYPESCRIPT_END -->

<details>
<summary>📄 TypeScript implementation snippet</summary>

```typescript
import * as fs from 'fs';
const s = JSON.parse(fs.readFileSync('current_state.json', 'utf8'));
// Apply logic...
fs.writeFileSync('current_state.json', JSON.stringify(s, null, 2));
```

</details>

---

## 🐹 Go

<!-- GO_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Go+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Go+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Go+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Go+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Go+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Go+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Go+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Go+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Go+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Go+board)
<!-- GO_END -->

---

## 🦀 Rust

<!-- RUST_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Rust+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Rust+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Rust+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Rust+board)
<!-- RUST_END -->

---

## ☕ Java

<!-- JAVA_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Java+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Java+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Java+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Java+board)
<!-- JAVA_END -->

---

## 🎯 Kotlin

<!-- KOTLIN_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Kotlin+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Kotlin+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Kotlin+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Kotlin+board)
<!-- KOTLIN_END -->

---

## 🐘 PHP

<!-- PHP_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+PHP+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Reset&body=Reset+PHP+board)
<!-- PHP_END -->

---

## 💎 Ruby

<!-- RUBY_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Ruby+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Ruby+board)
<!-- RUBY_END -->

---

## 🔵 C#

<!-- CSHARP_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%23+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%23+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%23+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Reset&body=Reset+C%23+board)
<!-- CSHARP_END -->

---

## ⚙️ C

<!-- C_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Reset&body=Reset+C+board)
<!-- C_END -->

---

## 🔩 C++

<!-- CPPLUS_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%2B%2B+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%2B%2B+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%2B%2B+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Reset&body=Reset+C%2B%2B+board)
<!-- CPPLUS_END -->

---

## 🔴 Scala

<!-- SCALA_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Scala+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Scala+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Scala+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Scala+board)
<!-- SCALA_END -->

---

## 🐦 Swift

<!-- SWIFT_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Swift+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Swift+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Swift+board) |

Turn: ❌ **X** is next

[🔄 Reset Board](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Reset&body=Reset+Swift+board)
<!-- SWIFT_END -->

---

## Language × GitHub Actions Support

| Language | Runtime | Actions Setup |
|----------|---------|---------------|
| Python | 3.12 | `setup-python@v5` |
| JavaScript | Node 20 | `setup-node@v4` |
| TypeScript | Node 20 + ts-node | `setup-node@v4` |
| Go | 1.22 | `setup-go@v5` |
| Rust | stable | `dtolnay/rust-toolchain` |
| Java | Temurin 21 | `setup-java@v4` |
| Kotlin | JVM (via java) | `setup-java@v4` |
| PHP | 8.3 | `shivammathur/setup-php@v2` |
| Ruby | 3.3 | `ruby/setup-ruby@v1` |
| C# | .NET 8 | `setup-dotnet@v4` |
| C | gcc (pre-installed) | — |
| C++ | g++ (pre-installed) | — |
| Scala | 3.x via java | `setup-java@v4` |
| Swift | 5.10 | `swift-actions/setup-swift@v2` |

---

*Built with GitHub Actions. Each ➕ opens a pre-filled issue — submitting it triggers the workflow.*
