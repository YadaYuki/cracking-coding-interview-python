def compress(s:str) -> str:
    compressed = ""
    n = len(s)
    same_letter_count = 0
    for i in range(n):
        if i == n - 1:
            compressed += s[i] + str(same_letter_count+1)
            break
        if s[i] != s[i+1]:
            compressed += s[i] + str(same_letter_count+1)
            same_letter_count = 0
        else :
            same_letter_count += 1
    return compressed if n > len(compressed) else s

if __name__ == "__main__":
    print(compress("aabcccccaaa")) # a2b1c5a3
    print(compress("abcdef")) # abcdef
