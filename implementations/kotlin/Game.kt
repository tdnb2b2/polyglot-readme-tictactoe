import java.io.File
import com.google.gson.Gson
import com.google.gson.GsonBuilder

data class Move(val player: String, val cell: String)
data class State(var board: List<List<String>>, var turn: String, var winner: String?, var log: List<Move>)

fun main() {
    val gson = GsonBuilder().setPrettyPrinting().serializeNulls().create()
    val file = File("current_state.json")
    val state = gson.fromJson(file.readText(), State::class.java)

    val cell = System.getenv("CELL")?.uppercase() ?: ""
    val action = System.getenv("ACTION") ?: "put"

    if (action == "reset") {
        val isFull = state.board.all { row -> row.all { it.isNotEmpty() } }
        if (state.winner != null || isFull) {
            state.board = listOf(listOf("","",""), listOf("","",""), listOf("","",""))
            state.turn = "X"
            state.winner = null
            state.log = emptyList()
        }
    } else if (cell.isNotEmpty() && state.winner == null) {
        val r = cell[1] - '1'
        val c = cell[0] - 'A'
        if (r in 0..2 && c in 0..2 && state.board[r][c].isEmpty()) {
            val newBoard = state.board.map { it.toMutableList() }
            newBoard[r][c] = state.turn
            state.board = newBoard
            state.log = state.log + Move(state.turn, cell)
            
            val win = checkWinner(state.board)
            if (win != null) state.winner = win
            else {
                if (state.board.all { row -> row.all { it.isNotEmpty() } }) state.winner = "draw"
                else state.turn = if (state.turn == "X") "O" else "X"
            }
        }
    }
    file.writeText(gson.toJson(state))
}

fun checkWinner(b: List<List<String>>): String? {
    val lines = listOf(listOf(0,1,2),listOf(3,4,5),listOf(6,7,8),listOf(0,3,6),listOf(1,4,7),listOf(2,5,8),listOf(0,4,8),listOf(2,4,6))
    val flat = b.flatten()
    for (l in lines) {
        if (flat[l[0]].isNotEmpty() && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]]) return flat[l[0]]
    }
    return null
}
