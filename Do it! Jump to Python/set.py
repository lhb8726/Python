# Set
a = set([1, 2, 3])
print(a)

b = set("Hello")
print(b)

c = list(a)
print(c)
print(c[0])

d = tuple(a)
print(d)
print(d[0])

# 교집합 : &, .intersection
e = set([1, 2, 3, 4, 5, 6])
f = set([4, 5, 6, 7, 8, 9])
print(e & f)
print(e.intersection(f))

# 합집합 : |, .union
print(e|f)
print(e.union(f))

# 차집합 : -, .difference
print(e-f)
print(f-e)
print(e.difference(f))
print(f.difference(e))

# 값 1개 추가 : add
g = set([1, 2, 3])
g.add(4)
print(g)

# 값 여러 개 추가 : update
h = set([1, 2, 3])
h.update([4, 5, 6])
print(h)

# 특정 값 제거 : remove
i = set([1, 2, 3])
i.remove(2)
print(i)


