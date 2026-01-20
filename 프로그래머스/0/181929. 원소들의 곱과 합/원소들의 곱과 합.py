def solution(num_list):
    answer = 0
    
    a = 0
    b = 1
    
    for i in range(len(num_list)):
        a = a + int(num_list[i])
        b = b * int(num_list[i])
        
    a = a*a
    if(a>b):
        answer = 1
    else:
        answer = 0
    return answer