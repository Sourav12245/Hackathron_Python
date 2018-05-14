i, j, b, n, N, str1 = 0, 0, 0, 0, 0, 0
N = int(input())
str1 = str(input())
str_search = 'hackerearth'
lat_main = [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2]

lst_str = []
for i in str1:
    lst_str.append(i)


lst_str_search = []
for i in str_search:
    lst_str_search.append(i)

c = 0
n =[]
for i in lst_str_search:
    for j in lst_str:
        if i == j:
            c = c + 1
    n.append(c)
    c = 0

k = []
for i in range(0, len(n)):
    b = n[i] / lat_main[i]
    k.append(int(b))

k.sort()
print(k[0])
