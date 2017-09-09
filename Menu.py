from Persistencia import Persistencia
from TableroCelular import TableroCelular


class Menu(object):

    def menu(self):
        try:
            while True:
                numero1 = self.leer_entero(self.leer_teclado('Ingrese modo de juego: \n' '1- Modo normal \n'
                                                             '2- Modo vida estatica \n' '3- Salir \n'),
                                            'Ingrese modo de juego: \n' '1- Modo normal \n' '2- Modo vida estatica \n' '3- Salir \n')
                if numero1 == 1:
                    numero2 = self.leer_entero(self.leer_teclado('Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                                                 '2- Crear tablero manualmente \n' '3- Cargar tablero \n'),
                                                'Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                                '2- Crear tablero manualmente \n' '3- Cargar tablero \n')
                    if numero2 == 1:
                        tamaño_del_tablero = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la matriz:'),
                                                              'Ingrese el tamaño de la matriz:')
                        self.tablero = TableroCelular(tamaño_del_tablero)
                        cantidad_de_celulas = self.leer_entero(self.leer_teclado('Ingrese la cantidad de celulas vivas:'),
                                                              'Ingrese la cantidad de celulas vivas:')
                        self.tablero.rellenar_matriz_al_azar(cantidad_de_celulas)
                        self.tablero.imprimir_tablero()
                        numero2_1 = self.leer_entero(self.leer_teclado('Ingrese una accion: \n' '1- Siguiente paso \n'
                                                                       '2- Modificar tablero \n' '3- Guardar tablero \n'),
                                                     'Ingrese una accion: \n' '1- Siguiente paso \n' 
                                                     '2- Modificar tablero \n' '3- Guardar tablero \n')
                        if numero2_1 == 1:
                            '''SIGUIENTE PASO'''
                        elif numero2_1 == 2:
                            '''MODIFICAR TABLERO'''
                        elif numero2_1 == 3:
                            '''GUARDAR TABLERO'''
                        else:
                            raise Exception
                    elif numero2 == 2:
                        tamaño_del_tablero = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la matriz:'),
                                                              'Ingrese el tamaño de la matriz:')
                        self.tablero = TableroCelular(tamaño_del_tablero)
                        while True:
                            numero2_2_1 = self.leer_entero(self.leer_teclado('Ingrese accion: \n' '1- Modificar celda \n' '2- Comenzar juego'),
                                                                  'Ingrese accion: \n' '1- Modificar celda \n' '2- Comenzar juego')
                            if numero2_2_1 == 1:
                                try:
                                    fila = self.leer_entero(self.leer_teclado('Ingrese fila: '), 'Ingrese fila: ')
                                    columna = self.leer_entero(self.leer_teclado('Ingrese columna: '), 'Ingrese columna: ')
                                    estado = self.leer_teclado('Ingrese estado (* viva o - muerta): ')
                                    self.tablero.rellenar_matriz_manualmente(fila, columna, estado)
                                except IndexError:
                                    print('Ingrese fila o columna correcta entre 0 y ' + str(len(self.tablero.matriz)-1))
                            elif numero2_2_1 == 2:
                                break
                            else:
                                raise Exception
                        '''COMENZAR JUEGO'''
                    elif numero2 == 3:
                        while True:
                            try:
                                direccion = self.leer_teclado('Ingrese ruta del archivo: ')
                                clave = self.leer_entero(self.leer_teclado('Ingrese posicion de guardado: '), 'Ingrese posicion de guardado: ')
                                persistencia = Persistencia()
                                self.tablero.matriz = persistencia.cargar(direccion, clave)
                                break
                            except Exception:
                                print('No existe un tablero guardado en esa posicion.')
                    else:
                        raise Exception
                elif numero1 == 2:
                    numero3 = self.leer_entero(self.leer_teclado('Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                                                    '2- Crear tablero manualmente \n' '3- Cargar tablero \n'),
                                                'Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                                '2- Crear tablero manualmente \n' '3- Cargar tablero \n')
                    if numero3 == 1:
                        '''PATRON AL AZAR MODO VIDA ESTATICA'''
                    elif numero3 == 2:
                        '''TABLERO MANUAL MODO VIDA ESTATICA'''
                    elif numero3 == 3:
                        '''CARGAR TABLERO'''
                    else:
                        raise Exception
                elif numero1 == 3:
                    break
                else:
                    raise Exception
        except Exception:
            print('Por favor, ingrese un numero valido.')
            return self.menu()


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
