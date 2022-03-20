def romanToInt(s):
  number = 0
  symbols = {
      "I" : 1,
      "V" : 5,
      "X" : 10,
      "L" : 50,
      "C" : 100,
      "D" : 500,
      "M" : 1000,
  }            
  largest = int(symbols[s[0]])
  for letter in s:
      value = int(symbols[letter])
      if value <= largest:
          largest = symbols[letter]
          number += symbols[letter]
      elif symbols[letter] > largest:
          temp = symbols[letter] - (2 * largest)
          number += temp
          largest = symbols[letter]
  return number


print(romanToInt("MCMXCIV"))