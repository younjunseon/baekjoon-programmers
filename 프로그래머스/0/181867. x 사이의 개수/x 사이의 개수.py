def solution(myString):
    answer = []
    n=0
    
    for i in range(len(myString)):
        if(myString[i] == "x"):
            answer.append(n)
            n = 0
        else:
            n += 1
            
    answer.append(n)
    return answer