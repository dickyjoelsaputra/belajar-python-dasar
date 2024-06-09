file = open("64/data.txt", "r")
print(file.read())

print(f"status read file: {file.readable()}")
print(f"status write file: {file.writable()}")


with open("64/data.txt", "r") as file:
    content = file.readline()
    print(content)