class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        output = []
        for i in range(len(x)):
            output.append(x[i])
            output.append(y[i])
        return output
