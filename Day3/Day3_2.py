from re import findall
from operator import mul
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read()

mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

parts = data.split("do()")
filtered_parts = [part.split("don't()")[0] for part in parts]
data = " ".join(filtered_parts)

results = findall(mul_pattern, data)
total = 0
for expression in results:
    total += mul(int(expression[0]), int(expression[1]))

print(total)