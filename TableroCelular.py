import random

class TableroCelular(object):


    def __init__(self,numero_columnas_filas):
        self.matriz = []
        self.numero_columnas_filas = numero_columnas_filas
        self.creacion_de_la_matriz(numero_columnas_filas)

    def creacion_de_la_matriz(self,numero_columnas_filas):
        self.matriz = []
        for i in range(numero_columnas_filas):
            self.matriz.append(['-'] * numero_columnas_filas)

    def rellenar_matriz_al_azar(self):
        for i in range(self.numero_columnas_filas):
            for j in range(self.numero_columnas_filas):
                self.matriz[i][j] = random.choice(['*','-'])

    def rellenar_matriz_manualmente(self,fila,columna,valor_de_matriz):
        if(fila > self.numero_columnas_filas or columna > self.numero_columnas_filas):
            raise IndexError
        elif(valor_de_matriz != '-' or valor_de_matriz != '*'):
            raise KeyError #cambiar error
        else:
            self.matriz[fila][columna] = valor_de_matriz








