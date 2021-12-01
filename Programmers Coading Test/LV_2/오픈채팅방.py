record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
          "Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    answer = []
    temp = {}
    check = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for i in record:
        rec = i.split()
        if rec[0] in ["Enter", "Change"]:
            temp[rec[1]] = rec[2]

    for i in record:
        if i.split()[0] != "Change":
            answer.append(temp[i.split()[1]] + check[i.split()[0]])
    return answer

print(solution(record))