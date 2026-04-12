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
<!-- PYTHON_END -->

<details>
<summary>📄 Python implementation snippet</summary>

```python
import json, os, sys
sys.path.insert(0, '.')
from shared.board import load_state, save_state, check_winner, is_draw, CELL_TO_IDX

lang   = os.environ['LANG_KEY']   # 'python'
cell   = os.environ['CELL']       # e.g. 'B2'
action = os.environ['ACTION']     # 'put' | 'reset'
state  = load_state(lang)

if action == 'reset':
    state = {'board': [['','',''],['','',''],['','','']], 'turn':'X', 'winner':None, 'log':[]}
else:
    r, c = CELL_TO_IDX[cell]
    if not state['board'][r][c] and not state['winner']:
        state['board'][r][c] = state['turn']
        w = check_winner(state['board'])
        state['winner'] = w
        if not w and not is_draw(state['board']):
            state['turn'] = 'O' if state['turn'] == 'X' else 'X'
        state['log'].append({'player': state['turn'], 'cell': cell})

save_state(lang, state)
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
<!-- JAVASCRIPT_END -->

<details>
<summary>📄 JavaScript implementation snippet</summary>

```javascript
const fs = require('fs');
const CELL_TO_IDX = {
  A1:[0,0],A2:[0,1],A3:[0,2],
  B1:[1,0],B2:[1,1],B3:[1,2],
  C1:[2,0],C2:[2,1],C3:[2,2],
};
const WIN_LINES = [
  [[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
  [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
  [[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]],
];
const all = JSON.parse(fs.readFileSync('game_state.json'));
const lang = process.env.LANG_KEY;
const cell = process.env.CELL;
const action = process.env.ACTION;
const s = all[lang];
if (action === 'reset') {
  s.board = [['','',''],['','',''],['','','']];
  s.turn = 'X'; s.winner = null; s.log = [];
} else {
  const [r,c] = CELL_TO_IDX[cell];
  if (!s.board[r][c] && !s.winner) {
    s.board[r][c] = s.turn;
    const win = WIN_LINES.find(l => l.every(([r2,c2]) => s.board[r2][c2] === s.turn));
    if (win) { s.winner = s.turn; }
    else if (s.board.flat().every(Boolean)) { /* draw */ }
    else { s.turn = s.turn === 'X' ? 'O' : 'X'; }
    s.log.push({player: s.turn, cell});
  }
}
all[lang] = s;
fs.writeFileSync('game_state.json', JSON.stringify(all, null, 2));
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
<!-- TYPESCRIPT_END -->

<details>
<summary>📄 TypeScript implementation snippet</summary>

```typescript
import * as fs from 'fs';
type Board = string[][];
const CELL_TO_IDX: Record<string,[number,number]> = {
  A1:[0,0],A2:[0,1],A3:[0,2],
  B1:[1,0],B2:[1,1],B3:[1,2],
  C1:[2,0],C2:[2,1],C3:[2,2],
};
const all = JSON.parse(fs.readFileSync('game_state.json','utf8'));
const lang = process.env.LANG_KEY!;
const s = all[lang];
const action = process.env.ACTION!;
const cell = process.env.CELL!;
const checkWinner = (b: Board): string|null => {
  const lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  for (const [a,b2,c] of lines) {
    const flat = b.flat();
    if (flat[a] && flat[a]===flat[b2] && flat[a]===flat[c]) return flat[a];
  }
  return null;
};
if (action === 'reset') {
  s.board=[['','',''],['','',''],['','','']]; s.turn='X'; s.winner=null; s.log=[];
} else {
  const [r,c2] = CELL_TO_IDX[cell];
  if (!s.board[r][c2] && !s.winner) {
    s.board[r][c2] = s.turn;
    s.winner = checkWinner(s.board);
    if (!s.winner && s.board.flat().some((v:string)=>!v)) s.turn = s.turn==='X'?'O':'X';
    s.log.push({player:s.turn, cell});
  }
}
all[lang]=s;
fs.writeFileSync('game_state.json', JSON.stringify(all,null,2));
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
<!-- GO_END -->

<details>
<summary>📄 Go implementation snippet</summary>

```go
package main
import (
    "encoding/json"; "os"; "strings"
)
func checkWinner(b [3][3]string) string {
    lines := [][3][2]int{
        {{0,0},{0,1},{0,2}},{{1,0},{1,1},{1,2}},{{2,0},{2,1},{2,2}},
        {{0,0},{1,0},{2,0}},{{0,1},{1,1},{2,1}},{{0,2},{1,2},{2,2}},
        {{0,0},{1,1},{2,2}},{{0,2},{1,1},{2,0}},
    }
    for _, l := range lines {
        if b[l[0][0]][l[0][1]] != "" &&
           b[l[0][0]][l[0][1]] == b[l[1][0]][l[1][1]] &&
           b[l[1][0]][l[1][1]] == b[l[2][0]][l[2][1]] {
            return b[l[0][0]][l[0][1]]
        }
    }
    return ""
}
func main() {
    // reads game_state.json, applies move, saves back
    lang := os.Getenv("LANG_KEY") // "go"
    cell := strings.ToUpper(os.Getenv("CELL"))
    _ = lang; _ = cell
    // full impl in implementations/go/game.go
}
```

</details>

---

## 🦀 Rust

<!-- RUST_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Rust+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Rust+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Rust+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Rust+board) |

Turn: ❌ **X** is next
<!-- RUST_END -->

<details>
<summary>📄 Rust implementation snippet</summary>

```rust
use std::{env, fs};
use serde_json::{Value, json};
fn check_winner(board: &Vec<Vec<String>>) -> Option<String> {
    let lines = vec![
        [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)],
    ];
    for line in &lines {
        let vals: Vec<&str> = line.iter().map(|&(r,c)| board[r][c].as_str()).collect();
        if !vals[0].is_empty() && vals[0]==vals[1] && vals[1]==vals[2] {
            return Some(vals[0].to_string());
        }
    }
    None
}
fn main() {
    let lang = env::var("LANG_KEY").unwrap(); // "rust"
    let cell = env::var("CELL").unwrap();
    // reads game_state.json, applies move, saves back
    // full impl in implementations/rust/src/main.rs
}
```

</details>

---

## ☕ Java

<!-- JAVA_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Java+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Java+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Java+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Java+board) |

Turn: ❌ **X** is next
<!-- JAVA_END -->

<details>
<summary>📄 Java implementation snippet</summary>

```java
import org.json.*;
import java.nio.file.*;
import java.util.Map;
public class Game {
    static int[][] CELL_TO_IDX = {{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}};
    static String[] CELL_NAMES = {"A1","A2","A3","B1","B2","B3","C1","C2","C3"};
    public static void main(String[] args) throws Exception {
        String lang = System.getenv("LANG_KEY"); // "java"
        String cell = System.getenv("CELL");
        String action = System.getenv("ACTION");
        String raw = Files.readString(Path.of("game_state.json"));
        JSONObject all = new JSONObject(raw);
        JSONObject s = all.getJSONObject(lang);
        // apply move logic, save back to game_state.json
        // full impl in implementations/java/Game.java
    }
}
```

</details>

---

## 🎯 Kotlin

<!-- KOTLIN_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Kotlin+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Kotlin+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Kotlin+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Kotlin+board) |

Turn: ❌ **X** is next
<!-- KOTLIN_END -->

<details>
<summary>📄 Kotlin implementation snippet</summary>

```kotlin
import org.json.JSONObject
import java.io.File
val WIN_LINES = listOf(
    listOf(Pair(0,0),Pair(0,1),Pair(0,2)), listOf(Pair(1,0),Pair(1,1),Pair(1,2)),
    listOf(Pair(2,0),Pair(2,1),Pair(2,2)), listOf(Pair(0,0),Pair(1,0),Pair(2,0)),
    listOf(Pair(0,1),Pair(1,1),Pair(2,1)), listOf(Pair(0,2),Pair(1,2),Pair(2,2)),
    listOf(Pair(0,0),Pair(1,1),Pair(2,2)), listOf(Pair(0,2),Pair(1,1),Pair(2,0)),
)
fun checkWinner(board: List<List<String>>): String? {
    for (line in WIN_LINES) {
        val vals = line.map { (r,c) -> board[r][c] }
        if (vals[0].isNotEmpty() && vals[0]==vals[1] && vals[1]==vals[2]) return vals[0]
    }
    return null
}
// full impl in implementations/kotlin/Game.kt
```

</details>

---

## 🐘 PHP

<!-- PHP_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+PHP+board) |

Turn: ❌ **X** is next
<!-- PHP_END -->

<details>
<summary>📄 PHP implementation snippet</summary>

```php
<?php
$cellMap = [
    'A1'=>[0,0],'A2'=>[0,1],'A3'=>[0,2],
    'B1'=>[1,0],'B2'=>[1,1],'B3'=>[1,2],
    'C1'=>[2,0],'C2'=>[2,1],'C3'=>[2,2],
];
$lang   = getenv('LANG_KEY');  // 'php'
$cell   = strtoupper(getenv('CELL'));
$action = getenv('ACTION');
$all    = json_decode(file_get_contents('game_state.json'), true);
$s      = &$all[$lang];
if ($action === 'reset') {
    $s = ['board'=>[['','',''],['','',''],['','','']],'turn'=>'X','winner'=>null,'log'=>[]];
} else {
    [$r,$c] = $cellMap[$cell];
    if (!$s['board'][$r][$c] && !$s['winner']) {
        $s['board'][$r][$c] = $s['turn'];
        // check winner, update turn...
    }
}
file_put_contents('game_state.json', json_encode($all, JSON_PRETTY_PRINT));
// full impl in implementations/php/game.php
```

</details>

---

## 💎 Ruby

<!-- RUBY_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Ruby+board) |

Turn: ❌ **X** is next
<!-- RUBY_END -->

<details>
<summary>📄 Ruby implementation snippet</summary>

```ruby
require 'json'
CELL_TO_IDX = {
  'A1'=>[0,0],'A2'=>[0,1],'A3'=>[0,2],
  'B1'=>[1,0],'B2'=>[1,1],'B3'=>[1,2],
  'C1'=>[2,0],'C2'=>[2,1],'C3'=>[2,2],
}
WIN_LINES = [
  [[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
  [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
  [[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]
]
lang   = ENV['LANG_KEY']  # 'ruby'
cell   = ENV['CELL'].upcase
action = ENV['ACTION']
all    = JSON.parse(File.read('game_state.json'))
s      = all[lang]
if action == 'reset'
  s.merge!('board'=>[['','',''],['','',''],['','','']],'turn'=>'X','winner'=>nil,'log'=>[])
else
  r, c = CELL_TO_IDX[cell]
  unless s['board'][r][c] || s['winner']
    s['board'][r][c] = s['turn']
    # check winner, update turn...
  end
end
File.write('game_state.json', JSON.pretty_generate(all))
# full impl in implementations/ruby/game.rb
```

</details>

---

## 🔵 C\#

<!-- CSHARP_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%23+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%23+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%23+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%23+board) |

Turn: ❌ **X** is next
<!-- CSHARP_END -->

<details>
<summary>📄 C# implementation snippet</summary>

```csharp
using System.Text.Json;
var lang   = Environment.GetEnvironmentVariable("LANG_KEY")!; // "csharp"
var cell   = Environment.GetEnvironmentVariable("CELL")!;
var action = Environment.GetEnvironmentVariable("ACTION")!;
var raw    = File.ReadAllText("game_state.json");
var all    = JsonSerializer.Deserialize<Dictionary<string,GameState>>(raw)!;
var s      = all[lang];
if (action == "reset") {
    s.Board = new string[3,3]; s.Turn = "X"; s.Winner = null; s.Log.Clear();
} else {
    var (r,c) = CellToIdx(cell);
    if (s.Board[r,c] == "" && s.Winner == null) {
        s.Board[r,c] = s.Turn;
        s.Winner = CheckWinner(s.Board);
        if (s.Winner == null) s.Turn = s.Turn == "X" ? "O" : "X";
    }
}
// full impl in implementations/csharp/Game.cs
```

</details>

---

## ⚙️ C

<!-- C_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+board) |

Turn: ❌ **X** is next
<!-- C_END -->

<details>
<summary>📄 C implementation snippet</summary>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Uses cJSON for JSON parsing
const int WIN_LINES[8][3][2] = {
    {{0,0},{0,1},{0,2}},{{1,0},{1,1},{1,2}},{{2,0},{2,1},{2,2}},
    {{0,0},{1,0},{2,0}},{{0,1},{1,1},{2,1}},{{0,2},{1,2},{2,2}},
    {{0,0},{1,1},{2,2}},{{0,2},{1,1},{2,0}},
};
int main() {
    const char* lang = getenv("LANG_KEY");  // "c"
    const char* cell = getenv("CELL");
    // parse game_state.json, apply move, write back
    // full impl in implementations/c/game.c
    return 0;
}
```

</details>

---

## 🔩 C++

<!-- CPP_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%2B%2B+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%2B%2B+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%2B%2B+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%2B%2B+board) |

Turn: ❌ **X** is next
<!-- CPP_END -->

<details>
<summary>📄 C++ implementation snippet</summary>

```cpp
#include <iostream>
#include <fstream>
#include <map>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
const std::map<std::string,std::pair<int,int>> CELL_TO_IDX = {
    {"A1",{0,0}},{"A2",{0,1}},{"A3",{0,2}},
    {"B1",{1,0}},{"B2",{1,1}},{"B3",{1,2}},
    {"C1",{2,0}},{"C2",{2,1}},{"C3",{2,2}},
};
int main() {
    std::string lang = std::getenv("LANG_KEY"); // "cpp"
    std::string cell = std::getenv("CELL");
    // parse game_state.json, apply move, write back
    // full impl in implementations/cpp/game.cpp
    return 0;
}
```

</details>

---

## 🔴 Scala

<!-- SCALA_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Scala+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Scala+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Scala+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Scala+board) |

Turn: ❌ **X** is next
<!-- SCALA_END -->

<details>
<summary>📄 Scala implementation snippet</summary>

```scala
import scala.io.Source
import play.api.libs.json._
val cellToIdx = Map(
  "A1"->(0,0),"A2"->(0,1),"A3"->(0,2),
  "B1"->(1,0),"B2"->(1,1),"B3"->(1,2),
  "C1"->(2,0),"C2"->(2,1),"C3"->(2,2)
)
val lang   = sys.env("LANG_KEY")  // "scala"
val cell   = sys.env("CELL").toUpperCase
val action = sys.env("ACTION")
// parse game_state.json, apply move, write back
// full impl in implementations/scala/Game.scala
```

</details>

---

## 🐦 Swift

<!-- SWIFT_START -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| **A** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Swift+board) |
| **B** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Swift+board) |
| **C** | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Swift+board) | [➕](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Swift+board) |

Turn: ❌ **X** is next
<!-- SWIFT_END -->

<details>
<summary>📄 Swift implementation snippet</summary>

```swift
import Foundation
let cellToIdx: [String: (Int, Int)] = [
    "A1":(0,0),"A2":(0,1),"A3":(0,2),
    "B1":(1,0),"B2":(1,1),"B3":(1,2),
    "C1":(2,0),"C2":(2,1),"C3":(2,2),
]
let lang   = ProcessInfo.processInfo.environment["LANG_KEY"]!  // "swift"
let cell   = ProcessInfo.processInfo.environment["CELL"]!.uppercased()
let action = ProcessInfo.processInfo.environment["ACTION"]!
// parse game_state.json, apply move, write back
// full impl in implementations/swift/game.swift
```

</details>

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
| Scala | 3.x via Coursier | `setup-java@v4` |
| Swift | 5.10 | `swift-actions/setup-swift@v2` |

---

*Built with GitHub Actions. Each ➕ opens a pre-filled issue — submitting it triggers the workflow.*
