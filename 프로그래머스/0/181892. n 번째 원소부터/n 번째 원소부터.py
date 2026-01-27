def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list)-n+1):
        answer.append(num_list[n-1+i])
    return answer