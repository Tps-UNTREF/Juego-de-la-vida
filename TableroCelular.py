import random

class TableroCelular(object):

    def __init__(self,numero_filas,numero_columnas):
        self.matriz = self.matriz_nueva(numero_filas,numero_columnas)

    def matriz_nueva(self,numero_filas,numero_columnas):
        matriz_nueva = []
        for i in range(numero_filas):
            matriz_nueva.append(['-'] * numero_columnas)
        return matriz_nueva

    def rellenar_matriz_al_azar(self,numero_de_celdas_vivas):
        combinaciones = []

        if(numero_de_celdas_vivas <= len(self.matriz)*len(self.matriz[0])):
            for fila in range(len(self.matriz)):
                for columna in range(len(self.matriz[0])):
                    combinaciones.append((fila,columna))
            random.shuffle(combinaciones)
            for i in range(numero_de_celdas_vivas):
                combinacion_random = combinaciones.pop()
                self.matriz[combinacion_random[0]][combinacion_random[1]] = '*'
        else:
            raise IndexError


    def rellenar_matriz_manualmente(self,fila,columna,valor_de_matriz):
        if(fila > len(self.matriz) or columna > len(self.matriz[0])):
            raise IndexError
        elif(valor_de_matriz != '-' or valor_de_matriz != '*'):
            raise Exception('Ingresar - o * en el valor_de_la_matriz') #cambiar error
        else:
            self.matriz[fila][columna] = valor_de_matriz

    def imprimir_tablero(self):
        for f in self.matriz:
            print(str(f))

    def cantidad_de_vecinos(self, fila, columna):
        distancia_de_celdas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        celdas_vivas_alrededor = 0
        for x, y in distancia_de_celdas:
            if (x >= 0 and x < len(self.matriz) and (y >= 0 and y < len(self.matriz))): # Verifica que este dentro del tablero
                if(self.matriz[fila + x][columna + y] == '*'):
                    celdas_vivas_alrededor += 1
        return celdas_vivas_alrededor

    def mutar_celulas(self):
        pass
        '''matriz_actualizada = self.matriz_nueva(len(self.matriz))
        for x, y in self.matriz:'''















