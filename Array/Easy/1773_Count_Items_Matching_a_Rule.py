class Solution:
    
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        itemdict = {'type':0,'color':1,'name':2}
        count = 0
        ruleKeyid = itemdict[ruleKey]
        for item in items:
            if item[ruleKeyid] == ruleValue:
                count+=1
        return count
            
