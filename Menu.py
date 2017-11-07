from Excepciones.NumeroNoEstaEnMenu import NumeroNoEstaEnMenu
from Excepciones.ValorCelularNoValido import ValorCelularNoValido
from Persistencia import Persistencia
from TableroCelular import TableroCelular
from Extras.combination import combinations
from Excepciones.PatronesMayoresALaDimencion import PatronesMayoresALaDimencion

class Menu(object):
    def menu(self):
        while True:
            try:
                numero1 = self.leer_entero('Ingrese modo de juego: \n' '1- Modo normal \n'
                                                             '2- Modo vida estatica \n' '3- Salir \n')
                self.persistencia = Persistencia()
                self.tablero = TableroCelular(0, 0)

                if numero1 == 1:
                    '''MODO NORMAL'''
                    self.creacion_de_tableros()
                elif numero1 == 2:
                    while True:
                        try:
                            '''MODO VIDA ESTATICA'''
                            cargar = self.leer_entero('Desea cargar algun modo de vida estatico pasado?: \n' '1- si \n'
                                                       '2- no,continuar \n')
                            if cargar == 2:
                                self.modo_estatico()
                                return self.menu()
                            elif cargar == 1:
                                direccion = self.leer_teclado('Ingrese ruta del archivo sin comillas: ')
                                clave = self.leer_teclado('Ingrese posicion de guardado sin comillas: ')
                                lista_posicion_tablero = self.persistencia.cargar_vida_estatica(direccion,clave)
                                self.modo_estatico_cargado(lista_posicion_tablero[0],lista_posicion_tablero[1])
                        except PatronesMayoresALaDimencion:
                            print("Ingresar patron mas chico")
                        except (KeyboardInterrupt,EOFError):
                            condicion = self.leer_entero('Desea guardar el ultimo punto del modo de vida estatico? 1-Si 2-Salir')
                            if condicion == 1:
                                ruta = self.leer_teclado('Ingrese la ruta del archivo sin comillas:')
                                clave = self.leer_teclado('Ingrese la clave para guardar el tablero sin comillas:')
                                self.persistencia.guardar_vida_estatica_tupla(ruta, self.posicion_tupla_actual,self.tablero.matriz, clave)
                                return self.menu()
                            elif condicion == 2:
                                return self.menu()

                elif numero1 == 3:
                    print('El Programa se cerro correctamente!')
                    break
                else:
                    raise NumeroNoEstaEnMenu
            except (NumeroNoEstaEnMenu):
                print('Por favor, ingrese un numero del 1 al 3.')
            except (KeyboardInterrupt,EOFError):
                print('Error atrapado de Ctrl-C')
                



    def creacion_de_tableros(self):
        while True:
            try:

                numero2 = self.leer_entero('Elija una opción para crear el tablero: \n' '1- Patron al azar \n'
                                      '2- Crear tablero manualmente \n' '3- Cargar tablero \n' '4- Volver al menu \n')

                if numero2 == 1:
                    '''MODO NORMAL - PATRON AL AZAR'''
                    fila = self.leer_entero('Ingrese el tamaño de la fila de la matriz:')
                    columna = self.leer_entero('Ingrese el tamaño de la columna de la matriz:')
                    while True:
                        try:
                            self.tablero = TableroCelular(fila, columna)
                            cantidad_de_celulas = self.leer_entero('Ingrese la cantidad de celulas vivas:')
                            self.tablero.rellenar_matriz_al_azar(cantidad_de_celulas)

                            # MODO

                            self.modo_normal()

                            break
                        except IndexError:
                            print('La cantidad de celdas vivas tiene que ser hasta ' + str(
                                len(self.tablero.matriz) * len(self.tablero.matriz)))

                elif numero2 == 2:
                    '''MODO NORMAL - CREAR MANUALMENTE'''
                    fila = self.leer_entero('Ingrese el tamaño de la fila de la matriz:')
                    columna = self.leer_entero('Ingrese el tamaño de la columna de la matriz:')
                    self.tablero = TableroCelular(fila, columna)
                    while True:
                        '''COMENZAR JUEGO'''
                        numero2_2_1 = self.leer_entero('Ingrese accion: \n' '1- Modificar celda \n' '2- Comenzar juego \n')
                        if numero2_2_1 == 1:
                            try:
                                fila = self.leer_entero('Ingrese fila: ')
                                columna = self.leer_entero('Ingrese columna: ')
                                estado = self.leer_teclado('Ingrese estado "*" viva o "-" muerta (Sin comillas): ')
                                self.tablero.rellenar_matriz_manualmente(fila, columna, estado)
                            except IndexError:
                                print('Ingrese fila o columna correcta entre 0 y ' + str(
                                    len(self.tablero.matriz) - 1))
                            except ValorCelularNoValido:
                                print('Ingresar - o * en el valor_de_la_matriz')

                                # MODO

                        elif numero2_2_1 == 2:
                            self.modo_normal()
                            break
                        else:
                            raise NumeroNoEstaEnMenu

                elif numero2 == 3:
                    '''MODO NORMAL - CARGAR'''
                    while True:
                        try:
                            direccion = self.leer_teclado('Ingrese ruta del archivo sin comillas: ')
                            clave = self.leer_teclado('Ingrese posicion de guardado sin comillas: ')
                            self.tablero.matriz = self.persistencia.cargar(direccion, clave)

                            # MODO

                            self.modo_normal()
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
                print('Por favor, ingrese un numero del 1 al 4.')

    def modo_normal(self):
        while True:
            try:
                self.tablero.imprimir_tablero()
                numero_de_modo_normal = self.leer_entero('Ingrese una accion: \n' '1- Siguiente paso \n'
                                      '2- Modificar tablero \n' '3- Guardar tablero \n' '4- Volver \n')

                if numero_de_modo_normal == 1:
                    '''MODO NORMAL - SIGUIENTE PASO'''
                    self.tablero.mutar_celulas_modo_normal()
                elif numero_de_modo_normal == 2:
                    '''MODIFICAR TABLERO'''
                    while True:
                        try:
                            fila = self.leer_entero('Ingrese posicion de fila:')
                            columna = self.leer_entero('Ingrese posicion de columna:')
                            valor = self.leer_teclado('Ingrese "*" o "-"(Sin comillas):')
                            self.tablero.rellenar_matriz_manualmente(fila, columna, valor)
                            break
                        except IndexError:
                            print("Por favor ingrese un numero de fila comprendido entre 0 y " + str(
                                len(self.tablero.matriz)) + "y columna comprendido entre 0 y " + str(
                                len(self.tablero.matriz[0])))
                        except Exception:
                            print(Exception)

                elif numero_de_modo_normal == 3:
                    '''GUARDAR TABLERO'''
                    while True:
                        try:
                            tablero = self.tablero.matriz
                            ruta = self.leer_teclado('Ingrese la ruta del archivo sin comillas:')
                            clave = self.leer_teclado('Ingrese la clave para guardar el tablero sin comillas:')
                            self.persistencia.guardar(ruta, tablero, clave)
                            break
                        except Exception:
                            print('Fallo la ruta del teclado')

                elif numero_de_modo_normal == 4:
                    break
                else:
                    raise NumeroNoEstaEnMenu
            except NumeroNoEstaEnMenu:
                print('Por favor ingrese un numero del 1 al 4')

    def modo_estatico(self):
        fila = self.leer_entero('Ingrese el tamaño de la fila de la matriz:')
        columna = self.leer_entero('Ingrese el tamaño de la columna de la matriz:')
        patrones = self.leer_entero('Cantidad de celdas vivas:')

        self.tablero = TableroCelular(fila, columna)

        dimencion_de_tablero = fila * columna

        lista_tuplas = []

        cantidad_tableros = 0

        if (patrones <= dimencion_de_tablero):
            for x in combinations(range(dimencion_de_tablero), patrones):
                self.posicion_tupla_actual = x
                self.tablero.matriz = self.tablero.matriz_nueva(fila, columna)
                self.tablero.contador_vidas_estaticas = 0
                self.tablero.diccionario_de_celdas = {}
                encontro = True
                contador = 0
                for posicion_tupla in x:  # este for rellena los vivos con las combinaciones
                    coordenadas = (
                    posicion_tupla // len(self.tablero.matriz[0]), posicion_tupla % len(self.tablero.matriz[0]))
                    self.tablero.rellenar_matriz_manualmente(coordenadas[0], coordenadas[1], '*')

                self.tablero.mutar_celulas()


                if self.tablero.matriz_antigua == self.tablero.matriz:
                    self.tablero.imprimir_tablero()
                    cantidad_tableros += 1
                    print('--------------------------------------')

            if cantidad_tableros > 0:
                print('Se encontraron ' + str(cantidad_tableros) + ' tableros estáticos.')
            else:
                print('No se encontraron tableros estáticos.')

        else:
            raise PatronesMayoresALaDimencion

    def modo_estatico_cargado(self, posicion_tupla_guardada, tablero):

        empezar = False
        self.tablero.matriz = tablero
        fila = len(self.tablero.matriz)
        columna = len(self.tablero.matriz[0])
        contador_vivos = 0
        patrones = len(posicion_tupla_guardada)
        dimencion_de_tablero = fila * columna

        cantidad_tableros = 0

        if (patrones <= dimencion_de_tablero):
            for x in combinations(range(dimencion_de_tablero), patrones):
                self.tablero.matriz = self.tablero.matriz_nueva(fila, columna)
                self.tablero.contador_vidas_estaticas = 0
                self.tablero.diccionario_de_celdas = {}
                if x == posicion_tupla_guardada:
                    empezar = True
                for posicion_tupla in x:  # este for rellena los vivos con las combinaciones
                    coordenadas = (
                            posicion_tupla // len(self.tablero.matriz[0]), posicion_tupla % len(self.tablero.matriz[0]))
                    self.tablero.rellenar_matriz_manualmente(coordenadas[0], coordenadas[1], '*')

                if empezar:
                    self.tablero.mutar_celulas()

                    if self.tablero.matriz_antigua == self.tablero.matriz:
                        self.tablero.imprimir_tablero()
                        cantidad_tableros += 1
                        print('--------------------------------------')

            if cantidad_tableros > 0:
                print('Se encontraron ' + str(cantidad_tableros) + ' tableros estáticos.')
            else:
                print('No se encontraron tableros estáticos.')

        else:
            raise PatronesMayoresALaDimencion



    def leer_teclado(self, texto):
        while True:
            try:
                ingresado = str(input(texto))
                break
            except (EOFError, KeyboardInterrupt):
                print('Error atrapado de Ctrl-C')
        return ingresado

    def leer_entero(self,texto):
        while True:
            try:
                ingresado = eval(input(texto))
                if type(ingresado) == int:
                    return ingresado
                else:
                    raise Exception
            except (Exception, ValueError):
                print('Por favor ingrese un numero entero')
            except (EOFError, KeyboardInterrupt):
                print('Error atrapado de Ctrl-C')



if __name__ == '__main__':
    Menu().menu()
