class kucing : #class
    def __init__(self):  # untuk melakukan pengubahan sebuah fungsi maka diperlukan fungsi
        print("membuat objek baru")
    
   # pass # gantikan dengan pernyataan-pernyataan, misal: atribut atau metode
    def __init__(self,name):  
        self.name = name # name dibelakang sebagai parameter seperti di atas
        #self.name merupakan atribut dari user
        
cat1 = kucing("black") #objek || mencetak objek baru sebanyak objek
cat2 = kucing('mochi')

#cat1.name = "Black" # atribut
#cat2.name = "Mochi"

print(cat1.name)
print(cat2.name)