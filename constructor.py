class Mobil:

    def __init__(self, nama_mobil, kecepatan):
        self.nama_mobil = nama_mobil
        self.kecepatan = kecepatan

    def print_nama_mobil(self):
        print("nama mobil : ", self.nama_mobil)
        print("kecepatan ", self.kecepatan)

ferari = Mobil("Ferari", "150 km/jam")
ferari.print_nama_mobil()

bmw = Mobil("BMW", "100 km/jam")
bmw.print_nama_mobil()