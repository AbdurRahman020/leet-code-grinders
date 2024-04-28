class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[':']', '{':'}', '(':')'}
        
        for brackets in s:
            if brackets in pairs:
                stack.append(brackets)
            elif len(stack) == 0 or brackets != pairs[stack.pop()]:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('(){}[]'))
    print(s.isValid('[{()}][{]'))