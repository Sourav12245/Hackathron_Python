N,c,i = 0,0,0
def prime_check(num):
    c = 0
    for i in range(1, num):
        if num % i == 0:
            c = c + 1

    if c <= 1:
        print(num, end= " ")

N = int(input())
for i in range(2,N+1):
    prime_check(i)


# N = 10
# c = 0
# for i in range(1,N):
#     if N % i == 0:
#         c = c + 1
#
# if c <= 1:
#     print('Prime')
# else:
#     print('NOT Prime')


# c = 0
# k = []
# k.append(0)
# for i in range(1,N):
#     if N % i == 0:
#        k.append(i)
#
# print(k)