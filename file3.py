class mhs :
    jum = 0
    
    def __init__(self, nama, nim,semester,status):
        self.nama = nama
        self.nim = nim
        self.semester = semester
        self.status = status
        mhs.jum += 1
        
    def data(self): #print data atau objek
        return f"{self.nama} = {self.nim} = {self.semester} ,{self.status}"
    
    
    def update_status(self, new_status): #update status
        if self.status != "lulus": # kondisi
            self.status = new_status
    
        
biru = mhs ("biruu",2019610077,8,"belum lulus")
biru.update_status("lulus")
print(biru.data())

hendra = mhs("hendra",2019610004,7,"lulus")   
hendra.status = "cumlaude" 
print(hendra.data())

black = mhs("black", 2019610099, 7, "belum lulus")
black.update_status("lulus")
print(black.data())
    