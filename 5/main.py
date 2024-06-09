# tipa data 

# integer

data_integer = 1
print("data : ", data_integer , ", type : ", type(data_integer))

# float

data_float = 1.5
print("data : ", data_float , ", type : ", type(data_float))

# string

data_string = "ucup"
print("data : ", data_string , ", type : ", type(data_string))

# boolean
data_bool = True
print("data : ", data_bool , ", type : ", type(data_bool))

# data kompleks
data_complex = complex(5,6)
print("data : ", data_complex , ", type : ", type(data_complex))

# tipe data dari c

from ctypes import c_double , c_char
data_c_double = c_double(10.5)
print("data : ", data_c_double , ", type : ", type(data_c_double))
# data_c_char = c_char('A')
# print("data : ", data_c_char , ", type : ", type(data_c_char))