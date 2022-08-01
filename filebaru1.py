class Kendaraan :
    def __init__ (self, kecepatan, jarak) :
        self.max_speed = kecepatan
        self.mileage = jarak
        
        def KecepatanMax (self) :
            return 'Kecepatan maksimal = {}'.format(self.max_speed)
        def JarakMax (self) :
            return 'Jarak tempuh = {}'.format(self.mileage)
        
class Bus(Kendaraan) :
    safety_level = "Level IV"        
    def __init__ (self, merk, kecepatan, jarak):
        self.merk = merk
        super().__init__(kecepatan, jarak)
        
    def __str__(self):
        return 'Merk kendaraan = {}, Kecapatan maksimal = {}, Jarak tempuh = {}, Safety Level = {}'.format(self.merk, self.max_speed, self.mileage, self.safety_level)
        # return super().__str__() 
        
        
kendaraanprint = Bus('Volvo', 100, 12)
print (kendaraanprint)
