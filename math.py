from argparse import ArgumentError
from unittest import result


def add(*args):
    result = 0
    for num in args:
        result += num
    return result

def sub(num1,*args):
    result = num1
    for num in args:
        result -= num
    return result

def multi(*args):
    result = 1
    print("first arg",result)
    for num in args:
        result = result * num
    return result

def div(num1,num2):
    result = num1 / num2
    return result