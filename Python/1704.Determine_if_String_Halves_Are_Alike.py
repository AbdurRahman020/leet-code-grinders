class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # calculate the length of half of the string
        half = len(s)//2
        
        # divide the string into two halves
        left_part = s[:half]
        right_part = s[half:]
        
        # define the set of vowels
        vowels = 'AEIOUaeiou'
        # initialize counters for vowels in each half
        left_counter, right_counter = 0, 0
        
        # count vowels in the left half
        left_counter = sum(1 for ch in left_part if ch in vowels)
        # count vowels in the right half
        right_counter = sum(1 for ch in right_part if ch in vowels)
        
        # check if the number of vowels in both halves are equal
        return left_counter == right_counter

if __name__ == '__main__':
    s = Solution()
    print(s.halvesAreAlike("book"))
    print(s.halvesAreAlike("textbook"))