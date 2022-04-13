def searchRange(nums, target):
  res = []
  if len(nums) == 0:
      return [-1,-1]
  def Binary_Search(nums,target,low,high):
      if low > high:
          return None
      mid = (low + high) // 2
      guess = nums[mid]
      if guess == target:
          return mid
      elif guess > target:
          return Binary_Search(nums,target,low,mid-1)
      else:
          return Binary_Search(nums,target,mid+1,high)
  
  index = Binary_Search(nums,target,0,len(nums)-1)
  if index == None:
      return [-1,-1]
  
  for i in range(index,-1,-1): # finding the lowest index
      if i == 0 and nums[i] == target: 
          res.append(i)
      elif nums[i] != target:
          res.append(i + 1)
          break
          
  for j in range(index,len(nums)): #finding the highest index
      if j == len(nums)-1 and nums[j] == target:
          res.append(j)
      elif nums[j] != target:
          res.append(j-1)
          break
  return res




print(searchRange([5,5,6,7,7,8,8,8],8))
print(searchRange([5,5,6,7,7,8,8,8],5))
print(searchRange([5,5,6,7,7,8,8,8],7))