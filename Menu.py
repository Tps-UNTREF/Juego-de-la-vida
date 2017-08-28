class Menu(object):

    def Menu(self):
        tamaño_de_tablero = self.leer_entero(self.leer_teclado('Ingrese el tamaño del tablero: '),'Ingrese el tamaño del tablero: ')

    def leer_teclado(self,texto):
        try:
            ingresado = eval(input(texto))
            if (ingresado == ''):
                return None
            else:
                return ingresado
        except (EOFError, KeyboardInterrupt):
            return None

    def leer_entero(self,entrada,texto):
        try:
            if type(entrada) == int:
                return entrada
            else:
                raise Exception
        except Exception:
            print('Por favor ingrese un numero entero')
            return self.leer_entero(self.leer_teclado(texto))

     #Prueba github1 mergeado
        
