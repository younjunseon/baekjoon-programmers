def solution(n, control):
    answer = 0
    
    for i in range(len(control)):
        if(control[i] == "w"):
            n = n + 1
        elif(control[i] == "s"):
            n = n - 1
        elif(control[i] == "d"):
            n = n + 10
        elif(control[i] == "a"):
            n = n - 10
    answer = n
    
    return answer