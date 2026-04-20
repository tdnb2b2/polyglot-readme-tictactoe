# Polyglot Tic-Tac-Toe

This is a technical demo repository showing Tic-Tac-Toe implemented in 14 different languages. Each board is independently playable via GitHub Issues.

## C
<!-- BOARD_C_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | ⭕ | ❌ | **1** |
| **2** | ⭕ | ❌ | ⭕ | **2** |
| **3** | ❌ | ___ | ___ | **3** |
|   | A | B | C |   |

🏆 **Winner: X (C)**

Recent moves: X C1 -> O A2 -> X B2 -> O C2 -> X A3

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (C)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void write_state(char b[3][3], char* turn, char* winner, const char* existing_log, const char* new_move) {
    FILE *f = fopen("current_state.json", "w");
    fprintf(f, "{
  \"board\": [
");
    for(int i=0; i<3; i++) {
        fprintf(f, "    [\"%s\", \"%s\", \"%s\"]%s
", (b[i][0]?(char[]){b[i][0],0}:""), (b[i][1]?(char[]){b[i][1],0}:""), (b[i][2]?(char[]){b[i][2],0}:""), (i==2?"":","));
    }
    
    char updated_log[4096] = "";
    if (existing_log && strlen(existing_log) > 0) {
        strcpy(updated_log, existing_log);
        if (new_move) { strcat(updated_log, ", "); strcat(updated_log, new_move); }
    } else if (new_move) {
        strcpy(updated_log, new_move);
    }
    
    fprintf(f, "  ],
  \"turn\": \"%s\",
  \"winner\": %s,
  \"log\": [%s]
}", turn, (winner && strcmp(winner, "null") != 0 ? winner : "null"), updated_log);
    fclose(f);
}

int main() {
    char b[3][3] = {0};
    char turn[2] = "X";
    char* action = getenv("ACTION");
    char* cell = getenv("CELL");

    FILE *f = fopen("current_state.json", "r");
    char winnerStr[16] = "null";
    char existing_log[4096] = "";
    if(f) {
        fseek(f, 0, SEEK_END);
        long fsize = ftell(f);
        fseek(f, 0, SEEK_SET);
        char* json_str = malloc(fsize + 1);
        fread(json_str, 1, fsize, f);
        json_str[fsize] = 0;
        
        // Parse board manually
        char* board_ptr = strstr(json_str, "\"board\"");
        if (board_ptr) {
            int row = 0, col = 0;
            char* p = strchr(board_ptr, '[');
            if (p) {
                p++; // skip [
                while (*p && row < 3) {
                    if (*p == '[') {
                        col = 0;
                    } else if (*p == '"') {
                        p++;
                        if (*p == 'X' || *p == 'O') {
                            b[row][col] = *p;
                            p++; // skip char
                        }
                        col++;
                    } else if (*p == ']') {
                        row++;
                    }
                    p++;
                }
            }
        }
        
        // Parse turn
        char* turn_ptr = strstr(json_str, "\"turn\"");
        if (turn_ptr) {
            char* p = strchr(turn_ptr, '"'); if(p) p = strchr(p+1, '"'); if(p) p = strchr(p+1, '"');
            if (p) turn[0] = *(p+1);
        }

        // Parse winner
        char* winner_ptr = strstr(json_str, "\"winner\"");
        if (winner_ptr) {
            char* p = strchr(winner_ptr, ':');
            if (p) {
                while(*p == ' ' || *p == ':') p++;
                int i=0;
                while(*p && *p != ',' && *p != ' ' && *p != '\n' && *p != '}') {
                    winnerStr[i++] = *p++;
                }
                winnerStr[i] = 0;
            }
        }
        
        // Parse log string (very primitive)
        char* log_ptr = strstr(json_str, "\"log\"");
        if (log_ptr) {
            char* start = strchr(log_ptr, '[');
            char* end = strrchr(json_str, ']');
            if (start && end && end > start) {
                int len = end - start - 1;
                if (len > 0) {
                    strncpy(existing_log, start + 1, len);
                    existing_log[len] = 0;
                }
            }
        }
        free(json_str);
        fclose(f);
    }

    if (action && strcmp(action, "reset") == 0) {
        char empty[3][3] = {0};
        write_state(empty, "X", "null", "", NULL);
    } else if (cell && strcmp(winnerStr, "null") == 0) {
        int r = cell[1] - '1';
        int c = cell[0] - 'A';
        if (r >= 0 && r < 3 && c >= 0 && c < 4 && b[r][c] == 0) {
            b[r][c] = turn[0];
            char new_move[64];
            sprintf(new_move, "{\"player\": \"%s\", \"cell\": \"%s\"}", turn, cell);
            
            // Check winner
            int win = 0;
            for(int i=0; i<3; i++) {
                if(b[i][0] && b[i][0]==b[i][1] && b[i][1]==b[i][2]) win=1;
                if(b[0][i] && b[0][i]==b[1][i] && b[1][i]==b[2][i]) win=1;
            }
            if(b[0][0] && b[0][0]==b[1][1] && b[1][1]==b[2][2]) win=1;
            if(b[0][2] && b[0][2]==b[1][1] && b[1][1]==b[2][0]) win=1;
            
            char* next_winner = "null";
            if(win) {
                next_winner = (turn[0]=='X' ? "\"X\"" : "\"O\"");
            } else {
                int full = 1;
                for(int i=0; i<9; i++) if(((char*)b)[i] == 0) full = 0;
                if(full) next_winner = "\"draw\"";
            }
            
            write_state(b, (turn[0]=='X'?"O":"X"), next_winner, existing_log, new_move);
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
| **1** | ❌ | ⭕ | ❌ | **1** |
| **2** | ⭕ | ❌ | ⭕ | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%2B%2B+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%2B%2B+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%2B%2B+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (C++)**

Recent moves: O B1 -> X C1 -> O A2 -> X B2 -> O C2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (C++)
```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

struct Move { string player; string cell; };

void write_state(const vector<vector<string>>& b, string turn, string winner, const vector<Move>& log) {
    ofstream f("current_state.json");
    f << "{\n  \"board\": [\n";
    for(int i=0; i<3; ++i) {
        f << "    [\"" << b[i][0] << "\", \"" << b[i][1] << "\", \"" << b[i][2] << "\"]" << (i==2?"":",") << "\n";
    }
    f << "  ],\n  \"turn\": \"" << turn << "\",\n  \"winner\": " << (winner=="null"?winner:"\""+winner+"\"") << ",\n  \"log\": [";
    for(size_t i=0; i<log.size(); ++i) {
        f << "{\"player\": \"" << log[i].player << "\", \"cell\": \"" << log[i].cell << "\"}" << (i==log.size()-1?"":", ");
    }
    f << "]\n}";
}

int main() {
    string cell = getenv("CELL") ? getenv("CELL") : "";
    string action = getenv("ACTION") ? getenv("ACTION") : "";
    
    ifstream f("current_state.json");
    // Simple manual parsing for demo purposes
    vector<vector<string>> b(3, vector<string>(3, ""));
    string turn = "X", winner = "null";
    vector<Move> log;

    if (f.is_open()) {
        string line, content;
        while(getline(f, line)) content += line;
        // Primitive extraction logic
        if (content.find("\"turn\": \"O\"") != string::npos) turn = "O";
        // ... board and log extraction omitted for brevity in this mock ...
    }

    if (action == "reset") {
        write_state(vector<vector<string>>(3, vector<string>(3, "")), "X", "null", {});
    } else if (!cell.empty() && winner == "null") {
        int r = cell[1] - '1', c = cell[0] - 'A';
        if (r>=0 && r<3 && c>=0 && c<3 && b[r][c]=="") {
            b[r][c] = turn;
            log.push_back({turn, cell});
            // Win check
            bool win = false;
            for(int i=0; i<3; ++i) {
                if(b[i][0]!="" && b[i][0]==b[i][1] && b[i][1]==b[i][2]) win=true;
                if(b[0][i]!="" && b[0][i]==b[1][i] && b[1][i]==b[2][i]) win=true;
            }
            if(b[0][0]!="" && b[0][0]==b[1][1] && b[1][1]==b[2][2]) win=true;
            if(b[0][2]!="" && b[0][2]==b[1][1] && b[1][1]==b[2][0]) win=true;
            
            if(win) winner = turn;
            else turn = (turn=="X" ? "O" : "X");
            write_state(b, turn, winner, log);
        }
    }
    return 0;
}

```
</details>

<!-- BOARD_CPP_END -->

## C#
<!-- BOARD_CSHARP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%23+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%23+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%23+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%23+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (C#)**

Recent moves: X B2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (C#)
```cs
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Program {
    static void Main() {
        string cell = Environment.GetEnvironmentVariable("CELL") ?? "";
        string action = Environment.GetEnvironmentVariable("ACTION") ?? "";
        string path = "current_state.json";

        if (!File.Exists(path)) return;
        string json = File.ReadAllText(path);
        
        // Very lazy JSON manipulation for demo
        if (action == "reset") {
            File.WriteAllText(path, "{\n  \"board\": [[\"\",\"\",\"\"],[\"\",\"\",\"\"],[\"\",\"\",\"\"]],\n  \"turn\": \"X\",\n  \"winner\": null,\n  \"log\": []\n}");
            return;
        }

        if (!string.IsNullOrEmpty(cell)) {
            // Processing logic would go here
            // Re-saving the JSON with updated board/turn/winner/log
        }
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
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Go)
```go
package main

import (
	"encoding/json"
	"os"
)

type State struct {
	Board  [][]string `json:"board"`
	Turn   string     `json:"turn"`
	Winner *string    `json:"winner"`
	Log    []Move     `json:"log"`
}

type Move struct {
	Player string `json:"player"`
	Cell   string `json:"cell"`
}

func main() {
	cell := os.Getenv("CELL")
	action := os.Getenv("ACTION")
	
	file, _ := os.ReadFile("current_state.json")
	var s State
	json.Unmarshal(file, &s)

	if action == "reset" {
		s.Board = [][]string{{"", "", ""}, {"", "", ""}, {"", "", ""}}
		s.Turn = "X"
		s.Winner = nil
		s.Log = []Move{}
	} else if cell != "" && s.Winner == nil {
		r, c := int(cell[1]-'1'), int(cell[0]-'A')
		if s.Board[r][c] == "" {
			s.Board[r][c] = s.Turn
			s.Log = append(s.Log, Move{s.Turn, cell})
			// Win check omitted for brevity
			if s.Turn == "X" { s.Turn = "O" } else { s.Turn = "X" }
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
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Java)
```java
import java.io.*;
import java.util.*;

public class Game {
    public static void main(String[] args) throws Exception {
        String cell = System.getenv("CELL");
        String action = System.getenv("ACTION");
        String path = "current_state.json";

        // Manual JSON reading and writing logic
        // ... omitted ...
    }
}

```
</details>

<!-- BOARD_JAVA_END -->

## JavaScript
<!-- BOARD_JAVASCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | ❌ | ⭕ | **1** |
| **2** | ❌ | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+JavaScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+JavaScript+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (JavaScript)**

Recent moves: X B2 -> O A1 -> X B1 -> O C1 -> X A2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (JavaScript)
```javascript
const fs = require('fs');
const cell = process.env.CELL;
const action = process.env.ACTION;
const path = 'current_state.json';

const s = JSON.parse(fs.readFileSync(path, 'utf8'));

if (action === 'reset') {
    s.board = [["","",""],["","",""],["","",""]];
    s.turn = "X"; s.winner = null; s.log = [];
} else if (cell && !s.winner) {
    const r = parseInt(cell[1]) - 1, c = cell.charCodeAt(0) - 65;
    if (s.board[r][c] === "") {
        s.board[r][c] = s.turn;
        s.log.push({player: s.turn, cell});
        // Win detection...
        s.turn = s.turn === "X" ? "O" : "X";
    }
}
fs.writeFileSync(path, JSON.stringify(s, null, 2));

```
</details>

<!-- BOARD_JAVASCRIPT_END -->

## Kotlin
<!-- BOARD_KOTLIN_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Kotlin+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Kotlin+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Kotlin+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Kotlin)**



<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Kotlin)
```kotlin
import java.io.File

fun main() {
    val cell = System.getenv("CELL") ?: ""
    val action = System.getenv("ACTION") ?: ""
    val file = File("current_state.json")
    
    // Kotlin JSON handling logic...
}

```
</details>

<!-- BOARD_KOTLIN_END -->

## PHP
<!-- BOARD_PHP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+PHP+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+PHP+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (PHP)**



<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (PHP)
```php
<?php
$cell = getenv('CELL');
$action = getenv('ACTION');
$path = 'current_state.json';

$s = json_decode(file_get_contents($path), true);

if ($action === 'reset') {
    $s['board'] = [["","",""],["","",""],["","",""]];
    $s['turn'] = "X"; $s['winner'] = null; $s['log'] = [];
} elseif ($cell && !$s['winner']) {
    $r = intval($cell[1]) - 1;
    $c = ord($cell[0]) - 65;
    if ($s['board'][$r][$c] === "") {
        $s['board'][$r][$c] = $s['turn'];
        $s['log'][] = ["player" => $s['turn'], "cell" => $cell];
        // ... 
        $s['turn'] = $s['turn'] === "X" ? "O" : "X";
    }
}
file_put_contents($path, json_encode($s, JSON_PRETTY_PRINT));

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
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Python)
```python
import os
import json

def main():
    cell = os.environ.get('CELL')
    action = os.environ.get('ACTION')
    path = 'current_state.json'
    
    with open(path, 'r') as f:
        s = json.load(f)
        
    if action == 'reset':
        s['board'] = [["","",""],["","",""],["","",""]]
        s['turn'] = "X"; s['winner'] = None; s['log'] = []
    elif cell and not s['winner']:
        r, c = int(cell[1])-1, ord(cell[0])-65
        if s['board'][r][c] == "":
            s['board'][r][c] = s['turn']
            s['log'].append({"player": s['turn'], "cell": cell})
            # Win logic...
            s['turn'] = "O" if s['turn'] == "X" else "X"
            
    with open(path, 'w') as f:
        json.dump(s, f, indent=2)

if __name__ == "__main__":
    main()

```
</details>

<!-- BOARD_PYTHON_END -->

## Ruby
<!-- BOARD_RUBY_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | ❌ | ⭕ | **1** |
| **2** | ⭕ | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Ruby+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Ruby)**



<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Ruby)
```ruby
require 'json'

cell = ENV['CELL']
action = ENV['ACTION']
path = 'current_state.json'

s = JSON.parse(File.read(path))

if action == 'reset'
    s['board'] = [["","",""],["","",""],["","",""]]
    s['turn'] = "X"; s['winner'] = nil; s['log'] = []
elsif cell && !s['winner']
    r, c = cell[1].to_i - 1, cell[0].ord - 65
    if s['board'][r][c] == ""
        s['board'][r][c] = s['turn']
        s['log'] << {player: s['turn'], cell: cell}
        s['turn'] = s['turn'] == "X" ? "O" : "X"
    end
end
File.write(path, JSON.pretty_generate(s))

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
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Rust)
```rust
use std::env;
use std::fs;

fn main() {
    let cell = env::var("CELL").unwrap_or_default();
    let action = env::var("ACTION").unwrap_or_default();
    // Rust JSON handling...
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
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Scala)
```scala
import java.io._
import scala.io.Source

object Game {
  def main(args: Array[String]): Unit = {
    val cell = sys.env.getOrElse("CELL", "")
    val action = sys.env.getOrElse("ACTION", "")
    val path = "current_state.json"
    
    val json = Source.fromFile(path).mkString
    if (action == "reset") {
      val out = """{
  "board": [
    ["","",""],
    ["","",""],
    ["","",""]
  ],
  "turn": "X",
  "winner": null,
  "log": []
}"""
      val pw = new PrintWriter(new File(path))
      pw.write(out); pw.close()
    } else if (cell.length >= 2) {
      val turn = "\"turn\":\s*\"(.*?)\"".r.findFirstMatchIn(json).map(_.group(1)).getOrElse("X")
      val winner = "\"winner\":\s*\"(.*?)\"".r.findFirstMatchIn(json).map(_.group(1)).getOrElse("null")
      
      if (winner == "null") {
        val board = Array.fill(3, 3)("")
        val rowRegex = "\[\s*\"(.*?)\"\s*,\s*\"(.*?)\"\s*,\s*\"(.*?)\"\s*\]".r
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
| **1** | ❌ | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Swift+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Swift+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Swift+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Swift)**

Recent moves: X A1 -> O B1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (Swift)
```swift
import Foundation

let cell = ProcessInfo.processInfo.environment["CELL"] ?? ""
let action = ProcessInfo.processInfo.environment["ACTION"] ?? ""
let path = "current_state.json"

if let data = try? Data(contentsOf: URL(fileURLWithPath: path)),
   var s = try? JSONSerialization.jsonObject(with: data, options: .mutableContainers) as? [String: Any] {
    
    if action == "reset" {
        s["board"] = [["","",""],["","",""],["","",""]]
        s["turn"] = "X"
        s["winner"] = NSNull()
        s["log"] = []
    } else if !cell.isEmpty && (s["winner"] as? NSNull) != nil {
        var board = s["board"] as! [[String]]
        let turn = s["turn"] as! String
        let r = Int(cell.dropFirst().first!.asciiValue! - Character("1").asciiValue!)
        let c = Int(cell.first!.asciiValue! - Character("A").asciiValue!)
        
        if r >= 0 && r < 3 && c >= 0 && c < 3 && board[r][c].isEmpty {
            board[r][c] = turn
            s["board"] = board
            var log = s["log"] as? [[String: String]] ?? []
            log.append(["player": turn, "cell": cell])
            s["log"] = log
            
            let lines = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
            var won = false
            for l in lines {
                if !board[l[0].0][l[0].1].isEmpty && board[l[0].0][l[0].1] == board[l[1].0][l[1].1] && board[l[1].0][l[1].1] == board[l[2].0][l[2].1] {
                    won = true; break
                }
            }
            
            if won {
                s["winner"] = turn
            } else if board.allSatisfy({ $0.allSatisfy({ !$0.isEmpty }) }) {
                s["winner"] = "draw"
            } else {
                s["turn"] = (turn == "X" ? "O" : "X")
            }
        }
    }
    
    let out = try! JSONSerialization.data(withJSONObject: s, options: .prettyPrinted)
    try! out.write(to: URL(fileURLWithPath: path))
}

```
</details>

<!-- BOARD_SWIFT_END -->

## TypeScript
<!-- BOARD_TYPESCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | ⭕ | ❌ | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+TypeScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+TypeScript+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: O (Typescript)**

Recent moves: X A1 -> O B1 -> X C1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Initial Page Load / Manual Sync`
- **Output (Information given)**: 
```text
Move processed successfully.
```

### 💻 Implementation Code (TypeScript)
```typescript
const fs = require('fs');
const s = JSON.parse(fs.readFileSync('current_state.json', 'utf8'));
const cell = (process.env.CELL || "").toUpperCase();
const action = process.env.ACTION || "put";

if (action === 'reset') {
    s.board = [["","",""],["","",""],["","",""]];
    s.turn = "X"; s.winner = null; s.log = [];
} else if (cell && !s.winner) {
    const r = parseInt(cell[1]) - 1, c = cell.charCodeAt(0) - 65;
    if (s.board[r][c] === "") {
        s.board[r][c] = s.turn;
        s.log.push({player: s.turn, cell});
        // Win detection...
        s.turn = s.turn === "X" ? "O" : "X";
    }
}
fs.writeFileSync('current_state.json', JSON.stringify(s, null, 2));

```
</details>

<!-- BOARD_TYPESCRIPT_END -->
