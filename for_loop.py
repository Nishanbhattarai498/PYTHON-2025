#for loop = a control flow statement for specifying iteration, which allows code to be executed
#once for each item in a sequence, such as a list, tuple, set, or string

#while loop=unlimited iteration, but for loop is limited to the number of items in the sequence

# for i in range(10):
#     print(i) # prints 0 to 9

# for i in range (50,100):
#     print(i) # prints 50 to 99  

# for i in range(50,100,5):
#         print(i) # prints 50, 55, 60, 65, 70, 75, 80, 85, 90

# for i in "Nishan":
#     print(i,end="") # prints each character in the string "Nishan"

import time

for second in range(10,0,-1):
    print(second)
    time.sleep(1) # sleep for 1 second
print("Happy New Year!")