teman_teman = {
    "nama": "Budi",
    "umur": 20,
    "alamat": "Jakarta"
}


friends = teman_teman.copy()

print(f"teman_teman = {teman_teman}")
print(f"friends = {friends}")


friends["nama"] = "Andi"
print("=================")

print(f"teman_teman = {teman_teman}")
print(f"friends = {friends}")


# POP DICTIONARY
dataNama = friends.pop("nama")
print(f"data asep = ", dataNama)
print(f"teman_teman = {friends}")

# POP ITEM
dataNama = friends.popitem()
print(f"popitem = ", dataNama)
print(f"data terakhir = {friends}")