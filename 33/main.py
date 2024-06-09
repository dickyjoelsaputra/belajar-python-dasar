data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"Data list biasa : {data_list_biasa}")

list_2D = [data_0, data_1]

print(f"Data list 2D : {list_2D}")

print(f"Data list dicampur : ")


peserta_0 = ["ucup", 25 , "laki-laki"]
peserta_1 = ["otong", 26 , "laki-laki"]
peserta_2 = ["mario", 27 , "perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"Data peserta : {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Jenis Kelamin\t: {peserta[2]}")
    print("")


list_copy = list_peserta.copy()
print(f"Data list copy : {list_copy} \n")
peserta_0[0] = "budi"
print(f"Data list peserta : {list_peserta}")
print(f"Data list copy : {list_copy}")