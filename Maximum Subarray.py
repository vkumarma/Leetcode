def maxSubArray(nums):
  max_sum = nums[0]
  current_sum = nums[0]
  for elem in nums[1:]:
      current_sum = max(current_sum + elem,elem)
      max_sum = max(current_sum,max_sum)
  
  return max_sum