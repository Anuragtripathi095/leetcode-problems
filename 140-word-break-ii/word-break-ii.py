class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)   # O(1) lookup
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]   # base case
            
            res = []
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                
                if word in wordSet:
                    sub_sentences = dfs(end)
                    
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            
            memo[start] = res
            return res
        
        return dfs(0)