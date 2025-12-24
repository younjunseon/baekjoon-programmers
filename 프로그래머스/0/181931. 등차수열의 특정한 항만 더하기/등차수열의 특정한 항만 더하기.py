def solution(a, d, included):
    answer = 0
    sum = 0
    index = 0
    
    for i in included:
        if (i == True):
            
            sum = sum + a + d*index
            
        index += 1
            
    answer = sum
    
    return answer