class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=[None]*len(nums)
        j=0
        for i,num in enumerate(nums):
            if i == 0:
                sums[j]=num
                j+=1
            else:
                sums[j]=sums[j-1]+num
                j+=1
        return sums
