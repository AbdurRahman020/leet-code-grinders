from typing import List
from itertools import product

class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
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
        
        # initialize an empty list to store the resulting letter combinations
        letter_combo_list = []
        
        # define a helper function for backtracking
        def backtrack(combo, next_digits):
            # if there are no more digits to process, add the current combination to the list
            if not next_digits:
                letter_combo_list.append(combo)
                return
            
            # iterate over the letters corresponding to the current digit
            for letter in keyboard[next_digits[0]]:
                # recur with the current letter added to the combination and the remaining digits
                backtrack(combo + letter, next_digits[1:])
        
        # start the backtracking process with an empty combination and the full set of digits
        backtrack('', digits)
        
        # return the list of letter combinations generated
        return letter_combo_list
    
    def letterCombinations2(self, digits: str) -> List[str]:
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
    
    print(s.letterCombinations1("23"))
    print(s.letterCombinations1(""))
    print(s.letterCombinations1("2"))
    
    print(s.letterCombinations2("23"))
    print(s.letterCombinations2(""))
    print(s.letterCombinations2("2"))
