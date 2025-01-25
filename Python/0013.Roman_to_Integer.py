class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100,
                            'D': 500, 'M': 1000}
        
        total, prev = 0, 0

        for char in reversed(s):
            curr = roman_to_int_map[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr

        return total

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MIXCVL"))