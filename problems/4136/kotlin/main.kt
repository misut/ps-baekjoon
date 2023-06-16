private fun readInt() = readln().toInt()

private fun executeMove(board: Array<Array<Char>>, move: String, marker: Char) {
    val dir = move[0]
    val idx = move.substring(1).toInt() - 1
    val size = board.size
    when (dir) {
        'L' -> {
            for (i in 0 until size - 1) {
                if (board[idx][i] == '_') {
                    break
                } else if (board[idx][i] != '_') {
                    board[idx][0] = board[idx][i + 1].also { board[idx][i + 1] = board[idx][0] }
                }
            }
            board[idx][0] = marker
        }
        'R' -> {
            for (i in size - 1 downTo 1) {
                if (board[idx][i] == '_') {
                    break
                } else if (board[idx][i] != '_') {
                    board[idx][size - 1] = board[idx][i - 1].also { board[idx][i - 1] = board[idx][size - 1] }
                }
            }
            board[idx][size - 1] = marker
        }
        'T' -> {
            for (i in 0 until size - 1) {
                if (board[i][idx] == '_') {
                    break
                } else if (board[i][idx] != '_') {
                    board[0][idx] = board[i + 1][idx].also { board[i + 1][idx] = board[0][idx] }
                }
            }
            board[0][idx] = marker
        }
        'B' -> {
            for (i in size - 1 downTo 1) {
                if (board[idx][i] == '_') {
                    break
                } else if (board[idx][i] != '_') {
                    board[size - 1][idx] = board[i - 1][idx].also { board[i - 1][idx] = board[size - 1][idx] }
                }
            }
            board[size - 1][idx] = marker
        }
    }
}

private fun countStraightXO(board: Array<Array<Char>>): Pair<Int, Int> {
    var isXStraightCol: Boolean
    var isXStraightRow: Boolean
    var isOStraightCol: Boolean
    var isOStraightRow: Boolean
    var xStraight = 0
    var oStraight = 0

    val size = board.size
    for (i in 0 until size) {
        isXStraightCol = true
        isOStraightCol = true
        for (j in 0 until size) {
            if (board[i][j] == 'X') {
                isOStraightCol = false
            } else if (board[i][j] == 'O') {
                isXStraightCol = false
            } else {
                isXStraightCol = false
                isOStraightCol = false
            }
        }

        isXStraightRow = true
        isOStraightRow = true
        for (j in 0 until size) {
            if (board[j][i] == 'X') {
                isOStraightRow = false
            } else if (board[j][i] == 'O') {
                isXStraightRow = false
            } else {
                isXStraightRow = false
                isOStraightRow = false
            }
        }

        if (isXStraightCol) xStraight++
        if (isXStraightRow) xStraight++
        if (isOStraightCol) oStraight++
        if (isOStraightRow) oStraight++
    }

    return Pair(xStraight, oStraight)
}

private fun showBoard(board: Array<Array<Char>>) {
    for (col in board) {
        print(" ")
        for (marker in col) {
            print("$marker ")
        }
        println()
    }
    println("-".repeat(board.size * 2 + 2))
}

fun main() {
    val n = readInt()
    val board = Array(n) { _ ->
        Array(n) { _ ->
            '_'
        }
    }
    var marker = 'X'

    while (true) {
        val move = readln()
        if (move == "QUIT") {
            println("TIE GAME")
            break
        }

        executeMove(board, move, marker)
        // showBoard(board)
        val (xStraight, oStraight) = countStraightXO(board)
        if (xStraight > oStraight) {
            println("X WINS")
            break
        } else if (xStraight < oStraight) {
            println("O WINS")
            break
        }

        marker = if (marker == 'X') 'O' else 'X'
    }
}
