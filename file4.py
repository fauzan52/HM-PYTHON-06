#private atribut
class mhs:
    jum = 0

    def __init__(self, nama, nim, semester, status):
        self.nama = nama
        self.nim = nim
        self.semester = semester
        self.__status = status #private variabel || atribut || tidak bisa diakases diluar class
        mhs.jum += 1

    def data(self):  # print data atau objek
        return f"{self.nama} = {self.nim} = {self.semester} ,{self.__status}"

    def update_status(self, new_status):  # update status
        if self.__status != "lulus":  # kondisi
            self.__status = new_status
    
    
    def getstatus(self)    : # pemangginal status
        return self.__status    


biru = mhs("biruu", 2019610077, 8, "belum lulus")
biru._mhs__status = "sempurna"
print(biru.__dict__)
print(biru._mhs__status)
print(biru.getstatus())

#biru.update_status("lulus")
#print(biru.data())
'''
hendra = mhs("hendra", 2019610004, 7, "lulus")
hendra.status = "cumlaude"
print(hendra.data())

black = mhs("black", 2019610099, 7, "belum lulus")
black.update_status("lulus")
print(black.data())
'''