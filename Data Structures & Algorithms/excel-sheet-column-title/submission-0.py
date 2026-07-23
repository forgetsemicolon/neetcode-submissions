class Solution:
    def convertToTitle(self, num: int) -> str:
        if num == 0:
            return ''

        n = num - 1

        return self.convertToTitle(n//26) + chr(n%26 + ord('A'))