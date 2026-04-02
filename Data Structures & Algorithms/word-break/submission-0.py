class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def canBreak(s, stIdx):
            if stIdx in dp:
                return dp[stIdx]

            if stIdx == len(s):
                return True

            for endIdx in range(stIdx, len(s) + 1):
                word = s[stIdx:endIdx]
                if word in wordDict:
                    if canBreak(s, endIdx):
                        dp[stIdx] = True
                        return True
                    

            dp[stIdx] = False
            return False

        return canBreak(s, 0)