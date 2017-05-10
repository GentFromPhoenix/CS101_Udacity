# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def build_column(matrix, column_number):
    column = []
    for row in matrix:
        column = column + [row[column_number]]
    return column
               
def check_sudoku(matrix):
    size = len(matrix) # Matrix size
    column_number = 0
    for row in matrix:
        #print 'row and size is', row, size
        value_check = 1
        # since symmetrical build column 
        column = build_column(matrix,column_number)
        #print 'column', column_number, 'is    ', column
        column_number = column_number + 1
        # Check to see if values in rows and columns if not
        # return False
        while value_check <= size:
            if value_check not in row or value_check not in column:
                return False
            value_check = value_check + 1
    return True
        

            




    
    
print '--------------------'
print '    FALSE  '
print check_sudoku(incorrect)
#>>> False
print '--------------------'
print '    TRUE  '
print check_sudoku(correct)
#>>> True
print '--------------------'
print '    FALSE  '
print check_sudoku(incorrect2)
#>>> False
print '--------------------'
print '    FALSE  '
print check_sudoku(incorrect3)
#>>> False
print '--------------------'
print '    FALSE  '
print check_sudoku(incorrect4)
#>>> False
print '--------------------'
print '    FALSE  '
print check_sudoku(incorrect5)
#>>> False