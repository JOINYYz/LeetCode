class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0
        #注意index溢出
        for i in range(len(points)-1):            
            tmp = list(zip(points[i],points[i+1]))
            steps = [abs(i-j) for i,j in tmp]
            output += max(steps)
        return output
