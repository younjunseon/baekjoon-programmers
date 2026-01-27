def solution(str_list):
    answer = []
    a=0
    b=0
    
    for i in range(len(str_list)):
        if(str_list[i] == "l"):
            a = i
            for i in range(a):
                answer.append(str_list[i])
            return answer
        if(str_list[i] == "r"):
            b = i
            for i in range(b+1,len(str_list)):
                answer.append(str_list[i])
            return answer
            
                
        
    
    return answer