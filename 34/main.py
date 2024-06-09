data_0 = [0,1,2,3]
data_1 = [4,2,2,5]

data2D = [data_0,data_1]
data2D_copy = data2D

print(f"data = {data2D}")
print(f"data_copy = {data2D_copy}")

data = data2D[0]
print(f"data = {data}")

from copy import deepcopy
data2D_copy = deepcopy(data2D)
data2D_copy[0][0] = 999
print(f"data = {data2D}")
print(f"data_copy = {data2D_copy}")