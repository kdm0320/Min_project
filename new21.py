


def largestMagical(binString):
    lis = []
    for j in range(len(binString)):
        box = []
        one = 0
        two = 0
        o_c = 0
        z_c = 0
        new1 = ""
        new2 = ""
        check = False
        for i in range(j,len(binString)):
            if binString[i]=="1":
                o_c+=1
            else:
                z_c+=1
            box.append(binString[i])
            if i<len(binString)-1 and o_c==z_c:
                if len(new1) == 0 :
                    new1+="".join(box)
                    one+=i
                else:
                    new2+="".join(box)
                    two+=i
                o_c=0
                z_c = 0
                box = []
        if len(new1) > 0 and len(new2) > 0 and new1[0] != "0" and new2[0] != "0":
            check =True
        if check:
            if int(new2) > int(new1):
                tmp = int(binString[:one - 1] + new2 + new1 + binString[two + 1:])
                if tmp > int(binString):
                    lis.append(tmp)
    if len(lis)==0:
        return binString
    else:
        return str(max(lis))




binString = "11011000"

print(largestMagical(binString))