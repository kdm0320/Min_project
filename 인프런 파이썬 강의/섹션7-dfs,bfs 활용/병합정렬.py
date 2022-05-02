
def d_sort(lt,rt):
    if lt < rt:
        mid = (lt+rt)//2
        d_sort(lt,mid)
        d_sort(mid+1,rt)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1 <= mid and p2 <=rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1 <= mid:
            tmp+=arr[p1:mid+1]
        if p2 <= rt:
            tmp+=arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]


arr = [23,11,45,36,15,67,33,21]
print("Before Sort : ", end=" ")
print(arr)
d_sort(0,7) # 0번 인덱스부터 7번 리스트까지 정렬
print()
print("After Sort : ", end=" " )
print(arr)