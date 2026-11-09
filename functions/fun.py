#Function is colcetion of code porform spacify task

def say_hi():
    print("Hello user")
    
say_hi() # call the fuction

# pass information like parimter


def print_name(name):
    print("Hello " + name)

print_name("Tharuka")


# Return Statemant in python
def cuble(num): # to send a result back to the code that called it and immediately exit that function.
    return num * num * num
    
print(cuble(3))
