def solution(num_list, n):
    answer = []
    
    for i in range(n,n+len(num_list)):
        if(i<len(num_list)):
            answer.append(num_list[i])
        else:
            answer.append(num_list[i-len(num_list)])
    
    return answer