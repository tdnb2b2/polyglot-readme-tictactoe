# Polyglot Tic-Tac-Toe

This is a technical demo repository showing Tic-Tac-Toe implemented in 14 different languages. Each board is independently playable via GitHub Issues.

## C
<!-- BOARD_C_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (C)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `C: Tic-Tac-Toe: Put B1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (C)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void write_state(char b[3][3], char* turn, char* winner) {
    FILE *f = fopen("current_state.json", "w");
    fprintf(f, "{
  \"board\": [
");
    for(int i=0; i<3; i++) {
        fprintf(f, "    [\"%s\", \"%s\", \"%s\"]%s
", (b[i][0]? (char[]){b[i][0],0} : ""), (b[i][1]? (char[]){b[i][1],0} : ""), (b[i][2]? (char[]){b[i][2],0} : ""), (i==2?"":","));
    }
    fprintf(f, "  ],
  \"turn\": \"%s\",
  \"winner\": %s,
  \"log\": []
}", turn, winner? (strcmp(winner,"null")==0?"null": (char[]){'\"',winner[0],winner[1]?(winner[1]=='r'?'d':winner[0]):0,'\"',0} ) : "null");
    // Simplified winner string handling for C
    fclose(f);
}

int main() {
    char b[3][3] = {0};
    char turn[2] = "X";
    char* action = getenv("ACTION");
    char* cell = getenv("CELL");

    FILE *f = fopen("current_state.json", "r");
    if(f) {
        char line[256];
        int r=0;
        while(fgets(line, sizeof(line), f)) {
            if(strstr(line, "[") && !strstr(line, "board")) {
                // very simple parse
                if(strstr(line, "\"X\"")) b[r][0]='X'; else if(strstr(line, "\"O\"")) b[r][0]='O';
                char* p = strchr(line, ','); if(p) { if(strstr(p, "\"X\"")) b[r][1]='X'; else if(strstr(p, "\"O\"")) b[r][1]='O'; p=strchr(p+1,','); if(p) { if(strstr(p, "\"X\"")) b[r][2]='X'; else if(strstr(p, "\"O\"")) b[r][2]='O'; } }
                r++;
            }
            if(strstr(line, "\"turn\": \"O\"")) strcpy(turn, "O");
        }
        fclose(f);
    }

    if(action && strcmp(action, "reset")==0) {
        write_state((char[3][3]){{0,0,0},{0,0,0},{0,0,0}}, "X", "null");
    } else if(cell && strlen(cell)>=2) {
        int r = cell[1]-'1', c = cell[0]-'A';
        if(r>=0 && r<3 && c>=0 && c<3 && b[r][c]==0) {
            b[r][c] = turn[0];
            int win = 0;
            int lns[8][6] = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
            for(int i=0; i<8; i++) {
                if(b[lns[i][0]][lns[i][1]] && b[lns[i][0]][lns[i][1]]==b[lns[i][2]][lns[i][3]] && b[lns[i][2]][lns[i][3]]==b[lns[i][4]][lns[i][5]]) { win=1; break; }
            }
            if(win) write_state(b, turn, turn);
            else {
                int full=1; for(int i=0; i<3; i++) for(int j=0; j<3; j++) if(b[i][j]==0) full=0;
                if(full) write_state(b, turn, "\"draw\"");
                else write_state(b, (turn[0]=='X'?"O":"X"), "null");
            }
        }
    }
    return 0;
}

```
</details>

<!-- BOARD_C_END -->

