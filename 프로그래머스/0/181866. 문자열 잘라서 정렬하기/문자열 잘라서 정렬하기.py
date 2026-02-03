def solution(myString):
    answer = []
    temp = ""
    
    for i in range(len(myString)):
        if(myString[i] == "x"):
            if(temp != ""):
                answer.append(temp)
                temp = ""
        else:
            temp += myString[i]
    
    if(temp == ""):
        pass
    else:
        answer.append(temp)
    answer.sort()
    
    return answer