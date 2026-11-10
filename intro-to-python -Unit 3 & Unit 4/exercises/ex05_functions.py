"""Exercise 5: functions.

Topics: def, parameters, default values, return, calling one function from another.

From here on, exercises are written as functions. Several of these tasks are
the same problems you solved as plain scripts in Exercises 1 and 2, so you can
compare the two styles.

How to work:
    1. Each function contains  raise NotImplementedError(...).
       Delete that line and write the body so the function returns the right value.
    2. Read the docstring of each function: it shows example calls and results.
    3. Check your work: python check.py ex05
    4. Try your functions yourself in the Python shell:
           python
           >>> import sys; sys.path.insert(0, "exercises")
           >>> from ex05_functions import greet
           >>> greet("Ada")
"""


def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def is_even(number):
    """Return True if number is even, otherwise False."""
    return number % 2 == 0


def total_cost(price, quantity, vat_rate=0.2):
    """Return price x quantity plus VAT, rounded to 2 decimal places."""
    subtotal = price * quantity
    vat = subtotal * vat_rate
    return round(subtotal + vat, 2)


def grade_band(score):
    """Return the grade band for a score from 0 to 100."""

    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 70:
        return "Distinction"
    elif score >= 60:
        return "Merit"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


def describe_result(name, score):
    """Return a sentence about a student's result."""
    band = grade_band(score)
    return f"{name} scored {score}: {band}"
