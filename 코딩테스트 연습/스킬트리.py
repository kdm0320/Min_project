from collections import deque

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

#for-else

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        q = deque(skill)
        for s in skills:
            if s in skill:
                if s != q.popleft():
                    break
        else:
            answer += 1

    return answer
    
print(solution(skill,skill_trees))
