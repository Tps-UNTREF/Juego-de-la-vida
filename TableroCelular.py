import random
from Excepciones.ValorCelularNoValido import ValorCelularNoValido

class TableroCelular(object):

    def __init__(self, numero_filas, numero_columnas):
        self.matriz = self.matriz_nueva(numero_filas,numero_columnas)
        self.matriz_antigua = []
        self.contador_vidas_estaticas = 0
        self.diccionario_de_celdas = {}

    def matriz_nueva(self, numero_filas, numero_columnas):
        matriz_nueva = []
        for i in range(numero_filas):
            matriz_nueva.append(['-'] * numero_columnas)
        return matriz_nueva

    def rellenar_matriz_al_azar(self, numero_de_celdas_vivas):
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
        print(valor_de_matriz == '*')
        if(fila > len(self.matriz) or columna > len(self.matriz[0])):
            raise IndexError
        elif(valor_de_matriz != '-' and valor_de_matriz != '*'):
            raise ValorCelularNoValido
        else:
            self.matriz[fila][columna] = valor_de_matriz
            self.contador_vidas_estaticas = 0

    def imprimir_tablero(self):
        for f in self.matriz:
            print(str(f))

    def cantidad_de_vecinos(self, fila, columna):
        distancia_de_celdas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        celdas_vivas_alrededor = 0
        for x, y in distancia_de_celdas:
            if (fila + x >= 0 and fila + x < len(self.matriz) and (columna + y >= 0 and columna + y < len(self.matriz[0]))): # Verifica que este dentro del tablero
                if(self.matriz[fila + x][columna + y] == '*'):
                    celdas_vivas_alrededor += 1
        return celdas_vivas_alrededor

    def mutar_celulas(self):
        matriz_actualizada = self.matriz_nueva(len(self.matriz), len(self.matriz[0]))
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                if(self.matriz[x][y] == '-'):
                    if(self.cantidad_de_vecinos(x, y) >= 3):
                        matriz_actualizada[x][y] = '*'
                else:
                    if self.cantidad_de_vecinos(x, y) == 2 or self.cantidad_de_vecinos(x, y) == 3:
                        matriz_actualizada[x][y] = '*'
        self.matriz_antigua = self.matriz
        self.matriz = matriz_actualizada
        self.vidas_estaticas()

    def vidas_estaticas(self):
        son_iguales = True
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[0])):
                if self.matriz[x][y] != self.matriz_antigua[x][y]:
                    son_iguales = False
        if son_iguales:
            self.contador_vidas_estaticas += 1
        else:
            self.contador_vidas_estaticas = 0

    def mutar_celulas_modo_normal(self):
        if self.contador_vidas_estaticas < 3:
            self.mutar_celulas()
        else:
            print('GAME OVER: El tablero es vida estática.')

    def mutar_modo_vida_estatica(self):
        if self.diccionario_de_celdas == {}:
            for x in range(len(self.matriz)):
                for y in range(len(self.matriz[x])):
                    self.diccionario_de_celdas[(x, y)] = 0
        self.mutar_celulas_no_estaticas()
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[0])):
                if self.matriz[x][y] == self.matriz_antigua[x][y]:
                    self.diccionario_de_celdas[(x, y)] = self.diccionario_de_celdas[(x, y)] + 1
                    if self.diccionario_de_celdas[(x, y)] >= 3:
                        print('La celda ' + str(self.matriz[x][y]) + ' en la fila ' + str(x) + ' y columna '
                              + str(y) + ' es estática.')
                else:
                    self.diccionario_de_celdas[(x, y)] = 0

    def mutar_celulas_no_estaticas(self):
        matriz_actualizada = self.matriz_nueva(len(self.matriz), len(self.matriz[0]))
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                if self.diccionario_de_celdas[(x, y)] < 3:
                    if self.matriz[x][y] == '-':
                        if self.cantidad_de_vecinos(x, y) >= 3:
                            matriz_actualizada[x][y] = '*'
                    else:
                        if self.cantidad_de_vecinos(x, y) == 2 or self.cantidad_de_vecinos(x, y) == 3:
                            matriz_actualizada[x][y] = '*'
        self.matriz_antigua = self.matriz
        self.matriz = matriz_actualizada
        self.vidas_estaticas()







