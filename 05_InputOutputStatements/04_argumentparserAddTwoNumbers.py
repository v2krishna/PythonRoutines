"""
Add two numbers using the argumentparser concept
"""
import argparse

# create argumentparser class object

parser = argparse.ArgumentParser(description="This program calculates sum of two numbers:")


# add two argumnets with the names n1 and n2 and type as float
parser.add_argument("n1", type=float, help="Enter first number:")
parser.add_argument("n2", type=float, help="Enter second number:")

# retrieve the arguments passed to the program
args = parser.parse_args()

result = args.n1+args.n2
print("Sum of the result = ", result)

