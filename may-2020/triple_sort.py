"""

7 2 1 8 3 6 4 5

correct place = 2
incorrect = 6
fix 2 at a time till 4 is left, then fix one at time, then all three at once

0 6 3

8 2 1 4 3 6 7 5
correct place = 4
incorrect = 4

1, 2, 3
largest, smallest, middle

8 1 3 5
3 8 1

7 2 1 8 3 6 4 5
0 6 2 (find index of 1, linear search)
1 2 4 8 3 6 7 5
2 3 4
1 2 3 4 8 6 7 5


7 2 1 8 3 6 4 5
3 7 4
7 2 1 3 5 6 4 8
7 3 2

7 2 1 8 3 6 4 5
0 6 3
8 2 1 4 3 6 7 5

3 2 1 4 5 6 7 8

5 4 3 2 1
4 incorrect
4 1 3 2 5
1 2 3 4 5

5 2 3 4 1

3 2 1 ?

2 3 1
1 0 2
1 2 3


"""

import sys

def is_cyclic(arr, idx):
    temp = arr[idx] - 1
    count = 1
    while temp < len(arr) and temp >= 0 and temp != idx and count != 2:
        temp = arr[temp] - 1
        count += 1

    if temp == idx:
        return True
    else:
        return False

def swap(incorrect_map, arr, idx0, idx1, idx2):
    temp = arr[idx0]
    arr[idx0] = arr[idx2]
    arr[idx2] = arr[idx1]
    arr[idx1] = temp

    if arr[idx0] == idx0 + 1 and idx0 in incorrect_map:
        incorrect_map.pop(idx0)
    if arr[idx1] == idx1 + 1 and idx1 in incorrect_map:
        incorrect_map.pop(idx1)
    if arr[idx2] == idx2 + 1 and idx2 in incorrect_map:
        incorrect_map.pop(idx2)

    return arr

def get_index_when_cyclic(incorrect_map, idx0, idx1):
    for i in incorrect_map.keys():
        if i == idx0 or i == idx1:
            continue
        incorrect_map.pop(i)
        return i
    return -1

def solve(arr, n, k):
    steps = []
    idx = 0
    incorrect_map = {}

    for i, _ in enumerate(arr):
        if arr[i] != i + 1:
            incorrect_map[i] = i

    if len(incorrect_map) == 0:
        fo.write(str(0)+"\n")
        return
    
    while idx < n:
        if arr[idx] != idx + 1:
            if is_cyclic(arr, idx):
                idx0 = idx 
                idx1 = arr[idx] - 1
                idx2 = get_index_when_cyclic(incorrect_map, idx0, idx1)
                if idx2 == -1:
                    steps = []
                    break

                steps.append([idx0+1, idx1+1, idx2+1])
                arr = swap(incorrect_map, arr, idx0, idx1, idx2)
            else:
                steps.append([idx+1, arr[idx], arr[arr[idx] - 1]])
                arr = swap(incorrect_map, arr, idx, arr[idx] - 1, arr[arr[idx] - 1] - 1)
        else:
            idx += 1

    if len(steps) == 0 or len(steps) > K:
        fo.write(str(-1)+"\n")
    else:
        fo.write(str(len(steps))+"\n")
        for step in steps:
            fo.write(str(step[0])+" "+str(step[1])+" "+str(step[2])+"\n")

if __name__ == "__main__":
    f = sys.stdin
    fo = sys.stdout
    T = int(f.readline())
    for _T in range(T):
        N, K = map(int, f.readline().strip().split())
        arr = list(map(int, f.readline().strip().split()))
        solve(arr, N, K)
        