import sys

MOD = 1000000007

def solve(arr, n):

    profit = 0
    for i in range(n-1, -1, -1):
        deprecated_price = arr[i] - (n-1-i)
        if deprecated_price < 0:
            deprecated_price = 0
        profit = (profit + deprecated_price) % MOD
    
    return profit

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        N = int(f.readline())
        arr = list(map(int, f.readline().split()))

        # O(nlogn)
        arr.sort()
        result = solve(arr, N)
        print(result)
        