#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void write_state(char b[3][3], char* turn, char* winner) {
    FILE *f = fopen("current_state.json", "w");
    fprintf(f, "{\n  \"board\": [\n");
    for(int i=0; i<3; i++) {
        fprintf(f, "    [\"%s\", \"%s\", \"%s\"]%s\n", (b[i][0]? (char[]){b[i][0],0} : ""), (b[i][1]? (char[]){b[i][1],0} : ""), (b[i][2]? (char[]){b[i][2],0} : ""), (i==2?"":","));
    }
    fprintf(f, "  ],\n  \"turn\": \"%s\",\n  \"winner\": %s,\n  \"log\": []\n}", turn, winner? (strcmp(winner,"null")==0?"null": (char[]){'\"',winner[0],winner[1]?(winner[1]=='r'?'d':winner[0]):0,'\"',0} ) : "null");
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
