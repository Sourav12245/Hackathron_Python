num, tot = 0, 0
import re

num = int(input())
i = 1
while i <= num:
    # tot, s = [n for n in input()]
    # s = str(input())
    print(len(re.findall("\d+", s)))
    i = i + 1
