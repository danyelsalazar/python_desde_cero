"""Se ingresa un valor numérico por consola, determinar e informar si se trata de un número primo o no."""

a = int(input("Ingresa un numero\n"))

esPrimo = True
i = 2

if a <= 1:
    esPrimo = False
else:
    while (i < 1 and a % i != 0):
        i+=1
    esPrimo = (a == 1)
print(i)

if esPrimo:
    print("Es primo")
else:
    print("No es primo")