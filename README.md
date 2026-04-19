# Polyglot Tic-Tac-Toe

This is a technical demo repository showing Tic-Tac-Toe implemented in 14 different languages. Each board is independently playable via GitHub Issues.

## C
<!-- BOARD_C_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (C)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `C: Tic-Tac-Toe: Put A1`
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
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C#+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C#+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C#+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C#+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C#+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C#+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C#+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C#%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C#+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Csharp)**

Recent moves: X B2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `C#: Tic-Tac-Toe: Put B2`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (C#)
```cs
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Linq;

public class GameState {
    public List<List<string>> board { get; set; }
    public string turn { get; set; }
    public string winner { get; set; }
    public List<Move> log { get; set; }
}
public class Move {
    public string player { get; set; }
    public string cell { get; set; }
}

class Program {
    static void Main() {
        var json = File.ReadAllText("current_state.json");
        var s = JsonSerializer.Deserialize<GameState>(json);
        var cell = Environment.GetEnvironmentVariable("CELL")?.ToUpper();
        var action = Environment.GetEnvironmentVariable("ACTION");

        if (action == "reset") {
            s.board = new List<List<string>>{ new(){"","",""}, new(){"","",""}, new(){"","",""} };
            s.turn = "X"; s.winner = null; s.log = new();
        } else if (!string.IsNullOrEmpty(cell) && s.winner == null) {
            int r = cell[1] - '1', c = cell[0] - 'A';
            if (r>=0 && r<3 && c>=0 && c<3 && string.IsNullOrEmpty(s.board[r][c])) {
                s.board[r][c] = s.turn;
                s.log.Add(new Move { player = s.turn, cell = cell });
                if (Check(s.board)) s.winner = s.turn;
                else if (s.board.All(row => row.All(v => !string.IsNullOrEmpty(v)))) s.winner = "draw";
                else s.turn = s.turn == "X" ? "O" : "X";
            }
        }
        File.WriteAllText("current_state.json", JsonSerializer.Serialize(s, new JsonSerializerOptions { WriteIndented = true }));
    }
    static bool Check(List<List<string>> b) {
        int[,] lns = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
        for(int i=0; i<8; i++) if(!string.IsNullOrEmpty(b[lns[i,0]][lns[i,1]]) && b[lns[i,0]][lns[i,1]] == b[lns[i,2]][lns[i,3]] && b[lns[i,2]][lns[i,3]] == b[lns[i,4]][lns[i,5]]) return true;
        return false;
    }
}

```
</details>

<!-- BOARD_CSHARP_END -->

## Go
<!-- BOARD_GO_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Go+board) | **1** |
| **2** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Go+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Go+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Go)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Go: Tic-Tac-Toe: Put A2`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Go)
```go
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
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Java+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Java+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Java+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Java)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Java: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Java)
```java
import java.nio.file.*;
import java.util.regex.*;

public class Game {
    public static void main(String[] args) throws Exception {
        String path = "current_state.json";
        String content = Files.readString(Path.of(path));
        String cell = System.getenv("CELL");
        String action = System.getenv("ACTION");
        
        if ("reset".equals(action)) {
            Files.writeString(Path.of(path), "{
  \"board\": [[\"\",\"\",\"\"],[\"\",\"\",\"\"],[\"\",\"\",\"\"]],
  \"turn\": \"X\",
  \"winner\": null,
  \"log\": []
}");
            return;
        }

        if (cell == null || cell.length() < 2) return;
        cell = cell.toUpperCase();

        // Extract values from JSON (Minimalist approach)
        String winner = getJsonValue(content, "winner");
        if (!"null".equals(winner)) return;

        String turn = getJsonValue(content, "turn");
        String[][] board = new String[3][3];
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) board[i][j] = "";
        Pattern p = Pattern.compile("\[\"(.*?)\",\"(.*?)\",\"(.*?)\"\]");
        Matcher m = p.matcher(content);
        for (int i = 0; i < 3 && m.find(); i++) {
            board[i][0] = m.group(1);
            board[i][1] = m.group(2);
            board[i][2] = m.group(3);
        }

        // Correct Mapping: r is row (1-3), c is col (A-C)
        int r = cell.charAt(1) - '1';
        int c = cell.charAt(0) - 'A';

        if (r >= 0 && r < 3 && c >= 0 && c < 3 && board[r][c].isEmpty()) {
            board[r][c] = turn;
            
            String win = checkWinner(board);
            String nextTurn = turn.equals("X") ? "O" : "X";
            boolean draw = isDraw(board);

            // Reconstruct JSON
            StringBuilder sb = new StringBuilder();
            sb.append("{
  \"board\": [
");
            for (int i = 0; i < 3; i++) {
                sb.append("    [\"").append(board[i][0]).append("\",\"").append(board[i][1]).append("\",\"").append(board[i][2]).append("\"]");
                if (i < 2) sb.append(",");
                sb.append("
");
            }
            sb.append("  ],
  \"turn\": \"").append(nextTurn).append("\",
");
            sb.append("  \"winner\": ").append(win != null ? "\"" + win + "\"" : (draw ? "\"draw\"" : "null")).append(",
");
            sb.append("  \"log\": []
}"); // Simplified log for Java
            Files.writeString(Path.of(path), sb.toString());
        }
    }

    static String getJsonValue(String json, String key) {
        Pattern p = Pattern.compile("\"" + key + "\":\s*\"?(.*?)\"?(?:,|\n|\})");
        Matcher m = p.matcher(json);
        if (m.find()) return m.group(1).trim();
        return "null";
    }

    static String checkWinner(String[][] b) {
        int[][] lns = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
        for (int[] l : lns) {
            if (!b[l[0]][l[1]].isEmpty() && b[l[0]][l[1]].equals(b[l[2]][l[3]]) && b[l[2]][l[3]].equals(b[l[4]][l[5]])) return b[l[0]][l[1]];
        }
        return null;
    }

    static boolean isDraw(String[][] b) {
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) if (b[i][j].isEmpty()) return false;
        return true;
    }
}

```
</details>

