# 🕹️ Polyglot Tic-Tac-Toe on GitHub README

A playable Tic-Tac-Toe game on GitHub README, implemented in multiple programming languages! Make moves by creating issues.

---

## 🛠️ Individual Boards

### C
<!-- BOARD_C_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | ___ | ❌ | **1** |
| **2** | ___ | ❌ | ___ | **2** |
| **3** | ❌ | ___ | ⭕ | **3** |
|   | A | B | C |   |

🏆 Winner: ❌ (C)

Recent moves: ❌ B2 → ⭕ A1 → ❌ C1 → ⭕ C3 → ❌ A3

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (C)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void write_state(char b[3][3], char* turn, char* winner, const char* existing_log, const char* new_move) {
    FILE *f = fopen("current_state.json", "w");
    fprintf(f, "{\n  \"board\": [\n");
    for(int i=0; i<3; i++) {
        fprintf(f, "    [\"%s\", \"%s\", \"%s\"]%s\n", (b[i][0]?(char[]){b[i][0],0}:""), (b[i][1]?(char[]){b[i][1],0}:""), (b[i][2]?(char[]){b[i][2],0}:""), (i==2?"":","));
    }
    
    char updated_log[4096] = "";
    if (existing_log && strlen(existing_log) > 0) {
        strcpy(updated_log, existing_log);
        if (new_move) { strcat(updated_log, ", "); strcat(updated_log, new_move); }
    } else if (new_move) {
        strcpy(updated_log, new_move);
    }
    
    fprintf(f, "  ],\n  \"turn\": \"%s\",\n  \"winner\": %s,\n  \"log\": [%s]\n}", turn, (winner && strcmp(winner, "null") != 0 ? winner : "null"), updated_log);
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
        
        char* turn_ptr = strstr(json_str, "\"turn\"");
        if (turn_ptr) {
            char* p = strchr(turn_ptr, ':');
            if (p) {
                p = strchr(p, '"');
                if (p) {
                    p++;
                    if (*p == 'O') strcpy(turn, "O");
                }
            }
        }
        
        char* win_ptr = strstr(json_str, "\"winner\"");
        if (win_ptr) {
            char* p = strchr(win_ptr, ':');
            if (p) {
                p++;
                while (*p == ' ' || *p == '\n') p++;
                if (*p == '"') {
                    p++;
                    if (*p == 'X') strcpy(winnerStr, "X");
                    else if (*p == 'O') strcpy(winnerStr, "O");
                    else if (strncmp(p, "draw", 4) == 0) strcpy(winnerStr, "draw");
                }
            }
        }
        
        char* log_ptr = strstr(json_str, "\"log\"");
        if (log_ptr) {
            char* p = strchr(log_ptr, '[');
            if (p) {
                p++;
                char* end_p = strrchr(p, ']');
                if (end_p) {
                    int len = end_p - p;
                    if (len > 0 && len < 4096) {
                        strncpy(existing_log, p, len);
                        existing_log[len] = '\0';
                    }
                }
            }
        }
        
        free(json_str);
        fclose(f);
    }

    if(action && strcmp(action, "reset")==0) {
        int full=1; for(int i=0; i<3; i++) for(int j=0; j<3; j++) if(b[i][j]==0) full=0;
        if(strcmp(winnerStr, "null") != 0 || full) {
            write_state((char[3][3]){{0,0,0},{0,0,0},{0,0,0}}, "X", "null", "", NULL);
        }
        return 0;
    }
    if(strcmp(winnerStr, "null") != 0) return 0;

    if(cell && strlen(cell)>=2) {
        int r = cell[1]-'1', c = cell[0]-'A';
        if(r>=0 && r<3 && c>=0 && c<3 && b[r][c]==0) {
            b[r][c] = turn[0];
            int win = 0;
            int lns[8][6] = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
            for(int i=0; i<8; i++) {
                if(b[lns[i][0]][lns[i][1]] && b[lns[i][0]][lns[i][1]]==b[lns[i][2]][lns[i][3]] && b[lns[i][2]][lns[i][3]]==b[lns[i][4]][lns[i][5]]) { win=1; break; }
            }
            char new_move[64];
            sprintf(new_move, "{\"player\": \"%c\", \"cell\": \"%s\"}", turn[0], cell);
            char winner_buf[16] = "null";
            if(win) {
                sprintf(winner_buf, "\"%c\"", turn[0]);
                write_state(b, turn, winner_buf, existing_log, new_move);
            } else {
                int full=1; for(int i=0; i<3; i++) for(int j=0; j<3; j++) if(b[i][j]==0) full=0;
                if(full) {
                    write_state(b, turn, "\"draw\"", existing_log, new_move);
                } else {
                    write_state(b, (turn[0]=='X'?"O":"X"), "null", existing_log, new_move);
                }
            }
        }
    }
    return 0;
}

```
</details>

<!-- BOARD_C_END -->

### C++
<!-- BOARD_CPP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%2B%2B+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%2B%2B+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%2B%2B+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%2B%2B+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%2B%2B+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%2B%2B+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%2B%2B%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%2B%2B+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (C++)**

Recent moves: ❌ B2 → ⭕ A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (C++)
```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void write_state(char b[3][3], string turn, string winner, string existing_log, string new_move) {
    ofstream f("current_state.json");
    f << "{\n  \"board\": [\n";
    for(int i=0; i<3; i++) {
        f << "    [\"" << (b[i][0]?string(1,b[i][0]):"") << "\", \"" << (b[i][1]?string(1,b[i][1]):"") << "\", \"" << (b[i][2]?string(1,b[i][2]):"") << "\"]" << (i==2?"":",") << "\n";
    }
    string log_content = existing_log;
    if (new_move != "") {
        if (log_content.find("{") != string::npos) log_content += ", ";
        log_content += new_move;
    }
    f << "  ],\n  \"turn\": \"" << turn << "\",\n  \"winner\": " << (winner==""?"null":"\""+winner+"\"") << ",\n  \"log\": [" << log_content << "]\n}";
}

