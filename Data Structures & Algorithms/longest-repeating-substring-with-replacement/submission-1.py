class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # (windowLen - charFreq[most occuring char]) <= k
        
        charFreq = {}
        res = 0

        l = 0

        for r in range(len(s)):
            charFreq[s[r]] = 1 + charFreq.get(s[r], 0)

            while (r-l+1) - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)

        return res