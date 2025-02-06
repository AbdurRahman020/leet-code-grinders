from collections import deque

class Solution:
    def predictPartyVictory1(self, senate: str) -> str:
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
    
    def predictPartyVictory2(self, senate: str) -> str:
        # initialize a deque with the senators' string for efficient pop operations from both ends
        senators_queue = deque(senate)
        
        # initialize count to track the number of consecutive senators of the current party
        count = 0
        # variable to store the party of the senator currently being processed
        curr_party = ''
        
        # continue processing until the queue is empty or we've processed enough senators
        while senators_queue and count < len(senate):
            # remove the senator at the front of the queue to process them
            curr_senator = senators_queue.popleft()
                
            # if there is no current party or current senator belongs to the current party
            if curr_party == '':
                # set the current party to the party of this senator and reset count
                count = 1
                curr_party = curr_senator
                # re-add the senator to the end of the queue for future rounds
                senators_queue.append(curr_senator)
            # if the current senator is from the same party as the current party
            elif curr_party == curr_senator:
                # increment count as the senator is from the same party
                count += 1
                # re-add the senator to the end of the queue
                senators_queue.append(curr_senator)
            # if count is 1 and the senator is from the opposite party
            elif count == 1:
                # reset current party and count because the current party has been defeated
                count = 0
                curr_party = ''
            # if count is greater than 1 and the senator is from the opposite party
            else:
                # decrement count as the current party still has influence over the opposite party
                count -= 1
        
        # determine the winner based on the party of the last senator remaining in the queue
        return 'Radiant' if senators_queue[0] == 'R' else 'Dire'


if __name__ == '__main__':
    s = Solution()
    
    print(s.predictPartyVictory1('RD'))
    print(s.predictPartyVictory1('RDD'))
    
    print(s.predictPartyVictory2('RD'))
    print(s.predictPartyVictory2('RDD'))
