def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    n = len(begin)
    checked = [False]*(n-1)
    # for word in words:

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
t = ["SFO", "ATL", "ICN", "ATL", "SFO"]
print(t.sort(key= lambda x:x[0]))

print(solution(begin,target,words))