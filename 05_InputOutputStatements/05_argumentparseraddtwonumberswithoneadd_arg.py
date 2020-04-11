"""
Add two numbers using only one add_argument
"""
import argparse

# create ArgumentParser Class Object
parser = argparse.ArgumentParser(description="This program finds sum of two numbers using only one add_argument \
                                 and nargs")

# create args
parser.add_argument("nums", type=float, nargs=2, help="Enter two float numbers:")

# retrieve the arguments that are passed
args = parser.parse_args()

#now the arguments are passed
result = float(args.nums[0]) + float(args.nums[1])
print("Result of addition is :", result)