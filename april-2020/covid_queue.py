import sys

def solve(arr, n):
    prev_one = -1
    for i in range(n):
        if prev_one == -1 and arr[i] == 1:
            prev_one = i
        elif arr[i] == 1:
            diff = i - prev_one
            prev_one = i
            if diff < 6:
                return 'NO'
    
    return 'YES'

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        N = int(f.readline())
        arr = list(map(int, f.readline().split()))

        result = solve(arr, N)
        print(result)
        