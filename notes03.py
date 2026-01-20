import argparse

parser = argparse.Argument.Parser()
group = parser.add_mutually_exclusive_group()

parser.add_argument("x", type=int, help="base")
parser.add_argumento("y", type=int, help="expoente")
parser.add_argument("-v", "--verbosity", action="count", default=0)

args = parser.parse_args()
resposta = args.x**args.y

if args.v >= 2:
    print(f"Running '{__file__}'")
elif args.v >= 1:
    print(f"{args.x}^{args.y} == ", end="")
print(resposta)

