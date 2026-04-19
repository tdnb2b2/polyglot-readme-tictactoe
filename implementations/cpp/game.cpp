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
    int r=0;
    if (f.is_open()) {
        while(getline(f, f_line)) {
            full_content += f_line + "\n";
            if(f_line.find("[") != string::npos && f_line.find("board") == string::npos && f_line.find("log") == string::npos) {
                if(f_line.find("\"X\"") != string::npos) b[r][0] = 'X'; else if(f_line.find("\"O\"") != string::npos) b[r][0] = 'O';
                size_t pos = f_line.find(",");
                if(pos != string::npos) {
                    if(f_line.find("\"X\"", pos) != string::npos) b[r][1] = 'X'; else if(f_line.find("\"O\"", pos) != string::npos) b[r][1] = 'O';
                    pos = f_line.find(",", pos+1);
                    if(pos != string::npos) {
                        if(f_line.find("\"X\"", pos) != string::npos) b[r][2] = 'X'; else if(f_line.find("\"O\"", pos) != string::npos) b[r][2] = 'O';
                    }
                }
                if(r<2) r++;
            }
            if(f_line.find("\"turn\": \"O\"") != string::npos) turn = "O";
            if(f_line.find("\"winner\":") != string::npos) {
                size_t p1 = f_line.find(":");
                size_t p2 = f_line.find_first_of("\",\n", p1+1);
                size_t p3 = f_line.find_last_of("\"", p2);
                winnerStr = f_line.substr(p1+1);
                if (winnerStr.find("null") != string::npos) winnerStr = "null";
                else if (winnerStr.find("X") != string::npos) winnerStr = "X";
                else if (winnerStr.find("O") != string::npos) winnerStr = "O";
                else if (winnerStr.find("draw") != string::npos) winnerStr = "draw";
            }
        }
        f.close();
    }

    if (winnerStr != "null") return 0;

    string existing_log = "";
    size_t log_start = full_content.find("\"log\": [");
    if(log_start != string::npos) {
        log_start += 8;
        size_t log_end = full_content.find("]", log_start);
        if(log_end != string::npos) {
            existing_log = full_content.substr(log_start, log_end - log_start);
            size_t first = existing_log.find_first_not_of(" \n\r\t");
            size_t last = existing_log.find_last_not_of(" \n\r\t");
            if (first != string::npos && last != string::npos) existing_log = existing_log.substr(first, last - first + 1);
            else existing_log = "";
        }
    }

    if(action == "reset") {
        char empty_b[3][3] = {0};
        write_state(empty_b, "X", "", "", "");
    }
    else if(cell != "") {
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
