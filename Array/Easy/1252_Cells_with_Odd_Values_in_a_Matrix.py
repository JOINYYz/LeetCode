class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        #避免使用 [0]*m 的方式，引用同一个对象
        maxtrix = [[0 for i in range(n)] for j in range(m)]
        output = 0
        
        for index in indices:
            i = index[0]
            j = index[1]
            #遍历指定行
            for k in range(n):
                maxtrix[i][k] += 1   
            for q in range(m):
                maxtrix[q][j] += 1
                
        for row in maxtrix:
            for num in row:
                if num % 2 != 0 :
                    output +=1
        return output
            
        
