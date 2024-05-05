class Solution(object):
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral to an integer.

        :param s: The Roman numeral to be converted.
        :type s: str
        
        :return: The integer representation of the Roman numeral.
        :rtype: int
        """
        # dictionary to map each roman numeral to its corresponding integer value
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # variable to store the total integer value of the Roman numeral
        total = 0
        
        # iterate over each character in the input string
        for i in range(len(s)-1):
            # if the current numeral is smaller than the next numeral, subtract its value
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            # otherwise, add its value
            else:
                total += roman[s[i]]
        
        # add the value of the last numeral since it wasn't processed in the loop
        return total + roman[s[-1]]

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MIXCVL"))