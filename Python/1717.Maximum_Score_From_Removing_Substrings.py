class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # initialize stacks to track characters while processing
        primary_stack, secondary_stack = [], []
        # a variable to accumulate the total score from pairs found
        total_score = 0
        
        # determine the order of characters based on the scores
        first_ch, second_ch = ('a', 'b') if x > y else ('b', 'a')
        # assign min and max score based on the values of x and y
        min_score, max_score = sorted((x, y))
        
        # process the string to find first pairs (first_ch and second_ch)
        for ch in s:
            # if the current character is the second character and the last in the stack is the first character
            if ch == second_ch and primary_stack and primary_stack[-1] == first_ch:
                # we found a valid pair, pop the last character from the primary stack
                primary_stack.pop()
                # add the maximum score to total_score
                total_score += max_score
            else:
                # otherwise, just push the current character onto the primary stack
                primary_stack.append(ch)
        
        # process the remaining characters in the primary stack for the second pair
        for ch in primary_stack:
            # if the current character is the first character and the last in the secondary stack is the second character
            if ch == first_ch and secondary_stack and secondary_stack[-1] == second_ch:
                # we found another valid pair, pop the last character from the secondary stack
                secondary_stack.pop()
                # add the minimum score to total_score
                total_score += min_score
            else:
                # otherwise, push the current character onto the secondary stack
                secondary_stack.append(ch)
        
        # return the total score accumulated from the valid pairs
        return total_score

if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumGain("cdbcbbaaabab", 4, 5))
    print(solution.maximumGain("aabbaaxybbaabb", 5, 4))