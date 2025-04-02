class Mobil:
    def __init__(self, nama, warna, tahunPembuatan):
        self.nama = nama
        self.warna = warna
        self.__tahunPembuatan = tahunPembuatan
        self.__kecepatan = 0
    
    def ubahKecepatan(self, kecepatanBaru):
        self.__kecepatan = kecepatanBaru
        
    def __matikanMesin(self):
        self.__kecepatan = 0
    
    def informasiMobil(self):
        print("Nama mobil : ", self.nama)
        print("Warna mobil : ", self.warna)
        print("Tahun pembuatan : ", self.__tahunPembuatan)
        print("Kecepatan saat ini : ", self.__kecepatan)
    
mobil = Mobil("Avanza", "Merah", 2010)
mobil.informasiMobil()
print("=====================")
mobil.ubahKecepatan("200")
mobil.informasiMobil()
mobil.__matikanMesin()