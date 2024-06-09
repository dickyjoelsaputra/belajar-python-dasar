
data_dict = {
    "cup":"gelas",
    "otong":"otong",
    "mario":"bros",
}

lenDict = len(data_dict)
print(lenDict) # 3


KEY = "cup"
ada = KEY in data_dict
print(ada) # True

print(data_dict[KEY]) # gelas
print(data_dict.get(KEY)) # gelas


data_dict["ok"] = "ok"
data = data_dict.get("ok" , "no")
print(data) # gelas
print(data_dict)

data_dict.update({"ok":"mantul"})
print(data_dict)

data_dict.update({"faq":"swag"})
print(data_dict)

del data_dict["faq"]
print(data_dict)