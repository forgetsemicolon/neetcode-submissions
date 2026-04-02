class Solution:
    def checkValidString(self, s: str) -> bool:
        min = max = 0

        for i in range(len(s)):
            if s[i] == '(':
                min += 1
                max += 1

            elif s[i] == ')':
                min -= 1
                max -= 1
                if max < 0:
                    return False

            elif s[i] == '*':
                min -= 1
                max += 1
            
            if min < 0:
                min = 0

        return min == 0