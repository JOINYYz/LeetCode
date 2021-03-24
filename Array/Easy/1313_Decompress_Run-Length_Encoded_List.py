class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(0,len(nums),2):
            tmp = [nums[i+1]]*nums[i]
            output.extend(tmp)
        return output
            
