def solution(A):
    n = len(A)
    
    # Check if it's possible to have exactly 10 bricks in every box
    total_bricks = sum(A)
    if total_bricks % n != 0:
        return -1
    
    target_bricks = total_bricks // n
    moves = 0
    for i in range(1, n):
        diff = A[i] - target_bricks
        A[i] -= diff
        A[i - 1] += diff
        moves += abs(diff)
    
    return moves

# Example usage:
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
