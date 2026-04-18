#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void write_state(char b[3][3], string turn, string winner) {
    ofstream f("current_state.json");
    f << "{\n  \"board\": [\n";
    for(int i=0; i<3; i++) {
        f << "    [\"" << (b[i][0]?string(1,b[i][0]):"") << "\", \"" << (b[i][1]?string(1,b[i][1]):"") << "\", \"" << (b[i][2]?string(1,b[i][2]):"") << "\"]" << (i==2?"":",") << "\n";
    }
    f << "  ],\n  \"turn\": \"" << turn << "\",\n  \"winner\": " << (winner==""?"null":"\""+winner+"\"") << ",\n  \"log\": []\n}";
}

int main() {
    char b[3][3] = {0};
    string turn = "X";
    string action = getenv("ACTION")?getenv("ACTION"):"put";
    string cell = getenv("CELL")?getenv("CELL"):"";

    ifstream f("current_state.json");
    string line;
    int r=0;
    while(getline(f, line)) {
        if(line.find("[") != string::npos && line.find("board") == string::npos) {
            if(line.find("\"X\"") != string::npos) b[r][0] = 'X'; else if(line.find("\"O\"") != string::npos) b[r][0] = 'O';
            size_t pos = line.find(",");
            if(pos != string::npos) {
                if(line.find("\"X\"", pos) != string::npos) b[r][1] = 'X'; else if(line.find("\"O\"", pos) != string::npos) b[r][1] = 'O';
                pos = line.find(",", pos+1);
                if(pos != string::npos) {
                   if(line.find("\"X\"", pos) != string::npos) b[r][2] = 'X'; else if(line.find("\"O\"", pos) != string::npos) b[r][2] = 'O';
                }
            }
            if(r<2) r++;
        }
        if(line.find("\"turn\": \"O\"") != string::npos) turn = "O";
    }

    if(action == "reset") {
        char empty_b[3][3] = {0};
        write_state(empty_b, "X", "");
    }
    else if(cell != "") {
        int row = cell[1]-'1', col = cell[0]-'A';
        if(row>=0 && row<3 && col>=0 && col<3 && b[row][col]==0) {
            b[row][col] = turn[0];
            int lns[8][6] = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
            bool win = false;
            for(int i=0; i<8; i++) if(b[lns[i][0]][lns[i][1]] && b[lns[i][0]][lns[i][1]]==b[lns[i][2]][lns[i][3]] && b[lns[i][2]][lns[i][3]]==b[lns[i][4]][lns[i][5]]) win=true;
            if(win) write_state(b, turn, turn);
            else {
                bool full = true; for(int i=0; i<3; i++) for(int j=0; j<3; j++) if(b[i][j]==0) full=false;
                if(full) write_state(b, turn, "draw");
                else write_state(b, (turn=="X"?"O":"X"), "");
            }
        }
    }
    return 0;
}
