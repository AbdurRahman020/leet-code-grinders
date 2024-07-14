from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # initialize a stack with a defaultdict to store atom counts
        stack = [defaultdict(int)]
        # length of the formula string
        formula_length = len(formula)
        # start parsing from the beginning of the formula
        current_index = 0

        while current_index < formula_length:
            # if current character is '(', start a new defaultdict on the stack
            if formula[current_index] == "(":
                stack.append(defaultdict(int))
                current_index += 1
            # if current character is ')', pop the top defaultdict from stack
            elif formula[current_index] == ")":
                top = stack.pop()
                current_index += 1
                start_index = current_index

                # find the multiplicity (number after the closing bracket)
                while (current_index < formula_length and formula[current_index].isdigit()):
                    current_index += 1
                multiplicity = int(formula[start_index:current_index] or 1)

                # multiply counts of atoms in the popped defaultdict and add to the new top
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplicity
            else:
                # if it's an atom name (starts with uppercase letter)
                start_index = current_index
                current_index += 1

                # continue until lowercase letters (to complete the atom name)
                while (current_index < formula_length and formula[current_index].islower()):
                    current_index += 1
                atom = formula[start_index:current_index]

                # continue until digits (to find multiplicity)
                start_index = current_index
                while (current_index < formula_length and formula[current_index].isdigit()):
                    current_index += 1
                multiplicity = int(formula[start_index:current_index] or 1)

                # add the atom with its count to the current top of the stack
                stack[-1][atom] += multiplicity

        # after parsing, the stack should contain only one defaultdict with final counts
        count_map = stack.pop()
        # sort atoms alphabetically
        sorted_atoms = sorted(count_map.items())

        # generate the final output string
        return "".join([f"{atom}{count if count > 1 else ''}" for atom, count in sorted_atoms])

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