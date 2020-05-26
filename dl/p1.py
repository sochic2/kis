# def perm(n):
#     global solution
#     if n == N:
#       # print(result)
#       solution += 1
#       return
#     else:
#         result[n] = 1
#         perm(n+1)
#         result[n] = 0
#         perm(n+1)
#
# N = 26
# result = [0]*N
# solution = 0
# perm(0)
# print(solution)


import sys

sys.stdin = open("부분집합_input.txt")

A = list(range(1, 13))
# print(A)
T = int(input())
An = len(A)
for tc in range(T):
    N, K = map(int, input().split())
    # print(N)
    # print(K)
    cnt = 0

    for i in range(1 << An):
        A_bit = []
        ssum = 0
        for j in range(An + 1):
            if i & (1 << j):
                A_bit += [A[j]]
                ssum += A[j]
        if len(A_bit) == N and ssum == K:
            cnt += 1
    print(f'#{tc + 1} {cnt}')