def rotate(matrix):
  """
  Do not return anything, modify matrix in-place instead.
  """
  for i in range(len(matrix) // 2):
      temp = matrix[i]
      matrix[i] = matrix[len(matrix)-(i+1)]
      matrix[len(matrix)-(i+1)] = temp
  
  
  for j in range(0, len(matrix)-1):
      for k in range(1+j,len(matrix)):
          matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]
