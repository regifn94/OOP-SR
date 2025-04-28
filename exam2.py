class Dosen:
    def __init__(self, nama, nidn, gaji_pokok):
        self.nama = nama
        self.nidn = nidn
        self.__gaji_pokok = gaji_pokok # private property

    # getter 
    def get_gaji_pokok(self):
        return self.__gaji_pokok
    # setter
    def set_gaji_pokok(self, gaji):
        if gaji >= 3000000:
            self.__gaji_pokok = gaji
        else:
            print("Gaji pokok minimal 3.000.000")
  
    def hitung_total_pendapatan(self):
        return self.get_gaji_pokok()


class Peneliti:
    def __init__(self, id_penelitian, jumlah_penelitian, insentif_per_penelitian):
        self.id_penelitian = id_penelitian
        self.__jumlah_penelitian = jumlah_penelitian
        self.insentif_per_penelitian = insentif_per_penelitian

    def get_jumlah_penelitian(self):
        return self.__jumlah_penelitian

    def set_jumlah_penelitian(self, jumlah):
        if jumlah >= 0:
            self.__jumlah_penelitian = jumlah
        else:
            print("Jumlah penelitian tidak boleh negatif")

# multiple inheritance
class DosenPeneliti(Dosen, Peneliti):
    def __init__(self, nama, nidn, gaji_pokok, id_penelitian, jumlah_penelitian, insentif_per_penelitian):
        Dosen.__init__(self, nama, nidn, gaji_pokok)
        Peneliti.__init__(self, id_penelitian, jumlah_penelitian, insentif_per_penelitian)

    #overriding
    def hitung_total_pendapatan(self):
        return self.get_gaji_pokok() + (self.get_jumlah_penelitian() * self.insentif_per_penelitian)

    # Overloading method tampilkan_info dengan parameter opsional
    def tampilkan_info(self, ringkas=False):
        if ringkas:
            print(f"{self.nama} - NIDN: {self.nidn}")
        else:
            print(f"Nama: {self.nama}")
            print(f"NIDN: {self.nidn}")
            print(f"Gaji Pokok: {self.get_gaji_pokok()}")
            print(f"ID Penelitian: {self.id_penelitian}")
            print(f"Jumlah Penelitian: {self.get_jumlah_penelitian()}")
            print(f"Insentif per Penelitian: {self.insentif_per_penelitian}")
            print(f"Total Pendapatan: {self.hitung_total_pendapatan()}")



dp = DosenPeneliti(
    nama="Dr. Rina",
    nidn="0045678",
    gaji_pokok=6000000,
    id_penelitian="P-2025-02",
    jumlah_penelitian=0,
    insentif_per_penelitian=1000000
)

print("=== Info Lengkap ===")
dp.tampilkan_info()

print("\n=== Info Ringkas ===")
dp.tampilkan_info(ringkas=True)