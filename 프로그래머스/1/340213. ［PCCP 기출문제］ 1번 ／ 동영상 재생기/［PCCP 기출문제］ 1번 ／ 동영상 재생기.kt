class Solution {
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        var answer: String = ""
        var h = pos.substring(0,2).toInt()
        var m = pos.substring(3,5).toInt()
        
        var start = op_start.substring(0,2).toInt()*60 + op_start.substring(3,5).toInt()
        var end = op_end.substring(0,2).toInt()*60 + op_end.substring(3,5).toInt()
        
        var total = video_len.substring(0,2).toInt()*60 + video_len.substring(3,5).toInt()
        
        for(i in 0 until commands.size){
            
            var now = h*60 + m
   
            if (start<= now && now <= end){
                h = op_end.substring(0,2).toInt()
                m = op_end.substring(3,5).toInt()
            }
             
            // println("$h $m")
            if (commands[i] == "next"){
                if (now > total-10){
                    h = video_len.substring(0,2).toInt()
                    m = video_len.substring(3,5).toInt()
                } else{
                    m += 10
                    if (m>=60){
                        m-=60
                        h+=1
                    }
                }
            } else if  (commands[i] == "prev"){
                if (h==0 && m<10){
                    m =0 
                } else {
                      m -= 10
                    if (m<0){
                        m+=60
                        h-=1
                    }
                }
                
            }
//             var start = op_start.substring(0,2).toInt()*60 + op_start.substring(3,5).toInt()
//             var end = op_end.substring(0,2).toInt()*60 + op_end.substring(3,5).toInt()
//             var now = h*60 + m
            now = h*60 + m

            if (start<= now && now <= end){
                h = op_end.substring(0,2).toInt()
                m = op_end.substring(3,5).toInt()
            }
            
            // println("==$h $m")
        }
        
        val hStr = h.toString().padStart(2, '0')
        val mStr = m.toString().padStart(2, '0')
        return "${hStr}:${mStr}"
    }
}