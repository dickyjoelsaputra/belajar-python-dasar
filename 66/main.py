# while True :
#     angka = int(input("Masukkan angka: "))
#     try:
#         hasil = 10 / angka
#         print(f"hasil = {hasil}")
#         is_done = input("Lanjutkan? (y/n) ")
#         if is_done == "n":
#             break
#     except:
#         print("Terjadi kesalahan")
#         is_done = input("Lanjutkan? (y/n) ")
#         if is_done == "n":
#             break
        
# print("Program selesai")

# import numbers

# def tambah(a , b):
#     if not isinstance(a , numbers.Number) or not isinstance(b , numbers.Number):
#         raise "input harus angka"
    
#     return a+b

# print(tambah("a",2))


angka = 0

try:
    hasil = 10 / angka
except Exception as err:
    print(err)