import java.io.File
import java.util.regex.Pattern

fun main(args: Array<String>) {
    val path = "current_state.json"
    val file = File(path)
    if (!file.exists()) return
    val content = file.readText()
    val cellEnv = System.getenv("CELL")
    val action = System.getenv("ACTION") ?: "put"

    if (action == "reset") {
        file.writeText("{\n  \"board\": [[\"\",\"\",\"\"],[\"\",\"\",\"\"],[\"\",\"\",\"\"]],\n  \"turn\": \"X\",\n  \"winner\": null,\n  \"log\": []\n}")
        return
    }

    if (cellEnv == null || cellEnv.length < 2) return
    val cell = cellEnv.toUpperCase()

    val winner = getJsonValue(content, "winner")
    if (winner != "null") return

    val turn = getJsonValue(content, "turn")
    val board = Array(3) { Array(3) { "" } }
    val p = Pattern.compile("\\[\"(.*?)\",\"(.*?)\",\"(.*?)\"\\]")
    val m = p.matcher(content)
    var rowIndex = 0
    while (rowIndex < 3 && m.find()) {
        board[rowIndex][0] = m.group(1)
        board[rowIndex][1] = m.group(2)
        board[rowIndex][2] = m.group(3)
        rowIndex++
    }

    val r = cell[1] - '1'
    val c = cell[0] - 'A'

    if (r in 0..2 && c in 0..2 && board[r][c].isEmpty()) {
        board[r][c] = turn
        val win = checkWinner(board)
        val nextTurn = if (turn == "X") "O" else "X"
        val draw = isDraw(board)

        val winStr = if (win != null) "\"$win\"" else if (draw) "\"draw\"" else "null"
        val bStr = board.joinToString(",\n") { row ->
            "    [\"${row[0]}\",\"${row[1]}\",\"${row[2]}\"]"
        }

        val out = """{
  "board": [
$bStr
  ],
  "turn": "$nextTurn",
  "winner": $winStr,
  "log": []
}"""
        file.writeText(out)
    }
}

fun getJsonValue(json: String, key: String): String {
    val p = Pattern.compile("\"$key\":\\s*\"?(.*?)\"?(?:,|\\n|\\})")
    val m = p.matcher(json)
    return if (m.find()) m.group(1).trim() else "null"
}

fun checkWinner(b: Array<Array<String>>): String? {
    val lns = arrayOf(
        intArrayOf(0,0,0,1,0,2), intArrayOf(1,0,1,1,1,2), intArrayOf(2,0,2,1,2,2),
        intArrayOf(0,0,1,0,2,0), intArrayOf(0,1,1,1,2,1), intArrayOf(0,2,1,2,2,2),
        intArrayOf(0,0,1,1,2,2), intArrayOf(0,2,1,1,2,0)
    )
    for (l in lns) {
        if (b[l[0]][l[1]].isNotEmpty() && b[l[0]][l[1]] == b[l[2]][l[3]] && b[l[2]][l[3]] == b[l[4]][l[5]]) return b[l[0]][l[1]]
    }
    return null
}

fun isDraw(b: Array<Array<String>>): Boolean {
    for (i in 0..2) for (j in 0..2) if (b[i][j].isEmpty()) return false
    return true
}
