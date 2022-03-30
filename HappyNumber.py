def isHappy(n):
  hashtable = {}
  should_continue = True
  while should_continue:
      sum = 0
      for char in str(n):
          sum += (int(char) ** 2)
      hashtable[str(n)] = sum
      if hashtable[str(n)] == 1:
          should_continue = False
          return True
      else:
          n = hashtable[str(n)]
          if hashtable.get(str(n)):
              should_continue = False
              return False