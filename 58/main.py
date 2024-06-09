import datetime
from collections import Counter
import io

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.day}")
print(f"hari : {data_waktu.strftime('%A')}")

data = ["a", "b", "c", "a", "b", "a"]

data_counter = Counter(data)
print(data_counter)
print(data_counter["a"])

file = io.open("data.txt", "r")
print(file.read())