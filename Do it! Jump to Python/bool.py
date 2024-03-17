# Bool : True or False
a = True
b = False
print(type(a))
print(type(b))

print(1==1)
print(2>1)
print(2<1)

# 자료형의 참과 거짓
c = "python"
d =  ""
print(bool(c))
print(bool(d))

e = [1, 2, 3]
f = []
print(bool(e))
print(bool(f))

g = (1, 2, 3)
h = ()
print(bool(g))
print(bool(h))

i = {"a":1}
j = {}
print(bool(i))
print(bool(j))

k = 1
l = 0
m = None
print(bool(k))
print(bool(l))
print(bool(m))

n = [1, 2, 3, 4]
while n:
    print(n.pop())

if []:
    print("True")
else:
    print("False")

if [1, 2, 3]:
    print("True")
else:
    print("False")

# bool 연산
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))
print(bool(h))
print(bool(i))
print(bool(j))
print(bool(k))
print(bool(l))
print(bool(m))
print(bool(3))