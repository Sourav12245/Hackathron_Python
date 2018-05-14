N,Q,i,a,b = 0,0,0,0,0
N, Q = [int(n) for n in input().split(" ")]
lst = []
lst = [int(n) for n in input().split(" ")]
if N == len(lst):
    while i <= Q:
        a, b = [int(n) for n in input().split(" ")]
        if a in lst:
            a_numb =0
            a_numb = lst.index(a)
            if b in lst:
                b_numb =0
                b_numb = lst.index(b)
                lst_new = []
                for i in range(a_numb,b_numb+1):
                    j = lst[i]
                    lst_new.append(j)
                    s = 0
                    m = 0
                    k = 0
                    for k in lst_new:
                        s = s + k
                        m = s / len(lst_new)
        print(int(m))





