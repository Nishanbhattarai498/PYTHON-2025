import os


path="C:\\Users\\Acer Nitro\\OneDrive\\Desktop\\test.txt"

if os.path.exists(path):
    print("File exists")    
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("It is a directory")
else:
    print("File does not exist")
