import math

# Take input from the user and convert it to a floating-point number
num = float(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Square root of a negative number cannot be calculated using real numbers.")
else:
    # Calculate the square root
    result = math.sqrt(num)
    print(f"The square root of {num} is {result}")