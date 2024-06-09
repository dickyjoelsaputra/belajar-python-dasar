nama_global = "otong"

def fungsi():
    print(f"fungsi menampulkan nama_global {nama_global}")
    
fungsi()

for i in range(0,10):
    print(f"loop {i} = {nama_global}")
    
    
if True:
    print(f"if menampilkan {nama_global}")
    
def fungsi2():
    nama_local = "ucup"
    
    
# merubah global

angka = 0
name = "Ucup"
def ubah(nilai_baru,nama_baru):
    global angka
    global name
    angka = nilai_baru
    name = nama_baru
    
ubah(100,"Otong")
print(angka)
print(name)