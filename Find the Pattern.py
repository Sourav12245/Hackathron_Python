tc = int(input())
k = [int(n) for n in input().split(" ")]
k.sort(reverse=True)
b = k[0] + k[tc-1]
print(b)