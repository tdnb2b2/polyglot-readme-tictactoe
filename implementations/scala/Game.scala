import java.io._
import scala.io.Source
import scala.util.matching.Regex

object Game {
  def main(args: Array[String]): Unit = {
    val path = "current_state.json"
    val json = Source.fromFile(path).getLines().mkString
    val cell = sys.env.getOrElse("CELL", "").toUpperCase
    val action = sys.env.getOrElse("ACTION", "put")

    if (action == "reset") {
      val out = "{\n  \"board\": [[\"\",\"\",\"\"],[\"\",\"\",\"\"],[\"\",\"\",\"\"]],\n  \"turn\": \"X\",\n  \"winner\": null,\n  \"log\": []\n}"
      val pw = new PrintWriter(new File(path))
      pw.write(out); pw.close()
    } else if (cell.length >= 2) {
      val turn = "\"turn\":\\s*\"(.*?)\"".r.findFirstMatchIn(json).map(_.group(1)).getOrElse("X")
      val winner = "\"winner\":\\s*\"(.*?)\"".r.findFirstMatchIn(json).map(_.group(1)).getOrElse("null")
      
      if (winner == "null") {
        val board = Array.ofDim[String](3, 3)
        val rowRegex = "\\[\"(.*?)\",\"(.*?)\",\"(.*?)\"\\]".r
        rowRegex.findAllIn(json).matchData.zipWithIndex.foreach { case (m, i) =>
          if (i < 3) {
            board(i)(0) = m.group(1); board(i)(1) = m.group(2); board(i)(2) = m.group(3)
          }
        }

        // Correct Mapping: r is row (1-3), c is col (A-C)
        val r = cell(1) - '1'
        val c = cell(0) - 'A'

        if (r >= 0 && r < 3 && c >= 0 && c < 3 && board(r)(c).isEmpty) {
          board(r)(c) = turn
          val nextTurn = if (turn == "X") "O" else "X"
          val win = checkWinner(board)
          val draw = board.flatten.forall(_.nonEmpty)

          val winStr = if (win.isDefined) s""""${win.get}"""" else if (draw) "\"draw\"" else "null"
          val bStr = board.map(row => s"""["${row(0)}","${row(1)}","${row(2)}"]""").mkString("    ", ",\n    ", "")
          
          val out = s"""{
  "board": [
$bStr
  ],
  "turn": "$nextTurn",
  "winner": $winStr,
  "log": []
}"""
          val pw = new PrintWriter(new File(path))
          pw.write(out); pw.close()
        }
      }
    }
  }

  def checkWinner(b: Array[Array[String]]): Option[String] = {
    val lns = Array(Array(0,0,0,1,0,2),Array(1,0,1,1,1,2),Array(2,0,2,1,2,2), Array(0,0,1,0,2,0),Array(0,1,1,1,2,1),Array(0,2,1,2,2,2), Array(0,0,1,1,2,2),Array(0,2,1,1,2,0))
    for (l <- lns) {
      if (b(l(0))(l(1)).nonEmpty && b(l(0))(l(1)) == b(l(2))(l(3)) && b(l(2))(l(3)) == b(l(4))(l(5))) return Some(b(l(0))(l(1)))
    }
    None
  }
}
