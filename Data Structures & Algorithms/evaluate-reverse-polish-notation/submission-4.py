class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2-num1)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(t))

        return stack[0]

        #     if isinstance(t, int):
        #         stack.append(t)

        #     elif t in operators and len(stack) >= 2:
        #         num1 = stack.pop()
        #         num2 = stack.pop()
        #         print(num1)
        #         print(num2)
        #         print(t)
        #         res = str(int(eval(num2 + t + num1)))
        #         print(res)
        #         stack.append(res)

        # return int(stack[-1])