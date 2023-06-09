fun isGroupWord(word: String): Boolean {
    val charSet = mutableSetOf<Char>()
    var prevChar = '_'
    for (ch in word.iterator()) {
        if (ch != prevChar) {
            if (charSet.contains(ch)) {
                return false
            }
            charSet.add(ch)
        }
        prevChar = ch
    }
    return true
}

fun main() {
    val n = readln().toInt()
    var answer = 0
    for (idx in 1..n) {
        val word = readln()
        if (isGroupWord(word)) {
            answer++
        }
    }
    println(answer)
}
