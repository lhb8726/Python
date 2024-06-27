# 1. 홀수, 짝수 판별하기
def is_odd(number):
    if(number%2==1):
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))

# 2. 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))
3

# 3. 프로그램 오류 수정하기 1
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")
total = int(input1) + int(input2)
print("두 수의 합은 %d입니다." %total)

# 4. 출력 결과가 다른 것은?
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
# print("you", "need", "python")

# 5. 프로그램 오류 수정하기 2
f1 = open("test.txt", "w")
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", "r")
print(f2.read())
f2.close

# 6. 사용자 입력 저장하기
user_input = input("저장할 내용을 입력하세요: ")
f = open("test1.txt", "a")
f.write(user_input)
f.write("\n")
f.close()

# 7. 파일의 문자열 바꾸기
# Life is too short
# you need java
f = open("test.txt", "r")
body = f.read()
f.close()
f = open("test.txt", "w")
f.write(body.replace("java", "python"))
f.close

# 8. 입력값을 모두 더해 출력하기
import sys
result = 0
for i in sys.argv[1:]:
    result += int(i)
print(result)