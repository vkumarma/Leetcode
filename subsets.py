def subsets(nums):
   l = []
   index = 0
   def find_subsets(nums,index,l):
      if index >= len(nums):
          l.append([])
          return l
        
      res = find_subsets(nums, index+1,l)[:]
      for elem in res:
          new_l = [nums[index]] + elem[:]
          l.append(new_l)
        
      return l
   return find_subsets(nums,index,l)

print(subsets([1,2,3]))