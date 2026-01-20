def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(parts)):
        for j in range(len(my_strings[i])):
                       if(parts[i][0]<=j and j<=parts[i][1]):
                            answer += my_strings[i][j]
            
    return answer