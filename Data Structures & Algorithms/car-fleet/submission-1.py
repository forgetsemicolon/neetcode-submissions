class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # think of pos, time as coordinates in a linear setting
        # speed of each car is limited by the speed of the car
        # in the most front of the lineup 
        stack = []
        pair = [[p,s] for p,s in zip(position, speed)]
        
        for p, s in sorted(pair)[::-1]: # descending order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


        # for pos, sp in zip(position, speed):
        #     timeTaken = (target - pos) // sp
        #     if stack and timeTaken <= stack[-1]:
        #         fleetCount += 1
        #     stack.append(timeTaken)
            

        # return fleetCount