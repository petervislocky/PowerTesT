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
                        '2 CPU stress test\n>> ')
    
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
                            '4 = Extreme F(52) *WARNING* This option WILL take a long time\n>> ')
                
                if num in fib_options:
                    fibonacci_benchmark(fib_options[num])
                    break
                else:
                    print('Invalid selection, try again')
                    continue

        case '2':
            print('========================CPU Stress Test========================\n'
                  'This test runs a low-level algorithm written in C to maximize CPU usage on either single or multiple cores')

            while True:
                mode = input('Select mode:\n1 = Stress single core\n2 = Stress all cores\n>> ')
                if mode in ['1', '2']:
                    break
                else:
                    print(f'Invalid selection, "{mode}". Valid options are 1 or 2')

            while True:
                try:
                    duration = int(input('Enter time (in seconds) to stress test for >> '))
                    break
                except ValueError:
                    print(f'Not a valid value, "{duration}". Try again')
                
            is_all_cores = mode == '2'
            core_count = get_core_count() if is_all_cores else 1
            # right now only linux binary is compiled and supported
            binary_path = './c/stress_core'

            print(f'Starting stress test on {'all' if is_all_cores else 'single'} core(s) for {duration} seconds...')
            processes = start_stress_test(binary_path, core_count)

            try:
                time.sleep(duration)
                print(f'\n{duration} second stress test complete!')
            except KeyboardInterrupt:
                print('\nKeyboard interrupt detected. Aborting stress test.')

            stop_stress_test(processes)

        case _:
            print('Invalid selection, try again')

if __name__ == '__main__':
    main()
