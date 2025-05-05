import time
import multiprocessing
from components.algos import Algorithms
from components.c_stress_runner import get_core_count, start_stress_test, stop_stress_test 

def fibonacci_benchmark(n: int) -> None:
    """ Just a helper method to keep the main method clean, does the actual calling of the fibonacci method and handles
    spreading the workload across all cores
    """
    
    stress = Algorithms()
    workers = multiprocessing.cpu_count()
    print('Starting benchmark with fibonacci sequence...')
    start = time.time()
    
    with multiprocessing.Pool(processes=workers) as pool:
        for i in range(n + 1):
            """ okay this is cool, when i originally tried to print(F({i})) it printed 39 every time because the lambda was just referencing the i variable and wasn't
            capturing the value during every iteration of the loop, but when you set a param as i = i it captures the actual value, every iteration
            also this uses multiprocessing.Pool to use all cpu cores to calculate the function each to stress the processor more, and async allows me to get live
            results so I can print each fibonacci number as it is calculated rather than a list of results at the end which happens with pool.map()
            """
            pool.apply_async(stress.fib, args=(i,), callback=lambda result, i = i: print(f'F({i}) = {result}'))
        pool.close()
        pool.join()
    
    end = time.time()
    print(f'Time to complete: {end - start:.4f} seconds')

def main():
    print('========================PowerTesT========================')
    test_select = input('Choose a test to run\n'
                        '1 CPU speed benchmark\n'
                        '2 CPU stress test\n')
    
    match test_select:
        case '1':
            fib_options = {'1': 30, '2': 39, '3': 45, '4': 52}
            print('========================CPU Benchmark========================\n'
                  'This calculates all numbers in the Fibonacci sequence up to the selected value\n'
                  'Use to benchmark processor speed')
            
            while True:
                num = input('Select how high in the Fibonacci sequence to calculate up to\n'
                            '1 = Low F(30)\n'
                            '2 = Mid F(39)\n'
                            '3 = High F(45)\n'
                            '4 = Extreme F(52) *WARNING* This option WILL take a long time\n')
                
                if num in fib_options:
                    fibonacci_benchmark(fib_options[num])
                    break
                else:
                    print('Invalid selection, try again')
                    continue

        case '2':
            print('========================CPU Stress Test========================\n'
                  'This test is running matrix multiplication which stresses the FPU/ALUs within the processor as well as stressing memory bandwidth')
            stress = Algorithms()
            size = 5000
            workers = multiprocessing.cpu_count()
            
            while True:
                try:
                    duration = int(input('Enter time (in seconds) to stress test for >> '))
                    break
                except ValueError as e:
                    print('Not a valid value')
                    continue

            start_time = time.time()
            
            try:
                with multiprocessing.Pool(processes=workers) as pool:
                    while time.time() - start_time < duration:
                        pool.apply_async(stress.matrix_multiply, [size] * workers) # used pool.apply_async instead of pool.map to fix running longer than duration issue
                
                print(f'{duration} second stress test complete!')
            
            except KeyboardInterrupt as e:
                print('Keyboard interrupt detected, aborting stress test')
        
        case _:
            print('Invalid selection, try again')

if __name__ == '__main__':
    main()
