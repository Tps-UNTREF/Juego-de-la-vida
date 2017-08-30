import unittest
from TableroCelular import TableroCelular

class TestTableroCelular(unittest.TestCase):
    def setUp(self):
        self.tablero = TableroCelular(4)

    def test_creacion_de_matriz(self):
        print('Matriz Vacia')
        print(self.tablero.matriz)

    def test_rellenar_matriz_al_azar_completo(self):
        '''La idea es llenar la matriz para ver que no se pisen las posiciones'''
        print('Matriz Random')
        self.tablero.rellenar_matriz_al_azar(16)
        print(self.tablero.matriz)

    def test_rellenar_matriz_al_azar(self):
        self.tablero.crear_matriz_vacia(4)
        print('Matriz Random 4 celulas vivas')
        self.tablero.rellenar_matriz_al_azar(4)
        print(self.tablero.matriz)


if __name__ == '__main__':
        unittest.main()

