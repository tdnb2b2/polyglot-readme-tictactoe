<?php
$state = json_decode(file_get_contents('current_state.json'), true);

$cell = getenv('CELL') ? strtoupper(getenv('CELL')) : '';
$action = getenv('ACTION') ?: 'put';

function check_winner($b) {
    $lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    $flat = array_merge(...$b);
    foreach ($lines as $l) {
        if ($flat[$l[0]] && $flat[$l[0]] === $flat[$l[1]] && $flat[$l[0]] === $flat[$l[2]]) return $flat[$l[0]];
    }
    return null;
}

if ($action === 'reset') {
    $is_full = true;
    foreach ($state['board'] as $row) foreach ($row as $c) if ($c === '') $is_full = false;
    if ($state['winner'] !== null || $is_full) {
        $state = ["board" => [["","",""],["","",""],["","",""]], "turn" => "X", "winner" => null, "log" => []];
    }
} else if ($cell && $state['winner'] === null) {
    $r = (int)$cell[1] - 1;
    $c = ord($cell[0]) - ord('A');
    if ($r >= 0 && $r < 3 && $c >= 0 && $c < 3 && $state['board'][$r][$c] === '') {
        $state['board'][$r][$c] = $state['turn'];
        $state['log'][] = ["player" => $state['turn'], "cell" => $cell];
        $win = check_winner($state['board']);
        if ($win) $state['winner'] = $win;
        else {
            $full = true;
            foreach ($state['board'] as $row) foreach ($row as $x) if ($x === '') $full = false;
            if ($full) $state['winner'] = 'draw';
            else $state['turn'] = $state['turn'] === 'X' ? 'O' : 'X';
        }
    }
}

file_put_contents('current_state.json', json_encode($state, JSON_PRETTY_PRINT));
