# test_solution_3.py
from solution_3 import solution_3

def test_solution_3():
    # Test Case 1
    N = 3
    assert len(solution_3(N)) == N

    # Test Case 2
    N = 5
    assert len(solution_3(N)) == N

    # Test Case 3
    N = 30
    assert len(solution_3(N)) == N
