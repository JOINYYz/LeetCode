class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        stu_time = list(zip(startTime,endTime))
        output = 0
        for t in stu_time:
            if t[0]<= queryTime and t[1]>=queryTime:
                output+=1
        return output
