import java.io.File

data class Move(val player: String, val cell: String)
data class State(var board: List<MutableList<String>>, var turn: String, var winner: String?, var log: List<Move>)

fun main() {
    val file = File("current_state.json")
    val json = file.readText()
    val state = parseState(json)

    val cell = System.getenv("CELL")?.toUpperCase() ?: ""
    val action = System.getenv("ACTION") ?: "put"

    if (action == "reset") {
        val isFull = state.board.all { row -> row.all { it.isNotEmpty() } }
        if (state.winner != null || isFull) {
            state.board = listOf(mutableListOf("","",""), mutableListOf("","",""), mutableListOf("","",""))
            state.turn = "X"
            state.winner = null
            state.log = emptyList()
        }
    } else if (cell.isNotEmpty() && state.winner == null) {
        val r = cell[1] - '1'
        val c = cell[0] - 'A'
        if (r in 0..2 && c in 0..2 && state.board[r][c].isEmpty()) {
            state.board[r][c] = state.turn
            state.log = state.log + Move(state.turn, cell)
            
            val win = checkWinner(state.board)
            if (win != null) state.winner = win
            else {
                if (state.board.all { row -> row.all { it.isNotEmpty() } }) state.winner = "draw"
                else state.turn = if (state.turn == "X") "O" else "X"
            }
        }
    }
    file.writeText(stateToJson(state))
}

fun parseState(json: String): State {
    val board = mutableListOf(mutableListOf("","",""), mutableListOf("","",""), mutableListOf("","",""))
    var turn = "X"
    var winner: String? = null
    val log = mutableListOf<Move>()

    if (json.contains("\"board\"")) {
        val boardIdx = json.indexOf("\"board\"")
        val startIdx = json.indexOf("[", boardIdx)
        var row = 0
        var pos = startIdx + 1
        while (row < 3) {
            val rowStart = json.indexOf("[", pos)
            if (rowStart == -1) break
            val rowEnd = json.indexOf("]", rowStart)
            val rowStr = json.substring(rowStart + 1, rowEnd)
            val cells = rowStr.split(",")
            for (col in 0 until 3) {
                if (col < cells.size) {
                    board[row][col] = cells[col].trim().replace("\"", "")
                }
            }
            row++
            pos = rowEnd + 1
        }
    }
    
    if (json.contains("\"turn\"")) {
        val idx = json.indexOf("\"turn\"")
        val valStart = json.indexOf("\"", json.indexOf(":", idx))
        val valEnd = json.indexOf("\"", valStart + 1)
        turn = json.substring(valStart + 1, valEnd)
    }
    
    if (json.contains("\"winner\"")) {
        val idx = json.indexOf("\"winner\"")
        val colonIdx = json.indexOf(":", idx)
        val nextQuote = json.indexOf("\"", colonIdx)
        val nextComma = json.indexOf(",", colonIdx)
        val nextBrace = json.indexOf("}", colonIdx)
        val end = if (nextComma != -1) nextComma else nextBrace
        val value = json.substring(colonIdx + 1, end).trim()
        if (value.startsWith("\"")) {
            winner = value.substring(1, value.lastIndexOf("\""))
        } else if (value == "null") {
            winner = null
        } else {
            winner = value
        }
    }
    
    if (json.contains("\"log\"")) {
        val idx = json.indexOf("\"log\"")
        val start = json.indexOf("[", idx)
        val end = json.lastIndexOf("]")
        val logContent = json.substring(start + 1, end).trim()
        if (logContent.isNotEmpty()) {
            val entries = logContent.split("}")
            for (entry in entries) {
                if (entry.contains("{")) {
                    val pIdx = entry.indexOf("\"player\"")
                    val pValStart = entry.indexOf("\"", entry.indexOf(":", pIdx))
                    val pValEnd = entry.indexOf("\"", pValStart + 1)
                    val p = entry.substring(pValStart + 1, pValEnd)
                    
                    val cIdx = entry.indexOf("\"cell\"")
                    val cValStart = entry.indexOf("\"", entry.indexOf(":", cIdx))
                    val cValEnd = entry.indexOf("\"", cValStart + 1)
                    val c = entry.substring(cValStart + 1, cValEnd)
                    log.add(Move(p, c))
                }
            }
        }
    }

    return State(board, turn, winner, log)
}

fun stateToJson(s: State): String {
    val sb = StringBuilder()
    sb.append("{\n  \"board\": [\n")
    for (i in 0 until 3) {
        sb.append("    [\"${s.board[i][0]}\", \"${s.board[i][1]}\", \"${s.board[i][2]}\"]")
        if (i < 2) sb.append(",")
        sb.append("\n")
    }
    sb.append("  ],\n  \"turn\": \"${s.turn}\",\n")
    sb.append("  \"winner\": ").append(if (s.winner == null) "null" else "\"${s.winner}\"").append(",\n")
    sb.append("  \"log\": [\n")
    for (i in s.log.indices) {
        val m = s.log[i]
        sb.append("    {\"player\": \"${m.player}\", \"cell\": \"${m.cell}\"}")
        if (i < s.log.size - 1) sb.append(",")
        sb.append("\n")
    }
    sb.append("  ]\n}")
    return sb.toString()
}

fun checkWinner(b: List<List<String>>): String? {
    val lines = listOf(listOf(0,1,2),listOf(3,4,5),listOf(6,7,8),listOf(0,3,6),listOf(1,4,7),listOf(2,5,8),listOf(0,4,8),listOf(2,4,6))
    val flat = b.flatten()
    for (l in lines) {
        if (flat[l[0]].isNotEmpty() && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]]) return flat[l[0]]
    }
    return null
}

