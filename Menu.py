class Menu(object):

    def menu(self):
        try:
            while True:
                numero1 = self.leer_entero(self.leer_teclado('Ingrese una acción: \n' '1- Nuevo juego \n' '2- Salir \n'),
                                      'Ingrese una acción: \n' '1- Nuevo juego \n' '2- Salir \n')
                if numero1 == 1:
                    numero2 = self.leer_entero(self.leer_teclado('Ingrese un modo de juego: \n' '1- Patron al azar \n'
                                                                 '2- Introducir patron \n' '3- Modo vida estatica \n'),
                                                'Ingrese un modo de juego: \n' '1- Patron al azar \n'
                                                '2- Introducir patron \n' '3- Modo vida estatica \n')
                    if numero2 == 1:
                        numero3 = self.leer_entero(self.leer_teclado('Patron al azar: \n' '1- Nueva matriz \n' '2- Cargar matriz \n'),
                                                   'Patron al azar: \n' '1- Nueva matriz \n' '2- Cargar matriz \n')
                        if numero3 == 1:
                            pass
                        elif numero3 == 2:
                            pass
                        else:
                            raise Exception
                    elif numero2 == 2:
                        numero4 = self.leer_entero(
                            self.leer_teclado('Introducir patron: \n' '1- Nueva matriz \n' '2- Cargar matriz \n'),
                                                'Introducir Patron: \n' '1- Nueva matriz \n' '2- Cargar matriz \n')
                        if numero4 == 1:
                            pass
                        elif numero4 == 2:
                            pass
                        else:
                            raise Exception
                    elif numero2 == 3:
                        numero5 = self.leer_entero(
                            self.leer_teclado('Modo vida estatica: \n' '1- Nueva matriz \n' '2- Cargar matriz \n'),
                                                'Modo vida estatica: \n' '1- Nueva matriz \n' '2- Cargar matriz \n')
                        if numero5 == 1:
                            pass
                        elif numero5 == 2:
                            pass
                        else:
                            raise Exception
                    else:
                        raise Exception
                elif numero1 == 2:
                    break
                else:
                    raise Exception
        except Exception:
            print('Por favor, ingrese un numero valido.')


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
if __name__ == '__main__':
        Menu().menu()
