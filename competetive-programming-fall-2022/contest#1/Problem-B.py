for i in range(int(input())):
    trash = input()
    b = [int(k) for k in input().split()]
    print(max(b) - min(b))