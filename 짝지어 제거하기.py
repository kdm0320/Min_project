def solution(s):
    stack = [s[0]]
    after = s
    while after != "":
        for i in range(1,len(after)):
            if stack[-1] == after[i]:
                after = after.replace(after[i-1:i+1],"",1)
                if after == "":
                	return 1
								else:
                	break
            else:
                stack.append(s[i])
        else:
            return 0
    return 1

s = "baabaa"

print(solution(s))
