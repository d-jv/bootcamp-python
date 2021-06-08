#1) Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#     Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def biggieSize(l1st):
    newList = []
    for item in l1st:
        if item > 0:
            newList.append("big")
        else: newList.append(item)
    return newList
print(biggieSize([- 1, 3, 5, -5]))

#2) Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#     Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#     Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def countPositives(l1st):
    counter = 0
    for item in l1st:
        if item > 0:
            counter += 1
    l1st[-1]=counter
    return l1st
print(countPositives([- 1,1,1,1]))
print(countPositives([1,6, -4, -2, -7, -2]))


#3) Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#     Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#     Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sumTotal (l1st):
    sum = 0
    for item in l1st:
        sum += item
    return sum
print(sumTotal([1,2,3,4]))
print(sumTotal([6,3, -2]))

def sumTotal2 (l1st):
    suma = sum(l1st)
    return suma
print(sumTotal([1,2,3,4]))
print(sumTotal([6,3, -2]))


#4) Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#     Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def getAvg(l1st):
    sum = 0
    for item in l1st:
        sum += item
    avg = sum / len(l1st)
    return avg
print(getAvg([1,2,3,4]))


#5) Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#     Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#     Ejemplo: longitud ([]) debería devolver 0
def length(l1st):
    return len(l1st)

print(length([37,2,1, -9]))
print(length([]))


#6) Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#     Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#     Ejemplo: mínimo ([]) debería devolver False
def getMin(l1st):
    min = 999999
    if l1st == []:
        return False
    else:
        for item in l1st:
            if item <= min:
                min = item
    return min
print(getMin([37,2,1, -9]))
print (getMin([]))

def getMin2(l1st):
    if l1st == []: return False
    else: return min(l1st)
print(getMin2([37,2,1, -9]))
print (getMin2([]))


#7) Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#     Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#     Ejemplo: máximo ([]) debería devolver False
def getMax(l1st):
    if l1st == []: return False
    else: return max(l1st)
print (getMax([37,2,1, -9]))
print (getMax([]))


#8) Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#     Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}
def ultimateAnalysis (l1st):
    average = sum(l1st)/len(l1st)
    return {
        'total': sum(l1st),
        'promedio': average,
        'minimo': min(l1st),
        'maximo': max(l1st),
        'longitud': len(l1st)
    }
print(ultimateAnalysis([37,2,1, -9]))


#9) Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#     Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reverseList (l1st):
    l1st.reverse()
    return l1st
print(reverseList([37,2,1, -9]))