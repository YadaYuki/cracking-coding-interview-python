def is_substring(s1,s2):
    return s1 in s2 or s2 in s1

def is_rotate_str(s1:str,s2:str) -> bool:
    if len(s1) != len(s2):
        return False
    return is_substring(s1*2,s2)

if __name__ == "__main__":
    print(is_rotate_str("waterbottle","erbottlewat"))
