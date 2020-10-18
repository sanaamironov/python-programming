# File:    nums.py
# Started: by Dr. Gibson
# Author:  Sanaa Mironov
# Date:    Oct 24, 2016
# Section: 04
# Description:
#   This file contains python code that uses functions to
#   allow a user to get basic information about a number
#   they've entered.

MIN_VAL = -1000000
MAX_VAL =  1000000

def evenOrOdd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"    

def posNegZero(num):
    if num < 0 :
        return "negative"
    elif num == 0:
        return "zero"
    else:
        return "postive"    


def getValidInt(minn, maxx):
    message = "Please enter a number between " + str(minn) + " and " + \
        str(maxx) + " (inclusive): "

    newInt = int(input(message))
    while newInt <= minn or newInt >= maxx:
        newInt = int(input(message))
    return newInt



def main():

    print("Welcome to the number program!")

    userNum = getValidInt(MIN_VAL,MAX_VAL)

    sign = posNegZero(userNum)
    print("The number", userNum, "is", sign)

    result = evenOrOdd(userNum)
    print("The number", userNum, "is", result)

    print("Thank you for using the number program!  Come again!")


main()