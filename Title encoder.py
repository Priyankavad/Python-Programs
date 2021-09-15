file = open("/usercode/files/books.txt", "r")
Hp = file.readlines()
for line in Hp:
    a = line.split()
    for n in a:
        print(n[0])


file.close()
