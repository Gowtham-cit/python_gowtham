n = int(input())
l = list(map(int,input().split()))
a, b = map(int,input().split())
c = l.index(a)-l.index(b)
print(abs(c))