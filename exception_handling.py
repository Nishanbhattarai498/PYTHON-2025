#exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
#exception handling is a mechanism to handle runtime errors in a program.

try:
   numerator=int(input("Enter the numerator: "))
   denominator=int(input("Enter the denominator: "))
   result = numerator/denominator
   print(result)

except ZeroDivisionError as e:
   print(e)
   print("Error: Cannot divide by zero.")

except ValueError as e:
   print(e)
   print("Error: Invalid input. Please enter a number.")


except Exception as e:
    print(e)
    print("Error: An unexpected error occurred.")

else:
    print("The result is: ", result) 


finally:
   print("this block will always execute")