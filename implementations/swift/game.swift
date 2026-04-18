import Foundation

let cell = ProcessInfo.processInfo.environment["CELL"] ?? ""
let action = ProcessInfo.processInfo.environment["ACTION"] ?? ""
let path = "current_state.json"

if let data = try? Data(contentsOf: URL(fileURLWithPath: path)),
   var s = try? JSONSerialization.jsonObject(with: data, options: .mutableContainers) as? [String: Any] {
    
    if action == "reset" {
        s["board"] = [["","",""],["","",""],["","",""]]
        s["turn"] = "X"
        s["winner"] = NSNull()
        s["log"] = []
    } else if !cell.isEmpty && (s["winner"] as? NSNull) != nil {
        var board = s["board"] as! [[String]]
        let turn = s["turn"] as! String
        let r = Int(cell.dropFirst().first!.asciiValue! - Character("1").asciiValue!)
        let c = Int(cell.first!.asciiValue! - Character("A").asciiValue!)
        
        if r >= 0 && r < 3 && c >= 0 && c < 3 && board[r][c].isEmpty {
            board[r][c] = turn
            s["board"] = board
            var log = s["log"] as? [[String: String]] ?? []
            log.append(["player": turn, "cell": cell])
            s["log"] = log
            
            let lines = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
            var won = false
            for l in lines {
                if !board[l[0].0][l[0].1].isEmpty && board[l[0].0][l[0].1] == board[l[1].0][l[1].1] && board[l[1].0][l[1].1] == board[l[2].0][l[2].1] {
                    won = true; break
                }
            }
            
            if won {
                s["winner"] = turn
            } else if board.allSatisfy({ $0.allSatisfy({ !$0.isEmpty }) }) {
                s["winner"] = "draw"
            } else {
                s["turn"] = (turn == "X" ? "O" : "X")
            }
        }
    }
    
    let out = try! JSONSerialization.data(withJSONObject: s, options: .prettyPrinted)
    try! out.write(to: URL(fileURLWithPath: path))
}
