import numpy as np
import multiprocessing
import time

def prime_factors(n):
    i = 2
    factors = 0
    while i * i <= abs(n):
        if n % i:
            i += 1
        else:
            n //= i
            factors += 1
    if n > 1:
        factors += 1
    return factors

def factorize_parallel(data):
    total_factors = 0
    for number in data:
        total_factors += prime_factors(number)
    return total_factors

def main():
    starttime = time.time()
    with open('random_numbers_5000.txt', 'r') as f:
        num_list = [int(line.strip()) for line in f]

    data_split = np.array_split(np.array(num_list), 4)

    with multiprocessing.Pool(4) as pool:
        res = pool.map(factorize_parallel, data_split)

    print(np.sum(res))
    endtime = time.time()
    print(f'time:{endtime-starttime}')

if __name__ == '__main__':
    main()