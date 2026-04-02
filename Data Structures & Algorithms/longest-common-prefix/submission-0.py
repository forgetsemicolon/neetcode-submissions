class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # so we don't run out of bounds and first 
        # element of strs is shortest 
        strs.sort(key = len)

        for h in range(0,len(strs[0])):
            for i in range(1,len(strs)):
                if strs[i][h] == strs[0][h]:
                    continue 
                else:
                    return res

            res += strs[0][h]

        return res