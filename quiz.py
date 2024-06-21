from typing import List


def reverse_list(l: list):
    """
    Reverse a list without using any built in functions
    This function should return a sorted list.
    Input l is a list which can contain any type of data.

    Args:
        l (list): The list to be reversed.
    
    Returns:
        l (list): The reversed list.
    """
    left = 0
    right = len(l) - 1
    
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    
    return l

 
def solve_sudoku(matrix: List[List[int]]) -> List[List[int]]:

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.
    The input matrix is a 9x9 matrix. You need to write a program to solve it.
    
    Args:
        matrix[i][j] is 0 if the cell is empty.
        
    Returns:
        the solved 9x9 Sudoku board.
    """
    # solve the sudoku board with backtracking
    def solve(matrix, num_to_fill) -> bool:
        if num_to_fill == 0: # a solution find successfully, return True.
            return True
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == 0:
                    values = get_possible_values(matrix, i, j)
                    if len(values) == 0 and num_to_fill != 0:
                        return False
                    for val in values:
                        matrix[i][j] = val # try one value
                        is_solved = solve(matrix, num_to_fill - 1)
                        if is_solved:
                            return True
                        else:
                            matrix[i][j] = 0 # backtrack
                    return False
    
    # get possible values for a cell of the matrix[i][j]
    def get_possible_values(matrix, i, j) -> List[int]:
        values = {x for x in range(1, 10)}
        row_vals = {matrix[i][x] for x in range(9) if matrix[i][x] != 0}
        col_vals = {matrix[x][j] for x in range(9) if matrix[x][j] != 0}
        box_vals = {matrix[m][n] for m in range(i//3*3, i//3*3+3) for n in range(j//3*3, j//3*3+3) if matrix[m][n] != 0}
        values = values - (row_vals | col_vals | box_vals)
        return list(values)
    
    num_to_fill = 0 # the number of cells to fill
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                num_to_fill += 1
    solve(matrix, num_to_fill)
    
    def is_valid_sudoku(matrix) -> bool:
        s = {i for i in range(1, 10)}
        # check each row contains 1-9
        for i in range(9): 
            row_set = set(matrix[i])
            if row_set != s:
                return False
        # check each column contains 1-9
        for j in range(9): 
            column_set = set()
            for i in range(9):
                column_set.add(matrix[i][j])
            if column_set != s:
                return False
        # check each 3x3 box contains 1-9
        box = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9): 
            for j in range(9):
                box[i//3][j//3].add(matrix[i][j])
        for i in range(3):
            for j in range(3):
                if box[i][j] != s:
                    return False
        return True
    
    # if matrix can be solved as a valid sudoku matrix, return the matrix, otherwise return an empty matrix.    
    if is_valid_sudoku(matrix):
        return matrix    
    return [[]]