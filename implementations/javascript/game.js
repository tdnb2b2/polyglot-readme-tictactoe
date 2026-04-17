const fs = require('fs');
const s = JSON.parse(fs.readFileSync('current_state.json'));
const cell = (process.env.CELL || "").toUpperCase();
const action = process.env.ACTION || "put";

if (action === 'reset') {
    s.board = [["","",""],["","",""],["","",""]];
    s.turn = "X"; s.winner = null; s.log = [];
} else if (cell && !s.winner) {
    const r = cell.charCodeAt(0) - 65, c = parseInt(cell[1]) - 1;
    if (r >= 0 && r < 3 && c >= 0 && c < 3 && s.board[r][c] === "") {
        s.board[r][c] = s.turn;
        s.log.push({player: s.turn, cell});
        const lines = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]], [[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]];
        let win = lines.find(l => l.every(([r2,c2]) => s.board[r2][c2] === s.turn));
        if (win) s.winner = s.turn;
        else if (s.board.flat().every(v => v !== "")) s.winner = "draw";
        else s.turn = s.turn === "X" ? "O" : "X";
    }
}
fs.writeFileSync('current_state.json', JSON.stringify(s, null, 2));
