import itertools

#순열과 조합
data = [1,2]
print("순열 리스트들 : ", end=' ')
for x in itertools.permutations(data,2):
    print(x, end=' ')
print("조합 리스트들 : ", end=' ')
for x in itertools.combinations(data,2):
     print(x)


#cycle
test = [
    itertools.cycle([1, 2, 3, 4, 5]),
    itertools.cycle([1, 2, 3]),
    itertools.cycle([1, 2]),
]

for _ in range(10):
    print(str(next(test[0])) + ' ', end='')
print()

for _ in range(10):
    print(str(next(test[1])) + ' ', end='')
print()

for _ in range(10):
    print(str(next(test[2])) + ' ', end='')



it = itertools.cycle([1, 2])

print(f"\n{next(it)}")  # 1
print(next(it))  # 2
print(next(it))  # 1
print(next(it))  # 2