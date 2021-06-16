from ahorcado import Ahorcado
from palabras import palabras

def main():
    player_name = input("Por favor ingresa tu nombre: ")
    print(f'Hola {player_name}! Bienvenido al juego del Ahorcado 014')
    lives = selectDifficulty()
    newGame = Ahorcado(lives)
    seguir = seguirJugando()
    while seguir.upper() == 'S':
        #falta preguntar si gano o no
        if newGame.vidas>0:
            newGame.dibujar()
            newGame.jugar(input('Escriba una letra: \n').upper())
        else:
            seguir = input('Desea iniciar un nuevo juego? (S/N): \n')
            if seguir.upper() == 'S':
                lives = selectDifficulty()
                newGame = Ahorcado(lives)
            else: return

def selectDifficulty ():
    lives = 99
    difficulty = input('Ingrese dificultad, sin tilde (Facil, Normal o Dificil) : ')
    while difficulty.lower() not in ('facil', 'normal', 'dificil'):
        print('ERROR. Por favor elija una dificultad predeterminada')
        difficulty = input('Ingrese dificultad, sin tilde (Facil, Normal o Dificil) : ')
    if difficulty.lower() == 'facil':
        lives = 10
    elif difficulty.lower() == 'normal':
        lives = 6
    elif difficulty.lower() == 'dificil':
        lives = 3
    return lives

def seguirJugando ():
    seguir = input('Desea iniciar un nuevo juego? (S/N): \n')
    while seguir.lower() not in ('s','n'):
        print('ERROR. Por favor elija una opcion valida')
        seguir = input('Desea iniciar un nuevo juego? (S/N): \n')
    return seguir

main()