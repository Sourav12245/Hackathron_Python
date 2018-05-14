def checker(num):
    if num % 2 is 0:
        print("YES")
    else:
        print("NO")


tc = int(input())
i = 1

while i <= tc:
    k = int(input())
    checker(k)
    # if k % 2 is 0:
    #     print("YES")
    # else:
    #     print("NO")
    i = i + 1
