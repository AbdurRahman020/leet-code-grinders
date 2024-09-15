from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if the input string 'digits' is empty, return an empty list as there are no combinations
        if not digits:
            return []
        
        # define a mapping from each digit to its corresponding letters on a telephone keypad
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # create a generator expression that yields the string of letters corresponding
        # to each digit in 'digits'
        letter_combo_list = (keyboard[digit] for digit in digits)
        
        # compute the Cartesian product of these letter combinations using itertools.product
        # use a list comprehension to join each tuple of letters into a single string
        return [''.join(combo) for combo in product(*letter_combo_list)]

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations(""))
    print(s.letterCombinations("2"))