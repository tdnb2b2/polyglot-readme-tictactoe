import Foundation

struct Move: Codable { let player: String; let cell: String }
struct State: Codable { var board: [[String]]; var turn: String; var winner: String?; var log: [Move] }

func main() {
    let fileURL = URL(fileURLWithPath: "current_state.json")
    let data = try! Data(contentsOf: fileURL)
    var state = try! JSONDecoder().decode(State.self, from: data)

    let env = ProcessInfo.processInfo.environment
    let cell = env["CELL"]?.uppercased() ?? ""
    let action = env["ACTION"] ?? "put"

    if action == "reset" {
        let isFull = state.board.flatMap { $0 }.allSatisfy { !$0.isEmpty }
        if state.winner != nil || isFull {
            state.board = [["","",""],["","",""],["","",""]]
            state.turn = "X"
            state.winner = nil
            state.log = []
        }
    } else if !cell.isEmpty && state.winner == nil {
        let r = Int(String(cell.suffix(1)))! - 1
        let c = Int(cell.first!.asciiValue! - Character("A").asciiValue!)
        if r >= 0 && r < 3 && c >= 0 && c < 3 && state.board[r][c].isEmpty {
            state.board[r][c] = state.turn
            state.log.append(Move(player: state.turn, cell: cell))
            if let win = checkWinner(state.board) {
                state.winner = win
            } else if state.board.flatMap({ $0 }).allSatisfy({ !$0.isEmpty }) {
                state.winner = "draw"
            } else {
                state.turn = (state.turn == "X") ? "O" : "X"
            }
        }
    }
    let encoder = JSONEncoder(); encoder.outputFormatting = .prettyPrinted
    try! encoder.encode(state).write(to: fileURL)
}

func checkWinner(_ b: [[String]]) -> String? {
    let lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    let flat = b.flatMap { $0 }
    for l in lines {
        if !flat[l[0]].isEmpty && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]] { return flat[l[0]] }
    }
    return nil
}
main()
