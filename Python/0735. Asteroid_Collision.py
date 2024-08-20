from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # initialize an empty stack to keep track of surviving asteroids
        stack = []
        
        # iterate over each asteroid in the input list
        for asteroid in asteroids:
            # continue processing while there are asteroids in the stack and the current asteroid
            # is moving left (negative) while the top of the stack is moving right (positive)
            while stack and asteroid < 0 < stack[-1]:
                # if the current asteroid is larger (absolute value) than the top asteroid in 
                # the stack, the top asteroid is destroyed, so remove it from the stack
                if -asteroid > stack[-1]:
                    stack.pop()
                    # continue checking the next asteroid on the stack
                    continue
                # if both asteroids are of the same size, they both destroy each other, so
                # remove the top asteroid
                elif -asteroid == stack[-1]:
                    stack.pop()
                # break out of the while loop as the current asteroid has been processed
                break
            else:
                # if the while loop wasn't broken (meaning no collision occurred), add the current
                # asteroid to the stack
                stack.append(asteroid)
        
        # return the stack containing the surviving asteroids after all collisions
        return stack

if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([5,10,-5]))
    print(s.asteroidCollision([8,-8]))
    print(s.asteroidCollision([10,2,-5]))