def get_distance( number, pos):
  key_pad = {
    "1" : [0,0], "2" : [0,1], "3" : [0,2],
    "4" : [1,0], "5" : [1,1], "6" : [1,2],
    "7" : [2,0], "8" : [2,1], "9" : [2,2],
    "*" : [3,0], "0" : [3,1], "#" : [3,2]
  }

  number = str(number)
  pos = str(pos)
  x_number, y_number = key_pad[number]
  x_pos, y_pos = key_pad[pos]

  abs_dis = abs(x_number - x_pos) + abs(y_number - y_pos)

  return abs_dis



def solution(numbers, hand):
  answer = ''

  left_pos = '*'
  right_pos = '#'

  if hand == "right":
    hand = "R"
  else:
    hand = "L"

  for num in numbers:
    if num in [1,4,7]:
      answer += "L"
      left_pos = num
    elif num in [3,6,9]:
      answer += "R"
      right_pos = num
    else:
      dis_left = get_distance(num,left_pos)
      dis_right = get_distance(num,right_pos)

      if dis_left<dis_right:
        answer += "L"
        left_pos = num
      elif dis_left>dis_right:
        answer += "R"
        right_pos = num
      else:
        answer += hand
        if hand == "R":
          right_pos = num
        else:
          left_pos = num
          
  return answer