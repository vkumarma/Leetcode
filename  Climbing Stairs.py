def climbStairs(n):
  d = {1:1,2:2}
  def caching(n,d):
      if d.get(n):
          return d[n]
      else:
          if d.get(n-1):
              temp1 = d[n-1]
          else:
              temp1 = caching(n-1,d)

          if d.get(n-2):
              temp2 = d[n-2]
          else:
              temp2 = caching(n-2,d)

      d[n] = temp1+temp2
      return d[n]
  return caching(n,d)

print(climbStairs(5))