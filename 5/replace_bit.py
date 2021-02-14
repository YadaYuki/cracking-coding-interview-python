#5-1
def replace_bit(N,M,i,j):
    return bin(N + M * (2**i))

if __name__ == "__main__":
    N,M = 0b10000000000,0b10011
    i,j = 2,6
    print("Before replace:{}".format(bin(N)))
    print("After  replace:{}".format(replace_bit(N,M,i,j)))