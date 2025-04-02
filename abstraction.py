from abc import ABC, abstractmethod
import math

# Abstract Class
class Perhitungan(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

# Kelas Persegi (Implementasi Perhitungan)
class Persegi(Perhitungan):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi

# Kelas Lingkaran (Implementasi Perhitungan)
class Lingkaran(Perhitungan):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return math.pi * self.radius * self.radius

    def keliling(self):
        return 2 * math.pi * self.radius

# Contoh Penggunaan
persegi = Persegi(5)
print(f"Luas Persegi: {persegi.luas()}")
print(f"Keliling Persegi: {persegi.keliling()}")

lingkaran = Lingkaran(7)
print(f"Luas Lingkaran: {lingkaran.luas():.2f}")
print(f"Keliling Lingkaran: {lingkaran.keliling():.2f}")