s = str(input())
str_list = []
for i in s:
    str_list.append(i)

lst_big =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfa_find = 0
k = []
for i in str_list:
    if i in lst_big:
        alfa_find = lst_big.index(i)
        b = lst_small[alfa_find]
        k.append(b)
    if i in lst_small:
        alfa_find = lst_small.index(i)
        b = lst_big[alfa_find]
        k.append(b)

s1 = "".join(k)
print(s1)