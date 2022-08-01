# Inheritance pewarisan
class karyawan:
    def __init__(self, nama, email):  # atribut
        self.nama = nama
        self.email = email

    def kerja(self):  # Metode
        return f"{self.nama} sedang kerja"


class progames(karyawan):  # pewarisan dari kelas di atas
    def __init__(self, nama, email, lvl):  # atribut
        # super memanggil class yg diatasnya atau yg menjadi induk
        super().__init__(nama, email)
        self.lvl = lvl

    def main(self):
        return "main dota 10"
    
    def kerja(self): # melakukan penimpaan
        return f"{self.nama} sedang main game!!!"

class data(karyawan):
    def __init__(self, nama, email,lvl,kampus):
        super().__init__(nama,email)
        self.lvl = lvl
        self.kampus = kampus
        
    def kerja(self)    :
        return f"{self.nama} belajar di kampus ITP"
    
print("===============================================")

mochi = karyawan("mochi", "mochi@gmail.com")
print(mochi.kerja())
black = progames("si black", "Black@gmaial.com", "max pro")
print(black.kerja())
print(black.main())

biru = data("biruu","@biruu.com","100max","ITP")
print(biru.kerja())