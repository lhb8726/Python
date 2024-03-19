# 1. 평균 점수 구하기
kor = 80
eng = 75
math = 55
avg = (kor + eng + math) / 3
print(avg)

# 2. 홀수, 짝수 판별하기
num = 13
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4. 주민등록번호 인덱싱
pin = "881120-1068234"
print(pin[7])

# 5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# 6. 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7. 리스트를 문자열로 만들기
a = ["Life", "is", "too", "short"]
result = " ".join(a)
print(result)

# 8. 튜플 더하기
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9. 딕셔너리의 키
a = dict()
a["name"] = "python"
a[("a",)] = "python"
a[[1]] = "python" 
a[250] = "python"
# a[[1]] = "python" : 리스트 타입은 딕셔너리의 키 값이 될 수 없다

# 10. 딕셔너리 값 추출
a = {"A":90, "B":80, "C":70}
result = a.pop("B")
print(a)
print(result)

# 11. 리스트에서 중복 제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = a = set(a)
b = list(aSet)
print(b)

# 12. 파이썬 변수
a = b = [1, 2, 3]
a[1] = 4
print(b)
# [1, 4, 3]