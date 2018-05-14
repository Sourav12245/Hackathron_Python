n = int(input())
v = 1
while v <= n:

    s, g = [str(n) for n in input().split(" ")]
    lst_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    k = []
    j = []
    i = 0
    for i in s:
        k.append(i)
    i = 0
    for i in g:
        j.append(i)

    k_new = []
    i = 0
    for i in k:
        if i in lst_small:
            b = lst_small.index(i)
            k_new.append(b)


    j_new = []
    i = 0
    for i in j:
        if i in lst_small:
            b = lst_small.index(i)
            j_new.append(b)

    s1 = 0
    s2 = 0
    for i in j_new:
        s1 = s1 + i

    for i in k_new:
        s2 = s2 + i

    if s1 == s2:
        print('YES')
    else:
        print('NO')
    v = v + 1
