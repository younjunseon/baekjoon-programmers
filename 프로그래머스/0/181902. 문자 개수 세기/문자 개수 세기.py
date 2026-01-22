def solution(my_string):
    answer = []
    
    for i in range(26):
        temp = 0
        for j in range(len(my_string)):
            if(ord(my_string[j]) == 65+i):
                temp += 1
        answer.append(temp)
            
    for i in range(26):
        temp = 0
        for j in range(len(my_string)):
            if(ord(my_string[j]) == 97+i):
                temp += 1
        answer.append(temp)
            
    return answer