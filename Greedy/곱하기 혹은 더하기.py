s = input()

answer = 0
for i in s:
    if i == "0" or i=="1" or answer == 0:
        answer += int(i)
    else:
        answer *= int(i)

print(answer)