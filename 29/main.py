# LIST

data_angka = [1,2,3]
print(data_angka)

data_string = ['otong', 'surotong', 'udin']
print(data_string)

# campuran
data_campuran = [1, 'dua', 3, 'empat' , True]
print(data_campuran)

data_range = range(1,10)
print(data_range)

data_range = list(range(1,10,2))
print(data_range)

list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)


list_pake_for = [i for i in range(0,10) if i != 5 ]
print(list_pake_for)