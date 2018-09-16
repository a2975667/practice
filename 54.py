class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        if len(matrix) == 1:
            return matrix[0]
        
        col=0
        row=0
        limit_row = len(matrix)-1
        limit_col = len(matrix[0])-1
        
        result = []
        
        while col <= limit_col and row <= limit_row:
            for i in range(col, limit_col+1):
                result.append(matrix[row][i])
                #print('1: ', row, i)
            row += 1
            
            for i in range(row, limit_row+1):
                result.append(matrix[i][limit_col])
                #print('2: ', i, limit_col)
            limit_col -= 1
            
            if row <= limit_row:
                for i in range(col, limit_col+1)[::-1]:
                    result.append(matrix[limit_row][i])
                    #print('3: ', limit_row, i)
                limit_row -= 1
            
            if col <= limit_col:
                for i in range(row, limit_row+1)[::-1]:
                    result.append(matrix[i][col])
                    #print('4: ', i, col)
                col += 1
            
        return result