int main() {
    char b[3][3] = {0};
    string turn = "X";
    string winnerStr = "null";
    char* action_env = getenv("ACTION");
    char* cell_env = getenv("CELL");
    string action = action_env ? action_env : "put";
    string cell = cell_env ? cell_env : "";

    ifstream f("current_state.json");
    string f_line, full_content;
    if (f.is_open()) {
        while(getline(f, f_line)) {
            full_content += f_line + "\n";
        }
        f.close();
        
        size_t b_pos = full_content.find("\"board\"");
        if (b_pos != string::npos) {
            int row = 0, col = 0;
            for (size_t i = full_content.find("[", b_pos) + 1; i < full_content.length() && row < 3; i++) {
                char c = full_content[i];
                if (c == '[') col = 0;
                else if (c == '"') {
                    i++;
                    char val = full_content[i];
                    if (val == 'X' || val == 'O') {
                        b[row][col] = val;
                        i++; // skip char
                    }
                    col++;
                }
                else if (c == ']') row++;
            }
        }
        
        size_t t_pos = full_content.find("\"turn\"");
        if (t_pos != string::npos) {
            size_t p = full_content.find('"', full_content.find(':', t_pos));
            if (p != string::npos && full_content[p+1] == 'O') turn = "O";
        }
        
        size_t w_pos = full_content.find("\"winner\"");
        if (w_pos != string::npos) {
            size_t p = full_content.find(':', w_pos);
            if (p != string::npos) {
                p++;
                while(p < full_content.length() && (full_content[p] == ' ' || full_content[p] == '\n')) p++;
                if (full_content[p] == '"') {
                    p++;
                    if (full_content[p] == 'X') winnerStr = "X";
                    else if (full_content[p] == 'O') winnerStr = "O";
                    else if (full_content.substr(p, 4) == "draw") winnerStr = "draw";
                }
            }
        }
    }

    if (action == "reset") {
        bool full = true; for(int i=0; i<3; i++) for(int j=0; j<3; j++) if(b[i][j]==0) full=false;
        if (winnerStr != "null" || full) {
            char empty_b[3][3] = {0};
            write_state(empty_b, "X", "", "", "");
        }
        return 0;
    }
    if (winnerStr != "null") return 0;

    string existing_log = "";
    size_t log_start = full_content.find("\"log\"");
    if(log_start != string::npos) {
        log_start = full_content.find("[", log_start);
        if(log_start != string::npos) {
            log_start++;
            size_t log_end = full_content.rfind("]");
            if(log_end != string::npos && log_end > log_start) {
                existing_log = full_content.substr(log_start, log_end - log_start);
                size_t first = existing_log.find_first_not_of(" \n\r\t");
                size_t last = existing_log.find_last_not_of(" \n\r\t");
                if (first != string::npos && last != string::npos) existing_log = existing_log.substr(first, last - first + 1);
                else existing_log = "";
            }
        }
    }

    if(cell != "") {
        int row = cell[1]-'1', col = cell[0]-'A';
        if(row>=0 && row<3 && col>=0 && col<3 && b[row][col]==0) {
            b[row][col] = turn[0];
            int lns[8][6] = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
            bool win = false;
            for(int i=0; i<8; i++) if(b[lns[i][0]][lns[i][1]] && b[lns[i][0]][lns[i][1]]==b[lns[i][2]][lns[i][3]] && b[lns[i][2]][lns[i][3]]==b[lns[i][4]][lns[i][5]]) win=true;
            string new_move = "{\"player\": \"" + turn + "\", \"cell\": \"" + cell + "\"}";
            if(win) write_state(b, turn, turn, existing_log, new_move);
            else {
                bool full = true; for(int i=0; i<3; i++) for(int j=0; j<3; j++) if(b[i][j]==0) full=false;
                if(full) write_state(b, turn, "draw", existing_log, new_move);
                else write_state(b, (turn=="X"?"O":"X"), "", existing_log, new_move);
            }
        }
    }
    return 0;
}

```
</details>

<!-- BOARD_CPP_END -->

### C#
<!-- BOARD_CSHARP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%23+board) | ⭕ | **1** |
| **2** | ⭕ | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%23+board) | **2** |
| **3** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%23+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (C#)**

Recent moves: ❌ B2 → ⭕ C1 → ❌ A3 → ⭕ A2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (C#)
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Linq;

public class Move { public string player { get; set; } public string cell { get; set; } }
public class State { 
    public string[][] board { get; set; } 
    public string turn { get; set; } 
    public string winner { get; set; } 
    public List<Move> log { get; set; } 
}

class Program {
    static void Main() {
        string json = File.ReadAllText("current_state.json");
        var options = new JsonSerializerOptions { WriteIndented = true };
        var state = JsonSerializer.Deserialize<State>(json);

        string cell = Environment.GetEnvironmentVariable("CELL")?.ToUpper();
        string action = Environment.GetEnvironmentVariable("ACTION") ?? "put";

        if (action == "reset") {
            bool isFull = state.board.All(row => row.All(c => !string.IsNullOrEmpty(c)));
            if (state.winner != null || isFull) {
                state.board = new string[][] { new string[]{"","",""}, new string[]{"","",""}, new string[]{"","",""} };
                state.turn = "X";
                state.winner = null;
                state.log = new List<Move>();
            }
        } else if (!string.IsNullOrEmpty(cell) && state.winner == null) {
            int r = cell[1] - '1';
            int c = cell[0] - 'A';
            if (r >= 0 && r < 3 && c >= 0 && c < 3 && string.IsNullOrEmpty(state.board[r][c])) {
                state.board[r][c] = state.turn;
                state.log.Add(new Move { player = state.turn, cell = cell });
                string win = CheckWinner(state.board);
                if (win != null) state.winner = win;
                else if (state.board.All(row => row.All(x => !string.IsNullOrEmpty(x)))) state.winner = "draw";
                else state.turn = state.turn == "X" ? "O" : "X";
            }
        }
        File.WriteAllText("current_state.json", JsonSerializer.Serialize(state, options));
    }

    static string CheckWinner(string[][] b) {
        int[][] lines = { new[] {0,1,2}, new[] {3,4,5}, new[] {6,7,8}, new[] {0,3,6}, new[] {1,4,7}, new[] {2,5,8}, new[] {0,4,8}, new[] {2,4,6} };
        var flat = b.SelectMany(x => x).ToArray();
        foreach (var l in lines) {
            if (!string.IsNullOrEmpty(flat[l[0]]) && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]]) return flat[l[0]];
        }
        return null;
    }
}

```
</details>

