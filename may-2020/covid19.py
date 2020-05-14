import sys

def solve(arr, n):
    arr.sort()
    min_possible_infections = sys.maxsize
    max_possible_infections = 0
    count_left = [0]*n
    count_right = [0]*n
    
    for i in range(1, n):
        if arr[i] - arr[i-1] <= 2:
            count_left[i] = count_left[i-1] + 1
        else:
            count_left[i] = 0
    
    for j in range(n-2, -1, -1):
        if arr[j+1] - arr[j] <= 2:
            count_right[j] = count_right[j+1] + 1
        else:
            count_right[j] = 0
    
    for i in range(n):
        temp_sum = count_left[i] + count_right[i] + 1
        if min_possible_infections > temp_sum:
            min_possible_infections = temp_sum
        if max_possible_infections < temp_sum:
            max_possible_infections = temp_sum
    
    return min_possible_infections, max_possible_infections

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        N = int(f.readline())
        arr = list(map(int, f.readline().split()))

        min_possible_infections, max_possible_infections = solve(arr, N)
        print(min_possible_infections, max_possible_infections)
        