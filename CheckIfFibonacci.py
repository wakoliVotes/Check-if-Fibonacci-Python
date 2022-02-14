"""
The goal of this project is to create a function that when 
user inputs a number, the function checks whether the number 
belongs to the Fibonacci sequence or not
"""


# Declaring the function
def CheckIfFibonacci():
    # Next, asking user to define their target number to check
    numberToCheck = int(input("Enter Number: "))

# Notably, in the Fibonacci Sequence, the first three terms contains only 0 and 1
# This originates from the fact that the next value, is the sum of its two predecesors
# Thus, the first three values of the Fibonacci Sequence are 0, 1, 1
    numZero = 0
    numOne = 1
    numTwo = 1

# Part 1: Doing the first/initial check immediately the user enters a value based on 0 & 1

    if (numberToCheck == 0 or numberToCheck == 1):
        print("The Number is a part of Fibonacci Sequence")

# Part 2: For values greater than 0 and 1
    else:
        while numZero < numberToCheck:
            numZero = numOne + numTwo
            numTwo = numOne
            numOne = numZero
        if numZero == numberToCheck:
            print("The Number is part of Fibonacci Sequence")
        else:
            print("NO!, Number NOT part of Fibonacci Sequence")

# Call the function    
CheckIfFibonacci()