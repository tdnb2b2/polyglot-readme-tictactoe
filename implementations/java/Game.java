import java.nio.file.*;
import java.util.regex.*;

public class Game {
    public static void main(String[] args) throws Exception {
        String path = "current_state.json";
        String content = Files.readString(Path.of(path));
        String cell = System.getenv("CELL");
        String action = System.getenv("ACTION");
        
        if ("reset".equals(action)) {
            Files.writeString(Path.of(path), "{\n  \"board\": [[\"\",\"\",\"\"],[\"\",\"\",\"\"],[\"\",\"\",\"\"]],\n  \"turn\": \"X\",\n  \"winner\": null,\n  \"log\": []\n}");
            return;
        }

        if (cell == null || cell.length() < 2) return;
        cell = cell.toUpperCase();

        // Extract values from JSON (Minimalist approach)
        String winner = getJsonValue(content, "winner");
        if (!"null".equals(winner)) return;

        String turn = getJsonValue(content, "turn");
        String[][] board = new String[3][3];
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) board[i][j] = "";
        Pattern p = Pattern.compile("\\[\"(.*?)\",\"(.*?)\",\"(.*?)\"\\]");
        Matcher m = p.matcher(content);
        for (int i = 0; i < 3 && m.find(); i++) {
            board[i][0] = m.group(1);
            board[i][1] = m.group(2);
            board[i][2] = m.group(3);
        }

        // Correct Mapping: r is row (1-3), c is col (A-C)
        int r = cell.charAt(1) - '1';
        int c = cell.charAt(0) - 'A';

        if (r >= 0 && r < 3 && c >= 0 && c < 3 && board[r][c].isEmpty()) {
            board[r][c] = turn;
            
            String win = checkWinner(board);
            String nextTurn = turn.equals("X") ? "O" : "X";
            boolean draw = isDraw(board);

            // Reconstruct JSON
            StringBuilder sb = new StringBuilder();
            sb.append("{\n  \"board\": [\n");
            for (int i = 0; i < 3; i++) {
                sb.append("    [\"").append(board[i][0]).append("\",\"").append(board[i][1]).append("\",\"").append(board[i][2]).append("\"]");
                if (i < 2) sb.append(",");
                sb.append("\n");
            }
            sb.append("  ],\n  \"turn\": \"").append(nextTurn).append("\",\n");
            sb.append("  \"winner\": ").append(win != null ? "\"" + win + "\"" : (draw ? "\"draw\"" : "null")).append(",\n");
            sb.append("  \"log\": []\n}"); // Simplified log for Java
            Files.writeString(Path.of(path), sb.toString());
        }
    }

    static String getJsonValue(String json, String key) {
        Pattern p = Pattern.compile("\"" + key + "\":\\s*\"?(.*?)\"?(?:,|\\n|\\})");
        Matcher m = p.matcher(json);
        if (m.find()) return m.group(1).trim();
        return "null";
    }

    static String checkWinner(String[][] b) {
        int[][] lns = {{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2}, {0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2}, {0,0,1,1,2,2},{0,2,1,1,2,0}};
        for (int[] l : lns) {
            if (!b[l[0]][l[1]].isEmpty() && b[l[0]][l[1]].equals(b[l[2]][l[3]]) && b[l[2]][l[3]].equals(b[l[4]][l[5]])) return b[l[0]][l[1]];
        }
        return null;
    }

    static boolean isDraw(String[][] b) {
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) if (b[i][j].isEmpty()) return false;
        return true;
    }
}
