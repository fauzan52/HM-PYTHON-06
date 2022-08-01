# metode
#private atribut
class mhs:
    jum = 0 #class atribut

    def __init__(self, nama, nim, semester, status): #objek atribut
        self.nama = nama
        self.nim = nim
        self.semester = semester
        self.__status = status  # private variabel || atribut || tidak bisa diakases diluar class
        mhs.jum += 1

    def data(self):  # print data atau objek
        return f"{self.nama} = {self.nim} = {self.semester} ,{self.__status}"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):  # update status #parameter
        if self.__status != "lulus":  # kondisi
            self.__status = new_status

    @classmethod #dekorator
    def setjum(cls, jum): #cls mengacu pada mhs
        mhs.jum = jum          #self mengacu instace dari kelas || mhs bisa di ubah cls
        
    @classmethod
    def from_string(cls, string_param):    
        nama,nim,semester,status = string_param.split("-")
        return mhs(nama,nim,semester,status)

biru = mhs("biruu", "2019610077", "8", "lulust")
hendra = mhs("hendra", "2019610004", "7", "lulus")
black = mhs("black", "2019610099", "7", "belum lulus")

string_param = ("raden-2019610077-5-belum lulus")
raden = mhs.from_string(string_param)
print(raden.data())

print(mhs.jum)
mhs.setjum(10)
print(mhs.jum)