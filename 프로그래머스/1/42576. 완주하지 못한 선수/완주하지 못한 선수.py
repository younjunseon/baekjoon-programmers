def solution(participant, completion):

  people_dict = {}
  
  for p in participant:
    if p in people_dict:
      people_dict[p] += 1
    else:
      people_dict[p] = 1
  
  for c in completion:
    if people_dict[c] == 1:
      del people_dict[c]
    else:
      people_dict[c] -= 1

  answer = list(people_dict.keys())[0]

  return answer