<!-- BOARD_JAVA_END -->

## JavaScript
<!-- BOARD_JAVASCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+JavaScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+JavaScript+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+JavaScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+JavaScript+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Javascript)**

Recent moves: X B2 -> O A1

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
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+PHP+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Php)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `PHP: Tic-Tac-Toe: Put B2`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (PHP)
```php
<?php
$s = json_decode(file_get_contents('current_state.json'), true);
$cell = strtoupper(getenv('CELL') ?: "");
$action = getenv('ACTION') ?: "put";

if ($action === 'reset') {
    $s = ['board'=>[['','',''],['','',''],['','','']], 'turn'=>'X', 'winner'=>null, 'log'=>[]];
} elseif ($cell && !$s['winner']) {
    $r = (int)$cell[1] - 1; $c = ord($cell[0]) - 65;
    if ($r>=0 && $r<3 && $c>=0 && $c<3 && $s['board'][$r][$c] === "") {
        $s['board'][$r][$c] = $s['turn'];
        $win = false;
        $lns = [[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2],[0,0,1,1,2,2],[0,2,1,1,2,0]];
        foreach($lns as $l) {
            if ($s['board'][$l[0]][$l[1]] && $s['board'][$l[0]][$l[1]] === $s['board'][$l[2]][$l[3]] && $s['board'][$l[2]][$l[3]] === $s['board'][$l[4]][$l[5]]) $win = true;
        }
        if ($win) $s['winner'] = $s['turn'];
        else {
            $full = true; foreach($s['board'] as $row) foreach($row as $v) if($v === "") $full = false;
            if ($full) $s['winner'] = 'draw';
            else $s['turn'] = $s['turn'] === "X" ? "O" : "X";
        }
    }
}
file_put_contents('current_state.json', json_encode($s, JSON_PRETTY_PRINT));

```
</details>

