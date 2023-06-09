fun isCorrectParenthesisString(ps: String): Boolean {
    var cnt = 0
    for (ch in ps.iterator()) {
        if (ch == '(')
            cnt++
        else
            cnt--

        if (cnt < 0)
            return false
    }
    return cnt == 0
}

fun main() {
    val n = readln().toInt()
    for (idx in 1..n) {
        val ps = readln()

        if (isCorrectParenthesisString(ps)) {
            println("YES")
        } else {
            println("NO")
        }
    }
}
