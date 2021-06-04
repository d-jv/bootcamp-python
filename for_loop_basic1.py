# Crea un archivo de Python llamado for_loop_basic1.py que realice las siguientes tareas.

#     1)Básico : imprime todos los enteros del 0 al 150.
for i in range(151):
    print (i)

#     2)Múltiplos de cinco : imprime todos los múltiplos de 5, del 5 al 1,000
for i in range(5,1001,5):
    print (i)

#     3)Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for i in range(0,151):
    if i%5 == 0:
        print ("Coding")
    if i%10 == 0:
        print ("Coding Dojo")

#     4)¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
sum = 0
for i in range(5000001):
    if i%2 != 0:
        sum = sum + i
print (sum)

#     5)Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for i in range(2018, -1, -4):
    print (i)

#     6)Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
def flexCounter(lowNum, highNum, mul):
    for i in range(lowNum, highNum+1):
        if i%3 == 0:
            print(i)
flexCounter(2,9,3)

# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000
def prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
print(primes1000 = [x for x in range(2, 1001) if prime(x) is True])

