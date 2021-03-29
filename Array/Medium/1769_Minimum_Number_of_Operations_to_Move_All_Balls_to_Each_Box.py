class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        output = []
        for i in range(n):
            step = 0
            for j in range(n):
                if i!=j:
                    if boxes[j] != '0' :
                        step += int(boxes[j])*abs(j-i)
            output.append(step)
        return output
                
