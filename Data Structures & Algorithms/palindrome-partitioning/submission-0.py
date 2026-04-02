class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                # copy because there is only one part
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    # resume dfs at j+1 i.e. right after palindrome
                    dfs(j+1)
                    # since single part variable is being used, pop the latest addition to it once all combinations are checked for in the line before
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False

            l, r = l+1, r-1
        return True

