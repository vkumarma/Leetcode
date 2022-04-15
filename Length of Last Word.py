def lengthOfLastWord(s):
  s_list = s.split()
  if len(s_list) > 0:
      last_word_length = len(s_list[len(s_list) - 1])
  else:
      last_word_length = 0 
  return last_word_length


print(lengthOfLastWord("Hello World"))
