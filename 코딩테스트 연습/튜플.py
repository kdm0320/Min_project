import re
from collections import Counter


def solution(s):
    print(re.findall('\d',s))
    s = Counter(re.findall('\d',s))
    print(s)
    print(s.items())
    print(sorted(s.items(), key=lambda x: x[1], reverse=True))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

s="{{2},{2,1},{2,1,3},{2,1,3,4}}"

print(solution(s))