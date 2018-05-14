l, r, k ,c ,i = 0,0,0,0,0
l, r, k = [int(n) for n in input().split(" ")]
for i in range(l,r+1):
    if i % k ==0:
        c = c + 1
print(c)