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
            raise KeyError #cambiar error
        else:
            self.matriz[fila][columna] = valor_de_matriz










