from palabras import palabras
import random

class Ahorcado:
    def __init__(self, vidas=5) -> None:
        self.vidas = vidas
        palabra = palabras[random.randint(0, len(palabras))]
        estado = []
        for letra in palabra:
            estado.append({
                'letra': letra,
                'lista': False
            })
        self.palabra = palabra
        self.estado = estado
        self.letras_dichas = []
    
    def jugar(self, letra):
        # compruebo que letra no ha sido dicha
        if letra in self.letras_dichas:
            print('Ya dijo esta letra')
            return

        # actualizo el estado
        for elem in self.estado:
            if elem['letra'] == letra:
                elem['lista'] = True
        self.letras_dichas.append(letra)

        # compruebo si gané o no
        letras_ganadoras = [elem for elem in self.estado if elem['lista'] == True]
        if len(letras_ganadoras) == len(self.palabra):
            print(f'Felicidades por ganar!! Le achuntaste a la palabra: {self.palabra}')
            self.vidas = 0
        
        # comprobar si perdí
        if letra not in self.palabra:
            self.vidas -= 1
        if self.vidas == 0:
            print(f'Felicidades por perder!!!! La palabra era: {self.palabra}')
        
    def dibujar(self):
        palabra_mostrar = ''
        for elem in self.estado:
            if elem['lista'] == True:
                palabra_mostrar += elem['letra'] + ' '
            else:
                palabra_mostrar += '* '


        lines = [
            f"=== AHORCADO ===",
            f"______    Vidas: {self.vidas}",
            f"|    |    Letras Dichas: {'-'.join(self.letras_dichas)}",
            f"|    O",
            f"|   /|\\",
            f"|   / \\",
            f"|          {palabra_mostrar}"
        ]
        for line in lines:
            print(line)