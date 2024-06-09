salam = "BRI!"
print("normal: ", salam)
salam = salam.upper()
print("upper: ", salam)
salam = salam.lower()
print("lower: ", salam)

test = "ss"

apakah_lower = test.islower()
print("apakah lower: ", apakah_lower)

apakah_upper = test.isupper()
print("apakah upper: ", apakah_upper)


judul = "It Is Ok Pythonvc 4 "
cek_judul = judul.istitle()
print("apakah title: ", cek_judul)

judul = "WOI"
is_alpha = judul.isalpha()
print("is alpha: ", is_alpha)

is_num = judul.isalnum()
print("is num: ", is_num)


cek_start = "Sangjangnim Oppa"
print("start with: ", cek_start.startswith("Sangjangnim"))

print("end with: ", cek_start.endswith("Oppa"))

pisah = ['aku', 'kamu', 'dia']
gabung = " ".join(pisah)
print("join: ", gabung)


gabungan = "akuehemkamu"
print("split: ", gabungan.split("ehem"))


kanan = "kanan".rjust(10)
print("rjust: ", kanan)

kiri = "kiri".ljust(10)
print("ljust: ", kiri)

tengah = "tengah".center(10 , "s")
print("center: ", tengah)

# test = "a ds ds ds ds da ds a"
print("strip: ", tengah.strip("s"))