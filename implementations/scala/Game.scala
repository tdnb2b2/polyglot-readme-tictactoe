import java.io._
import scala.io.Source

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
    } else {
      // Logic for put...
    }
  }
}
