class Teacher:
    
    # instance creator (new empty object)
    def __new__(cls, *args, **kwars):
        print("1. Create a new instance of class Teacher")
        return super().__new__(cls)
    
    # constructor (instance initializer)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("2. Initialize the new instance of class Teacher")
        print("My name is {0} ({1} Years Old)".format(self.name, self.age))

    # string representator
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, age={self.age})"

    def __del__(self):
        print('3. Object destroyed')

t1 = Teacher("Semmy",30)
t2 = Teacher("Any",22)


# print(repr(t1))  # Teacher(name=Semmy, age=30)
# print(repr(t2))  # Teacher(name=Any, age=22)
# print(str(t1))   # Teacher Regi, 30 years old

#delete object
del t1
