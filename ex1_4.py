import argparse


def bag(c, wt, n):
    tabl = [[0 for x in range(c + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(c + 1):
            if i == 0 or j == 0:
                tabl[i][j] = 0
            elif wt[i - 1] <= j:
                tabl[i][j] = max(wt[i - 1] + tabl[i - 1][j - wt[i - 1]], tabl[i - 1][j])
            else:
                tabl[i][j] = tabl[i - 1][j]
    return tabl[n][c]


parser = argparse.ArgumentParser()
parser.add_argument("-c", type=int)
parser.add_argument("-n", type=int)
parser.add_argument("-w", nargs='+', type=int)
args = parser.parse_args()
if len(args.w) != args.n:
    print('Invalid numbers of golden bars')
else:
    print(bag(args.c, args.w, args.n))
