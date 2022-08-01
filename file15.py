#Turunan atau pewarisan
class ManusiaHidup:
    jumtangan = 2  # class atribut

    def __init__(self, nama, alamat):  # construktor
        self.name = nama  # nama ,adress objeck atribut
        self.adress = alamat
        self.jummata = "2"

    def hello(self):
        return "Heloo {}, selamat siang"  .format(self.name)

    def __str__(self):
        return 'nama {} alamat {} jumplah mata {} dengan tangan {}'.format(self.name, self.adress, self.jumtangan, self.jumtangan)


class Hidup:
    def hello(self):
        return "Selamat siang {} bagaimana kabarnya?".format(self.name)


class Pegawai(Hidup, ManusiaHidup):  # class turunan dari class manusia hidup
    pass  # class mencangkup semua yang dimiliki class pegawai karena merupakan turunan



ai = Pegawai("Shiro", "tulungagung")
print(ai)
print(ai.hello())