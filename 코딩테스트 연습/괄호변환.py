def check_right(w):
    check=0
    for i in w:
        if i==")":
            check-=1
        else:
            check+=1
        if check < 0:
            return False
    return True

def solution(p):
    answer = ''
    l = 0
    r = 0
    if p == "":
        return ""
    if check_right(p):
        return p
    for i in range(len(p)):
        if p[i] == "(":
            l+=1
        else:
            r+=1
        if l==r:
            u = p[:i+1]
            v = ""
            if i != len(p)-1:
                v=p[i+1:]
            if check_right(u):
                a = solution(v)
                return u+a
            else:
                a = solution(v)
                temp ="("+a+")"
                change = {"(":")",")":"("}
                b = "".join([change[i] for i in u[1:len(u)-1] ])
                return temp+b
