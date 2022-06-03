import numpy as np
example_matrix = np.array([[3,4,-1,1,0,0],
                 [1,0,3,0,1,0],
                 [2,5,-4,0,0,1]],dtype=float)


def get_zeros(matrix):
    
    for row in range(len(matrix)):
        if np.sum(matrix[row]) == 0:
            return row
    return -1
        
def get_nonzero_element(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return -1
def multiply_by_scalar(row,scalar):
    for i in range(len(row)):
        row[i] = row[i] * scalar
    return row

def row_addition_by_scalar(row1,row2,scalar):
    return_row = []
    for i in range(len(row1)):
        return_row.append(row1[i] + row2[i] * scalar )
    return np.array(return_row,dtype=float)
def echelon(matrix):
    zeros = get_zeros(matrix)
    if zeros != -1:
        zeros_row = matrix[zeros].copy()
        matrix[zeros] =  matrix[-1]
        matrix[-1] = zeros_row
        
        
    for i in range(len(matrix)-1):
        nonzero = get_nonzero_element(matrix[i])
        
        matrix[i] = multiply_by_scalar(matrix[i],1/matrix[i][nonzero])
        for j in range(i+1,len(matrix)):
            nonzero = get_nonzero_element(matrix[j])
            matrix[j] = row_addition_by_scalar(matrix[j],matrix[i],-matrix[j][nonzero])
            
    nonzero = get_nonzero_element(matrix[-1])
    if nonzero != -1:
        matrix[-1] = multiply_by_scalar(matrix[-1],1/matrix[-1][nonzero])
        
    return matrix
    
def rank(matrix):
    echelon_form = echelon(matrix)
    count = 0
    for row in echelon_form:
        for col in row:
            if col == 1:
                count += 1
                break
    return count

def reduced_echelon(matrix):
    echelon_form = echelon(matrix)

print(echelon(example_matrix))
                          