class Solution(object):
    def intToRoman(self, num: int) -> str:
        roman_map = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 
                       50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman_num = ''
        for i in roman_map.keys():
            while i <= num:
                roman_num += roman_map[i]
                num -= i
        return roman_num

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))
    print(s.intToRoman(58))
    print(s.intToRoman(267))