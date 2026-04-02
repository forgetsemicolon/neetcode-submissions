class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)

        res, lenRes = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                # update the result
                if (r - l + 1) < lenRes:
                    lenRes = r-l+1
                    res = [l, r]

                # pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        l, r = res
        return s[l:r+1] if lenRes != float('infinity') else ""
