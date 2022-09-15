a = int(input())
for i in range(a):
    flag = True
    b = input()
    if len(b) % 2 != 0:
        flag = False
    else:
        if b[:len(b)//2] != b[len(b)//2:]:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")