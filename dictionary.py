# Dictionary kosong
my_dict = {}

# Dictionary dengan data
student = {
    "name": "John",
    "age": 21,
    "grade": "A"
}

# Dictionary bersarang (nested dictionary)
nested_dict = {
    "student1": {"name": "Alice", "age": 22},
    "student2": {"name": "Bob", "age": 23}
}
print(student)
print(nested_dict)

# Mengakses Nilai
print(student["name"])  # Output: John

# Menambahkan / Mengubah Data
student["age"] = 22
student["city"] = "New York"

# Menghapus Data
del student["grade"]
student.pop("city")

# Mengakses Semua Key & Value
print(student.keys())    # Output: dict_keys(['name', 'age'])
print(student.values())  # Output: dict_values(['John', 22])
print(student.items())   # Output: dict_items([('name', 'John'), ('age', 22)])

# Iterasi Dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
