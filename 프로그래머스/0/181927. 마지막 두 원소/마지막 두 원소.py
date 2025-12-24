def solution(num_list):
    answer = []
    
    a = len(num_list) - 1
    
    if(num_list[a] > num_list[a-1]):
        num_list.append(int(num_list[a])-int(num_list[a-1]))
    else:
        num_list.append(int(num_list[a])*2)

    
    answer = num_list
    
    return answer