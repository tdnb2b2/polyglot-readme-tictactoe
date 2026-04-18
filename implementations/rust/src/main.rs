use serde::{Deserialize, Serialize};
use std::{env, fs};

#[derive(Serialize, Deserialize)]
struct GameState {
    board: Vec<Vec<String>>,
    turn: String,
    winner: Option<String>,
    log: Vec<serde_json::Value>,
}

fn main() {
    let data = fs::read_to_string("current_state.json").unwrap();
    let mut s: GameState = serde_json::from_str(&data).unwrap();
    let cell = env::var("CELL").unwrap_or_default().to_uppercase();
    let action = env::var("ACTION").unwrap_or_default();

    if action == "reset" {
        s.board = vec![vec!["".to_string(); 3]; 3];
        s.turn = "X".to_string(); s.winner = None; s.log = vec![];
    } else if !cell.is_empty() && s.winner.is_none() {
        let r = (cell.chars().nth(1).unwrap() as u8 - b'1') as usize;
        let c = (cell.chars().next().unwrap() as u8 - b'A') as usize;
        if r < 3 && c < 3 && s.board[r][c].is_empty() {
            s.board[r][c] = s.turn.clone();
            let lns = vec![
                (0,0,0,1,0,2),(1,0,1,1,1,2),(2,0,2,1,2,2),
                (0,0,1,0,2,0),(0,1,1,1,2,1),(0,2,1,2,2,2),
                (0,0,1,1,2,2),(0,2,1,1,2,0)
            ];
            let win = lns.iter().any(|&(r1,c1,r2,c2,r3,c3)| 
                !s.board[r1][c1].is_empty() && s.board[r1][c1] == s.board[r2][c2] && s.board[r2][c2] == s.board[r3][c3]
            );
            if win { s.winner = Some(s.turn.clone()); }
            else if s.board.iter().all(|row| row.iter().all(|v| !v.is_empty())) { s.winner = Some("draw".to_string()); }
            else { s.turn = if s.turn == "X" { "O".to_string() } else { "X".to_string() }; }
        }
    }
    fs::write("current_state.json", serde_json::to_string_pretty(&s).unwrap()).unwrap();
}
