# 🕹️ Polyglot Tic-Tac-Toe on GitHub README

このリポジトリは、GitHubのIssues機能を使って実際にプレイできる、**複数のプログラミング言語で実装された**三目並べ（Tic-Tac-Toe）です！

## 🚀 遊び方
1. 下のボードの空いているマス（`___`）のリンクをクリックします。
2. Issue作成画面が開くので、「Submit new issue」ボタンを押します。
3. GitHub Actionsが自動的にあなたの手を処理し、READMEを更新します！

---

## 🏗️ Languages
| Language | Board Link | Status |
|---|---|---|
| C | [#c-board](#c) | Interactive |
| C++ | [#cpp-board](#cpp) | Interactive |
| C# | [#csharp-board](#c) | Interactive |
| Go | [#go-board](#go) | Interactive |
| Java | [#java-board](#java) | Interactive |
| JavaScript | [#javascript-board](#javascript) | Interactive |
| Kotlin | [#kotlin-board](#kotlin) | Interactive |
| PHP | [#php-board](#php) | Interactive |
| Python | [#python-board](#python) | Interactive |
| Ruby | [#ruby-board](#ruby) | Interactive |
| Rust | [#rust-board](#rust) | Interactive |
| Scala | [#scala-board](#scala) | Interactive |
| Swift | [#swift-board](#swift) | Interactive |
| TypeScript | [#typescript-board](#typescript) | Interactive |

---

## 🎮 Current Language Board
<!-- BOARD_LANG_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | ❌ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Python+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Python+board) | ⭕ | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Python+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Python+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Python)**

Recent moves: X A1 → O B2

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `Python: Tic-Tac-Toe: Put A1`
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

<!-- BOARD_LANG_END -->

---

## 🛠️ Individual Boards

### C
<!-- BOARD_C_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (C)**

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
                while (*p == ' ' || *p == '
') p++;
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
                        existing_log[len] = ' ';
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
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+++board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+++board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+++board) | **3** |
|   | A | B | C |   |

🎮 **Next Move: X (Cpp)**

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
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void write_state(char b[3][3], string turn, string winner, string existing_log, string new_move) {
    ofstream f("current_state.json");
    f << "{
  \"board\": [
";
    for(int i=0; i<3; i++) {
        f << "    [\"" << (b[i][0]?string(1,b[i][0]):"") << "\", \"" << (b[i][1]?string(1,b[i][1]):"") << "\", \"" << (b[i][2]?string(1,b[i][2]):"") << "\"]" << (i==2?"":",") << "
";
    }
    string log_content = existing_log;
    if (new_move != "") {
        if (log_content.find("{") != string::npos) log_content += ", ";
        log_content += new_move;
    }
    f << "  ],
  \"turn\": \"" << turn << "\",
  \"winner\": " << (winner==""?"null":"\""+winner+"\"") << ",
  \"log\": [" << log_content << "]
}";
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
            full_content += f_line + "
";
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
                while(p < full_content.length() && (full_content[p] == ' ' || full_content[p] == '
')) p++;
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
                size_t first = existing_log.find_first_not_of(" 
	");
                size_t last = existing_log.find_last_not_of(" 
	");
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

(Other boards...)

---

<p align="center">
  Developed by <a href=\"https://github.com/tdnb2b2\">@tdnb2b2</a><br>
  Built with ❤️ and 🤖
</p>
