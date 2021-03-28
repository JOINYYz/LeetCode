class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        output = 0 
        for i in range(m):
            for j in range(m):
                if i == j or i == (m-1-j):
                    output += mat[i][j]
        return output
