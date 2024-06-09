# looping dari list

# for loop
kumpulan_angka = [4,5,6,7,8,9,10]
for i in kumpulan_angka:
    print(f"angka : {i}")


peserta = ["diding", "ucup", "otong", "mario"]
for nama in peserta:
    print(f"Nama peserta : {nama}")


# for loop dengan range
for i in range(10):
    print(f"Angka : {i}")

# while
    print(f"\nWhile Loop\n")

panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"Angka : {kumpulan_angka[i]}")
    i += 1



print(f"\nList Comprehension\n")

data = ["ucup",25 , 2.5 , True , "yes"]
[print(f"Data : {d}") for d in data]

# enumirate
print(f"\nEnmumirate\n")
for i , v in enumerate(data):
    print(f"Index : {i} , Value : {v}")