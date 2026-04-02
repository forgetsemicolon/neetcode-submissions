class Solution:
    def isPalindrome(self, s: str) -> bool:
        # option 1 - create a reversed string and check 
        # if it is equal to the original string 

        new_s = ""
        for char in s:
            if char.isalnum() and char != " ":
                new_s = new_s + char.lower()
                print(new_s)
        
        rev_s = new_s[::-1]

        return rev_s == new_s

        

