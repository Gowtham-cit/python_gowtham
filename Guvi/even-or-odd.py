a, b = map(int,input().split())

if a-b == 0 or (a-b)%2 == 0:
    print("even")
else:
    print("odd")