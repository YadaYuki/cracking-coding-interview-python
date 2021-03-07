def magic_index_recursion(arr,head,tail):
  if head > tail:
    return -1
  
  mid = int((head + tail)/2)

  if arr[mid] == mid:
    return mid
  elif arr[mid] > mid:
    return magic_index_recursion(arr,head=head,tail=mid-1)
  elif arr[mid] < mid:
    return magic_index_recursion(arr,head=mid+1,tail=tail)

  return []

def magic_index(arr):
  return magic_index_recursion(arr,head=0,tail=len(arr)-1)

if __name__ == "__main__":
  print(magic_index([-1,1,21,24,42,45])) # 1
  print(magic_index([-1,0,1,2,4,45])) # 4
  print(magic_index([-1,0,1,2,42,45])) # -1


