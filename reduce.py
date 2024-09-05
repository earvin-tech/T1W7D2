# built-in higher order function
# it takes a list/iterable then, performs some function and returns a single value

from functools import reduce

numbers = [3, 5, 8, 1, 2]

# def sum(a,b):
#     return a + b

# total_sum = reduce(sum, numbers)
total_sum = reduce(lambda a, b: a + b, numbers)

print(total_sum)