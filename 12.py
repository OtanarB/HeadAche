a = int(input())
b = int(input())
n = int(input())
totalcost = ((a * 100) + b)
r = int((totalcost * n) // 100)
k = int((totalcost * n) % 100)
print(r, k)
