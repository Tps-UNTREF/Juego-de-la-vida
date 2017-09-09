from Persistencia import Persistencia
from TableroCelular import TableroCelular


class Menu(object):
    def menu(self):
        try:
            while True:
                numero1 = self.leer_entero(self.leer_teclado('Ingrese modo de juego: \n' '1- Modo normal \n'
                                                             '2- Modo vida estatica \n' '3- Salir \n'))
                persistencia = Persistencia()
                if numero1 == 1:
                    '''MODO NORMAL'''
                    numero2 = self.leer_entero(
                        self.leer_teclado('Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                          '2- Crear tablero manualmente \n' '3- Cargar tablero \n'))
                    if numero2 == 1:
                        '''MODO NORMAL - PATRON AL AZAR'''
                        tamaño_del_tablero = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la matriz:'))
                        while True:
                            try:
                                self.tablero = TableroCelular(tamaño_del_tablero)
                                cantidad_de_celulas = self.leer_entero(
                                    self.leer_teclado('Ingrese la cantidad de celulas vivas:'))
                                self.tablero.rellenar_matriz_al_azar(cantidad_de_celulas)
                                self.tablero.imprimir_tablero()
                                numero2_1 = self.leer_entero(
                                    self.leer_teclado('Ingrese una accion: \n' '1- Siguiente paso \n'
                                                      '2- Modificar tablero \n' '3- Guardar tablero \n'))
                                break
                            except IndexError:
                                print('La cantidad de celdas vivas tiene que ser hasta ' + str(
                                    len(self.tablero.matriz) * len(self.tablero.matriz)))
                        if numero2_1 == 1:
                            '''SIGUIENTE PASO'''
                        elif numero2_1 == 2:
                            '''MODIFICAR TABLERO'''
                            while True:
                                try:
                                    fila = self.leer_entero(self.leer_teclado('Ingrese posicion de fila:'))
                                    columna = self.leer_entero(self.leer_teclado('Ingrese posicion de columna:'))
                                    valor = self.leer_teclado('Ingrese "*" o "-":')
                                    self.tablero.rellenar_matriz_manualmente(fila, columna, valor)
                                    break
                                except IndexError:
                                    print("Por favor ingrese un numero de fila y columna comprendido entre 0 y " + str(
                                        self.tablero.matriz))
                                except Exception:
                                    print(Exception)
                        elif numero2_1 == 3:
                            '''GUARDAR TABLERO'''
                            while True:
                                try:
                                    tablero = self.tablero.matriz
                                    ruta = self.leer_teclado('Ingrese la ruta del archivo:')
                                    clave = self.leer_teclado('Ingrese la clave para guardar el tablero:')
                                    persistencia.guardar(ruta,tablero,clave)
                                    break
                                except Exception:
                                    print('Fallo la ruta del teclado')
                        else:
                            raise Exception
                    elif numero2 == 2:
                        '''MODO NORMAL - CREAR MANUALMENTE'''
                        tamaño_del_tablero = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la matriz:'))
                        self.tablero = TableroCelular(tamaño_del_tablero)
                        while True:
                            numero2_2_1 = self.leer_entero(
                                self.leer_teclado('Ingrese accion: \n' '1- Modificar celda \n' '2- Comenzar juego'))
                            if numero2_2_1 == 1:
                                try:
                                    fila = self.leer_entero(self.leer_teclado('Ingrese fila: '))
                                    columna = self.leer_entero(self.leer_teclado('Ingrese columna: '))
                                    estado = self.leer_teclado('Ingrese estado (* viva o - muerta): ')
                                    self.tablero.rellenar_matriz_manualmente(fila, columna, estado)
                                except IndexError:
                                    print('Ingrese fila o columna correcta entre 0 y ' + str(
                                        len(self.tablero.matriz) - 1))
                            elif numero2_2_1 == 2:
                                break
                            else:
                                raise Exception
                        '''COMENZAR JUEGO'''
                    elif numero2 == 3:
                        '''MODO NORMAL - CARGAR'''
                        while True:
                            try:
                                direccion = self.leer_teclado('Ingrese ruta del archivo: ')
                                clave = self.leer_entero(self.leer_teclado('Ingrese posicion de guardado: '))
                                self.tablero.matriz = persistencia.cargar(direccion, clave)
                                break
                            except Exception:
                                print('No existe un tablero guardado en esa posicion.')
                    else:
                        raise Exception
                elif numero1 == 2:
                    '''MODO VIDA ESTATICA'''
                    numero3 = self.leer_entero(
                        self.leer_teclado('Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                          '2- Crear tablero manualmente \n' '3- Cargar tablero \n'))
                    if numero3 == 1:
                        '''PATRON AL AZAR - MODO VIDA ESTATICA'''
                    elif numero3 == 2:
                        '''TABLERO MANUAL - MODO VIDA ESTATICA'''
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

    def leer_teclado(self, texto):
        while True:
            try:
                ingresado = eval(input(texto))
                if (ingresado == ''):
                    return None
                else:
                    return ingresado
            except (EOFError, KeyboardInterrupt):
                return None

    def leer_entero(self, entrada):
        while True:
            try:
                if type(entrada) == int:
                    return entrada
                else:
                    raise Exception
            except Exception:
                print('Por favor ingrese un numero entero')

                # Prueba github1 mergeado


if __name__ == '__main__':
    Menu().menu()
