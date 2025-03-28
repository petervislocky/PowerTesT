import numpy as np
import multiprocessing


class Algorithms:

    def __init__(self):
        pass

    def fib(self, n: int) -> int:
        """ Fibonacci number generator
        """
        if n <= 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def matrix_multiply(self, size: int) -> list[int]:
        x = np.random.rand(size, size)
        y = np.rangom.rand(size, size)
        return np.dot(x, y)