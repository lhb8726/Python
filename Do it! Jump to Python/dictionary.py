# Dictionary : Key와 Value를 한 쌍으로 가지는 자료형
a = {"name":"pey", "phone":"010-9999-1234", "birth":"1118"}
b = {1:"hi"}
b = {"a":[1, 2, 3]}

# 딕셔너리 쌍 추가
c = {1:"a"}
c[2] = "b"
print(c)

c["name"] = "pey"
print(c)

c[3] = [1, 2, 3]
print(c)

# 딕셔너리 요소 삭제
del c[1]
print(c)

# 딕셔너리 Key를 사용해 Value 얻기
d = {"pey":10, "juliet":99}
print(d["pey"])
print(d["juliet"])

e = {1:"a", 2:"b"}
print(e[1])
print(e[2])

e = {"a":1, "b":2}
print(e["a"])
print(e["b"])

f = {"name":"pey", "phone":"010-9999-1234", "birth":"1118"}
print(f["name"])
print(f["phone"])
print(f["birth"])

# 딕셔너리 만들 때 주의 사항
# Key 값 중복으로 사용
g = {1:"a", 1:"b"} 
print(g)

# Key 값 리스트 사용
g = {[1, 2]:"hi"}
print(g)

# Key 리스트 만들기 : keys
h = {"name":"pey", "phone":"010-9999-1234", "birth":"1188"}
print(h.keys())

for k in h.keys():
    print(k)

print(list(h.keys()))

# Value 리스트 만들기 : values
print(h.values())

# Key, Value 쌍 얻기 : items
print(h.items())

# Key:Value 쌍 모두 지우기 : clear
h.clear()
print(h)

# Key로 Value 얻기 : get
f = {"name":"pey", "phone":"010-9999-1234", "birth":"1188"}
print(f.get("name"))
print(f.get("phone"))

print(f.get("nokey"))
print(f["nokey"])

print(f.get("nokey", "foo"))

# 해당 Key가 딕셔너리 안에 있는지 조사 : in
g = {"name":"pey", "phone":"010-9999-1234", "birth":"1188"}
print("name" in "g")
print("email" in "g")
