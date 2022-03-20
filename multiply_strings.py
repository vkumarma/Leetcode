def multiply(num1,num2):
  num_1 = 0
  num_a = num1[::-1]
  num_2 = 0
  num_b = num2[::-1]
  product = 0
  for i in range(0,len(num_a)):
      a = i
      n = ((ord(num_a[i]) % 48) * (10 ** a))
      num_1 += n
      
  for i in range(0,len(num_b)):
      b = i
      n = ((ord(num_b[i]) % 48) * (10 ** b))
      num_2 += n
      
      
  product = num_1 * num_2
  return str(product)

print(multiply(num1 = "123", num2 = "456"))