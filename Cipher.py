rot_number,c,i,l,s1 = 0,0,0,0,0
s = input()
rot_number = int(input())
s_list = []
c = 0
for i in s:
    s_list.append(i)
    c = c +1

lst_big =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst_num =['0','1','2','3','4','5','6','7','8','9']


new_list = []
for i in s_list:
    if i in lst_big:
        l = 25
        number_find = lst_big.index(i)
        new_num = number_find + rot_number
        while new_num > l:
            new_num = new_num-(l + 1)
        if new_num <= l:
            new_list.append(lst_big[new_num])
    elif i in lst_small:
        l = 25
        number_find = lst_small.index(i)
        new_num = number_find + rot_number
        while new_num > l:
            new_num = new_num - (l + 1)
        if new_num <= l:
            new_list.append(lst_small[new_num])
    elif i in lst_num:
        l = 9
        number_find = lst_num.index(i)
        new_num = number_find + rot_number
        while new_num > l:
            new_num = new_num - (l + 1)
        if new_num <= l:
            new_list.append(lst_num[new_num])
    else:
        new_list.append(i)


s1 = "".join(new_list)
print(s1)
