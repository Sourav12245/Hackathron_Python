# # dont be greedy. To be tested on the website
N, M, i, total, k = 0, 0, 0, 0, 0
N = int(input())
mouse_price = [int(n) for n in input().split(" ")]
M = int(input())
key_price = [int(n) for n in input().split(" ")]
total = int(input())
# mouse_price = [5]
# key_price = [10, 8,9,7,8,5,6,9,8,5,6,9,5]
# total = 15

s = 0
c = 0
if len(mouse_price) > len(key_price):
    k = len(mouse_price) - len(key_price)
    for i in range(k):
        key_price.append(0)

else:
    k = len(key_price) - len(mouse_price)
    for i in range(k):
        mouse_price.append(0)


for i in range(0, len(mouse_price)):
    if key_price[i] == mouse_price[i]:
        pass
    else:
        s1 = key_price[i] + mouse_price[i]
        s = s + s1
        if s <= total:
            c = c + 1

print(c)
