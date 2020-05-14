import sys
import math

def total_prime_factors(n):
    total_num_factors = 0
    
    while not n % 2:
        total_num_factors += 1
        n //= 2

    i = 3
    for i in range(3, int(math.sqrt(n)+1)):
        while not n % i:
            total_num_factors += 1
            n //= i
        i += 2
    
    if (n > 2):
        total_num_factors += 1

    return total_num_factors

def solve(X, K):
    if (total_prime_factors(X) >= K):
        return 1
    else:
        return 0

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        X, K = map(int, f.readline().split())

        result = solve(X, K)
        print(result)
        