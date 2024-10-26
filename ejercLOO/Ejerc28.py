""" FizzBuzz: Imprimir por pantalla los números del 1 al 100 pero considerando lo siguiente: 
a) Si el número es divisible por 3 se debe imprimir Fizz. 
b) Si el número es divisible por 5 se debe imprimir Buzz. c)
Si el número es divisible por 3 y por 5 se debe imprimir FizzBuzz 
"""

FizzBuzz = []

#llenamos el arreglo con numeros del 1 al 100

def llenarArreglo(a):
    for i in range(1, 101):
        FizzBuzz.append(i) #le agregamos i en cada iteracion
    
llenarArreglo(FizzBuzz)

#probamos que se haya llenado correctamente
print(FizzBuzz)

def imprimirFizzBuzz(a):

    for i in range(0, len(a)):

        if a[i] % 3 == 0 and a[i] % 5 == 0 :
            print(f"{a[i]} : FizzBuzz")

        elif a[i] % 3 == 0 :
            print(f"{a[i]} : Fizz")

        elif a[i] % 5 == 0 :
            print(f"{a[i]} : Buzz")


#llamamos a la funcion
imprimirFizzBuzz(FizzBuzz)