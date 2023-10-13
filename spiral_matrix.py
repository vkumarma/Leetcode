class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows*cols
        col_in, row_in = 0,0
        temp = 0
        output = []
        index = 0
        while index < size:
            for j in range(col_in,cols):
                output.append(matrix[row_in][j])
                index += 1
                
            col_in = j
            for i in range(row_in+1,rows):
                output.append(matrix[i][col_in])
                index += 1

            if index >= size:
                break
                
            row_in = i
            for k in range(temp,cols-1):
                col_in -= 1
                output.append(matrix[row_in][col_in])
                index += 1

            cols -= 1
            rows -= 1
            for k in range(temp,rows-1):
                row_in -= 1
                output.append(matrix[row_in][col_in])
                index += 1


            col_in += 1
            temp += 1
        
        return output
       
