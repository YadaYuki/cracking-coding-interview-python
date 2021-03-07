def permutation_string(string):
  if string == "":
    return [""]
  
  char = string[0]
  remainder = string[1:]
  remainder_permutaion_arr = permutation_string(remainder)
  permutation_arr = []
  for remainder_permutaion in remainder_permutaion_arr:
    for i in range(0,len(remainder)+1):
      permutation_arr.append(insert_char_to_string(remainder_permutaion,char,i))
  
  return permutation_arr

def insert_char_to_string(string,char,idx):
  head = string[0:idx]
  tail = string[idx:len(string)]
  return head + char + tail


if __name__ == "__main__":
  print(permutation_string("abcdefg"))
