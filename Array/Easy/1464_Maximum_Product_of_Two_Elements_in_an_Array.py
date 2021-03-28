class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        for i in range(n):
            for j in range(i+1,n):
                product = (nums[i]-1) *(nums[j]-1)
                if product > output:
                    output = product
        return output
               
        
    
