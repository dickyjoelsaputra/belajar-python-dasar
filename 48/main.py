import os

# LEBAR = int(input("Masukkan lebar: "))
# PANJANG = int(input("Masukkan panjang: "))

# LUAS = LEBAR * PANJANG
# KELILING = 2 * (LEBAR + PANJANG)

# print(f"Luas: {LUAS}")
# print(f"Keliling: {KELILING}")

def header():
    os.system("cls")

    print(f"{'Progaram Menghitung Luas':^40}")
    
def inputUser():
    lebar = int(input("Masukkan lebar: "))
    panjang = int(input("Masukkan panjang: "))
    
    return lebar, panjang

def hitungLuas(lebar, panjang):
    luas = lebar * panjang
    return luas

def hitungKeliling(lebar, panjang):
    keliling = 2 * (lebar + panjang)
    return keliling

def displayResult(luas, keliling):
    print(f"Luas: {luas}")
    print(f"Keliling: {keliling}")

while True:
    header()
    
    lebar , panjang = inputUser()
    luas = hitungLuas(lebar, panjang)
    keliling = hitungKeliling(lebar, panjang)
    
    displayResult(luas, keliling)
    
    isCountinue = input("Apakah anda ingin menghitung lagi? (y/n): ")
    if isCountinue == "n":
        break
    
print("Terima kasih sudah menggunakan program ini")
