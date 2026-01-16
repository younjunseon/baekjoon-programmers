def solution(l, r):
    answer = []
    
    for i in range(l,r+1):
        number = str(i)
        is_valid = True
        for char in number:
            if char not in ['0', '5']:
                is_valid = False
                break
        if(is_valid):
            answer.append(i)
    
    return answer if answer else [-1]