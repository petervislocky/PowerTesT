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

    def matrix_multiply(self, size: int) -> list[int]:
        """ Does matrix multiplication based on the size given in params
        """
        x = np.random.rand(size, size)
        y = np.random.rand(size, size)
        return np.dot(x, y)
    
    def memory_stress(self, size, duration):
        """ Creates an array of random bytes and continually makes copies of it and rewrites the new copies over the same vaiable over and over, to stress memory
        """
        arr = bytearray(size)
        start_time = time.time()

        while time.time() - start_time < duration:
            arr_copy = arr[:]
            arr[:] = arr[::-1]