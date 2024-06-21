import sys
sys.path.append('..')

import pytest
from review import add_to_list
def test_add_to_list_without_list():
    result = add_to_list(1)
    assert result == [1], f"Expected [1], but got {result}"

def test_add_to_list_with_list():
    my_list = [1, 2, 3]
    result = add_to_list(4, my_list)
    assert result == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], but got {result}"
    
    my_list.append(5)
    assert my_list == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], but got {my_list}"

def test_add_to_list_multiple_calls():
    my_list = []
    result1 = add_to_list(1, my_list)
    assert result1 == [1], f"Expected [1], but got {result1}"
    
    result2 = add_to_list(2)
    assert result2 == [1, 2], f"Expected [1, 2], but got {result2}"
    