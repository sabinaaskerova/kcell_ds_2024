def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

numerator = 10
denominator = 2
result = divide_numbers(numerator, denominator)
print(f"Division result of {numerator} by {denominator}: {result}")

numerator = 10
denominator = 0
result = divide_numbers(numerator, denominator)
print(f"Division result of {numerator} by {denominator}: {result}")