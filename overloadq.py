# class Demo:
#     def show(self):
#         return "Hello"

#     def show(self):
#         return 123

# d = Demo()
# print(d.show())  # Output: 123


def method_1(nama, umur):
        print(f"Nama: {nama}, Umur: {umur}")

def method_2(nama, umur):
        print(f"Nama: {nama}, Umur: {umur * 2}") # Perhatikan operasi pada umur

    # Memanggil method_1
method_1("Alice", 30)  # Tidak ada kesalahan karena tipe data argumen sesuai
method_1(30, "Alice") # Akan terjadi kesalahan karena tipe data argumen tidak sesuai

    # Memanggil method_2
method_2("Bob", 25)
method_2(25, "Bob") # Akan terjadi kesalahan karena tipe data argumen tidak sesuai