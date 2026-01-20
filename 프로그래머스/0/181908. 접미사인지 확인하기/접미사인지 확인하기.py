def solution(my_string, is_suffix):
    answer = 0
    n = len(my_string)-len(is_suffix)
    for i in range(len(is_suffix)):
        if(len(my_string) < len(is_suffix)):
            return 0
        if(my_string[n] != is_suffix[i]):
            return 0
        n += 1
        
    return 1