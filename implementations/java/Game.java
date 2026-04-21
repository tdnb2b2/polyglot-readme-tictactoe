import java.io.*;
import java.nio.file.*;
import java.util.*;
import com.google.gson.*;

public class Game {
    static class Move { String player; String cell; }
    static class State { String[][] board; String turn; String winner; List<Move> log; }

    public static void main(String[] args) throws Exception {
        Gson gson = new GsonBuilder().setPrettyPrinting().serializeNulls().create();
        String json = new String(Files.readAllBytes(Paths.get("current_state.json")));
        State state = gson.fromJson(json, State.class);

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
                Move m = new Move(); m.player = state.turn; m.cell = cell;
                state.log.add(m);
                String win = checkWinner(state.board);
                if (win != null) state.winner = win;
                else {
                    boolean full = true; for(String[] row : state.board) for(String x : row) if(x == null || x.isEmpty()) full = false;
                    if (full) state.winner = "draw";
                    else state.turn = state.turn.equals("X") ? "O" : "X";
                }
            }
        }
        Files.write(Paths.get("current_state.json"), gson.toJson(state).getBytes());
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
