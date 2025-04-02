class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self._name = name

    name = property(get_name, set_name)  # Membuat properti secara manual

# Contoh penggunaan
p = Person("John")
print(p.name)  # John
p.name = "Doe"
print(p.name)  # Doe