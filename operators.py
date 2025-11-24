# The basic mathematical operators are defined here.

def __add__(x, y):
    return x + y

def __subtract__(x, y):
    return x - y

def __multiply__(x, y):
    return x * y

def __divide__(x, y):
    return x / y

def solution(num_1, operator, num_2):
    if operator == "+":
        return num_1 + num_2
    if operator == "-":
        return num_1 - num_2
    if operator == "*":
        return num_1 * num_2
    if operator == "/":
        return num_1 / num_2