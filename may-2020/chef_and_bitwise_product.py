import sys
import math

def bits(x):
    return int(math.log(x)//math.log(2)) + 1

def decimal_to_binary(num):
    return bin(num)[2:]

def binary_to_decimal(num):
    return int(num, 2)

def solve(x, y, l, r):
    if l==r:
        return l
    num_bits_x = bits(x)
    num_bits_y = bits(y)
    max_bits = max(num_bits_x, num_bits_y)
    min_bits = min(num_bits_x, num_bits_y)

    max_value_max_bits = 2**max_bits
    max_value_min_bits = 2**min_bits

    if r <= l + max_value_max_bits - 1:
        r = r
    else:
        r = l + max_value_max_bits - 1
    
    if r <= l + max_value_min_bits - 1:
        return r
    else:
        """
            (r-x)%m = m-1
            x = m-1 - (r%m)
            return r - x 
        """
        return r - 1 - (r % max_value_min_bits)
    
    
    z = (1 << max_bits)
    while not ((z<=r and z>=l) or (z-1<=r and z-1>=l)):
        max_bits -= 1
        z = (1 << max_bits)
    return z

def solve1(x, y, l, r):
    bin_x = decimal_to_binary(x)
    bin_y = decimal_to_binary(y)
    bin_l = decimal_to_binary(l)
    bin_r = decimal_to_binary(r)
    max_bits_x_y = max(len(bin_x), len(bin_y))
    min_bits_x_y = min(len(bin_x), len(bin_y))
        
    # Case 1: when l has more bits than x and y    [x, y <= l <= r]
    if len(bin_l) > len(bin_x) and len(bin_l) > len(bin_x):
        extra_bits = len(bin_l) - max_bits_x_y
        z = ['0'] * len(bin_l)
        for i in range(extra_bits):
            z[i] = bin_l[i]
        print(z)
        iter_x = len(bin_x) - 1
        iter_y = len(bin_y) - 1
        
        if len(bin_l) < len(bin_r):
            for i in range(len(z)-1, extra_bits-1, -1):
                val_x = bin_x[iter_x] if iter_x >= 0 else '0'
                val_y = bin_y[iter_y] if iter_y >= 0 else '0'
                z[i] = str(int(val_x) | int(val_y))
                iter_x -= 1
                iter_y -= 1
        else:
            for i in range(len(z)-1, extra_bits-1, -1):
                val_x = int(bin_x[iter_x]) if iter_x >= 0 else 0
                val_y = int(bin_y[iter_y]) if iter_y >= 0 else 0
                val_l = int(bin_l[i])
                val_r = int(bin_r[i])
                z[i] = str((val_x | val_y) & (val_l | val_r))
                iter_x -= 1
                iter_y -= 1
        return binary_to_decimal(''.join(z))
    elif len(bin_l) <= min_bits_x_y and len(bin_r) >= max_bits_x_y:
        # Case 2: when l has less bits than x and y and r has more bits than x and y    [l <= x, y <= r]
        z = ['0'] * max_bits_x_y
        iter_x = len(bin_x) - 1
        iter_y = len(bin_y) - 1
        for i in range(len(z)-1, -1, -1):
            val_x = bin_x[iter_x] if iter_x >= 0 else '0'
            val_y = bin_y[iter_y] if iter_y >= 0 else '0'
            z[i] = str(int(val_x) | int(val_y))
            iter_x -= 1
            iter_y -= 1

        
        return binary_to_decimal(''.join(z))

    elif len(bin_l) <= min_bits_x_y and len(bin_r) < max_bits_x_y:
        # Case 3: when l has more bits than x and y    [l <= x <= r <= y] Assuming y has more bits than x
        z = ['0'] * max_bits_x_y
        return binary_to_decimal(''.join(z))
    else:
        z = ['0'] * len(bin_l)
        return binary_to_decimal(''.join(z))
    """
    000101  -> 5
    001100  -> 12

    011001  -> 25
    100010 -> 34

    max bits of all 4 -> 6 bits
    max bits between x and y is 4
    since l has 5 bits that means 5th bit will be one
    z will have 5 bits

    l > x and y so, z will have num of bits equal to l
    first bit of extra bits will be one.
    Here only 1 bit is extra that means
    1 _ _ _ _ First bit of z is final
    1 1 1 0 1 


    1010101
    1011011
          0 1 0 1
          1 1 0 0

          0 1 0 1
          1 1 0 1
    1 0 1 _ _ _ _

    x | y & r

    """


if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        x, y, l, r = map(int, f.readline().split())
        result = solve(x, y, l, r)
        print(result)
        

"""
max -> (x&z) * (y&z)
maximizing a*b

(a-b)^2 >= 0
(a+b)^2 - 4ab >= 0
ab >= (a+b)^2 / 4
(x&z) + y&z  maxmimize???



x = 6 (0110), y = 12 (1100)
max (x&z)
max (y&z)

if r >= max(x, y) ===> 2^max_bits(x, y) - 1 if this is less than r and greater than l otherwise check 2^max_bits(x, y)-1 and a number less than that
if l < x and y

l < x < y < r
l < x < r < y
l < r < x < y
x < l < y < r
x < y < l < r
x < l < r < y



"""