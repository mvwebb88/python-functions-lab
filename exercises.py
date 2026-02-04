# exercises.py
# Python Functions Lab - Full Solutions
#
# Each exercise below defines a function and then prints a test call.
# Run with:
#   python3 exercises.py


# Exercise 1: Calculate Area of a Triangle

def calculate_area_triangle(base, height):
    """
    Return the area of a triangle using:
    area = (base * height) / 2
    """
    # Convert to float to ensure we return a decimal value (like 25.0)
    return (base * height) / 2


print("Exercise 1:", calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest

def simple_interest(principal, rate, time):
    """
    Return simple interest using:
    (principal * rate * time) / 100
    Where rate is a percentage (example: 5 means 5%).
    """
    return (principal * rate * time) / 100


print("Exercise 2:", simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount

def apply_discount(price, discount_percentage):
    """
    Return the new price after applying a discount percentage.

    Example:
      price=100, discount_percentage=25 -> 75
    """
    # Convert percentage to a decimal discount factor
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount


print("Exercise 3:", apply_discount(100, 25))


# Exercise 4: Convert Temperature

def convert_temperature(temp, unit):
    """
    Convert a temperature between Celsius and Fahrenheit.

    unit:
      'C' means temp is Celsius, convert to Fahrenheit
      'F' means temp is Fahrenheit, convert to Celsius
    """
    # Normalize unit to avoid issues with lowercase input like 'c' or 'f'
    unit = unit.strip().upper()

    if unit == "C":
        # Celsius -> Fahrenheit
        return (temp * 9 / 5) + 32
    elif unit == "F":
        # Fahrenheit -> Celsius
        return (temp - 32) * 5 / 9
    else:
        # If unit is not valid, raise a clear error
        raise ValueError("Unit must be 'C' or 'F'.")


print("Exercise 4: Convert 0°C to Fahrenheit:", convert_temperature(0, "C"))
print("Exercise 4: Convert 32°F to Celsius:", convert_temperature(32, "F"))


# Exercise 5: Sum to N

def sum_to(n):
    """
    Return the sum of all integers from 1 to n.

    Example:
      n=6 -> 1+2+3+4+5+6 = 21
    """
    total = 0

    # Loop from 1 up to and including n
    for num in range(1, n + 1):
        total += num

    return total


print("Exercise 5:", sum_to(6))


# Exercise 6: Find the Largest Number

def largest(a, b, c):
    """
    Return the largest of three integers.
    """
    # Start by assuming a is the largest
    current_largest = a

    # Compare b and c against the current largest
    if b > current_largest:
        current_largest = b
    if c > current_largest:
        current_largest = c

    return current_largest


print("Exercise 6:", largest(1, 2, 3))


# Exercise 7: Calculate a Tip

def calculate_tip(bill_amount, tip_percentage):
    """
    Return the tip amount based on:
      tip = bill_amount * (tip_percentage / 100)

    tip_percentage should be a whole number (ex: 20 for 20%).
    """
    return bill_amount * (tip_percentage / 100)


print("Exercise 7:", calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers (*args)

def product(*nums):
    """
    Return the product of any amount of numbers passed in.

    Examples:
      product(-1, 4) -> -4
      product(2, 5, 5) -> 50
    """
    result = 1

    # Multiply each number into result
    for n in nums:
        result *= n

    return result


print("Exercise 8:", product(2, 5, 5))


# Exercise 9: Basic Calculator

def basic_calculator(num1, num2, operation):
    """
    Perform a basic operation on two numbers.

    operation options:
      'add', 'subtract', 'multiply', 'divide'
    """
    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Prevent crashing on division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Operation must be: add, subtract, multiply, or divide.")


print("Exercise 9 Result:", basic_calculator(10, 5, "subtract"))