<!-- BOARD_CSHARP_END -->

### Go
<!-- BOARD_GO_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Go+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Go+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Go+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Go+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (Go)**

Recent moves: ❌ B2 → ⭕ A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Go)
```go
package main

import (
	"encoding/json"
	"os"
	"strings"
)

type Move struct {
	Player string `json:"player"`
	Cell   string `json:"cell"`
}

type State struct {
	Board  [][]string `json:"board"`
	Turn   string     `json:"turn"`
	Winner *string    `json:"winner"`
	Log    []Move     `json:"log"`
}

func writeState(state State) {
	f, _ := os.Create("current_state.json")
	defer f.Close()
	enc := json.NewEncoder(f)
	enc.SetIndent("", "  ")
	enc.Encode(state)
}

func checkWinner(b [][]string) *string {
	lines := [][]int{{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}}
	flat := []string{}
	for _, row := range b {
		flat = append(flat, row...)
	}
	for _, l := range lines {
		if flat[l[0]] != "" && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]] {
			res := flat[l[0]]
			return &res
		}
	}
	return nil
}

func main() {
	f, _ := os.ReadFile("current_state.json")
	var state State
	json.Unmarshal(f, &state)

	cell := strings.ToUpper(os.Getenv("CELL"))
	action := os.Getenv("ACTION")
	if action == "" {
		action = "put"
	}

	if action == "reset" {
		isFull := true
		for _, row := range state.Board {
			for _, c := range row {
				if c == "" {
					isFull = false
				}
			}
		}
		if state.Winner != nil || isFull {
			state = State{
				Board:  [][]string{{"", "", ""}, {"", "", ""}, {"", "", ""}},
				Turn:   "X",
				Winner: nil,
				Log:    []Move{},
			}
		}
	} else if cell != "" && state.Winner == nil {
		r := int(cell[1]-'1')
		c := int(cell[0]-'A')
		if r >= 0 && r < 3 && c >= 0 && c < 3 && state.Board[r][c] == "" {
			state.Board[r][c] = state.Turn
			state.Log = append(state.Log, Move{Player: state.Turn, Cell: cell})
			win := checkWinner(state.Board)
			if win != nil {
				state.Winner = win
			} else {
				full := true
				for _, row := range state.Board {
					for _, x := range row {
						if x == "" {
							full = false
						}
					}
				}
				if full {
					d := "draw"
					state.Winner = &d
				} else {
					if state.Turn == "X" {
						state.Turn = "O"
					} else {
						state.Turn = "X"
					}
				}
			}
		}
	}

	writeState(state)
}

```
</details>

<!-- BOARD_GO_END -->

### Java
<!-- BOARD_JAVA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Java+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Java+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Java+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Java+board) | ❌ | **3** |
|   | A | B | C |   |

🎮 **Next Move: ⭕ (Java)**

