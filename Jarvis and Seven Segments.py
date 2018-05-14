s = str(input())


def check():
    if '111111' in s:
        return True

    if '000000' in s:
        return True


k = check()
if k is True:
    print("Sorry, sorry!")
else:
    print("Good luck!")
