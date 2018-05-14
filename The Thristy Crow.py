j,k,s,N,i = 0,0,0,0,0
j = int(input())
while j > 0:
    dim = [int(n) for n in input().split(" ")]
    N = int(input())
    g = [int(n) for n in input().split(" ")]
    s = dim[3]
    k = dim[2]
    g.sort(reverse=True)
    c = 0
    for i in g:
        if k >= s:
            s = s + i
            c = c + 1
    j = j -1
    print(c)
# j = int(input())
# k = []
# dim = [int(n) for n in input().split(" ")]
# print(dim)
# for i in dim:
#     k.append(int(i))
# print(k)
# dim = [12, 6, 22,8]
# N = int(input())
# g = [2, 5, 4, 2, 3, 1, 2, 3, 1]
# s = dim[3]
# k = dim[2]
# g.sort(reverse=True)
# c = 0
# for i in g:
#     if k >= s:
#         s = s + i
#         c = c + 1
# print(c)
