const val MAX_NUMBER = 10000

fun calculate(number: Int): Int {
    var cur = number
    var res = number
    while (cur > 0) {
        res += cur % 10
        cur /= 10
    }
    return res
}

fun main(args: Array<String>) {
    val isSelfNumber: Array<Boolean> = Array(MAX_NUMBER + 1) { _ -> true }

    for (number in isSelfNumber.indices) {
        val notSelf = calculate(number)
        if (notSelf > MAX_NUMBER)
            continue
        isSelfNumber[notSelf] = false
    }

    isSelfNumber.forEachIndexed { number, isSelf -> if (isSelf) { println(number) } }
}
