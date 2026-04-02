class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '{': '}', '[': ']'}
        print(parentheses.keys())
        print(parentheses.values())

        for c in s:
            if c in parentheses.keys():
                print(stack)
                stack.append(c)

            elif c in parentheses.values() and stack and parentheses[stack[-1]] == c:
                stack.pop()

            else:
                return False

        return len(stack) == 0