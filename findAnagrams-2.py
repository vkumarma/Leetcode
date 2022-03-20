def findAnagrams(self, s: str, p: str) -> List[int]:
  p_hash = {}
  s_hash = {}
  lis = []
  if len(p) > len(s):
      return lis
  
  for i in range(len(p)):
      p_hash[p[i]] = 1 + p_hash.get(p[i],0)
      s_hash[s[i]] = 1 + s_hash.get(s[i],0)
      
  if p_hash == s_hash:
      lis.append(0)
  
  l = 0 # left pointer
  for i in range(len(p), len(s)):
      s_hash[s[i]] = 1 + s_hash.get(s[i],0)
      s_hash[s[l]] -= 1
      
      if s_hash[s[l]] == 0:
          s_hash.pop(s[l])
      
      l += 1
      if s_hash == p_hash:
          lis.append(l)
  return lis

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".