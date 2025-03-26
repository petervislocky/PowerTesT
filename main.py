import time
import multiprocessing
from components.algos import Algorithms

def fibonacci_stress_test(n):
    stress = Algorithms()
    start = time.time()
    workers = multiprocessing.cpu_count()
    print('Starting stress test with fibonacci sequence...')
    with multiprocessing.Pool(processes=workers) as pool:
        for i in range(n + 1):
            # okay this is cool, when i originally tried to print(F({i})) it printed 38 every time because the lambda was just referencing the i variable and wasn't
            # capturing the value during every iteration of the loop, but when you set a param as i = i it captures the actual value, every iteration
            # also this uses multiprocessing.Pool to use all cpu cores to calculate the function each to stress the processor more, and async allows me to get live
            # results so I can print each fibonacci number as it is calculated rather than a list of results at the end which happens with pool.map()
            pool.apply_async(stress.fib, args=(i,), callback=lambda result, i = i: print(f'F({i}) = {result}'))
        pool.close()
        pool.join()
    end = time.time()
    print(f'Time to complete: {end - start:.4f} seconds')

def main():
    print('Stress Test\nExecutes algorithm across all cores to evenly stress processor')
    num = input('Choose how hard to stress the processor\n'
                '1 = Low F(30)\n'
                '2 = Mid F(39)\n'
                '3 = High F(45)\n'
                '4 = Extreme F(52) *WARNING* This option WILL take a long time\n')
    match num:
        case '1':
            fibonacci_stress_test(30)
        case '2':
            fibonacci_stress_test(39)
        case '3':
            fibonacci_stress_test(45)
        case '4':
            fibonacci_stress_test(52)
        case _:
            print('Invalid selection try again')

if __name__ == '__main__':
    main()