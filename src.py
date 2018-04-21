print("Enter a number and this tool check if its a prime number")
try:
    theNumber = int(input())
    assert theNumber > 0, "***ERROR: You must enter a positive integer."
except ValueError:
    print("***ERROR: You must enter an integer.")
    raise

#Generating the divisors
divisors = (i for i in range(2,theNumber))

successfulDivisors = []

#Checking divisors against the number one by one
#Store the divisor if it divides the number evenly
for k in range(2,theNumber):
    divisor = (next(divisors))
    if theNumber % divisor == 0:
        successfulDivisors.append(divisor)

#Presenting the outcome
if (len(successfulDivisors)) > 0:
    print("\nThe number is not a prime number since it can be divided evenly with the following numbers:")
    print(successfulDivisors)
else:
    print("The number is a prime number since it can be divided evenly with only the value of 1 and itself.")
