"""
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
▣ 입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.
▣ 출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.
▣ 입력예제 1
5
level
moon
abcba soon gooG
▣ 출력예제 1
#1 YES
#2 NO
#3 YES
#4 NO #5 YES

"""
#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/1. 회문 문자열 검사/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/1. 회문 문자열 검사/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------


#------------ 내 풀이 코드 -----------------

n = int(input())
words = []
for _ in range(n):
    w = input().lower()
    words.append(w)

for index,word in enumerate(words):
    first = ""
    sec = ""
    i = 0
    j = len(word) -1
    for _ in range(len(word)//2):
        if word[i]!= word[j]:
            print(f"#{index+1} NO")
            break
        else:
            i+=1
            j-=1
    else:
        print(f"#{index+1} YES")






