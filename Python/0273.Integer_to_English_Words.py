class Solution:
    def numberToWords(self, num: int) -> str:
        # dictionary mapping numbers to their corresponding words
        number_to_word = {
          1000000000: 'Billion',
          1000000: 'Million',
          1000: 'Thousand',
          100: 'Hundred',
          90: 'Ninety',
          80: 'Eighty',
          70: 'Seventy',
          60: 'Sixty',
          50: 'Fifty',
          40: 'Forty',
          30: 'Thirty',
          20: 'Twenty',
          19: 'Nineteen',
          18: 'Eighteen',
          17: 'Seventeen',
          16: 'Sixteen',
          15: 'Fifteen',
          14: 'Fourteen',
          13: 'Thirteen',
          12: 'Twelve',
          11: 'Eleven',
          10: 'Ten',
          9: 'Nine',
          8: 'Eight',
          7: 'Seven',
          6: 'Six',
          5: 'Five',
          4: 'Four',
          3: 'Three',
          2: 'Two',
          1: 'One'
        }
        
        # handle the special case where the number is zero
        if num == 0:
            return 'Zero'
        
        # initialize an empty string to build the result
        words = ''
        
        # iterate over the dictionary items in descending order
        for val, unit in number_to_word.items():
            # initialize count to 0 for each value
            count = 0
            # check if the current number is greater than or equal to the current dictionary key
            if num >= val:
                # compute how many times the current dictionary key fits into num
                count = num // val
                # update num to the remainder after extracting the value
                num %= val
                
                # check if count is greater than 1 or if the value is 100 or more
                if count > 1 or val >= 100:
                    # recursively call numberToWords to convert the count to words, and append the unit
                    words = words + ' ' + self.numberToWords(count) + ' ' + unit
                else:
                    # append the unit directly if count is 1 or less
                    words += ' ' + unit
        
        # remove leading spaces from the resulting words string
        words = words[1:]
        
        # return the final word representation
        return words

if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(123))
    print(s.numberToWords(12345))
    print(s.numberToWords(1234567))