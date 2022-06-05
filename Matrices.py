import numpy as np
#  np.array([[0,-2,7],
#                  [6,5,4],
#                  [1,7,5],
#                  [0,5,4]
#                  ],dtype=float)
example_matrix = np.array([[2,1,3,-9],
                 [1,-1,2,-7],
                 [4,3,5,-15],
                 
                 ],dtype=float)


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

def get_nonone_element(row):
    for i in range(len(row)):
        if row[i] != 0 and row[i] != 1:
            return i
    return -1
def echelon(matrix):
    zeros = get_zeros(matrix)
    if zeros != -1:
        zeros_row = matrix[zeros].copy()
        matrix[zeros] =  matrix[-1]
        matrix[-1] = zeros_row
        
    nonzero = get_nonzero_element(matrix[0])
        
    
    for i in range(len(matrix)):
        nonzero = get_nonzero_element(matrix[i])
        if nonzero != -1:
            matrix[i] = multiply_by_scalar(matrix[i],1/matrix[i][nonzero])
        for j in range(i+1,len(matrix)):
            nonzero = get_nonzero_element(matrix[j])
            
            if (matrix[i][nonzero] != 0 and nonzero == i):
                
                matrix[j] = row_addition_by_scalar(matrix[j],matrix[i],-matrix[j][nonzero]/matrix[i][nonzero])
            else:
                matrix[j] = row_addition_by_scalar(matrix[j],matrix[i],0)

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
    for i in range(len(echelon_form)-1,-1,-1):
        nonzero = get_nonzero_element(echelon_form[i])
        if nonzero != -1:
            for j in range(i):
                nonzero = get_nonone_element(echelon_form[j])
                echelon_form[j] = row_addition_by_scalar(echelon_form[j],echelon_form[i],-echelon_form[j][nonzero])
    nonzero = get_nonzero_element(echelon_form[-1])
    print(nonzero)
    if nonzero != -1:
        echelon_form[0] = row_addition_by_scalar(echelon_form[0],echelon_form[-1],-echelon_form[0][nonzero])
    return echelon_form
print(reduced_echelon(example_matrix))
                          