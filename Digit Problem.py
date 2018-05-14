i, j, k, o = 0, 0, 0, 0
num_main, num_c = [int(n) for n in input().split(" ")]
lst = list(map(int, str(num_main)))

new = []
c = 0


def check():
    le = len(new)
    # print(le)
    for o in range(le, len(lst)):
        new.append(lst[o])


for i in range(0, len(lst) - 1):
    k = lst[i]
    if k != 9:
        if c == num_c:
            check()
            break
        lst[i] = 9
        j = lst[i]
        c = c + 1
        new.append(j)

    else:
        new.append(k)

for j in new:
    print(j, end="")

# X, K = map(str, input().split())
# X_NEW = ""
# K = int(K)
# for i in range(0 , len(X)):
#     if X[i] != "9" and K != 0:
#         X_NEW += "9"
#         K -= 1
#     else:
#         X_NEW += X[i]
#
# print(X_NEW)