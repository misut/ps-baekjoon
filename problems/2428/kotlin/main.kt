private fun readInt() = readln().toInt()
private fun readStrings() = readln().split(" ")
private fun readInts() = readStrings().map { it.toInt() }

private fun countPairs(sizeArray: Array<Int>, idx: Int): Int {
    val size = sizeArray[idx]
    var l = 0
    var r = idx - 1
    while (l <= r) {
        val m = (l + r) / 2
        if (sizeArray[m] < size * 0.9)
            l = m + 1
        else
            r = m - 1
    }
    return idx - l
}

fun main() {
    val n = readInt()
    val sizeArray = readInts().toTypedArray().sortedArray()
    println(
        sizeArray.indices.fold(0.toLong()) { count: Long, idx: Int ->
            count + countPairs(sizeArray, idx)
        }
    )
}
