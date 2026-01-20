def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        temp = ''
        for j in range(len(intStrs[i])):
            if(s<=j and j<s+l):
                temp += str(intStrs[i][j])
                
        if(int(temp)>k):
            answer.append(int(temp))
                
    
    return answer