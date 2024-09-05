# built-in higher order function 
# it takes an iterable (list), performs some function on each item of that 
# iterable and creates a new iterable with those values that returned true
# when passed into the function

names = ["John", "Mary", "James", "Michael","Patricia", "Marcus"]

# def longer_than_five(name):
#     return len(name) > 5
    # if len(name) > 5:
    #     return True
    # else:
    #     return False
    
# longer_names = filter(longer_than_five, names)
longer_names = filter(lambda name: len(name) > 5,names)
print(list(longer_names))