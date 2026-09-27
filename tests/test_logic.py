import unittest
from src.tools.performance import consultar_metricas
from src.tools.security import consultar_alertas_seguranca


class TesteLaboratorio(unittest.TestCase):
    def test_metricas_todas(self):
        self.assertEqual(len(consultar_metricas()), 3)

    def test_metricas_filtro(self):
        self.assertEqual(consultar_metricas('roteador-01')[0]['latencia_ms'], 25)

    def test_alertas_todos(self):
        self.assertEqual(len(consultar_alertas_seguranca()), 2)

    def test_alertas_filtro(self):
        self.assertEqual(len(consultar_alertas_seguranca('alto')), 1)

    def test_nivel_invalido(self):
        with self.assertRaises(ValueError):
            consultar_alertas_seguranca('urgente')


if __name__ == '__main__':
    unittest.main()
