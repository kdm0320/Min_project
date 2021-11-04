"""왕실 정원은 체스판과 같은 8X8 좌표평면이다. 정원의 특정한 칸에 나이트가 서있다.
나이트는 L자 형태로만 이동이 가능하며 정원 밖으로는 나갈 수 없다. 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다."""

'''1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
   2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기'''

'''나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하라 / 행 위치표현 = 1~8 , 열 위치 표현 = a~h'''

'''입력 조건 - 첫 줄에 현재 나이트가 위치한 곳의 좌표가 입력된다 ex)a1
   출력 조건 - 첫줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오 ex) 2'''

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

steps = [(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row+step[0]
    nex_column = column+step[1]

    if next_row>=1 and next_row<=8 and nex_column>=1 and nex_column<=8:
        result+=1
print(result)
