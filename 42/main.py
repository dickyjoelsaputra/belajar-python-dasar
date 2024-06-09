import datetime

mahasiswa = {
    'nama':"Ucup Surucup",
    'nim': '12312312312',  
    'sku_lulus' : 130,
    'beasiswa': False,
    'lahir': datetime.datetime(1999, 5, 22),
}

mahasiswa2 = {
    'nama':"Jarwo",
    'nim': '123321321',  
    'sku_lulus' : 120,
    'beasiswa': False,
    'lahir': datetime.datetime(2022, 1, 15),
}

mahasiswa3 = {
    'nama':"Sopo",
    'nim': '123321321',  
    'sku_lulus' : 120,
    'beasiswa': False,
    'lahir': datetime.datetime(2022, 1, 15),
}

data_mahasiswa = {
    'MAH001': mahasiswa,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

for mahasiswa in data_mahasiswa:
    print(f"Nama: {data_mahasiswa[mahasiswa]['nama']}")
    print(f"NIM: {data_mahasiswa[mahasiswa]['nim']}")
    print(f"SKU Lulus: {data_mahasiswa[mahasiswa]['sku_lulus']}")
    print(f"Beasiswa: {data_mahasiswa[mahasiswa]['beasiswa']}")
    print(f"Tanggal Lahir: {data_mahasiswa[mahasiswa]['lahir'].strftime('%d %B %Y')}")
    print("")