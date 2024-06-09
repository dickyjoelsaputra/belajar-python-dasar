import datetime
import os
import random
import string

mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    'sks_lulus':0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system('cls')

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print(f"{'-'*20}")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("Masukkan Nama Mahasiswa: ")
    mahasiswa['nim'] = input("Masukkan NIM Mahasiswa: ")
    mahasiswa['sku_lulus'] = int(input("Masukkan SKS Lulus Mahasiswa: "))
    TAHUN_LAHIR = int(input("Masukkan Tahun Lahir Mahasiswa (YYYY) : "))
    BULAN_LAHIR = int(input("Masukkan Bulan Lahir Mahasiswa (1-12) : "))
    TANGGAL_LAHIR = int(input("Masukkan Bulan Lahir Mahasiswa (1-31) : "))

    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    data_mahasiswa.update({'MAH'+str(len(data_mahasiswa)+1):mahasiswa})
    data_mahasiswa.update({KEY:mahasiswa})
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        # print(f"{'-'*20}")
        
        NAMA = data_mahasiswa[mahasiswa]['nama']
        NIM = data_mahasiswa[mahasiswa]['nim']
        SKU_LULUS = data_mahasiswa[mahasiswa]['sku_lulus']
        LAHIR = data_mahasiswa[mahasiswa]['lahir'].strftime('%d %B %Y')
        
        print(f"{KEY:<6} {NAMA:<6} {NIM:<6} {SKU_LULUS:<6} {LAHIR:<6}")
        
    print("\n")
    is_done = input("Tambah data mahasiswa lagi? (y/n) : ")
    if is_done.lower() == 'n':
        break 
        
print("Terima Kasih")