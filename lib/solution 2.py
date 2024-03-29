def digit_sum(num):
    return sum(map(int, str(num)))

def solution(A):
    max_sum = -1
    sum_dict = {}
    
    for num in A:
        curr_sum = digit_sum(num)
        
        if curr_sum in sum_dict:
            max_sum = max(max_sum, sum_dict[curr_sum] + num)
        
        sum_dict[curr_sum] = max(sum_dict.get(curr_sum, 0), num)
    
    return max_sum

