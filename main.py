import time
import multiprocessing
from components.algos import Algorithms

def fibonacci_benchmark(n: int) -> None:
    """ Just a helper method to keep the main method clean, does the actual calling of the fibonacci method and handles
    spreading the workload across all cores
    """
    stress = Algorithms()
    start = time.time()
    workers = multiprocessing.cpu_count()
    print('Starting benchmark with fibonacci sequence...')
    with multiprocessing.Pool(processes=workers) as pool:
        for i in range(n + 1):
            """ okay this is cool, when i originally tried to print(F({i})) it printed 38 every time because the lambda was just referencing the i variable and wasn't
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
            print('========Benchmark========\nThis calculates all numbers in the Fibonacci sequence up to the selected value\nUse to benchmark processor speed')
            while True:
                num = input('Select how high in the Fibonacci sequence to calculate up to\n'
                            '1 = Low F(30)\n'
                            '2 = Mid F(39)\n'
                            '3 = High F(45)\n'
                            '4 = Extreme F(52) *WARNING* This option WILL take a long time\n')
                match num:
                    case '1':
                        fibonacci_benchmark(30)
                        break
                    case '2':
                        fibonacci_benchmark(39)
                        break
                    case '3':
                        fibonacci_benchmark(45)
                        break
                    case '4':
                        fibonacci_benchmark(52)
                        break
                    case _:
                        print('Invalid selection, try again')
                        continue
        case _:
            print('Invalid selection, try again')

if __name__ == '__main__':
    main()