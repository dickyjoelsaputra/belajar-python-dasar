# program list buku

list_buku = []

while True:
    judul = input("Masukkan judul buku\t: ")
    penulis = input("Masukkan penulis buku\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    for i , buku in enumerate(list_buku) :
        print(f"No.{i+1} Judul: {buku[0]}, Penulis: {buku[1]}")