# #slicing is a way to access a range of elements in a sequence (like a list, tuple, or string) by specifying a start and end index.
# # In Python, slicing is done using the colon (:) operator within square brackets.
# # The syntax for slicing is: sequence[start:end:step], where:
# # - start is the index of the first element to include in the slice (inclusive)
# # - end is the index of the first element to exclude from the slice (exclusive)
# # - step is the number of elements to skip between each element in the slice (optional, default is 1)
# # Example of slicing a string

# name="John Doe"

# # Accessing a substring using slicing
# first_name = name[0:4]  # 'John'
# last_name = name[5:8]   # 'Doe'
# print("First Name:", first_name)
# print("Last Name:", last_name)

# funky_name=name[::2]  
# print("Funky Name:", funky_name)  # 'Jhn o'

# # reversed_name=name[::-1]
# print("Reversed Name:", reversed_name)  # 'eoD nhoJ'

website = "https://www.example.com"

slice=slice(8, -4)

print(website[slice])  # 'www.example'


