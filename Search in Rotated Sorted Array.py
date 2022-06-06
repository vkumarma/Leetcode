def search(arr,target):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    guess = arr[mid]

    if guess == target:
      return mid
      
    elif (target < arr[low] and guess >= arr[low]):
      low = mid + 1

    elif (target > arr[high] and guess <= arr[high]):
      high = mid - 1
      
    elif guess > target:
      high = mid - 1

    else: # guess < target
      low = mid + 1

  return -1
print(search([3,4,5,6,7,0,1,2],7))
  