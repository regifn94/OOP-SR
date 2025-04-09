class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__gender = None
        
    def setGender(self, gender):
        self.__gender = gender
        
    def getInfo(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.__gender}"

p = Person("Liwe", 20)

print(p.getInfo())

p.setGender("Pria")

print(p.getInfo()) 