from Excepciones.NumeroNoEstaEnMenu import NumeroNoEstaEnMenu
from Excepciones.ValorCelularNoValido import ValorCelularNoValido
from Persistencia import Persistencia
from TableroCelular import TableroCelular

class Menu(object):


    def menu(self):
        try:
            while True:
                numero1 = self.leer_entero(self.leer_teclado('Ingrese modo de juego: \n' '1- Modo normal \n'
                                                             '2- Modo vida estatica \n' '3- Salir \n'))
                self.persistencia = Persistencia()
                self.tablero = TableroCelular(0,0)

                if numero1 == 1:
                    '''MODO NORMAL'''
                    self.creacion_de_tableros('modo_normal')
                elif numero1 == 2:
                    '''MODO VIDA ESTATICA'''
                    self.creacion_de_tableros('modo_estatico')

                elif numero1 ==3:
                    print('El Programa se cerro correctamente!')
                    break

                else:
                    raise NumeroNoEstaEnMenu

        except NumeroNoEstaEnMenu:
            print('Por favor, ingrese un numero valido.')
            return self.menu()



    def creacion_de_tableros(self,tipo_de_modo):
        while True:
            try:

                numero2 = self.leer_entero(
                    self.leer_teclado('Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                      '2- Crear tablero manualmente \n' '3- Cargar tablero \n' '4- Volver al menu \n'))

                if numero2 == 1:
                    '''MODO NORMAL - PATRON AL AZAR'''
                    fila = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la fila de la matriz:'))
                    columna = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la columna de la matriz:'))
                    while True:
                        try:
                            self.tablero = TableroCelular(fila, columna)
                            cantidad_de_celulas = self.leer_entero(
                                self.leer_teclado('Ingrese la cantidad de celulas vivas:'))
                            self.tablero.rellenar_matriz_al_azar(cantidad_de_celulas)

                            #SELECCIONADOR DE MODO

                            if(tipo_de_modo == 'modo_normal'):
                                self.modos_de_juego('modo_normal')
                            elif(tipo_de_modo == 'modo_estatico'):
                                self.modos_de_juego('modo_estatico')
                            break
                        except IndexError:
                            print('La cantidad de celdas vivas tiene que ser hasta ' + str(
                                len(self.tablero.matriz) * len(self.tablero.matriz)))

                elif numero2 == 2:
                    '''MODO NORMAL - CREAR MANUALMENTE'''
                    fila = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la fila de la matriz:'))
                    columna = self.leer_entero(self.leer_teclado('Ingrese el tamaño de la columna de la matriz:'))
                    self.tablero = TableroCelular(fila, columna)
                    while True:
                        '''COMENZAR JUEGO'''
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
                            except ValorCelularNoValido:
                                print('Ingresar - o * en el valor_de_la_matriz')

                       #SELECCIONADOR DE MODO

                        elif numero2_2_1 == 2:
                            if(tipo_de_modo == 'modo_normal'):
                                self.modos_de_juego('modo_normal')
                            elif(tipo_de_modo == 'modo_estatico'):
                                self.modos_de_juego('modo_estatico')
                            break
                        else:
                            raise NumeroNoEstaEnMenu

                elif numero2 == 3:
                    '''MODO NORMAL - CARGAR'''
                    while True:
                        try:
                            direccion = self.leer_teclado('Ingrese ruta del archivo: ')
                            clave = self.leer_teclado('Ingrese posicion de guardado: ')
                            self.tablero.matriz = self.persistencia.cargar(direccion, clave)

                            # SELECCIONADOR DE MODO

                            if(tipo_de_modo == 'modo_normal'):
                                self.modos_de_juego('modo_normal')
                            elif(tipo_de_modo == 'modo_estatico'):
                                self.modos_de_juego('modo_estatico')
                            break
                        except FileNotFoundError:
                            print('Archivo no encontrado. Ingresar ruta valida.')
                        except TypeError:
                            print('Ingrese una posición de carga valida.')
                        except KeyError:
                            print('Ingresar una clave valida en un archivo correcto.')
                        except PermissionError:
                            print('Ingrese una ruta valida.')
                elif numero2 == 4:
                    break
                else:
                    raise NumeroNoEstaEnMenu
            except NumeroNoEstaEnMenu:
                print('Por favor, ingrese un numero valido.')



    def modos_de_juego(self,modo_de_juego):
        while True:
            try:
                self.tablero.imprimir_tablero()
                numero_de_modo_normal = self.leer_entero(
                    self.leer_teclado('Ingrese una accion: \n' '1- Siguiente paso \n'
                                      '2- Modificar tablero \n' '3- Guardar tablero \n' '4- Volver \n'))

                if numero_de_modo_normal == 1:
                    if modo_de_juego == 'modo_normal':
                        '''MODO NORMAL - SIGUIENTE PASO'''
                        self.tablero.mutar_celulas_modo_normal()
                    elif modo_de_juego == 'modo_estatico':
                        '''MODO ESTATICO - SIGUIENTE PASO'''
                        self.tablero.mutar_modo_vida_estatica()

                elif numero_de_modo_normal == 2:
                    '''MODIFICAR TABLERO'''
                    while True:
                        try:
                            fila = self.leer_entero(self.leer_teclado('Ingrese posicion de fila:'))
                            columna = self.leer_entero(self.leer_teclado('Ingrese posicion de columna:'))
                            valor = self.leer_teclado('Ingrese "*" o "-":')
                            self.tablero.rellenar_matriz_manualmente(fila, columna, valor)
                            break
                        except IndexError:
                            print("Por favor ingrese un numero de fila comprendido entre 0 y " + str(len(self.tablero.matriz)) + "y columna comprendido entre 0 y " + str(
                                len(self.tablero.matriz[0])))
                        except Exception:
                            print(Exception)

                elif numero_de_modo_normal == 3:
                    '''GUARDAR TABLERO'''
                    while True:
                        try:
                            tablero = self.tablero.matriz
                            ruta = self.leer_teclado('Ingrese la ruta del archivo:')
                            clave = self.leer_teclado('Ingrese la clave para guardar el tablero:')
                            self.persistencia.guardar(ruta, tablero, clave)
                            break
                        except Exception:
                            print('Fallo la ruta del teclado')

                elif numero_de_modo_normal == 4:
                    break
                else:
                    raise NumeroNoEstaEnMenu
            except NumeroNoEstaEnMenu:
                print('Por favor ingrese un numero entre el 1 y el 4')



    def leer_teclado(self, texto):
        while True:
            try:
                ingresado = eval(input(texto))
                if (ingresado == ''):
                    return None
                else:
                    return ingresado
            except (EOFError, KeyboardInterrupt,NameError):
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
                break



if __name__ == '__main__':
    Menu().menu()
