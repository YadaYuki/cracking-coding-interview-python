def is_insert_one_letter(sl:str,ss:str) -> bool: # len(sl) > len(ss)
    nl,ns = len(sl),len(ss)
    if (ns+1) is not nl:
        return False 
    for i in range(nl):
        if sl[0:i] + sl[i+1:nl] == ss:
            return True
    return False

def is_change_one_letter(s1:str,s2:str) -> bool:
    if len(s1) != len(s2):
        return False
    n = len(s1)
    diff_letter_num = 0
    for i in range(n):
        if s1[i] != s2[i]:
            diff_letter_num += 1
        if diff_letter_num >= 2:
            return False
    return True

def is_transform_one_operation(s1:str,s2:str) -> bool:
    n1,n2 = len(s1),len(s2)
    if  n1 == n2:
        return is_change_one_letter(s1,s2)
    if  n1 + 1 == n2:
        return is_insert_one_letter(s2,s1)
    if n1 == n2 + 1:
        return is_insert_one_letter(s1,s2)
    return False

if __name__ == "__main__":
    print(is_transform_one_operation("pale","ple")) # True
    print(is_transform_one_operation("pales","pale")) # True
    print(is_transform_one_operation("pale","bale")) # True
    print(is_transform_one_operation("pales","bake")) # False