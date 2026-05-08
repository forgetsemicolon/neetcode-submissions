class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]

                # new negative asteroid is larger than current positive
                # thus it destroys current positive
                if diff < 0:
                    stack.pop()
                # new negative is smaller than current positive thus it 
                # is destroyed itself 
                elif diff > 0:
                    ast = 0
                # new negative is same size as current positive, both
                # are destroyed 
                else:
                    ast = 0
                    stack.pop()
            
            # add the new asteroid if value is non 0
            if ast:
                stack.append(ast)

        return stack 

