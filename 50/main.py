
# def fungsi(data_list):
#     data = data_list.copy()
#     nama = data[0]
#     tinggi = data[1]
#     berat = data[2]
#     print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")
    
# fungsi(["Andi",170,70])

# def fungsi(*args):
#     nama = args[0]
#     tinggi = args[1]
#     berat = args[2]
#     print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")

def fungsi(nama,tinggi,berat):
    print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")
    
fungsi("Andi",170,70)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")
    
fungsi(["Otong",120,70])
    
# fungsi("dudung",120,20)

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"Nama: {nama} pada tinggi {tinggi} dan berat {berat}")
    
fungsi("dudung",120,20)


def tambah(*data):
    output = 0
    for i in data:
        output += i
        
    return output
    
hasil = tambah(1,2,3,4,5)
print(f"Hasil penjumlahan: {hasil}")