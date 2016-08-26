"""Fruit string calculator
https://www.codewars.com/kata/fruit-string-calculator

Given a string of words and numbers. Extract the expression including:
1. the operator: either addition or subtraction
2. the two numbers that we are operating on

Return the result of the calculation.

Example:

"Panda has 48 apples and loses 4" returns 44

"Jerry has 34 apples and gains 6" returns 40

"loses" and "gains" are the only two words describing operators.

Should be a nice little kata for you :)

Note:
No fruit debts nor bitten apples = The numbers are integers and no negatives.
"""

import re


def calculate(string):
    """Computes final number of fruits"""
    _, num1, num2 = re.split(r'\D+', string)
    return int(num1) + int(num2) if 'gains' in string else int(num1) - int(num2)
