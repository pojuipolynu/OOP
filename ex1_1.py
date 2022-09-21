import argparse
parser = argparse.ArgumentParser()
parser.add_argument('num', type=str)
args = parser.parse_args()
k = eval(args.num)
print(k)
