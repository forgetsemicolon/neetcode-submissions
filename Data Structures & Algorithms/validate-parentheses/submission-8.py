class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        return len(stack) == 0
        
        # stack = []
        # parentheses = {'(': ')', '{': '}', '[': ']'}
        # print(parentheses.keys())
        # print(parentheses.values())

        # for c in s:
        #     if c in parentheses.keys():
        #         print(stack)
        #         stack.append(c)

        #     elif c in parentheses.values() and stack and parentheses[stack[-1]] == c:
        #         stack.pop()

        #     else:
        #         return False

        # return len(stack) == 0