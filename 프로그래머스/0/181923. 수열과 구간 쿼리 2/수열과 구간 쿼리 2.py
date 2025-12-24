def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        max_val = -1  
        for i in range(s, e + 1):
            if arr[i] > k and (max_val == -1 or arr[i] < max_val):
                max_val = arr[i]
        answer.append(max_val)

    return answer