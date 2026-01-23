def solution(arr):
    answer = []
    a = -1
    b = -1
    for i in range(len(arr)):
        if(arr[i] == 2):
            a = i
            break
            
    for i in range(len(arr)):
        if(arr[i] == 2):
            b = i
    
    if (a != -1):
        for i in range(a,b+1):
            answer.append(arr[i])
    else:
        answer.append(-1)
        
    return answer