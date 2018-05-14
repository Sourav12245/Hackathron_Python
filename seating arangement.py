j, j_new, number, i1, n ,k = 0,0,0,0,0,0
def call_equal(number):
    num1 = [1, 2, 3, 4, 5, 6]
    num2 = [12, 11, 10, 9, 8, 7]

    if number in num1:
        j = num1.index(number)
        j_new = num2[j]
        return j_new

    elif number in num2:
        j = num2.index(number)
        j_new = num1[j]
        return j_new
    else:
        return -11

def seat_check(number):
    s1 = [2,5,8,11]
    s2 = [1,12,6,7,0]
    if number in s1:
        return 'MS'
    elif number in s2:
        return 'WS'
    else:
        return 'AS'

roll = int(input())
i1 = 1
while i1 <= roll:
    n = int(input())
    num = [1,2,3,4,5,6,7,8,9,10,11,12]
    # if n < 12:
    #     sc = seat_check(n)
    #     k = call_equal(n)
    #     print("{} {}".format(k, sc))
    #     # sys.exit()


    b = 0
    b = n - 12
    c = 0
    if b < 0:
        sc = seat_check(n)
        k = call_equal(n)
        print("{} {}".format(k, sc))

    elif b <= 12:
        c = c + 1
        k = call_equal(b)
        sc = seat_check(b)
        # print((c+1)*12+k)
        print("{} {}".format((c+ 0)*12+k, sc))
    else:
        while b > 12:
            c = c + 1
            b = b - 12
        k = call_equal(b)
        sc = seat_check(b)
        # print((c+1)*12+k)
        print("{} {}".format((c + 1) * 12 + k, sc))
    i1 = i1 + 1





