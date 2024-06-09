import datetime

# hari_ini = datetime.datetime.now()
hari_ini = datetime.date.today()
print(hari_ini)
print(f"Hari ini adalah hari {hari_ini:%A}")

# tanggal = datetime.date(2021, 12, 31)
# print(tanggal)


print("silahkan masukkan tanggal lahir anda")
tahun = int(input("tahun: "))
bulan = int(input("bulan: "))
hari = int(input("hari: "))

tanggal_lahir = datetime.date(tahun, bulan, hari)
print(f"tanggal lahir anda adalah {tanggal_lahir:%A, %d %B %Y}")
harinya = tanggal_lahir.strftime("%A")
print(f"hari lahir anda adalah hari {harinya}")

umur = (hari_ini - tanggal_lahir) // 365

print(f"umur anda adalah {umur.days:%A} tahun")