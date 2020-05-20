# Day_01_02_numpy.py

import numpy as np


# 문제
# 0~9까지의 리스트를 만들어서 거꾸로 출력하세요.

a = list(range(10))
print(a)
print([i for i in reversed(a)])

print(a[3:4])
print(a[3:3])
print(a[-1])

print(a[:])
print(a[::])
print(a[::2])

print(a[9:0:-1])
print(a[9:-1:-1])
print(a[-1:-1:-1])

print(a[::-1])

print('-------------------------------------------------------')

# broadcast 연산과 벡터연산이 numpy를 쓰는 가장 기본중의 기본 이유
b = np.arange(10)
print(b)
print(type(b))
print(b.shape, b.dtype, b.size)

print(b[0], b[-1])
print(b[:5])
print()

print(b + 3)            #broadcast
print(b + b)
print(b > 3)
print(b[b > 3])         # boolean 배열
# for i in b:
#     print(i + 3 , end=' ')
print()

d = b.reshape(2, 5)
print(d)
c = b.reshape(2, -1)
print(c)
e = b.reshape(-1, 5)
print(e)

print(np.sin(b))
print(np.sin(c))
print()
print(b)
print(c)
print()

g = b.copy()        #deep copy
b[0] = 123
print(b)
print(c)
print(g)

a1 = np.arange(3)
a2 = np.arange(6)
a3 = np.arange(3).reshape(1, 3)
a4 = np.arange(6).reshape(2, 3)

# print(a1+a2)  #error
print(a1+a3)    #vector
print(a1+a4)    #broadcast + vector
print()

print(np.arange(12).reshape(3, 4))
print(np.arange(12).reshape(2, -1))
print()

d = np.arange(12)
print(d)
print(np.reshape(d, (3, 4)))   # 추천방식
print(d.reshape(3, 4))


print(np.zeros(5, dtype=np.int32))
print(np.ones(5))
print(np.full(5, 2))
print(np.full(5, -1.0))
print(np.full(5, -1.0).dtype)

#문제
#테두리는1로, 속은 0으로 채워진 5행 5열 크기의 배열

f = np.zeros([5, 5], dtype=np.int32)
print(f)
# f[0], f[-1] = 1, 1   # 이거랑 밑에꺼 같은 의미
# f[0, :], f[-1, :] = 1, 1
f[[0, -1], :] = 1

f[:, 0], f[:, -1] = 1, 1
print(f)
print('---------------')
print()


g = np.ones([5, 5], dtype=np.int16)
g[1:-1, 1:-1] = 0
print(g)
print('----------')
print()

e = np.zeros([5, 5], dtype=np.int32)
# for i in range(5):
#     e[i, i] = 1
# print(e)
# print(np.eye(5))
# print(np.identity(5))
# e[[0, 1, -1], 0] = 1  #index array
# e[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]] = 1
e[range(5), range(5)] = 1
print(e)
print('---------')
print()















