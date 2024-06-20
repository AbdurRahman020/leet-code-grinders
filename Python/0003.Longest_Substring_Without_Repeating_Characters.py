class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize last_repeat_index to tracks the position of the last occurrence of each character
        # initialize max_length to store the length of the longest substring found
        last_repeat_index, max_length = -1, 0
        
        # dictionary to store the most recent index of each character
        last_seen_index = {}
        
        # iterate through each character in the string along with its index
        for i, current_char in enumerate(s):
            # check if the character `current_char` is already in the `last_seen_index`
            # dictionary and if its last occurrence is after `last_repeat_index`
            if (
                current_char in last_seen_index
                and last_seen_index[current_char] > last_repeat_index
            ):
                # update `last_repeat_index` to the index of the last occurrence of `current_char`
                last_repeat_index = last_seen_index[current_char]
            
            # update the index of the current character `current_char` to `i`
            last_seen_index[current_char] = i
            
            # calculate the length of the current substring without repeating characters
            current_length = i - last_repeat_index
            # update `max_length` to store the maximum length found so far
            max_length = max(max_length, current_length)
        
        # return the length of the longest substring without repeating characters
        return max_length

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("abcabcbb"))