# test_solution_2.py
from solution_2 import solution_2

def test_solution_2():
    # Test Case 1
    A = [51, 71, 17, 42]
    assert solution_2(A) == 93

    # Test Case 2
    A = [42, 33, 60]
    assert solution_2(A) == 102

    # Test Case 3
    A = [51, 32, 43]
    assert solution_2(A) == -1
