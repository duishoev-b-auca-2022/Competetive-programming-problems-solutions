a = int(input())
if 1 <= a <= 4:
    print("few")
elif 5 <= a <= 9:
    print("several")
elif 10 <= a <= 19:
    print("pack")
elif 20 <= a <= 49:
    print("lots")
elif 50 <= a <= 99:
    print("horde")
elif 100 <= a <= 249:
    print("throng")
elif 250 <= a <= 499:
    print("swarm")
elif 500 <= a <= 999:
    print("zounds")
elif 1000 <= a:
    print("legion")