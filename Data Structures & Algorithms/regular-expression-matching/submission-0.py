class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def helper(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i == len(s) and j == len(p):
                dp[(i,j)] = True
                return dp[(i,j)]

            if i < len(s) and j == len(p):
                dp[(i,j)] = False
                return dp[(i,j)]

            if j+1 < len(p) and p[j+1] == '*':
                # Match zero occurrences
                result = helper(i, j+2)
                
                # Match one or more (only if i is in bounds AND chars match)
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    result = result or helper(i+1, j)
                
                dp[(i,j)] = result

            else:
                # No '*', so we need exact match (or '.')
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    dp[(i,j)] = helper(i+1, j+1)
                else:
                    dp[(i,j)] = False

            return dp[(i,j)]

        return helper(0,0)

