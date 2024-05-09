class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_happiness = 0

        for turn in range(k):
            if happiness[turn] < turn:
                break
            total_happiness += (happiness[turn] - turn)
        return total_happiness

if __name__ == '__main__':
    s = Solution()
    print(s.maximumHappinessSum([1,2,3], 2))
    print(s.maximumHappinessSum([1,1,1,1], 2))
    print(s.maximumHappinessSum([2,3,4,5], 1))