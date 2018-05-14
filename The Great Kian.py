N = int(input())
numb = [int(n) for n in input().split(" ")]
# numb = [1,2,3,4,5]
numb1 = numb.copy()
b = len(numb) * 3
for i in range(b):
    numb1.append(0)

# print(numb1, len(numb1))
s = 0
j = 0
fin_out = []
while j <= 2:
    for i in range(j, b - 1, 3):
        s = s + numb1[i]
    fin_out.append(s)
    j = j + 1
    s = 0

# print(fin_out)
# new_fin_out = []
# for b in range(len(fin_out)):
#     new_fin_out.append(fin_out[b])
#
for n in fin_out:
    print(n, end=" ")


