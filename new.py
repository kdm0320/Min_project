def solution(logs):
    answer = 0

    first = [" team_name "," application_name "," error_level "]
    sec =": "
    f=False
    s=False
    for log in logs:
        k = ""
        for i in range(len(log)):
            if i==0:
                k+=" "
                k += log[i]
            else:
                if log[i]==":":
                    if k not in first:
                        answer+=1
                        break
                    else:
                        k=""
                        f = True
                        k+=log[i]
                elif f and not s:
                    k += log[i]
                    if k == sec:
                        k=""
                        s=True
                elif f and s:
                    if log[i].isspace():
                        for j in k:
                            if not j.isalpha():
                                answer+=1
                                break
                        else:
                            k=""
                            f=False
                            s=False
                            k += log[i]
                    else:
                        k += log[i]
                else:
                    k += log[i]
    return answer



logs = ["team_name : db application_name : dbtest error_level : info message : test",
        "team_name : test application_name : I DONT CARE error_level : error message : x",
        "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever",
        "team_name : oberervability application_name : LogViewer error_level : error"]

print(solution(logs))