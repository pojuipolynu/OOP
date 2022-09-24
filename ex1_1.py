import argparse
parser = argparse.ArgumentParser()
parser.add_argument('num', type=int)
parser.add_argument('op', type=str)
parser.add_argument('num1', type=int)
args = parser.parse_args()
if args.op not in ['+', '-', '*', '/']:
    print('Invalid arithmetic operation')
elif args.op == '/' and args.num1 == 0:
    print('Dividing by zero')
else:
    print(eval(str(args.num)+args.op+str(args.num1)))