Recent moves: ❌ B2 → ⭕ A1 → ❌ C3

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Java)
```java
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Game {
    static class Move { 
        String player; 
        String cell; 
        Move(String p, String c) { this.player = p; this.cell = c; }
    }
    static class State { 
        String[][] board = new String[3][3]; 
        String turn = "X"; 
        String winner = null; 
        List<Move> log = new ArrayList<>(); 
    }

    public static void main(String[] args) throws Exception {
        String json = new String(Files.readAllBytes(Paths.get("current_state.json")));
        State state = parseState(json);

        String cell = System.getenv("CELL");
        if (cell != null) cell = cell.toUpperCase();
        String action = System.getenv("ACTION");
        if (action == null) action = "put";

        if ("reset".equals(action)) {
            boolean isFull = true; for(String[] r : state.board) for(String c : r) if(c == null || c.isEmpty()) isFull = false;
            if (state.winner != null || isFull) {
                state.board = new String[][]{{"","",""}, {"","",""}, {"","",""}};
                state.turn = "X";
                state.winner = null;
                state.log = new ArrayList<>();
            }
        } else if (cell != null && !cell.isEmpty() && state.winner == null) {
            int r = cell.charAt(1) - '1';
            int c = cell.charAt(0) - 'A';
            if (r >= 0 && r < 3 && c >= 0 && c < 3 && (state.board[r][c] == null || state.board[r][c].isEmpty())) {
                state.board[r][c] = state.turn;
                state.log.add(new Move(state.turn, cell));
                String win = checkWinner(state.board);
                if (win != null) state.winner = win;
                else {
                    boolean full = true; for(String[] row : state.board) for(String x : row) if(x == null || x.isEmpty()) full = false;
                    if (full) state.winner = "draw";
                    else state.turn = state.turn.equals("X") ? "O" : "X";
                }
            }
        }
        Files.write(Paths.get("current_state.json"), stateToJson(state).getBytes());
    }

    static State parseState(String json) {
        State s = new State();
        // Simple manual parsing
        if (json.contains("\"board\"")) {
            int boardIdx = json.indexOf("\"board\"");
            int startIdx = json.indexOf("[", boardIdx);
            int row = 0;
            int pos = startIdx + 1;
            while (row < 3) {
                int rowStart = json.indexOf("[", pos);
                if (rowStart == -1) break;
                int rowEnd = json.indexOf("]", rowStart);
                String rowStr = json.substring(rowStart + 1, rowEnd);
                String[] cells = rowStr.split(",");
                for (int col = 0; col < 3 && col < cells.length; col++) {
                    String val = cells[col].trim().replace("\"", "");
                    s.board[row][col] = val;
                }
                row++;
                pos = rowEnd + 1;
            }
        }
        if (json.contains("\"turn\"")) {
            int idx = json.indexOf("\"turn\"");
            int valStart = json.indexOf("\"", json.indexOf(":", idx));
            int valEnd = json.indexOf("\"", valStart + 1);
            s.turn = json.substring(valStart + 1, valEnd);
        }
        if (json.contains("\"winner\"")) {
            int idx = json.indexOf("\"winner\"");
            int colonIdx = json.indexOf(":", idx);
            int nextQuote = json.indexOf("\"", colonIdx);
            int nextComma = json.indexOf(",", colonIdx);
            int nextBrace = json.indexOf("}", colonIdx);
            int end = (nextComma != -1) ? nextComma : nextBrace;
            String val = json.substring(colonIdx + 1, end).trim();
            if (val.startsWith("\"")) {
                s.winner = val.substring(1, val.lastIndexOf("\""));
            } else if (val.equals("null")) {
                s.winner = null;
            } else {
                s.winner = val;
            }
        }
        if (json.contains("\"log\"")) {
            int idx = json.indexOf("\"log\"");
            int start = json.indexOf("[", idx);
            int end = json.lastIndexOf("]");
            String logContent = json.substring(start + 1, end).trim();
            if (!logContent.isEmpty()) {
                String[] entries = logContent.split("\\}");
                for (String entry : entries) {
                    if (entry.contains("{")) {
                        int pIdx = entry.indexOf("\"player\"");
                        int pValStart = entry.indexOf("\"", entry.indexOf(":", pIdx));
                        int pValEnd = entry.indexOf("\"", pValStart + 1);
                        String p = entry.substring(pValStart + 1, pValEnd);
                        
                        int cIdx = entry.indexOf("\"cell\"");
                        int cValStart = entry.indexOf("\"", entry.indexOf(":", cIdx));
                        int cValEnd = entry.indexOf("\"", cValStart + 1);
                        String c = entry.substring(cValStart + 1, cValEnd);
                        s.log.add(new Move(p, c));
                    }
                }
            }
        }
        return s;
    }

    static String stateToJson(State s) {
        StringBuilder sb = new StringBuilder();
        sb.append("{\n  \"board\": [\n");
        for (int i = 0; i < 3; i++) {
            sb.append("    [\"").append(s.board[i][0]).append("\", \"").append(s.board[i][1]).append("\", \"").append(s.board[i][2]).append("\"]").append(i == 2 ? "" : ",").append("\n");
        }
        sb.append("  ],\n  \"turn\": \"").append(s.turn).append("\",\n");
        sb.append("  \"winner\": ").append(s.winner == null ? "null" : "\"" + s.winner + "\"").append(",\n");
        sb.append("  \"log\": [\n");
        for (int i = 0; i < s.log.size(); i++) {
            Move m = s.log.get(i);
            sb.append("    {\"player\": \"").append(m.player).append("\", \"cell\": \"").append(m.cell).append("\"}").append(i == s.log.size() - 1 ? "" : ",").append("\n");
        }
        sb.append("  ]\n}");
        return sb.toString();
    }

    static String checkWinner(String[][] b) {
        int[][] lines = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};
        String[] flat = new String[9];
        for(int i=0; i<3; i++) for(int j=0; j<3; j++) flat[i*3+j] = b[i][j];
        for(int[] l : lines) {
            if (flat[l[0]] != null && !flat[l[0]].isEmpty() && flat[l[0]].equals(flat[l[1]]) && flat[l[0]].equals(flat[l[2]])) return flat[l[0]];
        }
        return null;
    }
}


```
</details>

<!-- BOARD_JAVA_END -->

### JavaScript
<!-- BOARD_JAVASCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+JavaScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+JavaScript+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+JavaScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+JavaScript+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (JavaScript)**

Recent moves: ❌ B2 → ⭕ A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (JavaScript)
```javascript
const fs = require('fs');
const state = JSON.parse(fs.readFileSync('current_state.json', 'utf8'));

const cell = process.env.CELL ? process.env.CELL.toUpperCase() : '';
const action = process.env.ACTION || 'put';

function checkWinner(b) {
  const lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  const flat = b.flat();
  for (let l of lines) {
    if (flat[l[0]] && flat[l[0]] === flat[l[1]] && flat[l[0]] === flat[l[2]]) return flat[l[0]];
  }
  return null;
}

if (action === 'reset') {
  const isFull = state.board.every(row => row.every(c => c !== ''));
  if (state.winner || isFull) {
    state.board = [['','',''],['','',''],['','','']];
    state.turn = 'X';
    state.winner = null;
    state.log = [];
  }
} else if (cell && !state.winner) {
  const r = parseInt(cell[1]) - 1;
  const c = cell.charCodeAt(0) - 65;
  if (r >= 0 && r < 3 && c >= 0 && c < 3 && state.board[r][c] === '') {
    state.board[r][c] = state.turn;
    state.log.push({ player: state.turn, cell });
    const win = checkWinner(state.board);
    if (win) state.winner = win;
    else if (state.board.flat().every(x => x !== '')) state.winner = 'draw';
    else state.turn = state.turn === 'X' ? 'O' : 'X';
  }
}

fs.writeFileSync('current_state.json', JSON.stringify(state, null, 2));

```
</details>

<!-- BOARD_JAVASCRIPT_END -->

