#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/6. 알파코드/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/6. 알파코드/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------
#------------ 내 풀이 코드 ----------------- => 실패
# def dfs(l):
#     global res
#     if l> len(code):
#         return
#     if l==len(code):
#         a = ""
#         for i in res:
#             a+=h[i]
#         w.append(a)
#         res = []
#         return
#     else:
#         for i in range(27):
#             if code[l]==str(i):
#                 res.append(i)
#                 dfs(l+1)
#                 dfs(l+2)
#             res.append(i)
#
#
#
#
# code = input()
# alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# h = {}
# for index,i in enumerate(alpha):
#     h[index+1] = i
# w = []
# res =[]
# dfs(0)
# print(w)

#-----------영상 풀이 코드 -------------------
def DFS(l,p):
    global cnt
    if l==n:
        cnt+=1
        for j in range(p):
            print(chr(res[j]+64),end='')
        print()
    else:
        for i in range(1,27):
            if code[l]==i:
                res[p] = i
                DFS(l+1,p+1)
            elif i>=10 and code[l]==i//10 and code[l+1]==i%10:
                res[p] = i
                DFS(l+2,p+1)

code = list(map(int, input()))
n = len(code)
code.insert(n,-1)
res = [0]*(n+3)
cnt = 0
DFS(0,0)
print(cnt)