def solution(x1, x2, x3, x4):
    answer = True
    answer = bool( x1 + x2 ) * bool( x3 + x4 )
    if(answer == 1):
        return True
    else:
        return False