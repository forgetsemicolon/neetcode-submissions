class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # when temp is greater than temp from top of stack
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)

            stack.append([t,i])

        return res