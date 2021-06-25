class Nodo:

    def __init__(self, nombre, description, sgte=None):
        self.nombre = nombre
        self.description = description
        self.sgte = sgte

class Lista:

    def __init__(self):
        self.primero = None

    def add_nodo(self, nombre, description):
        # si la lista está vacía
        if self.primero is None:
            self.primero = Nodo(nombre, description)
            return

        #si la lista ya tiene al menos un nodo
        ultimo_nodo = self.primero
        while ultimo_nodo.sgte is not None:
            ultimo_nodo = ultimo_nodo.sgte
        ultimo_nodo.sgte = Nodo(nombre, description)

    def largo(self):
        if self.primero is None:
            return 0
        else:
            counter = 1
            ultimo_nodo = self.primero
            while ultimo_nodo.sgte is not None:
                counter += 1
                ultimo_nodo = ultimo_nodo.sgte
            return counter


    def buscar(self, nombre):
        if self.primero is None:
            return None
        else: # ahora empezamos a buscar
            nodo_actual  = self.primero
            if nodo_actual.nombre == nombre:
                return nodo_actual.description
            
            while nodo_actual.sgte is not None:
                nodo_actual = nodo_actual.sgte
                if nodo_actual.nombre == nombre:
                    return nodo_actual.description
            return None

# --- BONUS ----
# como agregar los nombres por orden alfabetico                     *** Falta esto, terminar el finde. ***
    # def ordenAlfab(self, nombre):
    #     if self.primero is None:
    #         return None
    #     else:
    #         nodo_actual = self.primero
    #         if  nodo_actual.nombre[0] < nodo_actual.sgte.nombre[0]:
    #             return


# Testing 
chile = Lista()
chile.add_nodo('Ben 10', 'delantero')
chile.add_nodo('Arturo Vidal', 'volante')
chile.add_nodo('Gary Medel', 'defensa')

print(chile.primero.sgte.nombre)
print(chile.primero.sgte.sgte.nombre)
print(chile.primero.description)

print(chile.largo())
print(chile.buscar('Ben 10'))