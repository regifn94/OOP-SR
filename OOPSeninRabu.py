class main():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        #print("nama saya : ", param1)

    def penjumlahan(self):
        print("result : ", self.param1 + self.param2)

    
# param1 = int(input)
param1 = int(input())
param2 = int(input())
mainObj = main(param1,param2)
mainObj.penjumlahan()