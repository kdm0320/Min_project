import itertools

data = [1,2]
print("순열 리스트들 : ", end=' ')
for x in itertools.permutations(data,2):
    print(x, end=' ')
print("조합 리스트들 : ", end=' ')
for x in itertools.combinations(data,2):
    print(x, end=' ')
