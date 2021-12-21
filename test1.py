
def solution(drum):
    answer = 0
    starts = [[[0,i],drum[0][i]] for i in range(len(drum))]
    for start in starts:
        try:
            stack = []
            while True:
                root = []
                if start[1] == "#":
                    root.append(start[1])
                    start[0][0]+=1
                    start[1] = drum[start[0][0]][start[0][1]]

                elif start[1] == ">":
                    root.append(start[1])
                    start[0][1]+=1
                    start[1] = drum[start[0][0]][start[0][1]]
                elif start[1] == "<":
                    root.append(start[1])
                    start[0][1]-=1
                    start[1] = drum[start[0][0]][start[0][1]]
                else:
                    if "*" in stack:
                        root.append(start[1])
                        break
                    else:
                        start[0][0] += 1
                        stack.append("*")
                        start[1] = drum[start[0][0]][start[0][1]]
        except:
             answer+=1

    return answer
drum = ["######",">#*###","####*#","#<#>>#",">#*#*<","######"]
print(solution(drum))