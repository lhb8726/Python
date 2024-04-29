# File
f = open("new.txt", "w")
f.close()

f = open("C:/doit/new.txt", "w")
f.close()

# File Write
f = open("new.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# File Read
f = open("C:/doit/new.txt", "r")
line = f.readline()
print(line)
f.close

f = open("C:/doit/new.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines
f = open("C:/doit/new.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/doit/new.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close

# read
f = open("C:/doit/new.txt", "r")
data = f.read()
print(data)
f.close()

# For
f = open("C:/doit/new.txt", "r")
for line in f:
    print(line)
f.close()

# Add
f = open("C:/doit/new.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# With
f = open("foo.txt", "w")
f.write("Life uf too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life uf too short, you need python")