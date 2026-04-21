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
