class Prey:

    def flee(self):
        print("The prey is fleeing!")

class Predator:
    
        def hunt(self):
            print("The predator is hunting!")

class Rabbit(Prey):
    
    def run(self):
        
        self.flee()  # Calling the flee method from the Prey class

class Hawk(Predator):
    
    def fly(self):
       
        self.hunt()  # Calling the hunt method from the Predator class

class Fish(Prey, Predator):
    
    def swim(self):
       
        self.flee()  # Calling the flee method from the Prey class
        self.hunt()  # Calling the hunt method from the Predator class


rabbit = Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()  # The prey is fleeing!
rabbit.run()  # The rabbit is running! The prey is fleeing!