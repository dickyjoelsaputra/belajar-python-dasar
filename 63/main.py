
print(f"nilai __name__ pada main.py : {__name__}")

import fungsi


def fungsi_tambah(a,b)->int:
    return a+b
if __name__ == "__main__":
    print(f"Hasil : {fungsi_tambah(3,4)}")