<!-- BOARD_PHP_END -->

## Python
<!-- BOARD_PYTHON_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Python+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Python+board) | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Python+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Python+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Python)**

Recent moves: X A1 -> O B2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Python: Tic-Tac-Toe: Put B2`
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
| **2** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Ruby+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Ruby)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Ruby: Tic-Tac-Toe: Put A2`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Ruby)
```ruby
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
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Rust+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Rust+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Rust+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Rust)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Rust: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Success
```

### 💻 Implementation Code (Rust)
```rust
use serde::{Deserialize, Serialize};
use std::{env, fs};

#[derive(Serialize, Deserialize)]
struct GameState {
    board: Vec<Vec<String>>,
    turn: String,
    winner: Option<String>,
    log: Vec<serde_json::Value>,
}

fn main() {
    let data = fs::read_to_string("current_state.json").unwrap();
    let mut s: GameState = serde_json::from_str(&data).unwrap();
    let cell = env::var("CELL").unwrap_or_default().to_uppercase();
    let action = env::var("ACTION").unwrap_or_default();

    if action == "reset" {
        s.board = vec![vec!["".to_string(); 3]; 3];
        s.turn = "X".to_string(); s.winner = None; s.log = vec![];
    } else if !cell.is_empty() && s.winner.is_none() {
        let r = (cell.chars().nth(1).unwrap() as u8 - b'1') as usize;
        let c = (cell.chars().next().unwrap() as u8 - b'A') as usize;
        if r < 3 && c < 3 && s.board[r][c].is_empty() {
            s.board[r][c] = s.turn.clone();
            let lns = vec![
                (0,0,0,1,0,2),(1,0,1,1,1,2),(2,0,2,1,2,2),
                (0,0,1,0,2,0),(0,1,1,1,2,1),(0,2,1,2,2,2),
                (0,0,1,1,2,2),(0,2,1,1,2,0)
            ];
            let win = lns.iter().any(|&(r1,c1,r2,c2,r3,c3)| 
                !s.board[r1][c1].is_empty() && s.board[r1][c1] == s.board[r2][c2] && s.board[r2][c2] == s.board[r3][c3]
            );
            if win { s.winner = Some(s.turn.clone()); }
            else if s.board.iter().all(|row| row.iter().all(|v| !v.is_empty())) { s.winner = Some("draw".to_string()); }
            else { s.turn = if s.turn == "X" { "O".to_string() } else { "X".to_string() }; }
        }
    }
    fs::write("current_state.json", serde_json::to_string_pretty(&s).unwrap()).unwrap();
}

```
</details>

<!-- BOARD_RUST_END -->

