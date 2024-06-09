def fungsi(nama , tinggi , berat):
    print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")
    
fungsi("Andi",170,70)

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    
    print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")
    
fungsi(nama="Andi",tinggi=170,berat=70)

def math(*args , **kwargs):
    hasil = 0
    if  kwargs['option'] == "tambah":
        for i in args:
            hasil += i
    elif kwargs['option'] == "kali":
        output = 1
        for i in args:
            output *= i
        hasil = output
    return hasil
    
    
hasil = math(1,2,3,option="tambah")
print(f"Hasil penjumlahan: {hasil}")
hasil = math(1,2,4,option="kali")
print(f"Hasil penjumlahan: {hasil}")