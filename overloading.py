class Perpustakaan:
    def cari_buku(self, judul):
        return f"Buku '{judul}' ditemukan di perpustakaan."
    
    # def cari_buku(self, judul, penulis):
    #     return f"Buku '{judul}' karangan '{penulis}' ditemukan di perpustaka"
    
    # def cari_buku(self, isbn):
    #     return f"Buku dengan ISBN '{isbn}' ditemukan di perpustakaan."
    
p = Perpustakaan()
print(p.cari_buku("programming"))