"""Se ingresa por consola un número entero que representa un sueldo que se debe pagar.
Considerando que existen billetes de las denominaciones que se indican más abajo; informar,
que cantidad de billetes de cada denominación se deberá utilizar, dando prioridad a
los de valor nominal más alto.
Denominaciones ($) = {100, 50, 20, 10, 5, 2, 1} """

Denominaciones = [100, 50, 20, 10, 5, 2, 1]
cantidadesUsar = [0, 0, 0, 0, 0, 0, 0]

sueldo = int(input("Ingresa un sueldo: \n"))
print(sueldo)
suma = 0
i = 0

while sueldo != suma:
    if suma + Denominaciones[i] > sueldo:
        i += 1
    else:
        suma += Denominaciones[i]
        cantidadesUsar[i] += 1

print(cantidadesUsar)