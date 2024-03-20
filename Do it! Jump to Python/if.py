# If : 조건문
a = True
if a:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 비교 연산자
b = 3
c = 2
print(b > c)
print(b < c)
print(b == c)
print(b!= c)

d = 2000
if d >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# and, or, not
e = 2000
f = True
if e >= 3000 and f:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if e >= 3000 or f:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if not f:
    print("걸어가라")

# in, not in
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print("a" in ["a", "b", "c"])
print("j" not in "python")

g = ["paper", "cellphone", "money"]
if "money" in g:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if "money" in g:
    pass
else:
    print("카드를 꺼내라")

# elif
h = ["paper", "cellphone"]
i = True
if "money" in h:
    print("택시를 타고 가라")
else:
    if i:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

if "money" in h:
    print("택시를 타고 가라")
elif i:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# if문을 한 줄로 작성
j = ["paper", "money", "cellphone"]
if "money" in j:
    pass
else:
    print("카드를 꺼내라")

if "money" in j: pass
else: print("카드를 꺼내라")

# 조건부 표현식
k = 50
if k >= 60:
    l = "success"
else:
    l = "fail"
print(l)
