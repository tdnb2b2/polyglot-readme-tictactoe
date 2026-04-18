<?php
$s = json_decode(file_get_contents('current_state.json'), true);
$cell = strtoupper(getenv('CELL') ?: "");
$action = getenv('ACTION') ?: "put";

if ($action === 'reset') {
    $s = ['board'=>[['','',''],['','',''],['','','']], 'turn'=>'X', 'winner'=>null, 'log'=>[]];
} elseif ($cell && !$s['winner']) {
    $r = (int)$cell[1] - 1; $c = ord($cell[0]) - 65;
    if ($r>=0 && $r<3 && $c>=0 && $c<3 && $s['board'][$r][$c] === "") {
        $s['board'][$r][$c] = $s['turn'];
        $win = false;
        $lns = [[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2],[0,0,1,1,2,2],[0,2,1,1,2,0]];
        foreach($lns as $l) {
            if ($s['board'][$l[0]][$l[1]] && $s['board'][$l[0]][$l[1]] === $s['board'][$l[2]][$l[3]] && $s['board'][$l[2]][$l[3]] === $s['board'][$l[4]][$l[5]]) $win = true;
        }
        if ($win) $s['winner'] = $s['turn'];
        else {
            $full = true; foreach($s['board'] as $row) foreach($row as $v) if($v === "") $full = false;
            if ($full) $s['winner'] = 'draw';
            else $s['turn'] = $s['turn'] === "X" ? "O" : "X";
        }
    }
}
file_put_contents('current_state.json', json_encode($s, JSON_PRETTY_PRINT));
