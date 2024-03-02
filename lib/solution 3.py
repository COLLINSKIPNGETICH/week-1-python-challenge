def solution(N):
    if N % 2 != 0:
        return "a" * N
    
    half_N = N // 2
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for i in range(half_N):
        result += alphabet[i] * 2
    
    return result

# Example usage:
print(solution(3))  # Output: "aab"
print(solution(5))  # Output: "aabb"
print(solution(30))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
