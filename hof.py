# Higher Order Function
# A function that takes another function as an argument
# built-in higher order functions

# map
# it takes an iterable (list), performs some function on each item of that 
# iterable and creates a new iterable with those updated item value

numbers_list = [5, 7, 2, 3 ]

# def square(num):
#     return num * num

# squared_list = [25, 49, 4, 9]
# squared_list = map(square, numbers_list)

squared_list = map(lambda num: num * num, numbers_list )

print(list(squared_list))