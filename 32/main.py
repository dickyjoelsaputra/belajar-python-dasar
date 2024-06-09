a = ["Ucup" , "Budi" , "Ahmad" , "Joko" , "Rudi"]
print(f"List a: {a}")

b = a
print(f"List b: {b}")

a[0] = "Nanda"
b.sort()
print(f"List a: {a}")
print(f"List b: {b}")

# menduplikat data
c = a.copy()
c[0] = "WOW"
print(f"List c: {c}")