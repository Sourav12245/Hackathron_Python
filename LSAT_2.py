n = 0
N, Q = [int(n) for n in input().split(" ")]
n = 0
fig = [int(n) for n in input().split(" ")]
fig_copy = fig.copy()
fig_copy_store = fig_copy.copy()

while Q is not 0:
    query = int(input())
    h = len(fig)
    while h is not 0:
        if len(fig_copy) % 2 is not 0:
            k = fig_copy[len(fig_copy) - 1]
            fig_copy.remove(k)
        else:
            pass
        for i in range(0, len(fig_copy) - 1, 2):
            try:
                if fig_copy[i] > fig_copy[i + 1]:
                    fig.append(fig_copy[i])
                    fig_copy_store.remove(fig_copy[i + 1])
                else:
                    fig.append(fig_copy[i + 1])
                    fig_copy_store.remove(fig_copy[i])
            except IndexError:
                pass

        fig_copy.clear()
        if len(fig_copy_store) == 2:
            break
        for g in fig_copy_store:
            fig_copy.append(g)
        h = h - 1
    b = fig.count(query)
    print(b)
    Q = Q - 1