### Kotlin
<!-- BOARD_KOTLIN_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | ❌ | ❌ | **1** |
| **2** | ⭕ | ❌ | ___ | **2** |
| **3** | ⭕ | ⭕ | ❌ | **3** |
|   | A | B | C |   |

🏆 Winner: ⭕ (Kotlin)

Recent moves: ⭕ A3 → ❌ B1 → ⭕ B3 → ❌ C1 → ⭕ A2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Kotlin)
```kotlin
import java.io.File

data class Move(val player: String, val cell: String)
data class State(var board: List<MutableList<String>>, var turn: String, var winner: String?, var log: List<Move>)

fun main() {
    val file = File("current_state.json")
    val json = file.readText()
    val state = parseState(json)

    val cell = System.getenv("CELL")?.toUpperCase() ?: ""
    val action = System.getenv("ACTION") ?: "put"

    if (action == "reset") {
        val isFull = state.board.all { row -> row.all { it.isNotEmpty() } }
        if (state.winner != null || isFull) {
            state.board = listOf(mutableListOf("","",""), mutableListOf("","",""), mutableListOf("","",""))
            state.turn = "X"
            state.winner = null
            state.log = emptyList()
        }
    } else if (cell.isNotEmpty() && state.winner == null) {
        val r = cell[1] - '1'
        val c = cell[0] - 'A'
        if (r in 0..2 && c in 0..2 && state.board[r][c].isEmpty()) {
            state.board[r][c] = state.turn
            state.log = state.log + Move(state.turn, cell)
            
            val win = checkWinner(state.board)
            if (win != null) state.winner = win
            else {
                if (state.board.all { row -> row.all { it.isNotEmpty() } }) state.winner = "draw"
                else state.turn = if (state.turn == "X") "O" else "X"
            }
        }
    }
    file.writeText(stateToJson(state))
}

fun parseState(json: String): State {
    val board = mutableListOf(mutableListOf("","",""), mutableListOf("","",""), mutableListOf("","",""))
    var turn = "X"
    var winner: String? = null
    val log = mutableListOf<Move>()

    if (json.contains("\"board\"")) {
        val boardIdx = json.indexOf("\"board\"")
        val startIdx = json.indexOf("[", boardIdx)
        var row = 0
        var pos = startIdx + 1
        while (row < 3) {
            val rowStart = json.indexOf("[", pos)
            if (rowStart == -1) break
            val rowEnd = json.indexOf("]", rowStart)
            val rowStr = json.substring(rowStart + 1, rowEnd)
            val cells = rowStr.split(",")
            for (col in 0 until 3) {
                if (col < cells.size) {
                    board[row][col] = cells[col].trim().replace("\"", "")
                }
            }
            row++
            pos = rowEnd + 1
        }
    }
    
    if (json.contains("\"turn\"")) {
        val idx = json.indexOf("\"turn\"")
        val valStart = json.indexOf("\"", json.indexOf(":", idx))
        val valEnd = json.indexOf("\"", valStart + 1)
        turn = json.substring(valStart + 1, valEnd)
    }
    
    if (json.contains("\"winner\"")) {
        val idx = json.indexOf("\"winner\"")
        val colonIdx = json.indexOf(":", idx)
        val nextQuote = json.indexOf("\"", colonIdx)
        val nextComma = json.indexOf(",", colonIdx)
        val nextBrace = json.indexOf("}", colonIdx)
        val end = if (nextComma != -1) nextComma else nextBrace
        val value = json.substring(colonIdx + 1, end).trim()
        if (value.startsWith("\"")) {
            winner = value.substring(1, value.lastIndexOf("\""))
        } else if (value == "null") {
            winner = null
        } else {
            winner = value
        }
    }
    
    if (json.contains("\"log\"")) {
        val idx = json.indexOf("\"log\"")
        val start = json.indexOf("[", idx)
        val end = json.lastIndexOf("]")
        val logContent = json.substring(start + 1, end).trim()
        if (logContent.isNotEmpty()) {
            val entries = logContent.split("}")
            for (entry in entries) {
                if (entry.contains("{")) {
                    val pIdx = entry.indexOf("\"player\"")
                    val pValStart = entry.indexOf("\"", entry.indexOf(":", pIdx))
                    val pValEnd = entry.indexOf("\"", pValStart + 1)
                    val p = entry.substring(pValStart + 1, pValEnd)
                    
                    val cIdx = entry.indexOf("\"cell\"")
                    val cValStart = entry.indexOf("\"", entry.indexOf(":", cIdx))
                    val cValEnd = entry.indexOf("\"", cValStart + 1)
                    val c = entry.substring(cValStart + 1, cValEnd)
                    log.add(Move(p, c))
                }
            }
        }
    }

    return State(board, turn, winner, log)
}

fun stateToJson(s: State): String {
    val sb = StringBuilder()
    sb.append("{\n  \"board\": [\n")
    for (i in 0 until 3) {
        sb.append("    [\"${s.board[i][0]}\", \"${s.board[i][1]}\", \"${s.board[i][2]}\"]")
        if (i < 2) sb.append(",")
        sb.append("\n")
    }
    sb.append("  ],\n  \"turn\": \"${s.turn}\",\n")
    sb.append("  \"winner\": ").append(if (s.winner == null) "null" else "\"${s.winner}\"").append(",\n")
    sb.append("  \"log\": [\n")
    for (i in s.log.indices) {
        val m = s.log[i]
        sb.append("    {\"player\": \"${m.player}\", \"cell\": \"${m.cell}\"}")
        if (i < s.log.size - 1) sb.append(",")
        sb.append("\n")
    }
    sb.append("  ]\n}")
    return sb.toString()
}

fun checkWinner(b: List<List<String>>): String? {
    val lines = listOf(listOf(0,1,2),listOf(3,4,5),listOf(6,7,8),listOf(0,3,6),listOf(1,4,7),listOf(2,5,8),listOf(0,4,8),listOf(2,4,6))
    val flat = b.flatten()
    for (l in lines) {
        if (flat[l[0]].isNotEmpty() && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]]) return flat[l[0]]
    }
    return null
}


```
</details>

