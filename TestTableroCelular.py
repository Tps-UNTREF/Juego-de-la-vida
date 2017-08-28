import unittest
from TableroCelular import TableroCelular

class TestTableroCelular(unittest.TestCase):
    def setUp(self):
        self.tablero = TableroCelular(4)

    def test_creacion_de_matriz(self):
        print('Matriz Vacia')
        print(self.tablero.matriz)

    def test_rellenar_matriz_al_azar(self):
        print('Matriz Random')
        self.tablero.rellenar_matriz_al_azar()
        print(self.tablero.matriz)


if __name__ == '__main__':
        unittest.main()

