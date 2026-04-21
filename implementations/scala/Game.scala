import upickle.default._
import java.nio.file.{Files, Paths}

case class Move(player: String, cell: String)
object Move { implicit val rw: ReadWriter[Move] = macroRW }

case class State(var board: List[List[String]], var turn: String, var winner: String, var log: List[Move])
object State { implicit val rw: ReadWriter[State] = macroRW }

object Game {
  def main(args: Array[String]): Unit = {
    val path = Paths.get("current_state.json")
    val json = new String(Files.readAllBytes(path))
    val state = read[State](json)

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
    Files.write(path, write(state, indent = 2).getBytes)
  }

  def checkWinner(b: List[List[String]]): Option[String] = {
    val lines = List(List(0,1,2),List(3,4,5),List(6,7,8),List(0,3,6),List(1,4,7),List(2,5,8),List(0,4,8),List(2,4,6))
    val flat = b.flatten
    lines.collectFirst {
      case l if flat(l(0)).nonEmpty && flat(l(0)) == flat(l(1)) && flat(l(0)) == flat(l(2)) => flat(l(0))
    }
  }
}
