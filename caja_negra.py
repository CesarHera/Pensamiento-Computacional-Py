import unittest


def suma(num1, num2):
    return num1 + num2

def division(num1, num2):
    return num1 / num2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, 15)


    def test_division(self):
        num1 = 10
        num2 = 2

        resultado = division(num1, num2)

        self.assertEqual(resultado, 5)

        
    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, -15)



if __name__ == '__main__':
    unittest.main()