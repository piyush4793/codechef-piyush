"""
Any number can be represented as a difference of squares if it is odd, or a multiple of 4. 
The problem arises when a product has only a single 2 in the prime factorisation.
"""
import sys 

def sum_n_nums(n):
    if n%2==0:
        return (n+1)*(n//2)
    return n*((n+1)//2)

def solve(n, arr):

    # 1 -> odd, 2-> 2, 4 -> 4*k (mutiple of 4)

    tracker = [None]*n
    left_odd = 0 # odd to left of two -> only to keep track of consecutive odd numbers left of two
    for i in range(n):
        if arr[i]%4==0:
            tracker[i] = [4, 0, 0]
            left_odd = 0
        elif arr[i]%2==0:
            tracker[i] = [2, left_odd, 0]
            left_odd = 0
        else:
            tracker[i] = [1, 0, 0]
            left_odd += 1 

    right_odd = 0
    for i in range(n-1, -1, -1):
        if tracker[i][0] == 4:
            right_odd = 0
        elif tracker[i][0] == 2:
            tracker[i][2] = right_odd
            right_odd = 0
        else:
            right_odd += 1
    
    total_subsequence = sum_n_nums(n)

    for i in range(n):
        if tracker[i][0] == 2:
            temp_sequence_size = tracker[i][1] + tracker[i][2] + 1
            total_subsequence -= sum_n_nums(temp_sequence_size)
            total_subsequence += sum_n_nums(tracker[i][1]) + sum_n_nums(tracker[i][2])
            
    return total_subsequence

if __name__ == "__main__":
    fi = sys.stdin
    fo = sys.stdout
    T = int(fi.readline())
    for _T in range(T):
        N = int(fi.readline())
        arr = list(map(int, fi.readline().split()))
        result = solve(N, arr)
        fo.write(str(result)+"\n")
