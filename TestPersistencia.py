import unittest

from Persistencia import Persistencia
from TableroCelular import TableroCelular


class TestPersistencia(unittest.TestCase):
    def setUp(self):
        self.tablero = TableroCelular(4,5)
        self.tablero.rellenar_matriz_al_azar(6)
        self.tablero2 = TableroCelular(5,6)
        self.tablero.rellenar_matriz_al_azar(15)
        self.persistencia = Persistencia()

    def test_guardado(self):
        print('TEST-GUARDADO-1')
        self.persistencia.guardar('tablero.s', self.tablero.matriz, 'tablero1')

    def test_guardado2(self):
        print('TEST-GUARDADO-2')
        self.persistencia.guardar('tablero.s', self.tablero2.matriz, 'tablero2')

    def test_cargar_mostrar_matriz(self):
        print('TEST-CARGAR-MATRIZ')
        print('Clave tablero1')
        print(self.persistencia.cargar('tablero.s', 'tablero1'))
        print('Clave tablero2')
        print(self.persistencia.cargar('tablero.s', 'tablero2'))


if __name__ == '__main__':
    unittest.main()
