# For
a = ["one", "two", "three"]
for i in a:
    print(i)

b = [(1, 2), (3, 4), (5, 6)]
for (first, last) in b:
    print(first + last)

# for 문의 응용
c = [90, 25, 67, 45, 80]
d = 0
for i in c:
    d += 1
    if i >= 60:
        print("%d번 학생은 합격입니다." %d)
    else:
        print("%d번 학생은 불합격입니다." %d)

# continue
e = [90, 25, 67, 45, 80]
f = 0
for i in e:
    f += 1
    if i < 60:
        continue
    print("%d번 학생 축하드립니다. 합격입니다." %f)

# range
g = range(10)
print(g)

h = range(1, 11)
print(h)

i = 0
for j in range(1, 11):
    i += j
print(i)

j = [90, 25, 67, 45, 80]
for i in range(len(j)):
    if j[i] < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다." %(i + 1))

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print("")

# 리스트 컴프리헨션
k = [1, 2, 3, 4]
l = []
for i in k:
    l.append(i * 3)
print(l)

m = [1, 2, 3, 4]
n = [i * 3 for i in m]
print(n)

o = [1, 2, 3, 4]
p = [i * 3 for i in o if i % 2 == 0]
print(p)

q = [i * j for i in range(2, 10)
     for j in range(1, 10)]
print(q)