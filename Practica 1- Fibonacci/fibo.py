import unittest


def fibonacci(n):
    """Genera la secuencia de Fibonacci hasta el enésimo término."""
    secuencia = [0, 1]
    if n == 1:
        return [0]  # Caso especial si solo quiere el primer número
    for i in range(2, n):
        next_term = secuencia[-1] + secuencia[-2]
        secuencia.append(next_term)
    return secuencia[:n]


class TestFibonacci(unittest.TestCase):
    """Clase de testeo para verificar la función Fibonacci."""

    def test_fibonacci_5th_position(self):
        """Verificamos que el quinto número de la secuencia es 3."""
        resultado = fibonacci(5)  # La secuencia hasta el quinto número debe ser [0, 1, 1, 2, 3]
        ## Tamén poderíamos verificar se outras posición son correctas
        ## self.assertEqual(fibonacci(1), [0])  # Primeiro número debe ser 0
        self.assertEqual(fibonacci(2), [0, 1])  # Segundo número debe ser 1
        self.assertEqual(fibonacci(3), [0, 1, 1])  # Tercer número debe ser 1
        self.assertEqual(resultado[4], 3)  # El 4 elemento de la lista se refiere al nº que ocupa la 4a posición


if __name__ == "__main__":
    unittest.main()
