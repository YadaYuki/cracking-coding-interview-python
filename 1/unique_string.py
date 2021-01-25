def is_unique(s: str) -> bool:
    if len(s) > 26:
        return False
    unique_char_map = {}
    for c in s:
        if unique_char_map.get(c):
            return False
        else :
            unique_char_map[c] = True
    return True

if __name__ == "__main__":
    print(is_unique("aaa")) # False
    print(is_unique("abc")) # True
    print(is_unique("abcdefghijklmnopqrstuvwxyz")) # True
    print(is_unique("abcdefghijklmnopqrstuvwxyza")) # False
