class Mobil:
    def __init__(self, merk, model, warna, kecepatan=0):
        """Constructor untuk inisialisasi atribut mobil."""
        self.merk = merk
        self.model = model
        self.warna = warna
        self.kecepatan = kecepatan

    def tampilkan_info(self):
        """Method untuk menampilkan informasi mobil."""
        print(f"Mobil {self.merk} {self.model} berwarna {self.warna} dengan kecepatan {self.kecepatan} km/jam.")

    def percepat(self, kecepatan_baru):
        """Method untuk menambah kecepatan mobil."""
        self.kecepatan += kecepatan_baru
        print(f"{self.merk} {self.model} dipercepat menjadi {self.kecepatan} km/jam.")

    def rem(self):
        """Method untuk menghentikan mobil."""
        self.kecepatan = 0
        print(f"{self.merk} {self.model} telah berhenti.")


# Membuat dua objek mobil
mobil1 = Mobil("Toyota", "Avanza", "Hitam")
mobil2 = Mobil("Honda", "Civic", "Merah")

# Menampilkan informasi awal kedua mobil
mobil1.tampilkan_info()
mobil2.tampilkan_info()

# Mempercepat mobil1
mobil1.percepat(50)

# Menampilkan informasi setelah perubahan kecepatan
mobil1.tampilkan_info()

# Menghentikan mobil1
mobil1.rem()

# Menampilkan informasi setelah direm
mobil1.tampilkan_info()
