# While
a = 0
while a < 10:
    a += 1
    print("나무를 %d번 찍었습니다." %a)
    if a == 10:
        print("나무 넘어갑니다.")
        
# while 문 강제로 빠져나가기
d = 10
e = 300
while e:
    print("돈을 받았으니 커피를 줍니다.")
    d = d -1
    print("남은 커피의 양은 %d개입니다." %d)
    if d == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

while True:
    e = int(input("돈을 넣어 주세요. : "))
    if e == 300:
        print("커피를 줍니다.")
        d = d - 1
    elif e > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(e - 300))
        d = d - 1
    else:
        print("돈을 다시 돌려 주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %d)
    if d == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while 문의 맨 처음으로 돌아가기
f = 0
while f < 10:
    f = f + 1
    if f % 2 == 0: continue
    print(f)

# 무한루프
while True:
    print("Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.")
