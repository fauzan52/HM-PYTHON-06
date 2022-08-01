class Database:
    def __init__(self, nama, alamat, usia):
        self.nama = nama
        self.alamat = alamat
        self.usia = usia

class Pegawai(Database) :
    def __init__(self, nama, alamat, usia ,noid):
        self.noid = noid
        super().__init__(nama,alamat,usia)
        
    def __str__(self):
        return 'Data Pegawai : {}, {}, {}, {}'.format(self.nama, self.alamat, self.usia, self.usia, self.noid)

class Customer(Database):
        def __init__(self, nama, alamat, usia, belanjaan):
        self.belanjaan = belanjaan
        super().__init__(nama,alamat,usia)
        
    def __str__(self):
        return 'Data Customer : {}, {}, {}, {}'.format(self.nama, self.alamat, self.usia, self.usia, self.belanjaan)
        


    
fauzan = Pegawai ('Fauzan', 'Jakarta', 22, '00123123')
print (fauzan)