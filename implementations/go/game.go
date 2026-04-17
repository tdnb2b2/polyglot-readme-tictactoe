package main
import (
    "encoding/json"; "os"; "strings"
)
type GameState struct {
    Board [][]string `json:"board"`
    Turn string `json:"turn"`
    Winner *string `json:"winner"`
    Log []interface{} `json:"log"`
}
func main() {
    b, _ := os.ReadFile("current_state.json")
    var s GameState
    json.Unmarshal(b, &s)
    cell := strings.ToUpper(os.Getenv("CELL"))
    action := os.Getenv("ACTION")
    if action == "reset" {
        s.Board = [][]string{{"","",""},{"","",""},{"","",""}}
        s.Turn = "X"; s.Winner = nil; s.Log = []interface{}{}
    } else if cell != "" && s.Winner == nil {
        r, c := int(cell[0]-'A'), int(cell[1]-'1')
        if r>=0 && r<3 && c>=0 && c<3 && s.Board[r][c] == "" {
            s.Board[r][c] = s.Turn
            win := false
            lns := [][]int{{0,0,0,1,0,2},{1,0,1,1,1,2},{2,0,2,1,2,2},{0,0,1,0,2,0},{0,1,1,1,2,1},{0,2,1,2,2,2},{0,0,1,1,2,2},{0,2,1,1,2,0}}
            for _, l := range lns {
                if s.Board[l[0]][l[1]] != "" && s.Board[l[0]][l[1]] == s.Board[l[2]][l[3]] && s.Board[l[2]][l[3]] == s.Board[l[4]][l[5]] { win = true }
            }
            if win { s.Winner = &s.Turn } else {
                full := true
                for _, row := range s.Board { for _, v := range row { if v == "" { full = false } } }
                if full { d := "draw"; s.Winner = &d } else { if s.Turn == "X" { s.Turn = "O" } else { s.Turn = "X" } }
            }
        }
    }
    out, _ := json.MarshalIndent(s, "", "  ")
    os.WriteFile("current_state.json", out, 0644)
}
