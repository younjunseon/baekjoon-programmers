def solution(my_string, queries):
    answer = ''
    
    for i in range(len(queries)):
        temp = ''
        for j in range(len(my_string)):
            if(queries[i][0]<=j<=queries[i][1]):
                a = queries[i][0] + queries[i][1] - j
                temp += my_string[a]
            else:
                temp += my_string[j]
        my_string = temp
           
    return my_string