## Scala
<!-- BOARD_SCALA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Scala+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Scala+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Scala+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Scala)**

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Scala: Tic-Tac-Toe: Put A1`
- **Output (Information given)**: 
```text
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-parent/1.5.27/logback-parent-1.5.27.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/interface/1.0.28/interface-1.0.28.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/interface/1.0.28/interface-1.0.28.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/interface/1.0.28/interface-1.0.28.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/interface/1.0.28/interface-1.0.28.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/sonatype/oss/oss-parent/7/oss-parent-7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/ow2/1.5.1/ow2-1.5.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/sonatype/oss/oss-parent/7/oss-parent-7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/ow2/1.5.1/ow2-1.5.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-parent/2.17.2/zipkin-reporter-parent-2.17.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave-parent/5.18.1/brave-parent-5.18.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j/2.23.0/log4j-2.23.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-bom/2.23.0/log4j-bom-2.23.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/logging-parent/10.6.0/logging-parent-10.6.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/31/apache-31.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/31/apache-31.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/31/apache-31.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/31/apache-31.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/apache/31/apache-31.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/apache/31/apache-31.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/fabric8/kubernetes-client-bom/5.12.4/kubernetes-client-bom-5.12.4.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/springframework/spring-framework-bom/5.3.32/spring-framework-bom-5.3.32.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/codehaus/groovy/groovy-bom/3.0.20/groovy-bom-3.0.20.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakarta.jakartaee-bom/9.1.0/jakarta.jakartaee-bom-9.1.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/jetty/jetty-bom/9.4.54.v20240208/jetty-bom-9.4.54.v20240208.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/netty/netty-bom/4.1.107.Final/netty-bom-4.1.107.Final.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/jakarta/platform/jakartaee-api-parent/9.1.0/jakartaee-api-parent-9.1.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/oss-parent/56/oss-parent-56.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/oss-parent/56/oss-parent-56.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/oss-parent/56/oss-parent-56.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/fasterxml/oss-parent/56/oss-parent-56.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/fasterxml/oss-parent/56/oss-parent-56.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/fasterxml/oss-parent/56/oss-parent-56.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/81/commons-parent-81.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/81/commons-parent-81.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/81/commons-parent-81.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/81/commons-parent-81.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/81/commons-parent-81.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/81/commons-parent-81.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/81/commons-parent-81.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson-parent/2.13.1/gson-parent-2.13.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin-parent/2.27.0/zipkin-parent-2.27.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/81/commons-parent-81.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/73/commons-parent-73.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/73/commons-parent-73.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/73/commons-parent-73.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/commons/commons-parent/73/commons-parent-73.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/73/commons-parent-73.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/73/commons-parent-73.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/73/commons-parent-73.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-parent/73/commons-parent-73.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/33/apache-33.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/33/apache-33.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/33/apache-33.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/apache/apache/33/apache-33.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/apache/33/apache-33.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/apache/33/apache-33.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/java-parent-pom/1.1.28/java-parent-pom-1.1.28.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_parent/2.38.0/error_prone_parent-2.38.0.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/net/openhft/root-parent-pom/1.2.12/root-parent-pom-1.2.12.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/openhft/root-parent-pom/1.2.12/root-parent-pom-1.2.12.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/net/openhft/root-parent-pom/1.2.12/root-parent-pom-1.2.12.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/net/openhft/root-parent-pom/1.2.12/root-parent-pom-1.2.12.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/root-parent-pom/1.2.12/root-parent-pom-1.2.12.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/root-parent-pom/1.2.12/root-parent-pom-1.2.12.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-parent/3.27.1/jline-parent-3.27.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-parent/3.27.1/jline-parent-3.27.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-parent/3.27.1/jline-parent-3.27.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/jline/jline-parent/3.27.1/jline-parent-3.27.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-parent/3.27.1/jline-parent-3.27.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-parent/3.27.1/jline-parent-3.27.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom.sha1
Downloading https://central.sonatype.com/repository/maven-snapshots/com/typesafe/config/1.4.2/config-1.4.2.pom
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/typesafe/config/1.4.2/config-1.4.2.pom
Downloading https://central.sonatype.com/repository/maven-snapshots/com/typesafe/config/1.4.2/config-1.4.2.pom.sha1
Failed to download https://central.sonatype.com/repository/maven-snapshots/com/typesafe/config/1.4.2/config-1.4.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.pom
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.pom
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.pom.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.pom.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.jar
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories-jni/0.1.2/directories-jni-0.1.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-java_2.12/3.2.0/monix-java_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc_2.12/1.12.0/zinc_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.jar
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-interface/1.11.7/util-interface-1.11.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-core_2.12/0.9.3/gigahorse-core_2.12-0.9.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/errorprone/error_prone_annotations/2.38.0/error_prone_annotations-2.38.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/io_2.12/1.10.5/io_2.12-1.10.5.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/zipkin2/zipkin/2.27.0/zipkin-2.27.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-shared_2.12/2.0.19/bloop-shared_2.12-2.0.19.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-compile-core_2.12/1.12.0/zinc-compile-core_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/mwiede/jsch/2.27.5/jsch-2.27.5.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-tail_2.12/3.2.0/monix-tail_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/config/1.4.2/config-1.4.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-backend_2.12/2.0.19/bloop-backend_2.12-2.0.19.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-core_2.12/1.12.0/librarymanagement-core_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-effect_2.12/2.1.3/cats-effect_2.12-2.1.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jctools/jctools-core/2.1.2/jctools-core-2.1.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/fansi_2.12/0.5.1/fansi_2.12-0.5.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-core_2.12/0.10.1/sjson-new-core_2.12-0.10.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-apiinfo_2.12/1.12.0/zinc-apiinfo_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-apache-httpclient5/0.9.3/shaded-apache-httpclient5-0.9.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/nailgun-server/1.0.7/nailgun-server-1.0.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/scribe_2.12/3.5.5/scribe_2.12-3.5.5.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-interface/1.12.0/compiler-interface-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/directory-watcher/0.8.0+6-f651bd93/directory-watcher-0.8.0+6-f651bd93.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-cache_2.12/1.11.7/util-cache_2.12-1.11.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal/3.27.1/jline-terminal-3.27.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/sourcecode_2.12/0.4.4/sourcecode_2.12-0.4.4.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/core-macros_2.12/1.11.7/core-macros_2.12-1.11.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/swoval/file-tree-views/2.1.12/file-tree-views-2.1.12.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-annotations_2.12/2.0.6/case-app-annotations_2.12-2.0.6.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix_2.12/3.2.0/monix_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/perfolation_2.12/1.2.8/perfolation_2.12-1.2.8.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter/2.17.2/zipkin-reporter-2.17.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-execution_2.12/3.2.0/monix-execution_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app-util_2.12/2.0.6/case-app-util_2.12-2.0.6.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-sender-urlconnection/2.17.2/zipkin-sender-urlconnection-2.17.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bsp4s_2.12/2.1.1/bsp4s_2.12-2.1.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-control_2.12/1.11.5/util-control_2.12-1.11.5.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/pprint_2.12/0.9.6/pprint_2.12-0.9.6.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-core/2.23.0/log4j-core-2.23.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-jawn-parser_2.12/1.3.2/shaded-jawn-parser_2.12-1.3.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist-core-assembly/1.12.0/zinc-persist-core-assembly-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-macros_2.12/2.13.3.2/jsoniter-scala-macros_2.12-2.13.3.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalaz/scalaz-core_2.12/7.3.8/scalaz-core_2.12-7.3.8.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-relation_2.12/1.11.5/util-relation_2.12-1.11.5.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-compiler/2.12.21/scala-compiler-2.12.21.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/google/code/gson/gson/2.13.1/gson-2.13.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-core_2.12/2.1.1/cats-core_2.12-2.1.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-position_2.12/1.11.7/util-position_2.12-1.11.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/sbinary_2.12/0.5.1/sbinary_2.12-0.5.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lihaoyi/unroll-annotation_2.12/0.1.12/unroll-annotation_2.12-0.1.12.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/openhft/zero-allocation-hashing/0.16/zero-allocation-hashing-0.16.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classpath_2.12/1.12.0/zinc-classpath_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/interface/1.0.28/interface-1.0.28.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-core_2.12/1.12.0/zinc-core_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/util-logging_2.12/1.11.7/util-logging_2.12-1.11.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-native/3.27.1/jline-native-3.27.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/lmax/disruptor/3.4.2/disruptor-3.4.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-persist_2.12/1.12.0/zinc-persist_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/jline/jline/2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18/jline-2.14.7-sbt-9a88bc413e2b34a4580c001c654d1a7f4f65bf18.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/brave/brave/5.18.1/brave-5.18.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-frontend_2.12/2.0.19/bloop-frontend_2.12-2.0.19.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/apache/logging/log4j/log4j-api/2.23.0/log4j-api-2.23.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/collections_2.12/1.11.7/collections_2.12-1.11.7.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.2/scala-parser-combinators_2.12-1.1.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/com-microsoft-java-debug-core/0.34.0+39/com-microsoft-java-debug-core-0.34.0+39.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/ivy/ivy/2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41/ivy-2.3.0-sbt-77cc781d727b367d3761f097d89f5a4762771d41.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-murmurhash_2.12/0.10.1/sjson-new-murmurhash_2.12-0.10.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/jniutils/windows-jni-utils/0.3.3/windows-jni-utils-0.3.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/compiler-bridge_2.12/1.12.0/compiler-bridge_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/plokhotnyuk/jsoniter-scala/jsoniter-scala-core_2.12/2.13.5.2/jsoniter-scala-core_2.12-2.13.5.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/outr/moduload_2.12/1.1.5/moduload_2.12-1.1.5.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/zeroturnaround/zt-zip/1.17/zt-zip-1.17.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/zinc-classfile_2.12/1.12.0/zinc-classfile_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/bloop-config_2.12/2.3.3/bloop-config_2.12-2.3.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/trees_2.12/4.13.8/trees_2.12-4.13.8.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/common_2.12/4.13.8/common_2.12-4.13.8.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/gigahorse-apache-http_2.12/0.9.3/gigahorse-apache-http_2.12-0.9.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/chuusai/shapeless_2.12/2.3.3/shapeless_2.12-2.3.3.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-core/1.5.27/logback-core-1.5.27.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-reflect/2.12.21/scala-reflect-2.12.21.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/fusesource/jansi/jansi/2.4.1/jansi-2.4.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/parsers_2.12/4.13.8/parsers_2.12-4.13.8.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-kernel_2.12/2.1.1/cats-kernel_2.12-2.1.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/typesafe/ssl-config-core_2.12/0.6.1/ssl-config-core_2.12-0.6.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-collection-compat_2.12/2.13.0/scala-collection-compat_2.12-2.13.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/cats-macros_2.12/2.1.1/cats-macros_2.12-2.1.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-eval_2.12/3.2.0/monix-eval_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/implicitbox_2.12/0.2.0/implicitbox_2.12-0.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/github/alexarchambault/bleep/jsonrpc4s_2.12/0.1.1/jsonrpc4s_2.12-0.1.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/sjson-new-scalajson_2.12/0.10.1/sjson-new-scalajson_2.12-0.10.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scalameta/io_2.12/4.13.8/io_2.12-4.13.8.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/net/java/dev/jna/jna/5.18.1/jna-5.18.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/scala-library/2.12.21/scala-library-2.12.21.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-reactive_2.12/3.2.0/monix-reactive_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/typelevel/macro-compat_2.12/1.1.1/macro-compat_2.12-1.1.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-lang/modules/scala-xml_2.12/2.3.0/scala-xml_2.12-2.3.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/eed3si9n/shaded-scalajson_2.12/1.0.0-M4/shaded-scalajson_2.12-1.0.0-M4.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/get-coursier/util/directories/0.1.2/directories-0.1.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/librarymanagement-ivy_2.12/1.12.0/librarymanagement-ivy_2.12-1.12.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/com/github/alexarchambault/case-app_2.12/2.0.6/case-app_2.12-2.0.6.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/scala-debug-adapter_2.12/4.2.8/scala-debug-adapter_2.12-4.2.8.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/launcher-interface/1.5.2/launcher-interface-1.5.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/epfl/scala/libdaemon_2.12/0.0.12/libdaemon_2.12-0.0.12.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/monix/monix-catnap_2.12/3.2.0/monix-catnap_2.12-3.2.0.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.jar.sha1
Downloading https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/scala-sbt/test-agent/1.12.1/test-agent-1.12.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/ch/qos/logback/logback-classic/1.5.27/logback-classic-1.5.27.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/zipkin/reporter2/zipkin-reporter-brave/2.17.2/zipkin-reporter-brave-2.17.2.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/org/jline/jline-terminal-jni/3.27.1/jline-terminal-jni-3.27.1.jar.sha1
Downloaded https://repo.scala-lang.org/artifactory/maven-nightlies/io/reactivex/rxjava2/rxjava/2.2.21/rxjava-2.2.21.jar.sha1
Starting compilation server
[90mCompiling project (Scala 3.8.3, JVM (17))[0m
[[33mwarn[0m] ./Game.scala:60:103
[[33mwarn[0m] Non local returns are no longer supported; use `boundary` and `boundary.break` in `scala.util` instead
[[33mwarn[0m]       if (b(l(0))(l(1)).nonEmpty && b(l(0))(l(1)) == b(l(2))(l(3)) && b(l(2))(l(3)) == b(l(4))(l(5))) return Some(b(l(0))(l(1)))
[[33mwarn[0m]                                                                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^
[90mCompiled project (Scala 3.8.3, JVM (17))[0m
```

### 💻 Implementation Code (Scala)
```scala
import java.io._
import scala.io.Source
import scala.util.matching.Regex

object Game {
  def main(args: Array[String]): Unit = {
    val path = "current_state.json"
    val json = Source.fromFile(path).getLines().mkString
    val cell = sys.env.getOrElse("CELL", "").toUpperCase
    val action = sys.env.getOrElse("ACTION", "put")

    if (action == "reset") {
      val out = "{
  \"board\": [[\"\",\"\",\"\"],[\"\",\"\",\"\"],[\"\",\"\",\"\"]],
  \"turn\": \"X\",
  \"winner\": null,
  \"log\": []
}"
      val pw = new PrintWriter(new File(path))
      pw.write(out); pw.close()
    } else if (cell.length >= 2) {
      val turn = "\"turn\":\s*\"(.*?)\"".r.findFirstMatchIn(json).map(_.group(1)).getOrElse("X")
      val winner = "\"winner\":\s*\"(.*?)\"".r.findFirstMatchIn(json).map(_.group(1)).getOrElse("null")
      
      if (winner == "null") {
        val board = Array.fill(3, 3)("")
        val rowRegex = "\[\"(.*?)\",\"(.*?)\",\"(.*?)\"\]".r
        rowRegex.findAllIn(json).matchData.zipWithIndex.foreach { case (m, i) =>
          if (i < 3) {
            board(i)(0) = m.group(1); board(i)(1) = m.group(2); board(i)(2) = m.group(3)
          }
        }

        // Correct Mapping: r is row (1-3), c is col (A-C)
        val r = cell(1) - '1'
        val c = cell(0) - 'A'

        if (r >= 0 && r < 3 && c >= 0 && c < 3 && board(r)(c).isEmpty) {
          board(r)(c) = turn
          val nextTurn = if (turn == "X") "O" else "X"
          val win = checkWinner(board)
          val draw = board.flatten.forall(_.nonEmpty)

          val winStr = if (win.isDefined) s""""${win.get}"""" else if (draw) "\"draw\"" else "null"
          val bStr = board.map(row => s"""["${row(0)}","${row(1)}","${row(2)}"]""").mkString("    ", ",
    ", "")
          
          val out = s"""{
  "board": [
$bStr
  ],
  "turn": "$nextTurn",
  "winner": $winStr,
  "log": []
}"""
          val pw = new PrintWriter(new File(path))
          pw.write(out); pw.close()
        }
      }
    }
  }

  def checkWinner(b: Array[Array[String]]): Option[String] = {
    val lns = Array(Array(0,0,0,1,0,2),Array(1,0,1,1,1,2),Array(2,0,2,1,2,2), Array(0,0,1,0,2,0),Array(0,1,1,1,2,1),Array(0,2,1,2,2,2), Array(0,0,1,1,2,2),Array(0,2,1,1,2,0))
    for (l <- lns) {
      if (b(l(0))(l(1)).nonEmpty && b(l(0))(l(1)) == b(l(2))(l(3)) && b(l(2))(l(3)) == b(l(4))(l(5))) return Some(b(l(0))(l(1)))
    }
    None
  }
}

```
</details>

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
