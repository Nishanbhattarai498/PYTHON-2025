import random

x=random.randint(1,6)
y=random.random() # random number between 0 and 1 floating point number
myList=['Rock','Paper','Scissors']  

z=random.choice(myList) # random choice from a list


cards=['Ace','King','Queen','Jack','10','9','8','7','6','5','4','3','2']    

random.shuffle(cards) # shuffle a list



print(x)
print(y)
print(z)
print(cards)
