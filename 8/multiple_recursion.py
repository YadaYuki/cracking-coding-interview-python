def multiple_recursion(bigger,smaller,memo):
  if smaller == 0:
    return 0
  elif smaller == 1:
    return bigger
  elif memo[smaller] != 0:
    return memo[smaller]
  
  s = int(smaller/2)
  s1 = multiple_recursion(bigger,s,memo)
  s2 = 0
  if smaller % 2 == 1:
    s2 = multiple_recursion(bigger,s+1,memo)
  else :
    s2 = multiple_recursion(bigger,s,memo)
  
  memo[smaller] = s1 + s2
  
  return s1 + s2




def multiple(a:int,b:int):
  bigger = max(a,b)
  smaller = min(a,b)
  memo = [0 for _ in range(smaller+1)]
  return multiple_recursion(bigger,smaller,memo)

if __name__ == "__main__":
  print(multiple(4,4))