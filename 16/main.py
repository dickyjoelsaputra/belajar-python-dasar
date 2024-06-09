nama_pertama = "Budi"
nama_tengah = "Raharjo"
nama_akhir = "Santosoz"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

len_nama = len(nama_lengkap)
print(len_nama)

len_nama_pertama = len(nama_pertama)
print(len_nama_pertama)

s = "b"
status = s in nama_lengkap
print(status)


print("wk"*19)


print(nama_lengkap[3])
print(nama_lengkap[-1])

print(nama_lengkap[0:6])
print(nama_lengkap[5:9])

print(nama_lengkap[0:9:2])

# paling kecil
print(min(nama_lengkap))

# paling besar
print(max(nama_lengkap))


ascii_code = ord("a")
print(ascii_code)


data = 97
print(chr(data))


print(nama_lengkap.upper())
print(nama_lengkap.count("z"))