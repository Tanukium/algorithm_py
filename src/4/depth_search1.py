tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]


def search(pos):
    print(pos, end=' ')  # 配下のノードを調べる前に出力
    for i in tree[pos]:  # 配下のノードを調べる
        search(i)  # 再帰的に探索


if __name__ == "__main__":
    search(0)
