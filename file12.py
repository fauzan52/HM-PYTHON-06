class ManusiaHidup():
    jumtangan = 2 #class atribut
    
    def __init__(self,nama, alamat): #construktor
        self.name = nama  #nama ,adress objeck atribut
        self.adress = alamat
        self.jummata = "2"
        
    def hello (self):
        return "Heloo {}, selamat siang"  .format(self.name)  
    def __str__(self):
        return 'nama {} alamat {} jumplah mata {} dengan tangan {}'.format(self.name,self.adress,self.jumtangan,self.jumtangan)
        
        
aku = ManusiaHidup("biruu","tulungagung")      
print(aku.name)  
print(aku.adress)
print(aku.jummata)
print(aku.jumtangan)
print(aku)
print(aku.hello())