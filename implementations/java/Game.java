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

