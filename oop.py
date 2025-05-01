# activity 1

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, I protect {self.city} using {self.power}!")

# Inherited class with encapsulation
class FlyingHero(Superhero):
    def __init__(self, name, power, city, altitude_limit):
        super().__init__(name, power, city)
        self.__altitude_limit = altitude_limit  # Encapsulated attribute

    def fly(self):
        print(f"{self.name} is flying at {self.__altitude_limit} feet!")

# Another subclass
class SpeedHero(Superhero):
    def __init__(self, name, power, city, max_speed):
        super().__init__(name, power, city)
        self.max_speed = max_speed

    def run(self):
        print(f"{self.name} runs at {self.max_speed} mph!")

        # Create instances of the subclasses
hero1 = FlyingHero("Superman", "Super Strength", "Metropolis", 30000)
hero2 = SpeedHero("Spiderman", "Web-Spider", "New York", 100)

        #polymorphism challenge
class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Moved outside the class!
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each one behaves differently — POLYMORPHISM!





