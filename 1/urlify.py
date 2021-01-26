def urlify(s:str,n:int) -> str:
    s_urlify = list(s).copy()
    space_num = s[:n].count(" ")
    idx = n + space_num * 2 - 1# NOTE: " " WILL BE REPLACE TO "%20" ... + (2 * space_num) length
    for i in range(n-1,-1,-1):
        if s[i] == " ":
            s_urlify[idx] = "0"
            s_urlify[idx-1] = "2"
            s_urlify[idx-2] = "%"
            idx -= 3
        else:
            s_urlify[idx] = s[i] 
            idx -= 1

    return "".join(s_urlify) 
if __name__=="__main__":
    print(urlify("Mr John Smith      ",13))