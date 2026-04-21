use serde::{Deserialize, Serialize};
use std::env;
use std::fs;

#[derive(Serialize, Deserialize, Clone)]
struct Move { player: String, cell: String }

#[derive(Serialize, Deserialize)]
struct State { board: Vec<Vec<String>>, turn: String, winner: Option<String>, log: Vec<Move> }

fn main() {
    let data = fs::read_to_string("current_state.json").unwrap();
    let mut state: State = serde_json::from_str(&data).unwrap();

    let cell = env::var("CELL").unwrap_or_default().to_uppercase();
    let action = env::var("ACTION").unwrap_or_else(|_| "put".to_string());

    if action == "reset" {
        let is_full = state.board.iter().all(|row| row.iter().all(|c| !c.is_empty()));
        if state.winner.is_some() || is_full {
            state.board = vec![vec!["".to_string(); 3]; 3];
            state.turn = "X".to_string();
            state.winner = None;
            state.log = vec![];
        }
    } else if !cell.is_empty() && state.winner.is_none() {
        let r = (cell.chars().nth(1).unwrap() as u8 - b'1') as usize;
        let c = (cell.chars().nth(0).unwrap() as u8 - b'A') as usize;
        if r < 3 && c < 3 && state.board[r][c].is_empty() {
            state.board[r][c] = state.turn.clone();
            state.log.push(Move { player: state.turn.clone(), cell: cell.clone() });
            if let Some(win) = check_winner(&state.board) {
                state.winner = Some(win);
            } else if state.board.iter().all(|row| row.iter().all(|x| !x.is_empty())) {
                state.winner = Some("draw".to_string());
            } else {
                state.turn = if state.turn == "X" { "O".to_string() } else { "X".to_string() };
            }
        }
    }
    fs::write("current_state.json", serde_json::to_string_pretty(&state).unwrap()).unwrap();
}

fn check_winner(b: &[Vec<String>]) -> Option<String> {
    let lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    let flat: Vec<_> = b.iter().flatten().collect();
    for l in lines {
        if !flat[l[0]].is_empty() && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]] {
            return Some(flat[l[0]].clone());
        }
    }
    None
}
