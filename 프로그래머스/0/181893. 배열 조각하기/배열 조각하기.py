def solution(arr, query):
    for i in range(len(query)):
        val = query[i]
        if i % 2 == 0:
            # 짝수 인덱스: 0부터 query[i]까지 남김
            arr = arr[:val + 1]
        else:
            # 홀수 인덱스: query[i]부터 끝까지 남김
            arr = arr[val:]
    return arr
