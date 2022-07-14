import numpy as np
import copy
#  np.array([[0,-2,7],
#                  [6,5,4],
#                  [1,7,5],
#                  [0,5,4]
#                  ],dtype=float)
# np.array([[0,6,4,0],
#                  [3,0,-7,0],
#                  [1,5,1,0],
#                  [-1,1,3,0]
                 
#                  ],dtype=float)
example_matrix = np.array([[0,-2,7],
                 [6,5,4],
                 [1,7,5],
                 [0,5,4]
                 ],dtype=float)

def get_first_nonzero_element(row):
    
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

def check_if_zero_row(row):
    return True if(get_first_nonzero_element(row) == len(row)) else False

def row_scalar_multiplication(row,k):
    return (1/k) * row


def row_addition(row1,row2,k):
    return np.round(row2 - row1*(k),10)

def sort_matrix(matrix):
    nonzero_indexes = [get_first_nonzero_element(row) for row in matrix]
    
    matrix_copy = copy.deepcopy(matrix)
    min_index = min(nonzero_indexes)
    
    for i in range(len(matrix)):
        relative_index = nonzero_indexes[i] - min_index
        
        if nonzero_indexes[i] < len(matrix[0]) and nonzero_indexes[relative_index] - min_index < len(matrix[0]):
             
            matrix_copy[nonzero_indexes[relative_index] - min_index] = matrix[relative_index].copy()
        else:
            
            matrix_copy[-1] = np.zeros(len(matrix[0]))
        
    
    
    return matrix_copy

def echelon_form(matrix):
    for i in range(len(matrix)):
        matrix = sort_matrix(matrix)
        nonzero_indexi = get_first_nonzero_element(matrix[i])
        if nonzero_indexi != len(matrix[i]):
            matrix[i] = row_scalar_multiplication(matrix[i],matrix[i][nonzero_indexi])
            for j in range(i+1,len(matrix)):
                nonzero_indexj = get_first_nonzero_element(matrix[j])
                if nonzero_indexj != len(matrix[i]) and nonzero_indexj == nonzero_indexi:
                    matrix[j] = row_addition(matrix[i],matrix[j],matrix[j][nonzero_indexj])
                
    nonzero_index = get_first_nonzero_element(matrix[-1])
    if nonzero_index != len(matrix[-1]):
        matrix[-1] = row_scalar_multiplication(matrix[-1],matrix[-1][nonzero_index])
    return matrix


        
        
        
            

def reduced_echelon_form(matrix):
    matrix = echelon_form(matrix)
   
    for i in range(len(matrix)-1,0,-1):
        nonzero_indexi = len(matrix[i]) - get_first_nonzero_element(matrix[i][-1::-1]) - 1
        if nonzero_indexi != -1:
            for j in range(i-1,-1,-1):
                nonzero_indexj = len(matrix[j]) - get_first_nonzero_element(matrix[j][-1::-1]) - 1
                if nonzero_indexj != -1 and nonzero_indexj == nonzero_indexi:
                    matrix[j] = row_addition(matrix[i],matrix[j],matrix[j][nonzero_indexj])
        
                
                
    return matrix
            
        
    
        
    
        
    


print(reduced_echelon_form(example_matrix))

                          