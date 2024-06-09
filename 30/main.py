data = ["otong", "surotong", "udin"]

data_0 = data[0]
print(f"data pertama index 0 = {data_0}") # otong

data_terakhir = data[-1]
print(f"data terakhir index -1 = {data_terakhir}") # udin

data.insert(1, "mamat")
print(data) # ['otong', 'mamat', 'surotong', 'udin']


data.append("siti")
print(data) # ['otong', 'mamat', 'surotong', 'udin', 'siti']

data_baru = ["joko", "budi"]
data.extend(data_baru)
print(data) # ['otong', 'mamat', 'surotong', 'udin', 'siti', 'joko', 'budi']

data[2] = "michael"
print(data) # ['otong', 'mamat', 'michael', 'udin', 'siti', 'joko', 'budi']

data.remove("mamat")
print(data) # ['otong', 'michael', 'udin', 'siti', 'joko', 'budi']

data.pop()
print(data) # ['otong', 'michael', 'udin', 'siti', 'joko']