<!-- BOARD_KOTLIN_END -->

### PHP
<!-- BOARD_PHP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+PHP+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) | ❌ | **3** |
|   | A | B | C |   |

🎮 **Next Move: ⭕ (PHP)**

Recent moves: ❌ B2 → ⭕ A1 → ❌ C3

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (PHP)
```php
<?php
$state = json_decode(file_get_contents('current_state.json'), true);

$cell = getenv('CELL') ? strtoupper(getenv('CELL')) : '';
$action = getenv('ACTION') ?: 'put';

function check_winner($b) {
    $lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    $flat = array_merge(...$b);
    foreach ($lines as $l) {
        if ($flat[$l[0]] && $flat[$l[0]] === $flat[$l[1]] && $flat[$l[0]] === $flat[$l[2]]) return $flat[$l[0]];
    }
    return null;
}

if ($action === 'reset') {
    $is_full = true;
    foreach ($state['board'] as $row) foreach ($row as $c) if ($c === '') $is_full = false;
    if ($state['winner'] !== null || $is_full) {
        $state = ["board" => [["","",""],["","",""],["","",""]], "turn" => "X", "winner" => null, "log" => []];
    }
} else if ($cell && $state['winner'] === null) {
    $r = (int)$cell[1] - 1;
    $c = ord($cell[0]) - ord('A');
    if ($r >= 0 && $r < 3 && $c >= 0 && $c < 3 && $state['board'][$r][$c] === '') {
        $state['board'][$r][$c] = $state['turn'];
        $state['log'][] = ["player" => $state['turn'], "cell" => $cell];
        $win = check_winner($state['board']);
        if ($win) $state['winner'] = $win;
        else {
            $full = true;
            foreach ($state['board'] as $row) foreach ($row as $x) if ($x === '') $full = false;
            if ($full) $state['winner'] = 'draw';
            else $state['turn'] = $state['turn'] === 'X' ? 'O' : 'X';
        }
    }
}

file_put_contents('current_state.json', json_encode($state, JSON_PRETTY_PRINT));

```
</details>

<!-- BOARD_PHP_END -->

### Python
<!-- BOARD_PYTHON_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Python+board) | ⭕ | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Python+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Python+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Python+board) | ❌ | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (Python)**

Recent moves: ❌ B2 → ⭕ A1 → ❌ C3 → ⭕ C1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
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
    # Only allow reset if game is finished
    is_full = all(all(x != '' for x in row) for row in s['board'])
    if s.get('winner') or is_full:
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

### Ruby
<!-- BOARD_RUBY_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Ruby+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Ruby+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) | ❌ | **3** |
|   | A | B | C |   |

🎮 **Next Move: ⭕ (Ruby)**

Recent moves: ❌ B2 → ⭕ A1 → ❌ C3

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Ruby)
```ruby
require 'json'

state = JSON.parse(File.read('current_state.json'))

cell = (ENV['CELL'] || '').upcase
action = ENV['ACTION'] || 'put'

def check_winner(b)
  lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  flat = b.flatten
  lines.each do |l|
    return flat[l[0]] if flat[l[0]] != '' && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]]
  end
  nil
end

if action == 'reset'
  is_full = state['board'].flatten.all? { |c| c != '' }
  if state['winner'] || is_full
    state = {"board" => [["","",""],["","",""],["","",""]], "turn" => "X", "winner" => nil, "log" => []}
  end
elsif cell != '' && !state['winner']
  r = cell[1].to_i - 1
  c = cell[0].ord - 'A'.ord
  if r >= 0 && r < 3 && c >= 0 && c < 3 && state['board'][r][c] == ''
    state['board'][r][c] = state['turn']
    state['log'] << {"player" => state['turn'], "cell" => cell}
    win = check_winner(state['board'])
    if win
      state['winner'] = win
    elsif state['board'].flatten.all? { |x| x != '' }
      state['winner'] = 'draw'
    else
      state['turn'] = state['turn'] == 'X' ? 'O' : 'X'
    end
  end
end

File.write('current_state.json', JSON.pretty_generate(state))

```
</details>

<!-- BOARD_RUBY_END -->

### Rust
<!-- BOARD_RUST_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Rust+board) | **1** |
| **2** | ❌ | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Rust+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Rust+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (Rust)**

Recent moves: ❌ A2 → ⭕ B2 → ❌ B1 → ⭕ A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Rust)
```rust
use serde::{Deserialize, Serialize};
use std::env;
use std::fs;

#[derive(Serialize, Deserialize, Clone)]
struct Move { player: String, cell: String }

#[derive(Serialize, Deserialize)]
struct State { board: Vec<Vec<String>>, turn: String, winner: Option<String>, log: Vec<Move> }

fn main() {
    let data = fs::read_to_string("current_state.json").unwrap();
    let mut state: State = serde_json::from_str(&data).unwrap();

    let cell = env::var("CELL").unwrap_or_default().to_uppercase();
    let action = env::var("ACTION").unwrap_or_else(|_| "put".to_string());

    if action == "reset" {
        let is_full = state.board.iter().all(|row| row.iter().all(|c| !c.is_empty()));
        if state.winner.is_some() || is_full {
            state.board = vec![vec!["".to_string(); 3]; 3];
            state.turn = "X".to_string();
            state.winner = None;
            state.log = vec![];
        }
    } else if !cell.is_empty() && state.winner.is_none() {
        let r = (cell.chars().nth(1).unwrap() as u8 - b'1') as usize;
        let c = (cell.chars().nth(0).unwrap() as u8 - b'A') as usize;
        if r < 3 && c < 3 && state.board[r][c].is_empty() {
            state.board[r][c] = state.turn.clone();
            state.log.push(Move { player: state.turn.clone(), cell: cell.clone() });
            if let Some(win) = check_winner(&state.board) {
                state.winner = Some(win);
            } else if state.board.iter().all(|row| row.iter().all(|x| !x.is_empty())) {
                state.winner = Some("draw".to_string());
            } else {
                state.turn = if state.turn == "X" { "O".to_string() } else { "X".to_string() };
            }
        }
    }
    fs::write("current_state.json", serde_json::to_string_pretty(&state).unwrap()).unwrap();
}

fn check_winner(b: &[Vec<String>]) -> Option<String> {
    let lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    let flat: Vec<_> = b.iter().flatten().collect();
    for l in lines {
        if !flat[l[0]].is_empty() && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]] {
            return Some(flat[l[0]].clone());
        }
    }
    None
}

```
</details>

