def solution(a, b):
    answer = 0
    answer1 = str(a)+str(b)
    answer2 = str(b)+str(a)
    
    answer1 = int(answer1)
    answer2 = int(answer2)
    
    if(answer1>answer2):
        answer = answer1
    else:
        answer = answer2
    return answer