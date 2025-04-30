name="Nishan"
# this is a global variable 
# it is accessible from anywhere in the code
# it is not limited to the function
# this is a good example of variable scope



def display_name():
    name="Brother"
    print(name)
    # this is a local variable
    # it is only accessible within the function
    # it is not accessible outside the function
    # this is a good example of variable scope

print(name)
# this will raise an error because name is not defined outside the function

display_name()

#LEGB rule
# Local, Enclosing, Global, Built-in
# this is the order in which python looks for variables
# it first looks for the variable in the local scope
# then it looks for the variable in the enclosing scope
# then it looks for the variable in the global scope
# then it looks for the variable in the built-in scope
# this is a good example of variable scope
