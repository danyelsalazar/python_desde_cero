"""Escribir una función que reciba dos arreglos a1 y a2, de enteros ordenados de
menor a mayor e intercale los elementos de los arreglos que recibe en un nuevo arreglo,
tal que el arreglo resultante también esté ordenado. Por ejemplo:

a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]
resultado = [-10, -5, 0, 0, 0, 1, 5, 7]"""

a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]

def intercalar(a1,a2):
    aux = a1[0]
    a3 = []
    i = 0
    j = 0

    while(i < len(a1) and j < len(a2)):
        if(a1[i] < a2[j]):
            a3.append(a1[i])
            i += 1
        else:
            a3.append(a2[j])
            j += 1

    if i == len(a1):
        for k in range(j,len(a2)):
            a3.append(a2[k])
    else:
        for l in range(i, len(a1)):
            a3.append(a1[l]) 


    return a3

print(intercalar(a1,a2))

            
