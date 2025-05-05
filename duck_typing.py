#Duck Typing :: concept where the type or class of an object is
#  less important than the methods it defines or the way it behaves.
# In other words, if an object behaves like a certain type (i.e., it has the required methods), 
# it can be treated as that type,
#  regardless of its actual class.

# This is often summarized by the phrase "If it looks like a duck and quacks like a duck, it's a duck."

class Duck:
    def walk(self):
        print("Duck is walking")

    def talk(self):
        print("Duck is quacking")

class Chicken:
    # def walk(self):
    # print("Chicken is walking")

    def talk(self):
        print("Chicken is clucking")


class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("Person caught the animal")

duck=Duck()
chicken=Chicken()
person=Person()


person.catch(duck)
person.catch(chicken)
