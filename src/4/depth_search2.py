tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]


def search(pos):
    for i in tree[pos]:
        search(i)
    print(pos, end=' ')  # 配下のノードを調べた後に出力


if __name__ == "__main__":
    search(0)
