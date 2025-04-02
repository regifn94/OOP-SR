from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, merk, harga, tahun):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self.merk = merk
        self.harga = harga
        self.tahun = tahun

    @abstractmethod
    def hitung_premi(self):
        pass

    @abstractmethod
    def tampilkan_info(self):
        pass

class Mobil(Kendaraan):
    def hitung_premi(self):
        return 1000000 + (0.01 * self.harga)

    def tampilkan_info(self):
        return f"Mobil: {self.merk}, Tahun: {self.tahun}, Premi: Rp{self.hitung_premi():,.0f}"

class Motor(Kendaraan):
    def hitung_premi(self):
        return 500000 + (0.015 * self.harga)

    def tampilkan_info(self):
        return f"Motor: {self.merk}, Tahun: {self.tahun}, Premi: Rp{self.hitung_premi():,.0f}"

class MobilListrik(Mobil):
    def hitung_premi(self):
        premi_normal = super().hitung_premi()
        return premi_normal * 0.8

    def tampilkan_info(self):
        return f"Mobil Listrik: {self.merk}, Tahun: {self.tahun}, Premi: Rp{self.hitung_premi():,.0f}"

try:
    kendaraan_list = [
        Mobil("Toyota Avanza", 200_000_000, 2020),
        Motor("Honda Beat", 20_000_000, 2021),
        MobilListrik("Tesla Model 3", 800_000_000, 2022),
        Motor("Yamaha NMAX", 35_000_000, 2019)
    ]

    total_premi = 0
    for kendaraan in kendaraan_list:
        print(kendaraan.tampilkan_info())
        total_premi += kendaraan.hitung_premi()

    print(f"\nTotal Premi yang Harus Dibayarkan: Rp{total_premi:,.0f}")
except ValueError as e:
    print(e)
