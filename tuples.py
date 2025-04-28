student=("Nishan",30,"Nepal")
print(student)
print(student.count("Nishan")) # count the number of occurrences of "Nishan" in the tuple
print(student.index("Nepal")) # find the index of "Nepal" in the tuple

for x in student: # iterate through the tuple
    print(x) # print each item in the tuple

if "Nishan" in student: # check if "Nishan" is in the tuple
    print("Nishan is in the tuple") # print if "Nishan" is in the tuple
else:
    print("Nishan is not in the tuple")
    