#private atribut
class mhs:
    jum = 0

    def __init__(self, nama, nim, semester, status):
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

    def getstatus(self):  # pemangginal status
        return self.__status


biru = mhs("biruu", 2019610077, 8, "lulust")
print(biru.status)
print(biru.nama)
print(biru.__dict__)
biru.status = "hahahahahhah"
print(biru.data())