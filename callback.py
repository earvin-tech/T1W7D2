# Callback function 
# the main function finishes executing 
# and then the callback function is executed

def greet(name, cb):
    print(f"Hello {name}")
    cb()

def say_bye():
    print("Bye!!")

greet("Steve", say_bye)