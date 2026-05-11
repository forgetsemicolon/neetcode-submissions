class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''

        for c in s:
            if c != ']':
                stack.append(c)
            
            else:
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp # we won't have to reverse if we concatenate this way 
                stack.pop() # pop the [

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # concatenating string 
                
                temp = temp * int(k)
                stack.append(temp)

        return ''.join(stack)

        
