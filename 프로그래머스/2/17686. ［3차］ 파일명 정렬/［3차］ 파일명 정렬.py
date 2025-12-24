import re

def solution(files):
    answer = []

    # (head: 소문자, number: 숫자(제로패딩 처리), 원본순서)
    my_files = []
    
    for idx, s in enumerate(files):
      numbers = re.findall(r"\d+",s)
      real_number = int(numbers[0])  # 0012 -> 12
      head = s[:s.index(numbers[0])]
      head = head.lower()
      my_files.append([head, real_number, idx]) # 같은 쌍끼리 묶어줘야 함
    
    my_files.sort(key= lambda x : (x[0], x[1],x[2]))


    answer = [files [j[2]] for j in my_files]

    return answer