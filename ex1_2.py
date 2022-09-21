import argparse
import operator
parser = argparse.ArgumentParser()
parser.add_argument('op', type=str)
parser.add_argument('num', type=int, nargs='+')
args = parser.parse_args()
function = getattr(operator, args.op)
print(function(*args.num))
