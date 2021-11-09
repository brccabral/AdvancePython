# Loop without a loop
# map(func, iterable1, [iterable2...])
# map(func, *iterables)
# the number of parameters in func must be the same count 
# of iterables passed

# Basic usage
people = ['Matt', 'Bryan', 'Tammy', 'Markus']

# old way
counts = []
for x in people:
    counts.append(len(x))
print(f'Old way: {counts=}')

# modern way
print(f'Mapped: {list(map(len, people))}')



# More complex - combine elements
# Notice different lens, multiple args

first_names = ['Apple', 'Chocolate', 'Fudge', 'Pizza']
last_names = ['Pie', 'Cake', 'Brownies']

def merg(a, b):
    return a + ' ' + b

# map stops at the shortest iterable
x = map(merg, first_names, last_names)
print(x)
print(list(x))



# Multiple functions = combine functions
# call multiple functions in one map call

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

from typing import Callable

def do_all(func: Callable, num: list):
    return func(num[0], num[1])

f = (add, subtract, multiply, divide)
v = [[5,3]]
n = list(v) * len(f) # [[5, 3], [5, 3], [5, 3], [5, 3]]
print(f'{f=} , {n=}')
# n is a list of list
m = map(do_all, f, n)
print(list(m))
