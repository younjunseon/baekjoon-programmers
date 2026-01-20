def solution(a, b, c, d):
    answer = 0
    
    if(a == b == c == d):
        return 1111*int(a)
    elif(a == b == c):
        return (a * 10 + d)*(a * 10 + d)
    elif(a == b == d):
        return (a * 10 + c)*(a * 10 + c)
    elif(a == c == d):
        return (a * 10 + b)*(a * 10 + b)
    elif(b == c == d):
        return (b * 10 + a)*(b * 10 + a)
    elif(a == b and c == d):
        if(a>c):
            return (a+c)*(a-c)
        else:
            return (c+a)*(c-a)
    elif(a == c and b == d):
        if(a>b):
            return (a+b)*(a-b)
        else:
            return (b+a)*(b-a)
    elif(a == d and c == b):
        if(a>c):
            return (a+c)*(a-c)
        else:
            return (c+a)*(c-a)
    elif(a == b):
        return c*d
    elif(a == c):
        return b*d
    elif(a == d):
        return b*c
    elif(b == c):
        return a*d
    elif(b == d):
        return a*c
    elif(c == d):
        return a*b
    else:
        if(a>b):
            if(b>c):
                if(c>d):
                    return d
                else:
                    return c
            else:
                if(b>d):
                    return d
                else:
                    return b
        else:
            if(a>c):
                if(c>d):
                    return d
                else:
                    return c
            else:
                if(a>d):
                    return d
                else:
                    return a
                    
        
#    return answer