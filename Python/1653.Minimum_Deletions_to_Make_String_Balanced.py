class Solution:
    def minimumDeletions(self, s: str) -> int:
        # initialize the count of 'b' characters encountered so far
        b_count = 0
        # initialize the minimum number of deletions needed
        deletions_needed = 0
        
        # iterate over each character in the string
        for char in s:
            if char == 'b':
                # increment the count of 'b' characters
                b_count += 1
            else:
                # for each 'a' encountered, update the deletions_needed
                # this is the minimum of:
                #  i. The current deletions_needed + 1 (deleting this 'a')
                # ii. The count of 'b' characters seen so far (i.e., the number of 'b' 
                #     characters we need to remove to keep all 'a's before them)
                deletions_needed = min(deletions_needed + 1, b_count)
        
        # return the minimum number of deletions required
        return deletions_needed

if __name__ == '__main__':
    s = Solution()
    print(s.minimumDeletions("aababbab"))
    print(s.minimumDeletions("bbaaaaabb"))