class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_len = len(arr)
        sums = 0
        listlen = [i for i in range(1,arr_len+1,2)]
        for l in listlen:
            for i in range(arr_len):
              #注意要判断index是否溢出
                if i+l <= arr_len:
                    tmp = arr[i:i+l]
                    sums += sum(tmp)
        return sums
