import sys

if __name__ == "__main__":
    f = sys.stdin
    fo = sys.stdout
    n = int(f.readline().strip())
    while(n != 42):
        fo.write(str(n)+"\n")
        n = int(f.readline().strip())
        