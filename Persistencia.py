import shelve


class Persistencia(object):
    def __init__(self):
        pass

    def guardar(self, ruta, tablero_celular, clave):
        modulo_guardado = shelve.open(ruta)
        if not clave in modulo_guardado:
            modulo_guardado[clave] = tablero_celular
            print("-------" + "tablero guardado con exito" + "--------")
            modulo_guardado.close()
        else:
            modulo_guardado[clave] = tablero_celular
            print("-------" + "tablero sobreescrito con exito" + "--------")
            modulo_guardado.close()

    def cargar(self, ruta, clave):
        tablero_celular = None
        modulo_a_cargar = shelve.open(ruta)

        if modulo_a_cargar[clave] != None:
            tablero_celular = modulo_a_cargar[clave]
            print("------" + "tablero cargado con exito" + "-------")
            return tablero_celular

    def guardar_vida_estatica_tupla(self,ruta,tupla , tablero, clave):
        modulo_guardado = shelve.open(ruta)
        if not clave in modulo_guardado:
            modulo_guardado[clave] = [tupla,tablero]
            print("-------" + "Posicion actual guardada con exito" + "--------")
            modulo_guardado.close()
        else:
            modulo_guardado[clave] = [tupla,tablero]
            print("-------" + "Posicion sobreescrita con exito" + "--------")
            modulo_guardado.close()

    def cargar_vida_estatica(self, ruta, clave):
        tablero_celular = None
        modulo_a_cargar = shelve.open(ruta)

        if modulo_a_cargar[clave] != None:
            lista_posicion_tablero = modulo_a_cargar[clave]
            print("------" + "tablero de vida estatica cargado con exito" + "-------")
            return lista_posicion_tablero

    def cargar(self, ruta, clave):
        tablero_celular = None
        modulo_a_cargar = shelve.open(ruta)

        if modulo_a_cargar[clave] != None:
            tablero_celular = modulo_a_cargar[clave]
            print("------" + "tablero cargado con exito" + "-------")
            return tablero_celular