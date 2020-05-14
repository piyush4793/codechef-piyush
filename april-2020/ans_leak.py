import sys 

if __name__ == "__main__":
    fi = sys.stdin
    fo = sys.stdout
    T = int(fi.readline().strip())
    for _T in range(T):
        n, m, k = map(int, fi.readline().strip().split())

        arr = list(map(int, fi.readline().split()))
        mst=[]
        for j in range(n):
            a=list(map(int, fi.readline().split()))
            mst.append(a)
        c=1
        for j in range(n):
            fo.write(c+' ')
            c+=1
            if(c>m):
                c=1
        fo.write("\n")
