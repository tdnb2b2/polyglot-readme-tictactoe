import java.nio.file.{Files, Paths}
import scala.collection.mutable.ListBuffer

case class Move(player: String, cell: String)
case class State(var board: List[List[String]], var turn: String, var winner: String, var log: List[Move])

object Game {
  def main(args: Array[String]): Unit = {
    val path = Paths.get("current_state.json")
    val json = new String(Files.readAllBytes(path))
    val state = parseState(json)

    val cell = sys.env.getOrElse("CELL", "").toUpperCase
    val action = sys.env.getOrElse("ACTION", "put")

    if (action == "reset") {
      val isFull = state.board.flatten.forall(_.nonEmpty)
      if ((state.winner != null && state.winner != "null") || isFull) {
        state.board = List(List("","",""), List("","",""), List("","",""))
        state.turn = "X"
        state.winner = null
        state.log = List()
      }
    } else if (cell.nonEmpty && (state.winner == null || state.winner == "null")) {
      val r = cell(1) - '1'
      val c = cell(0) - 'A'
      if (r >= 0 && r < 3 && c >= 0 && c < 3 && state.board(r)(c).isEmpty) {
        state.board = state.board.updated(r, state.board(r).updated(c, state.turn))
        state.log = state.log :+ Move(state.turn, cell)
        val win = checkWinner(state.board)
        if (win.isDefined) state.winner = win.get
        else if (state.board.flatten.forall(_.nonEmpty)) state.winner = "draw"
        else state.turn = if (state.turn == "X") "O" else "X"
      }
    }
    Files.write(path, stateToJson(state).getBytes)
  }

  def parseState(json: String): State = {
    var board = List(List("","",""), List("","",""), List("","",""))
    var turn = "X"
    var winner: String = "null"
    val log = ListBuffer[Move]()

    if (json.contains("\"board\"")) {
      val boardIdx = json.indexOf("\"board\"")
      val startIdx = json.indexOf("[", boardIdx)
      var row = 0
      var pos = startIdx + 1
      val newBoard = ListBuffer[List[String]]()
      while (row < 3) {
        val rowStart = json.indexOf("[", pos)
        if (rowStart == -1) {
           newBoard += List("","","")
        } else {
          val rowEnd = json.indexOf("]", rowStart)
          val rowStr = json.substring(rowStart + 1, rowEnd)
          val cells = rowStr.split(",").map(_.trim.replace("\"", ""))
          val cellList = ListBuffer[String]()
          for (col <- 0 until 3) {
            if (col < cells.length) cellList += cells(col) else cellList += ""
          }
          newBoard += cellList.toList
          pos = rowEnd + 1
        }
        row += 1
      }
      board = newBoard.toList
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
      val value = json.substring(colonIdx + 1, end).trim
      if (value.startsWith("\"")) {
        winner = value.substring(1, value.lastIndexOf("\""))
      } else {
        winner = value // e.g. null
      }
    }

    if (json.contains("\"log\"")) {
      val idx = json.indexOf("\"log\"")
      val start = json.indexOf("[", idx)
      val end = json.lastIndexOf("]")
      val logContent = json.substring(start + 1, end).trim
      if (logContent.nonEmpty) {
        val entries = logContent.split("}")
        for (entry <- entries) {
          if (entry.contains("{")) {
            val pIdx = entry.indexOf("\"player\"")
            val pValStart = entry.indexOf("\"", entry.indexOf(":", pIdx))
            val pValEnd = entry.indexOf("\"", pValStart + 1)
            val p = entry.substring(pValStart + 1, pValEnd)
            
            val cIdx = entry.indexOf("\"cell\"")
            val cValStart = entry.indexOf("\"", entry.indexOf(":", cIdx))
            val cValEnd = entry.indexOf("\"", cValStart + 1)
            val c = entry.substring(cValStart + 1, cValEnd)
            log += Move(p, c)
          }
        }
      }
    }

    State(board, turn, winner, log.toList)
  }

  def stateToJson(s: State): String = {
    val sb = new StringBuilder()
    sb.append("{\n  \"board\": [\n")
    for (i <- 0 until 3) {
      sb.append(s"    [\"${s.board(i)(0)}\", \"${s.board(i)(1)}\", \"${s.board(i)(2)}\"]")
      if (i < 2) sb.append(",")
      sb.append("\n")
    }
    sb.append("  ],\n")
    sb.append(s"  \"turn\": \"${s.turn}\",\n")
    sb.append(s"  \"winner\": ${if (s.winner == null || s.winner == "null") "null" else "\"" + s.winner + "\""},\n")
    sb.append("  \"log\": [\n")
    for (i <- s.log.indices) {
      val m = s.log(i)
      sb.append(s"    {\"player\": \"${m.player}\", \"cell\": \"${m.cell}\"}")
      if (i < s.log.size - 1) sb.append(",")
      sb.append("\n")
    }
    sb.append("  ]\n}")
    sb.toString()
  }

  def checkWinner(b: List[List[String]]): Option[String] = {
    val lines = List(List(0,1,2),List(3,4,5),List(6,7,8),List(0,3,6),List(1,4,7),List(2,5,8),List(0,4,8),List(2,4,6))
    val flat = b.flatten
    lines.collectFirst {
      case l if flat(l(0)).nonEmpty && flat(l(0)) == flat(l(1)) && flat(l(0)) == flat(l(2)) => flat(l(0))
    }
  }
}

