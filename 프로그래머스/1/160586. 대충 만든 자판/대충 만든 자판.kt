class Solution {
    fun solution(keymap: Array<String>, targets: Array<String>): IntArray {
        // 문자별 최소 눌러야 하는 횟수 저장
        val minPress = mutableMapOf<Char, Int>()
        for (key in keymap) {
            key.forEachIndexed { idx, ch ->
                minPress[ch] = minOf(minPress.getOrDefault(ch, Int.MAX_VALUE), idx + 1)
            }
        }

        // 각 target별로 결과 계산
        return targets.map { target ->
            var sum = 0
            for (ch in target) {
                val cnt = minPress[ch]
                if (cnt == null) {
                    sum = -1
                    break
                }
                sum += cnt
            }
            sum
        }.toIntArray()
    }
}
