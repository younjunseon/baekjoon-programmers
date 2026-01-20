def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        temp = ''
        for j in range(len(my_string)-i):
            temp += my_string[i+j]
        answer.append(temp)
        
    answer.sort()
    return answer