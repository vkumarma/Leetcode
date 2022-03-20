def countAndSay(n):
  def count(n):
      c = 0
      compressed_string = ""
      if n == 1:
          return "1"
      else:
          s_str = count(n-1)
          for i in range(0, len(s_str)):
              c += 1
              if i + 1 >= len(s_str) or s_str[i] != s_str[i+1]:
                  compressed_string += str(c) + s_str[i]
                  c = 0
      return compressed_string
  return count(n)

print(countAndSay(12))
