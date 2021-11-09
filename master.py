log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]


def solution(log):
    count = 0
    time = [[],[]]
    temp = []
    for i in log:
        time[count].append(int(i[0:2]))
        time[count].append(int(i[3:5]))
        if count==1:
            count = 0
            hour = (time[1][0] - time[0][0])*60
            min = time[1][1] - time[0][1]
            times = 0
            if hour+min >= 105:
                times += 105
            elif hour+min <= 4:
                pass
            else:
                times+=hour+min
            temp.append(times)
            time = [[],[]]
        else:
            count += 1
    answer = f"0{sum(temp)//60}:{sum(temp)%60}"
    return answer

print(solution(log))








