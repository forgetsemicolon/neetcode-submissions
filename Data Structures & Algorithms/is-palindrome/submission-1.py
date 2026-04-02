class Solution:
    def isPalindrome(self, s: str) -> bool:
        # option 1 - create a reversed string and check 
        # if it is equal to the original string 

        # new_s = ""
        # for char in s:
        #     if char.isalnum() and char != " ":
        #         new_s = new_s + char.lower()
        
        # rev_s = new_s[::-1]

        # return rev_s == new_s

        # option 2: 2 pointers

        l, r = 0, len(s)-1

        while l<r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

