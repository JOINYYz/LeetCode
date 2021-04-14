class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        output = []
        P = [ i for i in range(1,m+1)]
        for num1 in queries:
            for num2 in P:
                if num1==num2:
                    num2_id = P.index(num2)
                    output.append(num2_id)
                    for i in range(1,num2_id+1)[::-1]:
                        P[i] = P[i-1]
                    P[0] = num2
        return output
        
