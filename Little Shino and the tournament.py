x = int(input())
j = 0
k = 0
while x is not 0:
    y = input()
    lst = [int(n) for n in input().split(' ')]

    for i in range(j, len(lst) - 2):
        try:
            a = lst[j]
            b = lst[j + 1]
            c = lst[j + 2]
            j = j + 1

            if a < b < c:
                if k == len(lst) - 3:
                    print('Correct')
                k = k + 1
            elif b > c:
                print("{} {}".format('Incorrect', b))
                break
            else:
                pass
        except IndexError:
            pass
    x = x - 1
