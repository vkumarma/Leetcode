def groupAnagrams(strs):
  hash = {}
  for elem in strs:
      count = [0] * 26
      for c in elem:
          count[ord(c)-ord("a")] += 1
      
      if hash.get(tuple(count)):
          hash[tuple(count)].append(elem)
      else:
          
          hash[tuple(count)] = [elem]
      print(hash)
          
  return list(hash.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))