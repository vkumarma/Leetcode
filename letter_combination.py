def letterCombinations(digits):
  h_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv",9:"wxyz"}
  num = digits
  l = []
  index = 0
  sub = ""
  def combination(num, index, l , sub):
      if index >= len(num):
          return l

      else:
          s = h_map[int(num[index])]
          old_sub = sub
          for i in range(0, len(s)):
              sub += s[i]
              sub_l = combination(num, index+1,l,sub)
              if len(sub) == len(num):
                  if sub not in sub_l:
                      sub_l.append(sub)
              sub = old_sub

      return l

  return combination(num,index,l,sub)

print(letterCombinations("2379"))

