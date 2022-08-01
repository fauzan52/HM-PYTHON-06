class kucing:  # class 
    total = 0 #variabel === milik dari kucing
    #penggunaan misal menghitung user yang sudah adalah
    
    
    def __init__(self,name,warna,makan):  
        self.name = name # name dibelakang sebagai parameter seperti di atas
        #self.name merupakan atribut dari user
        self.warna = warna  # adalah variabel pada constructor, self. adalah variabel dari class
        self.makan = makan # variabel yg berlaku dari atribut || instanace variabel = hannya berlaku unt masing" instance  
                          # class variabel nilainya berlaku lingkup class
        kucing.total +=1
   

cat1 = kucing("black","hitam","wiskas")  # objek || mencetak objek baru sebanyak objek
print(kucing.total)
cat2 = kucing("uning", "kuning","wiskas")
print(kucing.total)
cat3 = kucing("putih", "putih hitam", "snak")
print(kucing.total)
#cat1.name = "Black" # atribut || instance
#cat2.name = "Mochi"

#print(cat1.name)
#print(cat1.warna)
#print(cat1.__dict__)


#print(cat2.__dict__)


#print(cat3.__dict__)