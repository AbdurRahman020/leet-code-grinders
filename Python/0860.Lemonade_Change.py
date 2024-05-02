class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # initialize variables to keep track of available change
        available_5, available_10 = 0, 0
        # iterate through each bill in the list
        for b in bills:
            # if the bill is $5
            if b == 5:
                # increase the count of available $5 bills
                available_5 += 1
            # if the bill is $10
            elif b == 10:
                # check if there's no available $5 bill to give change
                if available_5 == 0:
                    return False
                # increase the count of available $10 bills
                available_10 += 1
                # decrease the count of available $5 bills since we gave change
                available_5 -= 1
            # if the bill is $20
            else:
                # check if we can give change using a combination of $5 and $10 bills
                if available_5 >= 1 and available_10 >= 1:
                    # use a $5 bill for change
                    available_5 -= 1
                    # use a $10 bill for change
                    available_10 -= 1
                 # check if we can give change using three $5 bills
                elif available_5 >= 3:
                    # use three $5 bills for change
                    available_5 -= 3
                else:
                    # if neither condition is satisfied, return False as we can't give change
                    return False
        # if all bills are successfully processed, return True
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.lemonadeChange([5,5,5,10,20]))
    print(s.lemonadeChange([5,5,10,10,20]))