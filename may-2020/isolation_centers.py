import sys

def solve(dieseases, num_people):
    # tracks how many people have S-i th diesease
    freq = {}
    # how many person can be admitted if there is 1 center, 2 centers, .. and so on
    center_to_people = [0] * (num_people + 1) # can be optimized to max freq of a diesease, improves avg case not worst case
    center_to_people[0] = 0

    for diesease in dieseases:
        freq[diesease] = freq[diesease] + 1 if diesease in freq else 1
        center_to_people[freq[diesease]] = center_to_people[freq[diesease]] + 1
    
    for idx in range(len(center_to_people)):
        if idx>1:
            center_to_people[idx] += center_to_people[idx-1]

    return center_to_people
    

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        N, Q = map(int, f.readline().strip().split())
        s = f.readline().strip()
        center_to_people = solve(s, N)
        for _Q in range(Q):
            c = int(f.readline().strip())
            if c > N:
                # No pending people in queue
                result = 0
            else:
                result = N - center_to_people[c]
            print(result)
        