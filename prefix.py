import os
import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("What's the operation you want to do?")
    n1 = input("Number 1: ")
    n2 = input("Number 2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Invalid arguments")
    print("Ex: 'sum 1 2'")
    sys.exit(1)

operation, *nums = arguments

valid_ops = ("sum", "sub", "mul", "div")
if operation not in valid_ops:
    print("Invalid operation")
    print(valid_ops)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.isdigit():
        print(f"Invalid number: '{num}'")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

# cria o log
path = os.curdir
filepath = os.path.join(path, "calc.log")
with open(filepath, "a") as file_:
    file_.write(f"{operation}, {n1}, {n2} = {result}\n")

print(f"O resultado é {result}.")
