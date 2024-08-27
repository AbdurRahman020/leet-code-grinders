from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
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
    print(s.predictPartyVictory('RD'))
    print(s.predictPartyVictory('RDD'))