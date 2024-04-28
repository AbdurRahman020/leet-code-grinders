class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right)//2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))
    print(s.mySqrt(792))