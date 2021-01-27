
ALPHABET_NUM = 26
A_CODE = ord("a")

def is_anagram(s1:str,s2:str) -> bool:
    if len(s1) is not len(s2):
        return False
    c1_arr,c2_arr = [0 for i in range(ALPHABET_NUM)],[0 for i in range(ALPHABET_NUM)]
    n = len(s1) 
    for i in range(n):
        c1_arr[ord(s1[i]) - A_CODE] += 1
        c2_arr[ord(s2[i]) - A_CODE] += 1
    for i in range(n):
        if c1_arr[i] != c2_arr[i]:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("abc","cba")) # True
    print(is_anagram("abc","bbbaa")) # False
    print(is_anagram("sdfasdfa","asdfasdf")) # True
