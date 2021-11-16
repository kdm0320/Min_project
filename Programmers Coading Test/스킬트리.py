from collections import deque

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    q = deque([i for i in skill])

    for tree in skill_trees:
        for i in tree:
            if i in q and q.index(i) != 0:
                break
            elif i not in q:
                pass
            elif i in q and q.index(i) == 0:
                answer += 1
                q.popleft()
    return answer

print(solution(skill,skill_trees))