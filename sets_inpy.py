# # utensils={"hey","spoon","fork","knife","plate","bowl","cup","glass","mug","pot","pan"}

# # for x in utensils:
# #     print(x) # print each item in the set   


# # #sets are unordered, meaning the items do not have a defined order and that order may change over time. Sets do not allow duplicate values.
# # # Sets are mutable, meaning they can be changed after creation. Sets are created using curly braces {} or the
# # # set() constructor and can contain items of different data types.
# # # Sets are iterable, meaning you can loop through the items in a set using a for loop or other iteration methods.
# # # Sets can be nested, meaning you can have sets within sets.
# # # Sets can be sliced, meaning you can access a range of items in a set using the colon (:) operator.
# # # Sets can be concatenated, meaning you can combine two or more sets into one using the union() method or the | operator.
# # # Sets can be repeated, meaning you can repeat a set multiple times using the * operator.
# # # Sets can be sorted, meaning you can sort the items in a set using the sorted() function.
# # # Sets can be reversed, meaning you can reverse the order of the items in a set using the reversed() function.
# # # Sets can be copied, meaning you can create a copy of a set using the copy() method.
# # #set do not allow duplicate values, meaning you cannot have two identical items in a set.

# # #sets vs lists
# # # Sets are unordered, meaning the items do not have a defined order and that order may change over time. Lists are ordered, meaning the items have a defined order, and that order will not change unless you explicitly reorder the list.


utensils={"spoon","fork","knife","plate",}
# utensils.add("plate") # add an item to the set
# print(utensils) # print the set after adding an item
# utensils.remove("fork") # remove an item from the set
# print(utensils) # print the set after removing an item

# utensils.clear() # clear the set
# print(utensils) # print the set after clearing

dishes={"plate","bowl","cup","glass","mug","pot","pan"}
# utensils.update(dishes) # add multiple items to the set
# for x in utensils:
#     print(x) # print each item in the set

# dinner_table=utensils.union(dishes) # combine two sets into one

# for x in dinner_table:
#     print(x) # print each item in the set   


print(utensils.difference(dishes)) # find the difference between two sets
print(utensils.intersection(dishes)) # find the intersection between two sets