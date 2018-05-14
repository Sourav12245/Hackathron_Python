A = 2
N = 5
obs = [0, 0, 1, 0, 1]


def check():
    if s < 0:
        print('{} {}'.format('No', 0))
    elif s >= 0 and c is A:
        print('{} {}'.format('Yes', s))
    else:
        print('{} {}'.format('Yes', s))


s = A
c = 0
for i in obs:
    if i == 0:
        s = s - 1
        c = c + 1
        if s == 0:
            check()

    else:
        s = s + 3 - 1
        c = c + 1
        if s == 0:
            check()


# print(s,c)
# if s is 0 and c is A:
#     print('{} {}'.format('Yes', s))
# elif s is not 0 and c is A:
#     print('{} {}'.format('Yes', s))
# else:
#     pass

