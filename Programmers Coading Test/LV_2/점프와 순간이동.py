

n = 5

"""이진법 활용"""

#bin() = 입력받은 수를 이진수로 바꾸는 함수

def solution(n):
    return bin(n).count('1')


# def solution(n):
#     ans = 0
#     lis = []
#     ans+=1
#     k = 1
#     if n == 1:
#         return ans
#     else:
#         lis.append(n)
#         while n//2 != 1:
#             n//=2
#             lis.append(n)
#     lis.sort()
#     for i in range(len(lis)):
#         k *= 2
#         if k != lis[i]:
#             ans+=1
#             k+=1
#
#     return ans

print(solution(n))