package main

import (
	"encoding/json"
	"os"
	"strings"
)

type Move struct {
	Player string `json:"player"`
	Cell   string `json:"cell"`
}

type State struct {
	Board  [][]string `json:"board"`
	Turn   string     `json:"turn"`
	Winner *string    `json:"winner"`
	Log    []Move     `json:"log"`
}

func writeState(state State) {
	f, _ := os.Create("current_state.json")
	defer f.Close()
	enc := json.NewEncoder(f)
	enc.SetIndent("", "  ")
	enc.Encode(state)
}

func checkWinner(b [][]string) *string {
	lines := [][]int{{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}}
	flat := []string{}
	for _, row := range b {
		flat = append(flat, row...)
	}
	for _, l := range lines {
		if flat[l[0]] != "" && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]] {
			res := flat[l[0]]
			return &res
		}
	}
	return nil
}

func main() {
	f, _ := os.ReadFile("current_state.json")
	var state State
	json.Unmarshal(f, &state)

	cell := strings.ToUpper(os.Getenv("CELL"))
	action := os.Getenv("ACTION")
	if action == "" {
		action = "put"
	}

	if action == "reset" {
		isFull := true
		for _, row := range state.Board {
			for _, c := range row {
				if c == "" {
					isFull = false
				}
			}
		}
		if state.Winner != nil || isFull {
			state = State{
				Board:  [][]string{{"", "", ""}, {"", "", ""}, {"", "", ""}},
				Turn:   "X",
				Winner: nil,
				Log:    []Move{},
			}
		}
	} else if cell != "" && state.Winner == nil {
		r := int(cell[1]-'1')
		c := int(cell[0]-'A')
		if r >= 0 && r < 3 && c >= 0 && c < 3 && state.Board[r][c] == "" {
			state.Board[r][c] = state.Turn
			state.Log = append(state.Log, Move{Player: state.Turn, Cell: cell})
			win := checkWinner(state.Board)
			if win != nil {
				state.Winner = win
			} else {
				full := true
				for _, row := range state.Board {
					for _, x := range row {
						if x == "" {
							full = false
						}
					}
				}
				if full {
					d := "draw"
					state.Winner = &d
				} else {
					if state.Turn == "X" {
						state.Turn = "O"
					} else {
						state.Turn = "X"
					}
				}
			}
		}
	}

	writeState(state)
}
