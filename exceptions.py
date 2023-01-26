import sys


try:
    x = int(input("x: "))
    y = int(input("u: "))
except ValueError:
    print("Error intercepted: Invalid input")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error intercepted: Cannot divide by 0.")
    sys.exit(1)


print (f"The result of {x} divided by {y} is {result}")
