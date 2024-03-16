# Tuple
a = ()
b = (1,)
c = (1, 2, 3)
d = 1, 2, 3
e = ("a", "b", ("ab", "cd"))

# 튜플 요솟값을 삭제하려 할때
f = (1, 2, "a", "b")
del f[0]

# 튜플 요솟값을 변경하려 할때
g = (1, 2, "a", "b")
g[0] = "c"

# Indexing
h = (1, 2, "a", "b")
print(h[0])
print(h[3])

# Slicing
i = (1, 2, "a", "b")
print(i[1:])

# 튜플 더하기
j = (1, 2, "a", "b")
k = (3, 4)
l = j + k
print(l)

# 튜플 곱하기
m = (3, 4)
n = m * 3
print(n)

# 튜플 길이
o = (1, 2, "a", "b")
print(len(o))