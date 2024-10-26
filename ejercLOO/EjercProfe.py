"""Implementar una funcion que reciba dos arreglos enteros y devuelva otro areglo resultado 
de `poner uno a  continuacion del otro"""

#Forma 1 ---------------------------------------------------------
print("-------Forma 1-------------")

a = [1, 4, 9, 32]
b = [2, 56, 7, 7]

def unir(a,b):
    c = a + b
    return c

print(unir(a,b)) #muestro el arreglo directo por consola

#Forma 2-----------------------------------------------------------
print("-------Forma 2-------------")

def unir(a,b):
    return  a + b

d = unir(a,b)
#print(d) probamos

for e in d:    #recorro el nuevo arreglo y muestro sus elementos:
    print(e)
