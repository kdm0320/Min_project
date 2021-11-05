"""
0과 1로만 된 문자열이 주어진다 이 문자열을 뒤집어서 문자열의 모든 숫자를 같게 만드려고 한다.
뒤집는 최소 횟수를 구하라
문자열을 한번에 뒤집을 수 있다
ex) 1110011 -> 4번째 문자부터 5번째 문자까지 한번에 뒤집기 가능
"""

# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중 더 적은 횟수를 가지는 경우를 계산
s = input()

count0 = 0
count1 = 0

if s[0] == "1":
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))






