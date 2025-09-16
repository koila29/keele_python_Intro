def factorial(n):
    if n == 0:
        return 1
    else:
        print n * factorial(n - 1)
        
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}.")
print("This is the second line that should be printed in blue color")

#This is the name of the main repository
