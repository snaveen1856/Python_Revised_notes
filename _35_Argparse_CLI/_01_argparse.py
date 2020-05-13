import argparse

"""
parase = argparse.ArgumentParser()
parase.add_argument('echo', help='echo the string you use here')
args = parase.parse_args()
print(args.echo)
"""
"""
parser = argparse.ArgumentParser()
parser.add_argument('square', help='display the square of the number', type=int)
args = parser.parse_args()
print(args.square**2)

"""

# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on ... just f ")
# else:
#     print("Rod f ")


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("square", type=int, help="display a square of a given number")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"The square of {args.square} equal to {answer}")
else:
    print(f"The square of {answer}")







