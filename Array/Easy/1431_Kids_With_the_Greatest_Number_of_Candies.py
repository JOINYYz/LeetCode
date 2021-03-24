class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        output = []
        for candy in candies:
            tmp = candy+extraCandies
            if tmp >= max_candy:
              #注意这里不可以用'false'，bool('false')=true
                output.append(1)
            else:
                output.append(0)                               
        return output
