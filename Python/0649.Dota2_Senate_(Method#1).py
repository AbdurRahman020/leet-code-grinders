from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # initialize two deques to keep track of the positions of 'R' (Radiant) and 'D' (Dire) senators
        radiant_queue, dire_queue = deque(), deque()
        # get the total number of senators in the input string
        total_senators = len(senate)
        
        # populate the deques with the indices of 'R' and 'D' senators
        for i in range(total_senators):
            if senate[i] == 'R':
                # append the index of the 'R' senator to radiant_queue
                radiant_queue.append(i)
            else:
                # append the index of the 'D' senator to dire_queue
                dire_queue.append(i)
        
        # continue the loop as long as there are senators from both parties
        while len(radiant_queue) != 0 and len(dire_queue) != 0:
            # get the position of the next 'R' senator and remove it from the queue
            radiant_pos = radiant_queue.popleft()
            # get the position of the next 'D' senator and remove it from the queue
            dire_pos = dire_queue.popleft()
            # increment the total_senators count to simulate the next round
            total_senators += 1
            
            # determine which senator wins and will be re-added to the queue
            if radiant_pos < dire_pos:
                # the 'R' senator wins and will appear in the next round
                radiant_queue.append(total_senators)
            else:
                # the 'D' senator wins and will appear in the next round
                dire_queue.append(total_senators)
        
        # after the loop ends, check which queue is not empty
        if len(radiant_queue) > 0:
            # if radiant_queue has senators left, Radiant wins
            return 'Radiant'
        # if dire_queue has senators left, Dire wins
        return 'Dire'

if __name__ == '__main__':
    s = Solution()
    print(s.predictPartyVictory('RD'))
    print(s.predictPartyVictory('RDD'))