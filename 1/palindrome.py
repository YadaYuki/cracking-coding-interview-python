def is_palindrome(s:str) -> bool:
    # To Lower Case
    s = s.replace(" ","").lower()
    char_map = {}
    for c in s:
        if char_map.get(c) == None:
            char_map[c] = 1
        else :
            char_map[c] += 1
    odd_num_count = 0
    for c in char_map:
        if char_map[c] % 2 == 1:
            odd_num_count += 1
        if odd_num_count >= 2:
            return False
    return True

if __name__ == "__main__":
    print(is_palindrome("HOGE gOH")) # TRUE