#5-7
def exchange_bit(x):
    even_digit = 0xaaaaaaaa & x 
    odd_digit = 0x55555555 & x
    return (even_digit >> 1 ) | (odd_digit << 1 )

if __name__ == "__main__":
    print(bin(exchange_bit(0b110000101010101010)))
    print(bin(exchange_bit(0b010100)))
