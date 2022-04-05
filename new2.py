
def getMaxSumOfArray(arr1, arr2):
    arr1.sort(reverse=True)
    arr2.sort()
    s = 0
    for i in range(len(arr1)):
        s+= (arr2[i]-arr1[i])*(i+1)
    return s


arr1 = [1,2,3]
arr2 = [10,10,10]

print(getMaxSumOfArray(arr1,arr2))