<!-- BOARD_RUST_END -->

### Scala
<!-- BOARD_SCALA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Scala+board) | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Scala+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Scala+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Scala+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Scala+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (Scala)**

Recent moves: ❌ B2 → ⭕ B1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Scala)
```scala
import java.nio.file.{Files, Paths}
import scala.collection.mutable.ListBuffer

case class Move(player: String, cell: String)
case class State(var board: List[List[String]], var turn: String, var winner: String, var log: List[Move])

object Game {
  def main(args: Array[String]): Unit = {
    val path = Paths.get("current_state.json")
    val json = new String(Files.readAllBytes(path))
    val state = parseState(json)

    val cell = sys.env.getOrElse("CELL", "").toUpperCase
    val action = sys.env.getOrElse("ACTION", "put")

    if (action == "reset") {
      val isFull = state.board.flatten.forall(_.nonEmpty)
      if ((state.winner != null && state.winner != "null") || isFull) {
        state.board = List(List("","",""), List("","",""), List("","",""))
        state.turn = "X"
        state.winner = null
        state.log = List()
      }
    } else if (cell.nonEmpty && (state.winner == null || state.winner == "null")) {
      val r = cell(1) - '1'
      val c = cell(0) - 'A'
      if (r >= 0 && r < 3 && c >= 0 && c < 3 && state.board(r)(c).isEmpty) {
        state.board = state.board.updated(r, state.board(r).updated(c, state.turn))
        state.log = state.log :+ Move(state.turn, cell)
        val win = checkWinner(state.board)
        if (win.isDefined) state.winner = win.get
        else if (state.board.flatten.forall(_.nonEmpty)) state.winner = "draw"
        else state.turn = if (state.turn == "X") "O" else "X"
      }
    }
    Files.write(path, stateToJson(state).getBytes)
  }

  def parseState(json: String): State = {
    var board = List(List("","",""), List("","",""), List("","",""))
    var turn = "X"
    var winner: String = "null"
    val log = ListBuffer[Move]()

    if (json.contains("\"board\"")) {
      val boardIdx = json.indexOf("\"board\"")
      val startIdx = json.indexOf("[", boardIdx)
      var row = 0
      var pos = startIdx + 1
      val newBoard = ListBuffer[List[String]]()
      while (row < 3) {
        val rowStart = json.indexOf("[", pos)
        if (rowStart == -1) {
           newBoard += List("","","")
        } else {
          val rowEnd = json.indexOf("]", rowStart)
          val rowStr = json.substring(rowStart + 1, rowEnd)
          val cells = rowStr.split(",").map(_.trim.replace("\"", ""))
          val cellList = ListBuffer[String]()
          for (col <- 0 until 3) {
            if (col < cells.length) cellList += cells(col) else cellList += ""
          }
          newBoard += cellList.toList
          pos = rowEnd + 1
        }
        row += 1
      }
      board = newBoard.toList
    }

    if (json.contains("\"turn\"")) {
      val idx = json.indexOf("\"turn\"")
      val valStart = json.indexOf("\"", json.indexOf(":", idx))
      val valEnd = json.indexOf("\"", valStart + 1)
      turn = json.substring(valStart + 1, valEnd)
    }

    if (json.contains("\"winner\"")) {
      val idx = json.indexOf("\"winner\"")
      val colonIdx = json.indexOf(":", idx)
      val nextQuote = json.indexOf("\"", colonIdx)
      val nextComma = json.indexOf(",", colonIdx)
      val nextBrace = json.indexOf("}", colonIdx)
      val end = if (nextComma != -1) nextComma else nextBrace
      val value = json.substring(colonIdx + 1, end).trim
      if (value.startsWith("\"")) {
        winner = value.substring(1, value.lastIndexOf("\""))
      } else {
        winner = value // e.g. null
      }
    }

    if (json.contains("\"log\"")) {
      val idx = json.indexOf("\"log\"")
      val start = json.indexOf("[", idx)
      val end = json.lastIndexOf("]")
      val logContent = json.substring(start + 1, end).trim
      if (logContent.nonEmpty) {
        val entries = logContent.split("}")
        for (entry <- entries) {
          if (entry.contains("{")) {
            val pIdx = entry.indexOf("\"player\"")
            val pValStart = entry.indexOf("\"", entry.indexOf(":", pIdx))
            val pValEnd = entry.indexOf("\"", pValStart + 1)
            val p = entry.substring(pValStart + 1, pValEnd)
            
            val cIdx = entry.indexOf("\"cell\"")
            val cValStart = entry.indexOf("\"", entry.indexOf(":", cIdx))
            val cValEnd = entry.indexOf("\"", cValStart + 1)
            val c = entry.substring(cValStart + 1, cValEnd)
            log += Move(p, c)
          }
        }
      }
    }

    State(board, turn, winner, log.toList)
  }

  def stateToJson(s: State): String = {
    val sb = new StringBuilder()
    sb.append("{\n  \"board\": [\n")
    for (i <- 0 until 3) {
      sb.append(s"    [\"${s.board(i)(0)}\", \"${s.board(i)(1)}\", \"${s.board(i)(2)}\"]")
      if (i < 2) sb.append(",")
      sb.append("\n")
    }
    sb.append("  ],\n")
    sb.append(s"  \"turn\": \"${s.turn}\",\n")
    sb.append(s"  \"winner\": ${if (s.winner == null || s.winner == "null") "null" else "\"" + s.winner + "\""},\n")
    sb.append("  \"log\": [\n")
    for (i <- s.log.indices) {
      val m = s.log(i)
      sb.append(s"    {\"player\": \"${m.player}\", \"cell\": \"${m.cell}\"}")
      if (i < s.log.size - 1) sb.append(",")
      sb.append("\n")
    }
    sb.append("  ]\n}")
    sb.toString()
  }

  def checkWinner(b: List[List[String]]): Option[String] = {
    val lines = List(List(0,1,2),List(3,4,5),List(6,7,8),List(0,3,6),List(1,4,7),List(2,5,8),List(0,4,8),List(2,4,6))
    val flat = b.flatten
    lines.collectFirst {
      case l if flat(l(0)).nonEmpty && flat(l(0)) == flat(l(1)) && flat(l(0)) == flat(l(2)) => flat(l(0))
    }
  }
}


```
</details>

