class Animal:
    def __init__(self, name, age, color, type):
        self.name = name
        self.age = age
        self.color = color,
        self.__type = type
    
    def __eat(self, type_food, time):  # Private method
        print(f"{self.name} is eating {type_food} at {time}.")

    def __run(self, duration):  # Private method
        print(f"{self.name} is running for {duration} minutes.")

    # Public method untuk memanggil metode private
    def do_eat(self, food, time):
        self.__eat(food, time)

    def do_run(self, duration):
        self.__run(duration)
    
    def fly(self, high):
        print(f"{self.name} is flying at {high} meters high.")
    
    def sleep(self, time):
        print(f"{self.name} is sleeping for {time} hours.")
    
    def sound(self):
        print("Animal makes a sound.")
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Color: {self.color}")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    def fly(self):
        print("Cat can't fly.")
    
    def sound(self):
        print("Meuw Meuw.")
    
    def play(self):
        print("Cat likes to play.")

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    def fly(self):
        print("Dog can't fly.")
    
    def sound(self):
        print("Guog Goug.")
    
    def play(self):
        print("Dog likes to play.")

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    def fly(self):
        print("Bird can fly.")
    
    def sound(self):
        print("Kiew Kiew.")
    
    def play(self):
        print("Bird doesn't like to play.")

# Membuat objek dari masing-masing class
animal = Animal("Generic Animal", 10, "Brown", "Burung")
animal.show()
animal.do_eat("Grass", "12:00 PM")
animal.do_run(15)
animal.fly(5)
animal.sleep(8)
animal.sound()

kitty = Cat("Kitty", 2, "White")
kitty.show()
kitty.eat("Fish", "1:00 PM")
kitty.run(5)
kitty.fly()
kitty.sleep(6)
kitty.sound()
kitty.play()


doggy = Dog("Doggy", 3, "Black")
doggy.show()
doggy.eat("Meat", "2:00 PM")
doggy.run(10)
doggy.fly()
doggy.sleep(7)
doggy.sound()
doggy.play()

birdy = Bird("Birdy", 5, "Yellow")
birdy.show()
birdy.eat("Seeds", "3:00 PM")
birdy.run(2)
birdy.fly()
birdy.sleep(5)
birdy.sound()
birdy.play()
