import concurrent.futures
import multiprocessing
import time


def factorize_sync(*numbers):
    results = []
    for number in numbers:
        denominators = []
        for i in range(1, number + 1):
            if not number % i:
                denominators.append(i)
        results.append(denominators)
    return results

def factorizor(number):
    denominators = []
    for i in range(1, number + 1):
        if not number % i:
            denominators.append(i)
    return denominators

def factorize_async(*numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(factorizor, numbers)
    return results


if __name__ == '__main__':
    start_time_sync = time.time()
    numbers = [128, 255, 99999, 10651060]
    results_sync = factorize_sync(*numbers)
    end_time_sync = time.time()
    start_time_async = time.time()
    results_async = factorize_async(*numbers)
    # a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    end_time_async = time.time()
    print("Result_sync:", results_sync)
    print("Result_async:", results_async)
    print("Time taken sync:", end_time_sync - start_time_sync, "seconds")
    print("Time taken async:", end_time_async - start_time_async, "seconds")





