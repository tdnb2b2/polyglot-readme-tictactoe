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
