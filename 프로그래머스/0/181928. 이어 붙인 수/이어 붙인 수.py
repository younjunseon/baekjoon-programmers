def solution(num_list):
    answer = 0
    odd = ""
    even = ""
    
    for num in num_list:
        if(num%2 == 1):
            odd = odd + str(num)
        else:
            even = even + str(num)
            
    odd = int(odd)
    even = int(even)
    
    answer = odd + even
            
    return answer