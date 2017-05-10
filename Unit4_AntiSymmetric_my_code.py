# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def build_column(matrix, column_number):
    column = []
    for row in matrix:
        column = column + [row[column_number]]
    return column
               
def antisymmetric(matrix):
    size = len(matrix) # Matrix size
    column_number = 0
    for row in matrix:
        value_check = 1
        column = build_column(matrix,column_number) # Get the Column
        column_number = column_number + 1
        n = 0
        while n + 1 <= size:
            if row[n] != column[n] * -1:
                return False
            n = n + 1
            #if row != (column * -1): # Check if row & column are equal
            #return False
    return True

    
#Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

            

