def deep_reverse(arr):
  res = []
  if len(arr) <= 1:
    res += arr
    return res
    
  for i in range(len(arr)-1,-1,-1):
    if type(arr[i]) == int:
      res.append(arr[i])
    else:
      res.append(deep_reverse(arr[i]))

  return res

print(deep_reverse([1,2,[3,4,5,[1,2,3]]]))

