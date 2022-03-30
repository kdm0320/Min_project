

def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    teams = {}
    for n in range(1,num_teams+1):
        teams[str(n)] = [[]]

    for index,em in enumerate(employees):
        task = ""
        is_remote = False
        is_office = False
        for i in range(2,len(em)):
            if em[i].isspace():
                if task in remote_tasks:
                    is_remote = True
                else:
                    is_office = True
                task =""
                continue
            task+=em[i]
            if i==len(em)-1:
                if task in remote_tasks:
                    is_remote = True
                else:
                    is_office = True
                task =""
        if is_office:
            teams[em[0]][0].append(index+1)
        else:
            teams[em[0]].append(index + 1)
    for i in teams:
        if len(teams[i][0]) == 0:
            for j in teams[i][2:]:
                answer.append(j)
        else:
            for j in teams[i][1:]:
                answer.append(j)
    return answer

num_teams = 3

remote_tasks = ["design"]
office_tasks = ["building","supervise"]
employees =["2 design","1 supervise building design","1 design","2 design"]
print(solution(num_teams, remote_tasks, office_tasks, employees))