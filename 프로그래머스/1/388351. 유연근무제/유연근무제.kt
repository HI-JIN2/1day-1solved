class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        var answer: Int = 0
        
        for (i in 0 until schedules.size){
            var bad = 0
            for ( j in 0 until timelogs[i].size){
    
                val timeStr = timelogs[i][j].toString().padStart(4, '0')
                val scheduleStr = schedules[i].toString().padStart(4, '0')

                val a = timeStr.substring(0, 2).toInt() * 60 + timeStr.substring(2).toInt()
                val b = scheduleStr.substring(0, 2).toInt() * 60 + scheduleStr.substring(2).toInt()
                
                    if ((j+startday)%7 == 6 || (j+startday)%7 == 0){
                    continue
                }
                else if (a-b<=10 ){
                    // println("굿")
                    continue
                } else{
                    // println("배드")
                    bad+=1
                }
            }
            if (bad == 0) answer+=1
        }

        return answer
    }
}