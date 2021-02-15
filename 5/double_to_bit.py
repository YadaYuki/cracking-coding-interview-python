#5-2
def double_to_bit(d):
    s = ""
    while d != 0:
        if len(s) >= 32:
            return "ERROR"
        if d < 1:
            s += "0"
        else:
            s += "1"
            d -= 1
        d *= 2
    
    return s[0] + "." + s[1:]

if __name__ == "__main__":
    print(double_to_bit(0.625))
    print(double_to_bit(0.5 + 0.03125))

