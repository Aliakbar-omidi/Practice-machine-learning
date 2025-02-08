
from functools import reduce

num = [2, 3, 4, 5]


# map
def zarb_dar_do(x):
    return x * 2


print("map =>", list(map(zarb_dar_do, num)))


# filter
def fil(x):
    return x >= 3


print("filter =>", list(filter(fil, num)))


# reduce
def factorial(x, y):
    return x + y


print("reduce =>", reduce(factorial, num))

