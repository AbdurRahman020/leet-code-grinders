class Solution:
    def average(self, salary: list[int]) -> float:
        # sort the list of salaries in ascending order
        salary.sort()
        # initialize the sum of salaries.
        salary_sum = 0
        # iterate through each salary in the sorted list
        for s in salary:
            # add the current salary to the total sum
            salary_sum += s
        # calculate the average salary excluding the lowest and highest salaries
        # subtract the lowest and highest salaries from the total sum,
        # then divide by the number of salaries minus 2.
        return (salary_sum - salary[0] - salary[-1]) / (len(salary) - 2)

if __name__  == '__main__':
    s = Solution()
    print(s.average([1000,2000,3000]))
    print(s.average([4000,3000,1000,2000]))