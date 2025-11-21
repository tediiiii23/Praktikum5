# Adalah pasangan key-value nya, yang indeksnya bisa dirubah dari numerik menjadi tipe data lainnya
# contoh 
dict = {'Name' : ['Tedi', 'mhe'],
		'Age' : 25,
		'Class' : ['TI.25.A.2']
		}
print("dict[\"Name\"] : ", dict['Name'])
# ouput: dict["Name"] : Tedi

# Mengakses nilai pada dictionary
# name = dict['Name']
# print(name)
# output : Tedi
# class = dict.get("Class")
# print(class)
# output : TI.25.A.2

# Menghapus element dictionary
# del dict['Name']
# print(dict)
# output : {'Age': 25, 'Class': 'TI.25.A.2'}
# dict.clear()
# print(dict)
# output : {}

# Menambahkan 
dict.update({"Country": "Indonesian"}) # menambahkan key-value terbaru
print(dict)
