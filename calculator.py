# https://github.com/sofiagalindo5/lab10-SG-GP.git
# Partner 1: Sofia Galindo
# Partner 2: Gabrielle Polito

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b/a

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b

