def solution(arr, queries):
    # 각 query는 [s, e, k] 형태입니다.
    for s, e, k in queries:
        # s부터 e까지의 인덱스 i를 하나씩 확인합니다.
        for i in range(s, e + 1):
            # 문제의 핵심: "인덱스 i"가 k의 배수인지 확인
            if i % k == 0:
                # 해당 인덱스의 값을 1 증가시킴 (인덱스로 직접 수정)
                arr[i] += 1
                
    return arr