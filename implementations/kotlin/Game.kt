import java.io.File
import org.json.JSONObject

fun main() {
    val file = File("current_state.json")
    val s = JSONObject(file.readText())
    val cell = System.getenv("CELL")?.uppercase() ?: ""
    val action = System.getenv("ACTION") ?: "put"

    if (action == "reset") {
        s.put("board", listOf(listOf("","",""),listOf("","",""),listOf("","","")))
        s.put("turn", "X")
        s.put("winner", JSONObject.NULL)
        s.put("log", listOf<String>())
    } else if (cell.isNotEmpty() && s.isNull("winner")) {
        val board = s.getJSONArray("board")
        val turn = s.getString("turn")
        val r = cell[1] - '1'
        val c = cell[0] - 'A'
        if (r in 0..2 && c in 0..2 && board.getJSONArray(r).getString(c).isEmpty()) {
            board.getJSONArray(r).put(c, turn)
            // check win
            val lns = listOf(listOf(0,0,0,1,0,2),listOf(1,0,1,1,1,2),listOf(2,0,2,1,2,2),listOf(0,0,1,0,2,0),listOf(0,1,1,1,2,1),listOf(0,2,1,2,2,2),listOf(0,0,1,1,2,2),listOf(0,2,1,1,2,0))
            var win = false
            for (l in lns) {
                if (board.getJSONArray(l[0]).getString(l[1]).isNotEmpty() && board.getJSONArray(l[0]).getString(l[1]) == board.getJSONArray(l[2]).getString(l[3]) && board.getJSONArray(l[2]).getString(l[3]) == board.getJSONArray(l[4]).getString(l[5])) win = true
            }
            if (win) s.put("winner", turn)
            else {
                var full = true
                for (i in 0..2) for (j in 0..2) if (board.getJSONArray(i).getString(j).isEmpty()) full = false
                if (full) s.put("winner", "draw")
                else s.put("turn", if (turn == "X") "O" else "X")
            }
        }
    }
    file.writeText(s.toString(2))
}
