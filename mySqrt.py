def mySqrt(n):
  low = 0
  high = n
  while low <= high:
    mid = (low + high) // 2
    temp = mid * mid
    if temp < n:
        low = mid + 1

    elif temp > n:
        high = mid - 1

    else:
        return mid
  return high

print(mySqrt(8))