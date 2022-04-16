def combinationSum(candidates, target):
  total = 0
  res = []
  l = []
  index = 0
  def backtrack(total,l,candidates,index):
      old_t = total
      for i in range(index,len(candidates)):
          if total < target:
              total += candidates[i]
              l.append(candidates[i])
              if total == target:
                  res.append(l[:])
              backtrack(total,l,candidates,i)
              l.pop()
              total = old_t
          else:
              return 
          
  backtrack(total,l,candidates,index)
  return res


print(combinationSum([2,3,6,7], 11))