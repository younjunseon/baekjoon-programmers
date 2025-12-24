def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if (mode == 0):
            if(code[i] == "1"):
                mode = 1
                continue
            else:
               if(i%2 == 0):
                  ret = ret + code[i]
        else:
            if(code[i] == "1"):
                mode = 0
                continue
            else:
               if(i%2 == 1):
                  ret = ret + code[i]
                    
    if(ret == ''):
        ret = "EMPTY"
                
    return ret
