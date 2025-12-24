# 시도1 : 처음에 생각한 대로구현을 하면,,,==> 중복처리가 안 된 코드!
def solution(id_list, report, k):
    # answer = [] --> id_list의 갯수에 맞는 길이
    answer = [0] * len(id_list)# [0,0,0,0] ==> 전체 유저에 대한 카운팅

    # 1. 신고 내역에 대한 정리 : dict --> k:신고당한사람, v :신고한사람들[]
    # ==> 일단 모든 유저들을 대상으로 초기화!!!!
    #     d = { "ryan":[], "con":[]}
    reported_dict = {}
    for id in id_list:
        reported_dict[id] = set([])
    # --> 문제 조건 상 id중복X : 다 신규 등록으로 처리가 가능!!

    # 2. 신고 내역에 대한 처리 : report
    # ["a b", "a c",,,,,]==> 중복 신고 내역이 있다!!!
    # report --> set(report) --> list() : 중복 신고 내역 필터링!!
    for report_pair in report:
        # 개별 신고 내역을 어찌 정리할지 "a b"
        # 앞 : 신고한 사람 ==> v ==> append 추가
        # 뒤 : 신고당한 사람 ==> key
        reporter = report_pair.split(" ")[0]
        reported = report_pair.split(" ")[1]
        #a,b = report_pair.split(" ")
        # --> 나의 정리 dict에 기록!!!
        reported_dict[reported].add( reporter )
    # ---> 신고 내역에 대한 처리 끝!!!

    # 3) 시스템적인 기준 k 이상으로 신고당한 BL 필터링
    # 처리 기준 : v의 원소의 수  => 길이
    #             필요한 정보 : k
    # => LC 사용
    k_reported=[]
    for key_id, v in reported_dict.items():
      if len(v) >= k:
        k_reported.append(key_id)

    # => LC
    #k_reported = [key_id for key_id, v in reported_dict.items() if len(v)]

    # 4)  최종적으로 정지당한 id 돌아가면서 카운팅
    #     => BL만 돌아가면 됨 id -> d[BL] => value에 존재
    
    for ban_id in k_reported:
      #정지당한 아이디에서 신고한 사람 찾아서 +1 카운팅
      mail_res_ids = reported_dict[ban_id]
      #정지당한 id를 신고한 id 돌아가면서 메일 발송 +1 카운트
      for id in mail_res_ids:
        #신고한 id에서 할 일 => id_list에 어디에, answer에서 +1갱신
        id_index = id_list.index(id)
        answer [id_index] += 1
        
    return answer