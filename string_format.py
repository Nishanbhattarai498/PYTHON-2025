# animal ="Cow"
# item="moon"

# print("The {} is on the {}".format(animal,item))##format method
# # The Cow is on the moon
# print(f"The {animal} is on the {item}")#f-string
# # The Cow is on the moon
# print("The {0} is on the {1}".format(animal,item))#positional argument
# # The Cow is on the moon
# print("The {animal} is on the {item}".format(animal=item,item=item))#keyword argument
# # The Cow is on the moon

name = "Nishan"

print("Hello, my name is {}".format(name))#format method
print("Hello,my name is {:15} . hey silly".format(name))#format method with width
print("Hello,my name is {:<15} . hey silly".format(name))#format method with width left aligned
print("Hello,my name is {:>15} . hey silly".format(name))#format method with width right aligned
print("Hello,my name is {:^15} . hey silly".format(name))#format method with width center aligned