## C++
<!-- BOARD_CPP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+++board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+++board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+++board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Cpp)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `C++: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (C++)
```cpp
// Source code for cpp not found at implementations/cpp/tictactoe.cpp
```
</details>

<!-- BOARD_CPP_END -->

## C#
<!-- BOARD_CSHARP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%23+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%23+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%23+board) | **3** |
|   | A | B | C |   |

Turn: ❌ X is next

<!-- BOARD_CSHARP_END -->

## Go
<!-- BOARD_GO_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Go+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Go+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Go+board) | **3** |
|   | A | B | C |   |

Turn: ⭕ O is next

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Go: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Go)
```(go)
package main
import (
    "encoding/json"; "os"; "strings"
)
type GameState struct {
    Board [][]string `json:"board"`
    Turn string `json:"turn"`
    Winner *string `json:"winner"`
    Log []interface{} `json:"log"`
}
func main() {
    b, _ := os.ReadFile("current_state.json")
    var s GameState
    json.Unmarshal(b, &s)
    cell := strings.ToUpper(os.Getenv("CELL"))
    action := os.Getenv("ACTION")
    if action == "reset" {
        s.Board = [][]string{{"","",""},{"","",""},{"","",""}}
        s.Turn = "X"; s.Winner = nil; s.Log = []interface{}{}
    } else if cell != "" && s.Winner == nil {
        r, c := int(cell[1]-'1'), int(cell[0]-'A')
        if r>=0 && r<3 && c>=0 && c<3 && s.Board[r][c] == "" {
            s.Board[r][c] = s.Turn
            win := false
            lns := [][]int{{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2},{0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2},{0,0,1,1,2,2},{0,2,1,1,2,0}}
            for _, l := range lns {
                if s.Board[l[0]][l[1]] != "" && s.Board[l[0]][l[1]] == s.Board[l[2]][l[3]] && s.Board[l[2]][l[3]] == s.Board[l[4]][l[5]] { win = true }
            }
            if win { s.Winner = &s.Turn } else {
                full := true
                for _, row := range s.Board { for _, v := range row { if v == "" { full = false } } }
                if full { d := "draw"; s.Winner = &d } else { if s.Turn == "X" { s.Turn = "O" } else { s.Turn = "X" } }
            }
        }
    }
    out, _ := json.MarshalIndent(s, "", "  ")
    os.WriteFile("current_state.json", out, 0644)
}

```
</details>

<!-- BOARD_GO_END -->

## Java
<!-- BOARD_JAVA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Java+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Java+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Java+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Java)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Java: Tic-Tac-Toe: Reset`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Java)
```java
// Source code for java not found at implementations/java/tictactoe.java
```
</details>

<!-- BOARD_JAVA_END -->

## JavaScript
<!-- BOARD_JAVASCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+JavaScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+JavaScript+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+JavaScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+JavaScript+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Javascript)**

Recent moves: X B2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `JavaScript: Tic-Tac-Toe: Put B2`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (JavaScript)
```javascript
const fs = require('fs');
const s = JSON.parse(fs.readFileSync('current_state.json'));
const cell = (process.env.CELL || "").toUpperCase();
const action = process.env.ACTION || "put";

if (action === 'reset') {
    s.board = [["","",""],["","",""],["","",""]];
    s.turn = "X"; s.winner = null; s.log = [];
} else if (cell && !s.winner) {
    const r = parseInt(cell[1]) - 1, c = cell.charCodeAt(0) - 65;
    if (r >= 0 && r < 3 && c >= 0 && c < 3 && s.board[r][c] === "") {
        s.board[r][c] = s.turn;
        s.log.push({player: s.turn, cell});
        const lines = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]], [[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]];
        let win = lines.find(l => l.every(([r2,c2]) => s.board[r2][c2] === s.turn));
        if (win) s.winner = s.turn;
        else if (s.board.flat().every(v => v !== "")) s.winner = "draw";
        else s.turn = s.turn === "X" ? "O" : "X";
    }
}
fs.writeFileSync('current_state.json', JSON.stringify(s, null, 2));

```
</details>

<!-- BOARD_JAVASCRIPT_END -->

## Kotlin
<!-- BOARD_KOTLIN_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Kotlin+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Kotlin+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Kotlin+board) | **3** |
|   | A | B | C |   |

Turn: ❌ X is next

<!-- BOARD_KOTLIN_END -->

## PHP
<!-- BOARD_PHP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+PHP+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+PHP+board) | **3** |
|   | A | B | C |   |

