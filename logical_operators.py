temp=int((input("Enter the temperature in Celsius: ")))

if temp >=12 or temp ==1:
    print("hey hey ")
elif temp >=0 and temp <=30:
    print("The temperature is in the normal range.")
elif temp >30 and temp <=50:
    print("The temperature is high.")
elif temp >50:
    print("The temperature is very high.")  
elif not temp < 0:
    print("The temperature is very low.")
else:
    print("The temperature is extremely low.")


