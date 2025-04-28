rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ") 

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()  # Move to the next line after each row 