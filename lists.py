#list = used to store multiple items in a single variable. Lists are mutable, meaning they can be changed after creation. Lists are created using square brackets [] and can contain items of different data types.
# Lists are ordered, meaning the items have a defined order, and that order will not change unless you explicitly reorder the list. Lists allow duplicate values.
# Lists are indexed, meaning each item has a corresponding index number, starting from 0 for the first item.
# Lists are iterable, meaning you can loop through the items in a list using a for loop or other iteration methods.
# Lists can be nested, meaning you can have lists within lists.
# Lists can be sliced, meaning you can access a range of items in a list using the colon (:) operator.
# Lists can be concatenated, meaning you can combine two or more lists into one using the + operator.
# Lists can be repeated, meaning you can repeat a list multiple times using the * operator.
# Lists can be sorted, meaning you can sort the items in a list using the sort() method.
# Lists can be reversed, meaning you can reverse the order of the items in a list using the reverse() method.
# Lists can be copied, meaning you can create a copy of a list using the copy() method.
# Lists can be cleared, meaning you can remove all items from a list using the clear() method.
# Lists can be extended, meaning you can add multiple items to a list using the extend() method.
# Lists can be inserted, meaning you can add an item at a specific index using the insert() method.
# Lists can be removed, meaning you can remove an item from a list using the remove() method.
# Lists can be popped, meaning you can remove an item from a list using the pop() method. The pop() method removes the last item by default, but you can specify an index to remove a specific item.
# Lists can be counted, meaning you can count the number of occurrences of an item in a list using the count() method.
# Lists can be found, meaning you can find the index of the first occurrence of an item in a list using the index() method.
# Lists can be checked for membership, meaning you can check if an item is in a list using the in operator.
# Lists can be checked for length, meaning you can check the number of items in a list using the len() function.
# Lists can be checked for emptiness, meaning you can check if a list is empty using the not operator.
# Lists can be checked for type, meaning you can check if a variable is a list using the isinstance() function.
# Lists can be checked for equality, meaning you can check if two lists are equal using the == operator.
# Lists can be checked for identity, meaning you can check if two lists are the same object in memory using the is operator.
# Lists can be checked for sorting, meaning you can check if a list is sorted using the sorted() function.
# Lists can be checked for reversing, meaning you can check if a list is reversed using the reversed() function.
# Lists can be checked for copying, meaning you can check if a list is copied using the copy() function.
# Lists can be checked for extending, meaning you can check if a list is extended using the extend() function.
# Lists can be checked for inserting, meaning you can check if a list is inserted using the insert() function.
# Lists can be checked for removing, meaning you can check if a list is removed using the remove() function.
# Lists can be checked for popping, meaning you can check if a list is popped using the pop() function.
# Lists can be checked for counting, meaning you can check if a list is counted using the count() function.

# Lists can be checked for finding, meaning you can check if a list is found using the index() function.
# Lists can be checked for membership, meaning you can check if a list is a member using the in operator.


food=["pizza","burger","pasta","salad"]
print(food) # print the list
print(food[0]) # print the first item in the list
print(food[1]) # print the second item in the list

food[0]="sushi" # change the first item in the list
print(food) # print the list after changing the first item

food.append("Chicken") # add an item to the end of the list
print(food) # print the list after adding an item   

food.remove("burger") # remove an item from the list
print(food) # print the list after removing an item

food.insert(1,"fries") # insert an item at a specific index in the list
print(food) # print the list after inserting an item

food.sort() # sort the list in alphabetical order
print(food) # print the list after sorting

food.clear() # clear the list
print(food) # print the list after clearing
