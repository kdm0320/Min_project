numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    answer = ''
    key = {1:(0,3),2:(1,3),3:(2,3),4:(0,2),5:(1,2),
          6:(2,2),7:(0,1),8:(1,1),9:(2,1),0:(1,0)}
    hands = {"right":"R","left":"L"}
    left = (0,0)
    right = (2,0)
    
    for num in numbers:
        left_dist = abs(left[0]-key[num][0])+abs(left[1]-key[num][1])
        right_dist = abs(right[0]-key[num][0])+abs(right[1]-key[num][1])
        if num in [1,4,7]:
            answer+="L"
            left = key[num]
        elif num in [3,6,9]:
            answer+="R"
            right = key[num]
        else:
            if left_dist < right_dist:
                answer+="L"
                left = key[num]
            elif left_dist == right_dist:
                answer+=hands[hand]
                if hand == "left":
                    left = key[num]
                else:
                    right = key[num]
            else:
                answer+="R"
                right = key[num]
    
    return answer
    
print(solution(numbers,hand))
