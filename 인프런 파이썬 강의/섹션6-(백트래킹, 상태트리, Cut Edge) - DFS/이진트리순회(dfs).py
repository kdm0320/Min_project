
#------------ 내 풀이 코드 -----------------

def dfs(v):
  if v > 7:
    return
  else:
    print(v,end=" ")
    dfs(v*2)
    dfs(v*2+1)





def solution():
  dfs(1)


solution()


#-----------영상 풀이 코드 -------------------


