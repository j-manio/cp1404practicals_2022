"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur once the value type of the program is looking for is different. Like putting a letter
2. When will a ZeroDivisionError occur?
When a number is divided by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By while loop it can error check for zeros, or using ifs.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator > 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
