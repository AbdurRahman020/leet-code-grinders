class Solution:
    # define a static method to convert a string representing a number to an integer
    @staticmethod
    def str_to_int(s):
        # define a tuple containing characters representing digits
        nums = ('0','1','2','3','4','5','6','7','8','9')
        # initialize a buffer to hold the integer value
        buffer = 0
        # iterate through each character in the string
        for ch in s:
            # multiply the current value in buffer by 10 to shift digits to the left
            buffer *= 10
            # add the index of the current character in nums to buffer to convert it to integer
            buffer += nums.index(ch)
        # return the integer value
        return buffer
    
    def multiply(self, num1: str, num2: str) -> str:
        # convert both strings to integers using the defined static method, then multiply them
        # convert the result back to string and return
        return str(self.str_to_int(num1) * self.str_to_int(num2))

if __name__ == '__main__':
    s = Solution()
    print(s.multiply('2', '3'))
    print(s.multiply('123', '456'))