# Set kosong
my_set = set()

# Set dengan elemen
numbers_set = {1, 2, 3, 4, 5, 5,7,7,8,8}
mixed_set = {1, "Python", 3.14, True}

print(numbers_set)
print(mixed_set)

# Menambahkan Elemen
numbers_set.add(6)

# Menghapus Elemen
numbers_set.remove(3)  # Error jika elemen tidak ditemukan
numbers_set.discard(4) # Tidak error jika elemen tidak ditemukan
numbers_set.pop()      # Menghapus elemen secara acak
numbers_set.clear()    # Menghapus semua elemen

# Operasi Himpunan
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

print(set_A | set_B)  # Union: {1, 2, 3, 4, 5, 6}
print(set_A & set_B)  # Intersection: {3, 4}
print(set_A - set_B)  # Difference: {1, 2}
print(set_A ^ set_B)  # Symmetric Difference: {1, 2, 5, 6}
