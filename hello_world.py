# 1. TAREA: imprimir "Hola mundo"
print('Hola mundo')

# 2. imprimir "Hola Diego!" con el nombre en una variable
name = "Diego"
print('Hola', name)  # con una coma
print('Hola ' + name)  # con un +

# 3. imprimir "Hola 26!" con un numero en una variable
num = 26
print('Hola', num)  # con una coma
print('Hola ' + str(num))  # con un + - !Este debería darnos un error!

# 4. imprimir "Me encanta comer asaito y pizza." con los alimentos en variables
fave_food1 = "asaito"
fave_food2 = "pizza"
print('Me encanta comer {} y {}'.format(
    fave_food1, fave_food2))  # con .format()
print(f'Me encanta comer {fave_food1} y {fave_food2}')  # con una cadena f

curso = 'bloques'
codigo = 14
print(f'El nombre del curso es {curso} y su codigo es {codigo}')
print('El nombre del curso es ' + curso + 'y su codigo es ' + str(codigo))
