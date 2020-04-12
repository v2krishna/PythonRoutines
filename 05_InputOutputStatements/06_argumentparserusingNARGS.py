"""
Using the add_argument and using nargs to pass one or more arguments
and find the addition
"""
import argparse
# create ArgumentParser class objects

parser = argparse.ArgumentParser(description="Program to one or more arguments")

# pass the arguments
parser.add_argument("nums", type=float, nargs ="*", help="Enter the float type numbers for addition")

# retrieve the arguments
args = parser.parse_args()
sum = 0.0
for arg in args.nums:
    print(arg)
    sum += arg
print("sum:=", sum)
