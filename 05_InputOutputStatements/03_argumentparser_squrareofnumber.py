"""
Using the argument parser find the square of a number
"""
import argparse

# create ArgumentParser class object

parser = argparse.ArgumentParser(description="This program helps to display the square of a number:")

# add one argument named as num any type as integer

parser.add_argument("num", type= int, help="Enter a integer number:")

# retrieve the argument passed to the program
args = parser.parse_args()
result = args.num**2
print("Square of a number:", result)


