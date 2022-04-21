def topKFrequent(nums, k):
  import heapq
  freq_table = {}
  res = []
  heap = []
  heapq.heapify(heap)
  for n in nums:
      freq_table[n] = 1 + freq_table.get(n,0)
  
  for key in freq_table:
      heapq.heappush(heap,(freq_table[key] * -1,key))  # * -1 to use min heap as max heap
  
  while k != 0:
      temp = heapq.heappop(heap)
      res.append(temp[1])
      k -= 1
  
  return res


print(topKFrequent([1,1,1,1,2,2,6,6,3,4,4,5,5,5],2)) # [1,5]