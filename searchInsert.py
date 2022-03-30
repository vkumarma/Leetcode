def searchInsert(nums, target):
  low = 0
  high = len(nums) - 1
  value = 0
  while low <= high:
      mid = int((low+high)/2)
      guess = nums[mid]
      if guess == target:
          return mid
      if guess > target:
          high = mid - 1
      else:
          low = mid + 1
          value = low
  return value