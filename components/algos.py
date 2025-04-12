import numpy as np
import time

class Algorithms:

    
    def __init__(self):
        pass

    def fib(self, n: int) -> int:
        """ Fibonacci number generator
        """
        if n <= 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    # replace this with a better algo
    def matrix_multiply(self, size: int) -> list[int]:
        """ Does matrix multiplication based on the size given in params
        """
        x = np.random.rand(size, size)
        y = np.random.rand(size, size)
        return np.dot(x, y)
    
