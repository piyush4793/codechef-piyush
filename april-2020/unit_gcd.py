"""
No two even numbers can be in the same subset, so the minimal number of subsets is floor(n/2)
If n is even, you can easily achieve the bound with subsets {2i+1, 2i+2}. For n odd, you do the same, but put {n-2, n-1, n} in the last subset. Note that adjacent numbers are always coprime, and n,n-2 are coprime when n is odd.
"""
import sys 

def solve(n):
    
    # Special case n=1
    if n==1:
        fo.write("1\n")
        fo.write("1 1\n")
        # print(1)
        # print(1, 1)
        return
    
    half = n//2    
    # print(half)
    fo.write(str(half)+"\n")
    for i in range(half-1):
        # print(2, 2*i+1, 2*i+2)
        fo.write("2 {} {}\n".format(2*i+1, 2*i+2))

    if n%2==0:
        # print(2, n-1, n)
        fo.write("2 {} {}\n".format(n-1, n))
    else:
        # print(3, n-2, n-1, n)
        fo.write("3 {} {} {}\n".format(n-2, n-1, n))

if __name__ == "__main__":
    fi = sys.stdin
    fo = sys.stdout
    T = int(fi.readline().strip())
    # import time
    # start =  time.time()
    for _T in range(T):
        N = int(fi.readline().strip())
        solve(N)
    # print(time.time()-start)

# 57.434070110321045
