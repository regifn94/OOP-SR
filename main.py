class Main():

    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        print("ini method constructor")

    def pejumlahan(self):
        result = self.angka1 + self.angka2
        print("hasil penjumlahan " , result)

main = Main(10,2)
#main.detail_product()
main.pejumlahan()