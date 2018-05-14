leaf = int(input())
i = 1
exp_lst = []
while i <= leaf:
    exp = input()
    exp_lst.append(exp)
    i = i + 1
#
# print(exp_lst)


# exp_lst = ['4+8+9-6-2+4-1+5','2+8']
# for exp in exp_lst:
#     for j in exp:
#         s = j[0]
#         for i in range

k = []
get_numb =[]
sum_hold =[]
for expression in exp_lst:
    for numb in expression:
        k.append(numb)

    for i in range(0,len(k)):
        try:
            get_numb.append(int(k[i]))
        except ValueError:
            get_numb.append((k[i]))
        except IndexError:
            pass
    k.clear()

    s = get_numb[0]
    for i in range(1,len(get_numb)+1,2):
        try:
            if get_numb[i] == '+':
                s = s + int(get_numb[i+1])
            else:
                s = s - int(get_numb[i+1])
        except IndexError:
            continue

    sum_hold.append(s)
    get_numb.clear()
# print(sum_hold)

sum_hold.sort(reverse=True)
print(sum_hold[0])
#     s = 0
#     for i in range(1,len(k),2):
#         try:
#             if k[i] == '+':
#                 s = s + get_numb[i-1]
#             else:
#                 s = s - get_numb[i-1]
#             sum_hold.append(s)
#         except IndexError:
#             pass
#
#     k.clear()
#     get_numb.clear()
#
#
# print(sum_hold)
#     # lst = list(map(int, str(get_numb)))
    # print(lst)
    # lst.clear()
    # print(get_numb)


    # print(len(k))
    # print(k)
    # s = k[0]
    # for i in range(1, len(k),2):
    #     if k[i] == '+':
    #         try:
    #             s = s + k[i+1]
    #         except IndexError:
    #             pass
        # else:
        #     try:
        #         s = s - k[i+1]
        #     except IndexError:
        #         pass
#     sum_hold.append(s)
#     k.clear()
#
#
# print(sum_hold)
    #     try:
    #         print(k[i*2])
    #     except IndexError:
    #         pass
    # k.clear()







# s = []
# for i in exp_lst:
#     i.
#


# s = []
# for i in exp_lst:
#     print(i)

