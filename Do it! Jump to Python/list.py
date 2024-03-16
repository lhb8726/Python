# List : 문자(열)의 모음
a = []
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
d = [1, 2, "Life", "is"]
e = [1, 2, ["Life", "is"]]

# Indexing
f = [1, 2, 3]
print(f)
print(f[0])
print(f[0]+f[2])
print(f[-1])

f = [1, 2, 3, ["a", "b", "c"]]
print(f[0])
print(f[-1])
print(f[3])
print(f[-1][0])
print(f[-1][1])
print(f[-1][2])

f = [1, 2, ["a", "b", ["Life", "is"]]]
print(f[2][2][0])

# Slicing
g = [1, 2, 3, 4, 5]
print(g[0:2])
g = "12345"
print(g[0:2])

g = [1, 2, 3, 4, 5]
h = g[:2]
i = g[2:]
print(h)
print(i)

j = [1, 2, 3, ["a", "b", "c"], 4, 5]
print(j[2:5])
print(j[3][:2])

# 리스트 더하기 : +
k = [1, 2, 3]
l = [4, 5, 6]
print(k + l)

# 리스트 반복 : *
n = [1, 2, 3]
print(n*3)

# 리스트 길이
o = [1, 2, 3]
print(len(o))

# 리스트의 값 수정
p = [1, 2, 3]
p[2] = 4
print(p)

# 리스트 삭제 : del
q = [1, 2, 3]
del q[2]
print(q)

del q[2:]
print(q)

# 리스트에 요소 추가 : append
r = [1, 2, 3]
r.append(4)
print(r)

r.append([5, 6])
print(r)

# 리스트 정렬 : sort
s = [1, 4, 3, 2]
s.sort()
print(s)

s = ["a", "c", "b"]
s.sort()
print(s)

# 리스트 뒤집기 : reverse
t = ["a", "c", "b"]
t.reverse()
print(t)

# 인덱스 변환 : index
u = [1, 2, 3]
print(u.index(3))
print(u.index(1))
print(u.index(0))

# 리스트에 요소 삽입 : insert
v = [1, 2, 3]
v.insert(0, 4)
print(v)

v.insert(3, 5)
print(v)

# 리스트 요소 제거 : remove
w = [1, 2, 3, 1, 2, 3]
w.remove(3)
print(w)

w.remove(3)
print(w)

# 리스트 요소 끄집어 내기 : pop
x = [1, 2, 3]
print(x.pop())
print(x)
print(x.pop(1))
print(x)

# 리스트에 포한된 문자의 개수 세기 : count
y = [1, 2, 3, 1]
print(y.count(1))

# 리스트 확장 : extend
z = [1, 2, 3]
z.extend([4, 5])
print(z)
a2 = [6, 7]
z.extend(a2)
print(z)