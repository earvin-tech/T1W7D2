# lambda functions as anonymous functions

def greet(name, cb):
    print(f"Hello {name}")
    cb()

# def say_bye():
#     print("Bye!!!!")

# say_bye = lambda : print("Bye!!")

greet("John", lambda : print("Bye!!"))