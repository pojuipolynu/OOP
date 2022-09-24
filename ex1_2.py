import argparse
import operator
import math
parser = argparse.ArgumentParser()
parser.add_argument('op', type=str)
parser.add_argument('num', type=int, nargs='+')
args = parser.parse_args()
if args.op in dir(math):
    function = getattr(math, args.op)
    print(function(*args.num))
elif args.op in dir(operator):
    function = getattr(operator, args.op)
    print(function(*args.num))
else:
    print('There is no such math function')
