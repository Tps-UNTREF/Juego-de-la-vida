import unittest
from TableroCelular import TableroCelular

class TestTableroCelular(unittest.TestCase):
    def setUp(self):
        self.tablero = TableroCelular(4,6)

    def test_creacion_de_matriz(self):
        print('Matriz Vacia')
        print(self.tablero.matriz)

    def test_rellenar_matriz_al_azar_completo(self):
        '''La idea es llenar la matriz para ver que no se pisen las posiciones'''
        print('Matriz Random')
        self.tablero.rellenar_matriz_al_azar(24)
        print(self.tablero.matriz)

    def test_rellenar_matriz_al_azar(self):
        self.tablero.matriz = self.tablero.matriz_nueva(4,5)
        print('Matriz Random 4 celulas vivas')
        self.tablero.rellenar_matriz_al_azar(4)
        print(self.tablero.matriz)

    def test_cantidad_de_vecinos_vios(self):
        self.tablero.rellenar_matriz_manualmente(0,0,'*')
        self.tablero.rellenar_matriz_manualmente(0, 1, '*')
        self.tablero.rellenar_matriz_manualmente(1, 0, '*')
        self.tablero.imprimir_tablero()
        self.assertEquals(self.tablero.cantidad_de_vecinos(0,0),2)

    def test_celula_mutan(self):
        print('Tablero antes')
        self.tablero.rellenar_matriz_al_azar(8)
        self.tablero.imprimir_tablero()
        print('Tablero mutado')
        self.tablero.mutar_celulas()
        self.tablero.imprimir_tablero()

    def test_vida_estatica(self):
        self.tablero = TableroCelular(3, 3)
        self.tablero.rellenar_matriz_manualmente(0, 1, '*')
        self.tablero.rellenar_matriz_manualmente(1, 1, '*')
        self.tablero.rellenar_matriz_manualmente(2, 1, '*')
        self.tablero.mutar_modo_vida_estatica()
        self.tablero.imprimir_tablero()
        self.tablero.mutar_modo_vida_estatica()
        self.tablero.imprimir_tablero()
        self.tablero.mutar_modo_vida_estatica()
        self.tablero.imprimir_tablero()
        self.tablero.mutar_modo_vida_estatica()
        self.tablero.imprimir_tablero()

    def test_hola(self):
        self.test_vida_estatica()



if __name__ == '__main__':
        unittest.main()

