# Function
def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

# 매개변수와 인수
def add(a, b):
    return a + b
print(add(3, 4))

# 입력값과 리턴값에 따른 함수의 형태
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

# 입력값이 없는 함수
def say():
    return "Hi"

a = say()
print(a)

# 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a + b))

add(3, 4)

a = add(3, 4)
print(a)

# 입력값도, 리턴값도 없는 함수
def say():
    print("Hi")

say()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=5, a=3)
print(result)

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul("add", 1, 2, 3, 4, 5)
print(result)

result = add_mul("mul", 1, 2, 3, 4, 5)
print(result)

# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="foo", age=3)

# 함수의 리턴값
def add_and_mul(a, b):
    return a + b, a * b

result = add_and_mul(3, 4)
print(result)

result = (7, 12)
print(result)

result1, result2 = add_and_mul(3, 4)
print(result1, result2)

def add_and_mul(a, b):
    return a + b
    return a * b

result = add_and_mul(2, 3)
print(result)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

say_nick("야호")
say_nick("바보")

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

def say_myself(name, man=True, age):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a += 1

vartest(a)
print(a)

def vartest(hello):
    hello += 1

def vartest(a):
    a += 1

vartest(3)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# return 사용
a = 1
def vartest(a):
    a += 1
    return a

a = vartest(a)
print(a)

# global 사용
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)

# lambda 예약어
add = lambda a, b: a + b
result = add(3, 4)
print(result)

def add(a, b):
    return a + b

result = add(3, 4)
print(result)