import shelve
class Persistencia(object):

    def guardar(self, ruta , tablero_celular, clave):
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
            print("------" + "tablero cargado con exito" + "-------" )
            return tablero_celular
        else:
            print("-------" + "no existe tablero guardado en la clave" + " " + str(clave) + "--------")