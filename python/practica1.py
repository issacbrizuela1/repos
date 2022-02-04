from re import L


lista1=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lista1)
print(lista1[0])
print(lista1[-3])
print(lista1[:3])
lista1[0]=1
lista1[2:4] = ["blackcurrant", "watermelon"]
print(lista1)
print(len(lista1))
lista1.insert(8,"insertado")
print(lista1)
lista1.append("otra insercion")
print(lista1)
lista2=["elemento de otra lista1","elemento de otra lista2","elemento de otra lista3"]
lista1.extend(lista2)
print(lista1)
lista1.remove("elemento de otra lista2")
print(lista1)