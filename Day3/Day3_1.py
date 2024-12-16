import os
import re
from operator import mul

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read().splitlines()

reg = r"mul\(\d{1,3},\d{1,3}\)"

results = []
for line in data:
    results += re.findall(reg, line)

total = 0
for expression in results:
    total += eval(expression)

print(total)

