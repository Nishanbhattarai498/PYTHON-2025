#walrus operator=   := 
# The walrus operator is a new assignment expression operator introduced in Python 3.8.
# It allows you to assign a value to a variable as part of an expression, 
# which can make your code more concise and readable.
# The walrus operator is also known as the assignment expression operator.
# It is represented by the symbol :=.


# happy = True
# print(happy)  # Output: True

print(happy := True)  # Output: True


# foods =list()
# while True:
#     food = input("Enter a food item (or 'done' to finish): ")
#     if food == "done":
#         break
#     foods.append(food)


foods = list()

while (food := input("Enter a food item (or 'done' to finish): ")) != "done":
    foods.append(food)




