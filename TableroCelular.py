import random

class TableroCelular(object):


    def __init__(self,numero_columnas_filas):
        self.matriz = []
        self.numero_columnas_filas = numero_columnas_filas
        self.crear_matriz_vacia(numero_columnas_filas)

    def crear_matriz_vacia(self,numero_columnas_filas):
        self.matriz = []
        for i in range(numero_columnas_filas):
            self.matriz.append(['-'] * numero_columnas_filas)

    def rellenar_matriz_al_azar(self,numero_de_celdas_vivas):
        combinaciones = []

        if(numero_de_celdas_vivas <= len(self.matriz)*len(self.matriz)):
            for fila in range(len(self.matriz)):
                for columna in range(len(self.matriz)):
                    combinaciones.append((fila,columna))
            random.shuffle(combinaciones)
            for i in range(numero_de_celdas_vivas):
                combinacion_random = combinaciones.pop()
                self.matriz[combinacion_random[0]][combinacion_random[1]] = '*'
        else:
            raise IndexError


    def rellenar_matriz_manualmente(self,fila,columna,valor_de_matriz):
        if(fila > self.numero_columnas_filas or columna > self.numero_columnas_filas):
            raise IndexError
        elif(valor_de_matriz != '-' or valor_de_matriz != '*'):
            raise Exception('Ingresar - o * en el valor_de_la_matriz') #cambiar error
        else:
            self.matriz[fila][columna] = valor_de_matriz

    def proxima_generacion(self, cantidad_de_generaciones):

        for x in range(cantidad_de_generaciones):
            for j in range(self.__filas):
                for k in range(self.__columnas):
                    celdas_vecinas_vivas = self.num_vecinos_vivos(j, k)
                    if celdas_vecinas_vivas == 3:
                        self.__tablero[j][k] = '*'
                    elif celdas_vecinas_vivas < 2 or celdas_vecinas_vivas > 3:
                        self.__tablero[j][k] = '-'

            print('\n')
            self.get_tablero()

    def imprimir_tablero(self):
        for f in self.matriz:
            print(str(f))

