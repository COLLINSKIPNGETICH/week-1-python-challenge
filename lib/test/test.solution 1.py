# test_solution_1.py
from solution1 import solution_1

def test_solution_1():
    # Test Case 1
    A = [7, 15, 10, 8]
    assert solution_1(A) == 7

    # Test Case 2
    A = [11, 10, 8, 12, 8, 10, 11]
    assert solution_1(A) == 6

    # Test Case 3
    A = [7, 14, 10]
    assert solution_1(A) == -1
