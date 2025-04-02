class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Color: {self.color}")

    def __eat(self, type_food, time):  # Private method
        print(f"{self.name} is eating {type_food} at {time}.")

    def __run(self, duration):  # Private method
        print(f"{self.name} is running for {duration} minutes.")

    # Public method untuk memanggil metode private
    def do_eat(self, food, time):
        self.__eat(food, time)

    def do_run(self, duration):
        self.__run(duration)

# Membuat objek
animal = Animal("Bobby", 5, "Brown")

animal.show()

# Memanggil metode private melalui metode publik
animal.do_eat("Meat", "12:00 PM")
animal.do_run(10)

# Jika mencoba memanggil langsung metode private, akan terjadi error
# animal.__eat("Meat", "12:00 PM")  # Ini akan error
# animal.__run(10)  # Ini juga akan error
