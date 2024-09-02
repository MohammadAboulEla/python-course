# Try-Except for Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling Multiple Exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid input! Please enter a number.")
