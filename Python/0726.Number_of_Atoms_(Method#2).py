import re
from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # replace instances like 'O2' with '(O)2'
        formula = re.sub(r'([A-Z][a-z]*)(\d)', r'(\1)\2', formula)
        # ensure ')' is followed by either a digit or end of string to prevent syntax errors
        formula = re.sub(r'(\))(\D|$)', r'\g<1>1\2', formula)
        
        # tokenize the preprocessed formula
        tokens = re.findall(r'[A-Z][a-z]*|\d+|[()]', formula)
        
        # initialize a stack to manage nested multipliers
        coefficients = []
        # initialize a current multiplier for the current atom group
        multiplier = 1
        # initialize a counter to store counts of each atom
        counts = Counter()
        
        # traverse tokens in reverse order to compute counts
        for token in tokens[::-1]:
            if token == ')':
                # skip closing parentheses for now
                continue
            
            if token == '(':
                # adjust multiplier for nested parentheses
                multiplier //= coefficients.pop()
                continue
            
            if token.isnumeric():
                # store multiplier for the current atom group
                coefficients.append(int(token))
                # update current multiplier
                multiplier *= coefficients[-1]
                continue
            
            # if token is an atom (e.g. 'H', 'Ca'), add the atom count considering the current multiplier
            counts[token] += multiplier
        
        # format the output string i.e. join elements in sorted order, excluding counts of 1
        return ''.join(str(element) for pair in sorted(counts.items()) for element in pair if element != 1)

if __name__ == '__main__':
    s = Solution()
    print(s.countOfAtoms("H2O"))
    print(s.countOfAtoms("Mg(OH)2"))
    print(s.countOfAtoms("K4(ON(SO3)2)2"))
    print(s.countOfAtoms("Ca(OH)2Mg(OH)2"))
    print(s.countOfAtoms("((CH3)2(C2H5)3)2(Mg(CO3)2)"))
    print(s.countOfAtoms("K4(ON(SO3)2)3(Fe(CN)6)2"))
    print(s.countOfAtoms("((((H2SO4)50(NaCl)30)10(Cu(NO3)2)40)20(Mg(OH)2)60)5"))
    print(s.countOfAtoms("(((K4(ON(SO3)2)3(Fe(CN)6)2)10(Mg(OH)2)20)5(H2O)50)6"))
    print(s.countOfAtoms("(((K4(ON(SO3)2)3(Fe(CN)6)2)4(Mg(OH)2)10)2(H2O)5)3"))