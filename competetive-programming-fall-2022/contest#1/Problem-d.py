num = int(input())
for j in range(num):
    flag = True
    size = int(input())
    first = list(input())
    second = list(input())
    for i in range(size):
        if first[i] == second[i] == "1":
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")