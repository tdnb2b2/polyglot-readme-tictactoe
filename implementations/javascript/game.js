const fs = require('fs');
const state = JSON.parse(fs.readFileSync('current_state.json', 'utf8'));

const cell = process.env.CELL ? process.env.CELL.toUpperCase() : '';
const action = process.env.ACTION || 'put';

function checkWinner(b) {
  const lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  const flat = b.flat();
  for (let l of lines) {
    if (flat[l[0]] && flat[l[0]] === flat[l[1]] && flat[l[0]] === flat[l[2]]) return flat[l[0]];
  }
  return null;
}

if (action === 'reset') {
  const isFull = state.board.every(row => row.every(c => c !== ''));
  if (state.winner || isFull) {
    state.board = [['','',''],['','',''],['','','']];
    state.turn = 'X';
    state.winner = null;
    state.log = [];
  }
} else if (cell && !state.winner) {
  const r = parseInt(cell[1]) - 1;
  const c = cell.charCodeAt(0) - 65;
  if (r >= 0 && r < 3 && c >= 0 && c < 3 && state.board[r][c] === '') {
    state.board[r][c] = state.turn;
    state.log.push({ player: state.turn, cell });
    const win = checkWinner(state.board);
    if (win) state.winner = win;
    else if (state.board.flat().every(x => x !== '')) state.winner = 'draw';
    else state.turn = state.turn === 'X' ? 'O' : 'X';
  }
}

fs.writeFileSync('current_state.json', JSON.stringify(state, null, 2));
