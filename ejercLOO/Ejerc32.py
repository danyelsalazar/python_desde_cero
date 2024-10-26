"""
32: Implementar una función que reciba como parámetro un arreglo de enteros y muestre por pantalla 
cuántas veces se repite cada uno. 
El arreglo no está ordenado. Se garantiza que los valores del arreglo estan comprendidos entre 0 y 100"""

def frecuencias(a):
    f = []
    """llenamos el arreglo con 0"""
    for i in range(101):
        f.append(0)
    """le agregamos el numero de posicion a cada posicion"""
    for valor in a:
        f[valor] += 1
    
    for i in range(len(f)):
        if(f[i] != 0):
            print(i, f[i])


def swap(a,b):
    c = a
    a = b
    b = c


a = [23, 23, 0,1,1,1,1,45,7,7,8,1,1,89,9]

b = [1, 34, 56, 67, 77]

frecuencias(a)


#aqui como vemos no hizo el intercambio entre a y b ya quye toma los valores en la funcion por copia y no por referencia
swap(a,b)
print(f"Arreglo a : {a}")
print(f"Arreglo b : {b}")

#para cambiar estos valores debemos hacerlo afuera en el scope donde se encuetran dichas variables

c = a
a = b
b = c
#probamos ahora y vemos que ahora si se intercambiaron los valores:
print(f"Arreglo a : {a}")
print(f"Arreglo b : {b}")