# String : 문자, 단어, 문자열
a = "Hello World!"
print(a)

# 줄을 바꾸기 위한 Escape Code : \n
b = "Hello\nWorld"
print(b)

# 문자열 연산
head = "Python"
tail = " is fun!"
print(head + tail)
print(head*3)

# 문자열 길이
c = "Life is too short"
print(len(c))

# Indexing : 가리키다
d = "Life is too short, You need Python"
print(d[3])
print(d[0])
print(d[12])
print(d[-1])
print(d[-0])
print(d[-2])
print(d[-5])

# Slicing : 잘라 내다
e = d[0] + d[1] + d[2] + d[3]
print(e)
print(d[0:4])
print(d[19:])
print(d[:17])
print(d[:])
print(d[19:-7])

f = "20240310Sunny"
date = f[:8]
weather = f[8:]
print(date)
print(weather)

year = f[:4]
day = f[4:8]
print(year)
print(day)

# String Formatting : %s
print("I eat %d apples." %3)
print("I eat %s apples." %"five")

g = 3
print("I eat %d apples." %g)
h = "three"
print("I eat %d apples. so I was sick for %s days." %(g, h))

print("I have %s apples." %3)
print("Rate is %s" %3.234)

print("Error is %d%." %98)
print("Error is %d%%." %98)

print("%10s" %"hi")
print("%-10sjane." %"hi")

print("%0.4f" %3.42134234)
print("%10.4f" %3.42134234)

# format 함수를 이용한 Formatting
print("I eat {0} apples" .format(3))
print("I eat {0} apples" .format("five"))

i = 3
print("I eat {0} apples" .format(i))
j = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(i, j))

print("I ate {k} apples. so I was sick for {l} days." .format(k=10, l=3))
print("I ate {0} apples. so I was sick for {l} days." .format(10, l=3))

# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현
m = 3.42134234
print("{0:0.4f}".format(m))
print("{0:10.4f})".format(m))

# 문자 표현
print("{{ and }}".format())

# f문자열 포매팅 : 문자열 앞에 f접두사를 붙이면 f문자 포매팅 기능 사용 가능 
n = "홍길동"
o = 30
print(f"나의 이름은 {n}입니다. 나이는 {o}입니다.")

# 문자 개수
p = "hobby"
print(p.count("b"))

# 위치
q = "Python is that best choice"
print(q.find("b"))
print(q.find("k"))

r = "Life is too short"
print(r.index("t"))
# print(r.index("k"))

# 문자열 삽입 : .join
print(",".join("abcd"))
print(",".join(["a", "b", "c", "d"]))

# 소문자 -> 대문자 : .upper
s = "hi"
print(s.upper())

# 대문자 -> 소문자 : .lower
t = "HI"
print(t.lower())

# 왼쪽 공백 지우기 : lstrip
u = " hi "
print(u.lstrip())

# 오른쪽 공백 지우기 : rstrip
v = " hi "
print(v.rstrip())

# 양쪽 공백 지우기 : strip
w = " hi "
print(w.strip())

# 문자열 바꾸기 : replace
x = "Life is too short"
print(x.replace("Life", "Your leg"))

# 문자열 나누기 : split
y = "Life is too short"
print(y.split())
z = "a:b:c:d"
print(z.split(":"))