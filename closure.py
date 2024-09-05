# Closure
# it is the availablity of the variables of outer function inside the 
# inner function even when the outer function has already been complete

def greet(name):
    print("Hello")
    def display_name():
        print(name)

    return display_name


display = greet("John")
display()