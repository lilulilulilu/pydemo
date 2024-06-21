import sys
sys.path.append('..')

import pytest
from quiz import reverse_list, solve_sudoku

def test_reverse_list():
    # Test an empty list
    assert reverse_list([]) == []

    # Test a list with one element
    assert reverse_list([1]) == [1]

    # Test a list with two elements
    assert reverse_list([1, 2]) == [2, 1]

    # Test a list with multiple elements
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    # Test a list with different types of elements
    assert reverse_list([1, 'a', True, None]) == [None, True, 'a', 1]
    
def test_solve_sudoku():
    matrix = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
    expected = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
    matrix = solve_sudoku(matrix)
    assert matrix == expected

def test_solve_a_invalid_sudoku():
    matrix = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,1,0]
    ]
    expected = [[]]
    matrix = solve_sudoku(matrix)
    assert matrix == expected    



    