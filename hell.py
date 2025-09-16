def factorial(n):
    if n == 0:
        return 1
    else:
        print(n * factorial(n - 1))
        
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}.")
print("This is the second line that should be printed in blue color")

from itertools import imap
def factorial(x):
    return reduce(long.__mul__, imap(long, xrange(1, x + 1)))


print factorial(1000)
