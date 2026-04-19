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
        char line[256];
        int r=0;
        int in_log = 0;
        while(fgets(line, sizeof(line), f)) {
            if(strstr(line, "[") && !strstr(line, "board") && !strstr(line, "log")) {
                if(strstr(line, "\"X\"")) b[r][0]='X'; else if(strstr(line, "\"O\"")) b[r][0]='O';
                char* p = strchr(line, ','); if(p) { if(strstr(p, "\"X\"")) b[r][1]='X'; else if(strstr(p, "\"O\"")) b[r][1]='O'; p=strchr(p+1,','); if(p) { if(strstr(p, "\"X\"")) b[r][2]='X'; else if(strstr(p, "\"O\"")) b[r][2]='O'; } }
                r++;
            }
            if(strstr(line, "\"turn\": \"O\"")) strcpy(turn, "O");
            if(strstr(line, "\"winner\":")) {
                if(strstr(line, "\"X\"")) strcpy(winnerStr, "X");
                else if(strstr(line, "\"O\"")) strcpy(winnerStr, "O");
                else if(strstr(line, "\"draw\"")) strcpy(winnerStr, "draw");
            }
            
            char* log_ptr = strstr(line, "\"log\": [");
            if(log_ptr) {
                in_log = 1;
                char* start = strchr(log_ptr, '[');
                if(start) {
                    char* end = strrchr(start, ']');
                    if(end) { 
                        *end = '\0';
                        strcat(existing_log, start + 1);
                        in_log = 0;
                    } else {
                        strcat(existing_log, start + 1);
                    }
                }
            } else if(in_log) {
                char* end = strrchr(line, ']');
                if(end) {
                    *end = '\0';
                    strcat(existing_log, line);
                    in_log = 0;
                } else {
                    strcat(existing_log, line);
                }
            }
        }
        fclose(f);
    }

    if(strcmp(winnerStr, "null") != 0) return 0;

    if(action && strcmp(action, "reset")==0) {
        write_state((char[3][3]){{0,0,0},{0,0,0},{0,0,0}}, "X", "null", "", NULL);
    } else if(cell && strlen(cell)>=2) {
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
