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
