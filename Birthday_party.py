from sys import stdin, stdout


def main():
    j = int(stdin.readline())
    while j is not 0:
        N, M = map(int,stdin.readline().split(" "))
        if M % N is 0:
            stdout.write('Yes' + '\n')
        else:
            stdout.write('No' + '\n')
        j -= 1


if __name__ == "__main__":
    main()

