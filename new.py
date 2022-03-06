from datetime import datetime,timedelta

def add_date(money,answer,date_diff):
    if money < 10000:
        answer[0] += date_diff
    elif 10000 <= money < 20000:
        answer[1] += date_diff
    elif 20000 <= money < 50000:
        answer[2] += date_diff
    elif 50000 <= money < 100000:
        answer[3] += date_diff
    else:
        answer[4] += date_diff
    return answer

def solution(purchase): #필요한것 -> 행렬이동법, 행렬 대각선 판별
    answer = [0,0,0,0,0]
    date1 = ""
    money =0
    date2 = ""
    last_date = "2019/12/31"
    duration_date = ""
    format = '%Y/%m/%d'
    duration_format = '%Y-%m-%d %H:%M:%S'
    for purin, pur in enumerate(purchase):
        for index, i in enumerate(pur):
            if i.isspace():
                if purin == 0:
                    date1 += pur[:index]
                    date1 = datetime.strptime(date1,format)
                    duration_date += str(date1+timedelta(days=30))
                    money += int(pur[index+1:])
                    break
                else:
                    date2 += pur[:index]
                    date2 = datetime.strptime(date2, format)
                    duration_date = datetime.strptime(str(duration_date), duration_format)
                    if date2 <= duration_date:
                        date_diff = (date2-date1).days
                        duration_date += str(date2 + timedelta(days=30))
                        answer = add_date(money,answer,date_diff)
                        money=0
                        money+=int(pur[index+1:])
                    else:
                        date_diff = 30
                        answer = add_date(money, answer, date_diff)
                    date1 = date2
                    date2 = ""
                    money = 0
                    duration_date = ""
                    break


    return answer


purchase = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]

print(solution(purchase))