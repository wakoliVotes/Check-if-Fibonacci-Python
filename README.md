### Check if Fibonacci Python Script
#### Overview and Background
- This Python script works by checking if an entered number is part of the Fibonnacci Sequence or Not
- The background which forms the basis of the project is how the Fibonacci Sequence is structured
- Notably, in the Fibonacci Sequence, the next value in the Sequence, is the sum of its two predecesors
- Thus, in the Sequence, first three values 0, 1, 1
- Sample list of Fibonacci Sequence is:
> #### 0, 1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 ...
### Python Script

```python
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
```


#### Other External Resources
- To find out more on creating the Fibonacci Sequence, check this Link [Fibonacci Sequence](https://gist.github.com/danny-votez/3111f753f452bcfc43f66b18a033b411) on GitHub
- For more information, read the article on [Python 101: Ultimate Python Guide]() on Medium. 
