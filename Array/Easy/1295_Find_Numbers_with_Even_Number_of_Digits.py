class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0 
        for num in nums:
            num = str(num)
            if len(num) % 2 == 0:
                    output+=1
        return output
                
