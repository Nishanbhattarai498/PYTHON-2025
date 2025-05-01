     


try:
    with open('test.tx')as file:

        content = file.read()
        print(content)
except FileNotFoundError as e:
       print(e)
       print("File not found")
