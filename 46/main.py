def kuadrat(x):
    return x ** 2

y = kuadrat(5)
print(y)

def operasi_matematika(x , y):
    tambah = x + y
    kurang = x - y
    kali = x * y
    bagi = x / y
    return tambah, kurang, kali, bagi

tambah, kurang , kali , bagi = operasi_matematika(10, 5)
print(f"Opearsi Tambah: {tambah}")
print(f"Opearsi Kurang: {kurang}")
print(f"Opearsi Kali: {kali}")
print(f"Opearsi Bagi: {int(bagi)}")