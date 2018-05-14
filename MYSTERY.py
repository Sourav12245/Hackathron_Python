from sys import stdin, stdout

k = [int(n) for n in stdin.readline()]
g = len(k)
while g is not 0:
    for j in k:
        s = bin(j)
        na = []
        for i in range(2,len(s)):
            na.append(int(s[i]))

        sum = 0
        for i in na:
            sum = sum + i

        stdout.write(str(sum))
    g = g - 1