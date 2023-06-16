import kotlin.math.pow

infix fun Int.`**`(exponent: Int): Int {
    if (exponent == 0)
        return 1
    return toDouble().pow(exponent).toInt()
}

fun leftToPalindrome(meter: String): Int {
    val lengthHalf = meter.length / 2
    val former = meter.slice(0 until lengthHalf).reversed()
    val latter = meter.slice(meter.length - lengthHalf until meter.length)

    if (former == latter) {
        return 0
    }

    val formerInt = former.toInt()
    val latterInt = latter.toInt()
    if (formerInt > latterInt) {
        return formerInt - latterInt
    }

    val diff = (10 `**` lengthHalf) - latterInt
    var nextMeter = (meter.toInt() + diff).toString()
    nextMeter = "0".repeat(meter.length - nextMeter.length) + nextMeter
    return diff + leftToPalindrome(nextMeter)
}

fun main() {
    while (true) {
        val meter = readln();
        if (meter == "0") {
            break
        }
        println(leftToPalindrome(meter))
    }
}
