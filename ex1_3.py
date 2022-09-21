import argparse
parser = argparse.ArgumentParser()
parser.add_argument('num', type=str)
args = parser.parse_args()
l = list(args.num)
for i, j in enumerate(l[:-1]):
    if ((j == '+' or j == '-') and j != l[i+1]) or j.isnumeric():
        k = True
    else:
        k = False
        break
if k:
    print('True,', eval(args.num))
else:
    print('False, None')
