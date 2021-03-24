class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for customer in accounts:
            tmp=0
            for bank in customer:
                tmp += bank
            if tmp>maxwealth:
                maxwealth = tmp
        return maxwealth
                
       
