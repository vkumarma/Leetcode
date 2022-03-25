def twoSum(nums, target):
  l = []
  h = {}
  duplicates = []
  if len(nums) == 2:
      if nums[0] + nums[1] == target:
          l.append(0)
          l.append(1)
      return l
      
  for i in range(len(nums)):
      h[nums[i]] = True
  
  for i in range(len(nums)):
      temp = target - nums[i]
      
      if h.get(temp):
          if temp != nums[i]:
              l.append(i)
          else:
              duplicates.append(i)
              if len(duplicates) > 1:
                  return duplicates
  return l


print(twoSum(nums = [2,7,11,15], target = 9))