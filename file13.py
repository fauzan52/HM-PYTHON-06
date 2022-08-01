#Turunan atau pewarisan 
class ManusiaHidup():
    jumtangan = 2  # class atribut

    def __init__(self, nama, alamat):  # construktor
        self.name = nama  # nama ,adress objeck atribut
        self.adress = alamat
        self.jummata = "2"

    def hello(self):
        return "Heloo {}, selamat siang"  .format(self.name)

    def __str__(self):
        return 'nama {} alamat {} jumplah mata {} dengan tangan {}'.format(self.name, self.adress, self.jumtangan, self.jumtangan)

class Pegawai(ManusiaHidup): #class turunan dari class manusia hidup
        pass #class mencangkup semua yang dimiliki class pegawai karena merupakan turunan
    
you = ManusiaHidup("biruu", "tulungagung")
print(you)
print(you.hello())
print("perbadingan===========[karena class pegawai mempeunyai yang dipunyai class manusia hidup]")
ai = ManusiaHidup("Shiro", "tulungagung")
print(ai)
print(ai.hello())