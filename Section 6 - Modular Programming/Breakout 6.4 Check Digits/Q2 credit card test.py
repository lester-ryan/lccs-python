# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Breakout 6.4 Check digits Further Activities (ISBN and Credit Cards)
# Solution to Q2 - Luhn's algorithm


# The algorithm for summing the digits is the following.
# For digits at even indexes (the 0th digit, 2nd digit, etc.),
# simply add that digit to the cumulative sum.
# For digits at odd indexes (index 1, 3, etc.),
# double the digit's value, then if that doubled value is more than 10,
# add its digits together to make a number that is smaller than 10,
# then add this result into the sum.
def passLuhnTest(ccNo):
    
    if len(ccNo) != 16:
        return False

    if ccNo[0] != "4":
        return False

    sum = 0
    for i in range(16):
        digit = int(ccNo[i])
        if i%2 == 0:
            digit = digit * 2
            sum = sum + (digit//10)+(digit%10)
        else:
            sum = sum + digit
        
    return sum%10 == 0

# Test the function
print(passLuhnTest("4408041234567893")) # True => Pass (valid CC#)
print(passLuhnTest("4408041234567890")) # False => Fail (invalid CC#)

