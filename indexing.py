#index operator is used to access the elements of a list, tuple, or string. The index operator is represented by square brackets [] and is used to access the elements of a sequence by their index. The index operator can also be used to slice a sequence, which means to access a range of elements in a sequence using the start and end indices.


name="nishan Bhattarai"

# if (name[0].islower()):
#     print("First character is lowercase")
#     name=name.capitalize()
#     print(name)
# else:
#     print("First character is uppercase")
first_name=name[0:6].upper()
print(first_name)

last_name=name[7:16].lower()
print(last_name)

last_character=name[-1] # negative indexing
print(last_character)
    