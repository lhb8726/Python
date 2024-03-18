# Variable
a = 1
b = "Python"
c = [1, 2, 3]

# 변수가 가리키고 있는 주소 값
print(id(a))

# 리스트 복사
d = [1, 2, 3]
e = d
print(id(d))
print(id(e))

print(d is e)

d[1] = 4
print(d)
print(e)

# 리스트 복사 : [:]
f = [1, 2, 3]
g = f[:]
f[1] = 4
print(f)
print(g)

# copy 모듈
from copy import copy
h = [1, 2, 3]
i = copy(h)
print(h is i)

j = h.copy()
print(h is j)

# 변수를 만드는 여러 가지 방법
k, l  = ("python", "life")
print(k, l)

(k, l) = "python", "life"
print(k, l)

[k, l] = ["python", "life"]
print(k, l)

k = l = "python"
print(k, l)

m = 3
n = 5
n, m = m, n
print(m)
print(n)
