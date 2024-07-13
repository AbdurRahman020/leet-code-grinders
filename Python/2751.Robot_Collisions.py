from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # calculate the number of robots
        num_of_robos = len(positions)
        # create a list of robot indices sorted by their positions
        robots = sorted(range(num_of_robos), key=lambda x: positions[x])
        # initialize an empty stack to keep track of robots moving right ('R')
        stack = []

        # iterate through each robot in the sorted order of positions
        for curr_robo in robots:
            # if the robot moves to the right, add it to the stack
            if directions[curr_robo] == 'R':
                stack.append(curr_robo)
            else:
                # if the robot moves to the left
                while stack and healths[curr_robo] > 0:
                    # compare health of current robot with the robot on top of the stack
                    if healths[stack[-1]] > healths[curr_robo]:
                        # current robot loses all health
                        healths[curr_robo] = 0
                        # reduce health of the top robot in stack
                        healths[stack[-1]] -= 1
                    elif healths[stack[-1]] < healths[curr_robo]:
                        # reduce health of current robot
                        healths[curr_robo] -= 1
                        # top robot in stack loses all health
                        healths[stack.pop()] = 0
                    else:
                        # both robots lose all health
                        healths[curr_robo] = 0
                        healths[stack.pop()] = 0
        
        # return the healths of robots that survived (health > 0)
        return [health for health in healths if health > 0]

if __name__ == '__main__':
    s = Solution()
    print(s.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"))
    print(s.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"))
    print(s.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"))