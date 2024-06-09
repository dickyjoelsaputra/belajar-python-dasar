def kuadrat(angka):
    return angka ** 2

print(f"hasil fungsi kuadrat = {kuadrat(3)}")

kuadrat = lambda angka: angka ** 2
kurang = lambda angka1,angka2: angka1 - angka2
print(f"hasil fungsi kuadrat = {kuadrat(3)}")
print(f"hasil fungsi kurang = {kurang(3,2)}")


data_list = ["Ootong", "Ucup" , "Dudung","zaka"]
data_list.sort()
print(f"Data list: {data_list}")

data_list.sort(key=lambda x: len(x))
print(f"Data list with lambda: {data_list}")


data_angka = [12,213,123,12,312,312,31,23,25,15,12,5,1,61]
data_angka_baru = list(filter(lambda x: x > 100, data_angka))
print(f"Data angka baru: {data_angka_baru}")


# Anon Function
def pangkat(n):
    return lambda angka: angka ** n

data_hasil = pangkat(3)
print(f"Hasil pangkat: {data_hasil(10)}")
print(f"Hasil pangkat: {pangkat(3)(3)}")