Turn: ❌ X is next

<!-- BOARD_PHP_END -->

## Python
<!-- BOARD_PYTHON_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Python+board) | **1** |
| **2** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Python+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Python+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Python)**

Recent moves: X A2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Python: Tic-Tac-Toe: Put A2`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Python)
```python
import json, os

with open('current_state.json', 'r') as f:
    s = json.load(f)

cell = os.environ.get('CELL', '').upper()
action = os.environ.get('ACTION', 'put')

def check_winner(b):
    lines = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    for l in lines:
        v = [b[r][c] for r, c in l]
        if v[0] != '' and all(x == v[0] for x in v): return v[0]
    return None

if action == 'reset':
    s = {"board": [["","",""],["","",""],["","",""]], "turn": "X", "winner": None, "log": []}
elif cell and not s['winner']:
    r, c = int(cell[1]) - 1, ord(cell[0]) - ord('A')
    if 0 <= r < 3 and 0 <= c < 3 and s['board'][r][c] == '':
        s['board'][r][c] = s['turn']
        s['log'].append({"player": s['turn'], "cell": cell})
        win = check_winner(s['board'])
        if win: s['winner'] = win
        elif all(all(x != '' for x in row) for row in s['board']): s['winner'] = 'draw'
        else: s['turn'] = 'O' if s['turn'] == 'X' else 'X'

with open('current_state.json', 'w') as f:
    json.dump(s, f, indent=2)

```
</details>

<!-- BOARD_PYTHON_END -->

## Ruby
<!-- BOARD_RUBY_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Ruby+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Ruby+board) | **3** |
|   | A | B | C |   |

Turn: ⭕ O is next

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Ruby: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Ruby)
```(ruby)
require 'json'
s = JSON.parse(File.read('current_state.json'))
cell = (ENV['CELL'] || "").upcase
action = ENV['ACTION'] || "put"

if action == 'reset'
  s = {"board"=>[["","",""],["","",""],["","",""]], "turn"=>"X", "winner"=>nil, "log"=>[]}
elsif !cell.empty? && !s['winner']
  r, c = cell[1].to_i - 1, cell[0].ord - 65
  if r>=0 && r<3 && c>=0 && c<3 && s['board'][r][c] == ""
    s['board'][r][c] = s['turn']
    lns = [[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2],[0,0,1,1,2,2],[0,2,1,1,2,0]]
    win = lns.any? { |l| !s['board'][l[0]][l[1]].empty? && s['board'][l[0]][l[1]] == s['board'][l[2]][l[3]] && s['board'][l[2]][l[3]] == s['board'][l[4]][l[5]] }
    if win then s['winner'] = s['turn']
    elsif s['board'].flatten.none?(&:empty?) then s['winner'] = 'draw'
    else s['turn'] = (s['turn'] == "X" ? "O" : "X")
    end
  end
end
File.write('current_state.json', JSON.pretty_generate(s))

```
</details>

<!-- BOARD_RUBY_END -->

## Rust
<!-- BOARD_RUST_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Rust+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Rust+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Rust+board) | **3** |
|   | A | B | C |   |

Turn: ❌ X is next

<!-- BOARD_RUST_END -->

## Scala
<!-- BOARD_SCALA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Scala+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Scala+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Scala+board) | **3** |
|   | A | B | C |   |

Turn: ❌ X is next

<!-- BOARD_SCALA_END -->

## Swift
<!-- BOARD_SWIFT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Swift+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Swift+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Swift+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Swift)**

Recent moves: X A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Swift: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Swift)
```swift
// Source code for swift not found at implementations/swift/tictactoe.swift
```
</details>

<!-- BOARD_SWIFT_END -->

## TypeScript
<!-- BOARD_TYPESCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+TypeScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+TypeScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+TypeScript+board) | **3** |
|   | A | B | C |   |

Turn: ❌ X is next

<!-- BOARD_TYPESCRIPT_END -->