<!-- BOARD_SCALA_END -->

### Swift
<!-- BOARD_SWIFT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Swift+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Swift+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Swift+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Swift+board) | ⭕ | **3** |
|   | A | B | C |   |

🎮 **Next Move: ⭕ (Swift)**

Recent moves: ❌ B2 → ⭕ C3 → ❌ A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (Swift)
```swift
import Foundation

struct Move: Codable { let player: String; let cell: String }
struct State: Codable { var board: [[String]]; var turn: String; var winner: String?; var log: [Move] }

func main() {
    let fileURL = URL(fileURLWithPath: "current_state.json")
    let data = try! Data(contentsOf: fileURL)
    var state = try! JSONDecoder().decode(State.self, from: data)

    let env = ProcessInfo.processInfo.environment
    let cell = env["CELL"]?.uppercased() ?? ""
    let action = env["ACTION"] ?? "put"

    if action == "reset" {
        let isFull = state.board.flatMap { $0 }.allSatisfy { !$0.isEmpty }
        if state.winner != nil || isFull {
            state.board = [["","",""],["","",""],["","",""]]
            state.turn = "X"
            state.winner = nil
            state.log = []
        }
    } else if !cell.isEmpty && state.winner == nil {
        let r = Int(String(cell.suffix(1)))! - 1
        let c = Int(cell.first!.asciiValue! - Character("A").asciiValue!)
        if r >= 0 && r < 3 && c >= 0 && c < 3 && state.board[r][c].isEmpty {
            state.board[r][c] = state.turn
            state.log.append(Move(player: state.turn, cell: cell))
            if let win = checkWinner(state.board) {
                state.winner = win
            } else if state.board.flatMap({ $0 }).allSatisfy({ !$0.isEmpty }) {
                state.winner = "draw"
            } else {
                state.turn = (state.turn == "X") ? "O" : "X"
            }
        }
    }
    let encoder = JSONEncoder(); encoder.outputFormatting = .prettyPrinted
    try! encoder.encode(state).write(to: fileURL)
}

func checkWinner(_ b: [[String]]) -> String? {
    let lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    let flat = b.flatMap { $0 }
    for l in lines {
        if !flat[l[0]].isEmpty && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]] { return flat[l[0]] }
    }
    return nil
}
main()

```
</details>

<!-- BOARD_SWIFT_END -->

### TypeScript
<!-- BOARD_TYPESCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+TypeScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+TypeScript+board) | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+TypeScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+TypeScript+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: ❌ (TypeScript)**

Recent moves: ❌ B2 → ⭕ A1

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: ``
- **Output (Information given)**:
```text
Success
```

### 💻 Implementation Code (TypeScript)
```typescript
import * as fs from 'fs';

interface Move {
  player: string;
  cell: string;
}

interface State {
  board: string[][];
  turn: string;
  winner: string | null;
  log: Move[];
}

const state: State = JSON.parse(fs.readFileSync('current_state.json', 'utf8'));

const cell = process.env.CELL ? process.env.CELL.toUpperCase() : '';
const action = process.env.ACTION || 'put';

function checkWinner(b: string[][]): string | null {
  const lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  const flat = b.flat();
  for (let l of lines) {
    if (flat[l[0]] && flat[l[0]] === flat[l[1]] && flat[l[0]] === flat[l[2]]) return flat[l[0]];
  }
  return null;
}

if (action === 'reset') {
  const isFull = state.board.every(row => row.every(c => c !== ''));
  if (state.winner || isFull) {
    state.board = [['','',''],['','',''],['','','']];
    state.turn = 'X';
    state.winner = null;
    state.log = [];
  }
} else if (cell && !state.winner) {
  const r = parseInt(cell[1]) - 1;
  const c = cell.charCodeAt(0) - 65;
  if (r >= 0 && r < 3 && c >= 0 && c < 3 && state.board[r][c] === '') {
    state.board[r][c] = state.turn;
    state.log.push({ player: state.turn, cell });
    const win = checkWinner(state.board);
    if (win) state.winner = win;
    else if (state.board.flat().every(x => x !== '')) state.winner = 'draw';
    else state.turn = state.turn === 'X' ? 'O' : 'X';
  }
}

fs.writeFileSync('current_state.json', JSON.stringify(state, null, 2));

```
</details>

<!-- BOARD_TYPESCRIPT_END -->

---

<p align="center">
  Developed by <a href="https://github.com/tdnb2b2">@tdnb2b2</a><br>
  Built with ❤️ and 🤖
</p>
